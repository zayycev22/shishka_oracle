# Департамент строительства города Москвы

## :hammer_and_wrench: Languages and Tools :

<div align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/python/python-original.svg" height="40" width="40">
  <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/javascript/javascript-original.svg" height="40" width="40">
  <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/fastapi/fastapi-original.svg" height="40" width="40">
  <img src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/react/react-original.svg" height="40" width="40">
</div>

## :crystal_ball: Front-End
Загрузка зависимостей
```
cd frontend
npm install --legacy-peer-deps
```
Запуск frontend приложения
```
npm start
```
Сервер будет работать по ссылке 127.0.0.1:3000
## :hammer: Back-End
Создание виртуального окружения:
```
cd backend
pythom -m venv venv
venv\Scripts\Activate.ps1
```
Установка необходимых пакетов:
```
pip install -r .reqs.txt
```
Запуск backend приложения
```
python ./backend/main.py
```
Сервер будет работать по ссылке 127.0.0.1:8000
## :moyai: Описание приложения

В данном веб приложении используется предобученная модель для предсказания даты окончания задачи.

Данное решение предпологает то, что происходит предобработка в нужном формате csv файла.

Пример файла можно найти в oracul\backend\files\test_shrinked.csv

Видео с демонстрацией решения можете посмотреть [здесь](link).
