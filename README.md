# Website with map interesting places in Moscow 

Training project [Devman Django course](https://dvmn.org/modules/django/).  

All requirements are listed in the file: `requirements.txt`.

Link on website https://webspring58.pythonanywhere.com/.

Link on admin site https://webspring58.pythonanywhere.com/admin/.

#### For testing:
login: admin.

password: admin.

#### Установка проекта

Установить python.

Создать виртуальное окружение: 
```shell script
python -m venv env
```
Активировать виртуальное окружение:
```shell script
source env/scripts/activate
```
Установить зависимости:
```shell script
pip install -r requirements.txt
```
Запустить проект:
```shell script
./manage.py runserver
```
Открыть в браузере http://localhost:8000.

#### Загрузка данных из json

Для загрузки данных данных используется команда load_place:

```shell script
python manage.py load_place http://адрес/файла.json
```
Для загрузки данных из нескольких файлов ссылки указываются через пробел.


Тестовые данные взяты с сайта [Kudago](https://kudago.com/).
