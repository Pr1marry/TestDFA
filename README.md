# Тестовое задание от DFA
ТЕСТОВОЕ ЗАДАНИЕ BACKEND РАЗРАБОТЧИКУ

Необходимо спроектировать апи, на основе фреймворка Django + DRF

регистрация, модель / апи для юзера и его галереи

После выполнения задания, загрузите исходный код в ваш аккаунт на GitHub, и пришлите нам ссылку. После получения нашего ответа, удалите репозиторий с GitHub.
Требования к коду
Всё сделать в виде АПИ (в DRF)
CRUD к картинкам
Сделать роут для удаления всех картинок из базы для администратора
Любая авторизация, регистрация
Роут на получение текущего юзера
Дополнительные баллы можно получить за:
покрытие кода тестами
докеризацию

## Выполнено из доп. пунктов: Контейнеризация

# Инструкция по установке проекта:

### 1: Клонируем проект к себе командой: git clone https://github.com/Pr1marry/TestDFA
### 2: Переходим в деректорию (core) командой: cd core
### 3: Меняем настройки подключение к базе данных: в файле settings : ставим свою бд, в файле docker_compouse: меняем данные на свою бд
### 4: Запускаем контейнеры командой: docker-compose up -d
### 5: Приложение будет доступно на 8000 порту в Debug-моде.
### 6: Аннотации по api и их 'ручкам' описаны по адресу: http://0.0.0.0:8000/docs/ (Open_API)
