[app]

# (str) Название приложения
title = My KivyMD App

# (str) Имя пакета (без пробелов, только латиница)
package.name = mykivymdapp

# (str) Домен пакета
package.domain = org.test

# (str) Список файлов исходного кода (через запятую)
source.dir = .
source.exts = py,png,jpg,kv,atlas

# (list) Зависимости приложения. 
# Обязательно указываем python3, kivy и kivymd
requirements = python3,kivy,kivymd

# (str) Главный файл приложения
version = 0.1

# (list) Разрешения (Permissions)
android.permissions = INTERNET

# (int) Целевой уровень API Android
android.api = 31

# (int) Минимальный поддерживаемый API Android
android.minapi = 21

# (str) Ориентация экрана (all, portrait, landscape)
orientation = portrait

# (bool) Полноэкранный режим (1 - да, 0 - нет)
fullscreen = 0

# (str) Поддерживаемые архитектуры процессоров
android.archs = arm64-v8a, armeabi-v7a


[buildozer]

# (int) Уровень логирования (0 = error, 1 = info, 2 = debug (с выводом кэша), 4 = trace)
log_level = 2

# (int) Показывать предупреждения
warn_on = 0
