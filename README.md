# Project-Game-Library
Game Library Project for DFEcloud5
This is a app that can record game records. It does so by allowing the create.py to create the database to record the players entries. The HTML templates set the template for the webapp and formats how it will look. The template for form, creates a form that the user can input dater. The delete function allows users to delete rows of data. The add functions allows users to add more data to the table. The templatesa are solely used as webpage formatters. Init.py is the database and secret key stager. It creates a secret key and database from sqllite.The database is a local hosted one inside of the frontend container.
forms.py is the field validators and form variables, so it forces users to make sure the correct type of data is inputed and the data inputed is correct to the field values.
models.py is the database table creater, it makes 2 tables each with different field of information to be inputed/edited.
routes.py are the webapp pages and directories if you to search for them. Each route is linked to a new webpage, for example home is the first page we see that shows the editable table. Then add take you to a new webpage that allows you to fill out the form to edit the home webpage. When you are redirected to home you will see the updated webpage.
app.py is the run command and port oppener???
create.py creates my table and deletes any created before it, I also added some database entries into it. There are 2 tables and each have a row of data inputed, which is necessary but i also made these enteries to show a relationship. for example when create.py is run it creates the database adds the enteries and in the console prints a line linking both together.
requirements.txt holds all the requirements for my webapp to run aslo used in the Dockerfile.
The Dockerfile starts the containerisation and installs the requirements.txt and tells the container to start from creat.py and app.py. It also copies the whole of the frontend folder into the container.
The docker compose file automates the process it names the container and shows the port it is open to.
The jenkins file automates the process it stages the process to build and deploy the file. It builds the file to jenkins and then deploys it to docker hub.

*Add the ssh to the vm to connect* 
*eof tag to make a file will end it (please google)*
