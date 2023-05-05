# LUNASOUL WEBSITE
Capstone Project Level 3
This guide provides instructions on how to install and set up the Django project to run the website on your local machine

## Prerequisites
Before you start, make sure you have the following installed on your computer:

* Python (version 3 or above)
* pip (Python package installer)
You can download Python from the official website: https://www.python.org/downloads/.  
Pip should be included with your Python installation.

## Installation
1. Clone or download the project from the Github repository.
2. Open a terminal or command prompt and navigate to the project directory.
3. Create a virtual environment for the project using the following command:  
**python -m venv env**
  
4. Activate the virtual environment using the following command:  
For Windows:  
**env\Scripts\activate**   
For Unix or Linux:  
**source env/bin/activate**  
5. Install the required packages using pip:  
**pip install -r requirements.txt**  
6. Create a new file named .env in the project directory and add the following lines to it:  
**SECRET_KEY=your_secret_key_here**  
**DEBUG=True**  
Replace your_secret_key_here with a secret key of your choice.  
8. Run the following commands to create the database and apply the migrations:  
**python manage.py migrate**  
9. Finally, start the development server using the following command:  
**python manage.py runserver**
10. The server will start running at http://localhost:8000/. You can open this URL in your web browser to see the website.

## Credits
This project was built using a combination of various technologies to create a visually appealing and functional website. I would like to give credit to the following technologies:  
* Google Fonts - A library of open-source fonts that can be used on the web to enhance the website's visual appeal.  
* CSS (Cascading Style Sheets) - A language used for describing the presentation of a website, including its layout, colors, and fonts.  
* Bootstrap - A popular front-end framework for building responsive and mobile-first websites. It provides a range of CSS and JavaScript components and tools for developing modern and clean-looking interfaces.  
* SQLite - A lightweight and file-based relational database management system that we used to store data for this project.  
* HTML (Hypertext Markup Language) - A standard markup language used to create web pages and applications.  
* Python - A popular and versatile programming language that we used for developing the backend of the website.

