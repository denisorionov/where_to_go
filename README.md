# Website with map interesting places in Moscow 

Training project [Devman Django course](https://dvmn.org/modules/django/).  

All requirements are listed in the file: `requirements.txt`.

Link on website: https://webspring58.pythonanywhere.com/.

Link on admin site: https://webspring58.pythonanywhere.com/admin/.

### For testing:
login: admin.

password: adminadmin.

### Installing project

Install python.

Create virtual environment: 
```shell script
python -m venv env
```
Activate the virtual environment:
```shell script
source env/scripts/activate
```
Install requirements:
```shell script
pip install -r requirements.txt
```
Run the project:
```shell script
./manage.py runserver
```
Open in browser: http://localhost:8000.

### Loading data from json

For load data use command load_place:

```shell script
python manage.py load_place http://addres/file.json
```
For load data from several files, the links are separated by a space.


Data taken from [Kudago](https://kudago.com/).
