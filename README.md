# Todo-list
A simple app that will help you manage your daily task list.

## Installation
Python3 must be already installed

### 1.Clone the repository:
```bash
 git clone https://github.com/AnnaLub/todo-list 
 ```

### 2.Create a virtual environment and activate it:
```bash
 python -m venv .venv
 ```
```bash
.venv\Scripts\activate (on Windows)
```
```bash
source .venv/bin/activate (on macOS)
 ```

### 3.Install the project dependencies:
```bash
 pip install -r requirements.txt
 ```

### 4.Create a database and migrate the models:
``` bash
 python manage.py migrate 
 ```

### 5.Create a superuser:
```bash
 python manage.py createsuperuser
  ```

### 6.Start the server:
```bash
  python manage.py runserver
  ```

 Open your web browser and go to
http://127.0.0.1:8000.

## Features
* View your task list.
* Create, update, delete a task.
* Categorize tasks with tags.
* Change the task status
* create and edit a list of tags.


## Technologies Used
* Python
* Django
* HTML
* CSS