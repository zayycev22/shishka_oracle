# Разработка графического интерфейса для кейса "Разработка модели для прогнозирования нарушений в работе ИТ-решений"
> Ссылка на интерфейс: ...
### :hammer_and_wrench: Languages and Tools :

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
npm install
```
Запуск frontend приложения
```
npm start
```
Сервер будет работать по ссылке 127.0.0.1:3000
## :hammer: Back-End
Создание виртуального окружения:
```
pythom -m venv backend/venv
backend\venv\Scripts\Activate.ps1
```
Установка необходимых пакетов:
```
pip install -r ./backend/requirements.txt
```
Запуск backend приложения
```
python ./backend/main.py
```
Сервер будет работать по ссылке 127.0.0.1:3000
## :moyai: Описание приложения

В данном веб приложении используется предобученная модель для предсказания выявления переквалификации обращения.

Данное решение предпологает то, что на внешних сервисах происходит сбор данных, после чего, оператор/администратор может загрузить данные, и получить результат. Результат можно посмотреть как на сайте в таблице, так и скачать файл в формате .csv .

Видео с демонстрацией решения можете посмотреть [здесь](https://disk.yandex.ru/d/ibS70vjAJ01B5g).
