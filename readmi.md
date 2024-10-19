# Проект скрипта должен находится в директории root

1. Поставить python на сам сервер 

2. Уставновить библиотеку - psutil
    - Команда:  pip3 install psutil

3. Запустить файл main.py

# Если скрипт запустился без ошибок:
4. Переместить сервис "sngrep-killer-script.service" в /etc/systemd/system
    - Команда:  mv sngrep-killer-script.service /etc/systemd/system

5. Запустить сервисы: 
    5.1. Перезагрузите systemd, чтобы он увидел новый сервис:
        - sudo systemctl daemon-reload

    5.2. Запустите сервис:
        - sudo systemctl sngrep-killer-script
    
    5.3. Включить его автозапуск при перезагрузке:
        - sudo systemctl enable sngrep-killer-script

    5.4. Чтобы проверить статус сервиса и убедиться, что он запущен:
        - sudo systemctl status sngrep-killer-script