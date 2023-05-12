This is the project PizzaLair for the VLN-2 course. The program is intended to
handle pizza ordering and management of these orders, the basics of an online store.

For this project you need to set up a virtual environment and import the packages from
the requirements.txt file included within the project directory. Then you need to run the
statement 'python manage.py runserver 8000' from the verklegt-2 directory.

NOTE: This project has debug mode on because the group did not configure any error screens
because we preferred handling them with f.x. redirects when a user does something they should not,
as well as because we could not configure the project so the static files can be read with debug
mode off.

Some extra requirements we implemented are an auto logout when user is idle for 10 minutes and a footer
that includes information on our business.
