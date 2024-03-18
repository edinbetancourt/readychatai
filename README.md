* READYCHATAI TEST

Objective:

Create a simple ToDo list web application using Django. This project is designed to test your ability to implement CRUD (Create, Read, Update, Delete) operations in Django and your understanding of Django models, views, and templates.

Core Features:

Task Model: 

Define a task model in Django with fields for the task title, description, and a boolean field to mark the task as completed.

Task Management:

Implement a simple interface where users can add a new task, view a list of all tasks, mark a task as completed, and delete a task. Authentication is not required for this simple version.

User Interface: 

Use Django templates to create a basic but user-friendly web interface that allows for easy interaction with the task list. Ensure the interface is straightforward, with forms to add tasks and buttons or links to mark them as completed or delete them.

Create API endpoints for add/remove/update/delete/tasks.
 
Technical Requirements:

Utilize Django's ORM for handling the task data.

Make sure the application follows the MVC pattern, separating the logic, data, and presentation layers.

Ensure the application is secure by validating and sanitizing user inputs, even though authentication is not part of the requirement.


- INSTALL THE APP:

git clone https://github.com/edinbetancourt/readychatai.git


- CONFIG:

cd readychatai

python -m venv venv

./venv/scripts/activate

pip install -r requirements.txt


- RUN APP:

python manage.py runserver


- WEB ACCESS

http://localhost:8000/listtask


- SWAGGER:

http://localhost:8000/doc/schema/swagger-ui/



END.




