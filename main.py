import time
import psutil

def kill_sngrep():
    # Ищем процессы с именем sngrep
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'sngrep':
            print(f"Закрываем процесс sngrep с PID {proc.info['pid']}")
            proc.terminate()  # Отправляем сигнал на завершение
            proc.wait()  # Ждём завершения процесса

def monitor_sngrep():
    print("Запуск мониторинга процессов sngrep...")
    while True:
        # Ищем процессы с именем sngrep
        sngrep_found = False
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == 'sngrep':
                sngrep_found = True
                print(f"Процесс sngrep с PID {proc.info['pid']} найден. Начинаем отсчёт 5 минут.")
                
                # Ждём 5 минут (300 секунд)
                time.sleep(300)

                # Проверяем, существует ли процесс после ожидания
                if proc.is_running():
                    print(f"Процесс sngrep с PID {proc.info['pid']} всё ещё работает. Закрываем его.")
                    proc.terminate()  # Завершаем процесс
                    proc.wait()  # Ждём завершения
                else:
                    print(f"Процесс sngrep с PID {proc.info['pid']} был завершён ранее.")
        
        # Если не найдено ни одного процесса sngrep, подождём перед следующей проверкой
        if not sngrep_found:
            # print("Процесс sngrep не найден. Проверяем снова через 10 минуту.")
            time.sleep(600)

if __name__ == '__main__':
    monitor_sngrep()