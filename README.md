# api

I used to write api :

1. language: Python
2. framweork: django framework
3. program: Visual Studio Code, notepad++, cmder, powershell

How to run it.

1. Install python, and CMDER
2. Create virtual machines use command " python -m venv namemachine" 
3. Install django use command " python -m pip install Django "
4. In a folder with a virtual machine in console write command "Scripts\Activate"
5. Next write "cd api" 
6. Now you can run server "python manage.py runserver"

Server work on localhost and default port 8000,
On this moment you go write :
loclahost:8000/admin
This is admin panel login :admin password: admin  , you can Create, Update, Delete user, group, questions and answer from database 
loclahost:8000/ankieta
On this page you can choose question and mark the answer.
loclahost:8000/ankieta/question.id 
You have details about the question
loclahost:8000/ankieta/question.id/wyniki
You can see other people's answers
