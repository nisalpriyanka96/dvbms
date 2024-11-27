# Damn Vulnerable Book Management System (DVBMS)
**The Vulnerable API** *(Based on VAMPI)*

![DVBMA](https://i.imgur.com/wylr9Rl.png)

Book Management System vulnerable API made with Flask and it includes vulnerabilities from the API OWASP top 10 vulnerabilities for APIs. It was created and modified referencing popular Vulnerable API VAMPI.


#### Features
 - Based on OWASP Top 10 vulnerabilities for APIs.
 - OpenAPI3 specs and Postman Collection included.
 - Global switch on/off to have a vulnerable environment or not.
 - Token-Based Authentication
 - Available Swagger UI to directly interact with the API

An unregistered user can see minimal information about the dummy users included in the API. A user can register and then login to be allowed using the token received during login to post a book. For a book posted the data accepted are the title and a secret about that book. Each book is unique for every user and only the owner of the book should be allowed to view the secret.

A quick rundown of the actions included can be seen in the following table:

| **Action** |            **Path**           |                     **Details**                    |
|:----------:|:-----------------------------:|:--------------------------------------------------:|
|     GET    |           /createdb           | Creates and populates the database with dummy data |
|     GET    |               /               |                     VAmPI home                     |
|     GET    |           /users/v1           |      Displays all users with basic information     |
|     GET    |        /users/v1/_debug       |         Displays all details for all users         |
|    POST    |       /users/v1/register      |                  Register new user                 |
|    POST    |        /users/v1/login        |                   Login to VAmPI                   |
|     GET    |      /users/v1/{username}     |              Displays user by username             |
|   DELETE   |      /users/v1/{username}     |       Deletes user by username (Only Admins)       |
|     PUT    |   /users/v1/{username}/email  |             Update a single users email            |
|     PUT    | /users/v1/{username}/password |                Update users password               |
|     GET    |           /books/v1           |                 Retrieves all books                |
|    POST    |           /books/v1           |                    Add new book                    |
|     GET    |        /books/v1/{book}       |      Retrieves book by title along with secret     |
|     GET    |        /fetch-url?url=        |      Check the URL status                      |


#### List of Vulnerabilities
 - SQLi Injection
 - Unauthorized Password Change
 - Broken Object Level Authorization
 - Mass Assignment
 - Excessive Data Exposure through debug endpoint
 - User and Password Enumeration
 - RegexDOS (Denial of Service)
 - Lack of Resources & Rate Limiting
 - JWT authentication bypass via alg none
 - SSRF (Server Side Request Forgery)



 ## Run it
It is a Flask application so in order to run it you can install all requirements and then run the `app.py`.
To install all requirements simply run `pip3 install -r requirements.txt` and then `python3 app.py`.

## Deploy the HTML files in the frontend folder to a web server as the application's frontend.
Update the config.js file before deploying the frontend. (You can do this If required for get idea how API and Frontend is interconnected. And exploit the web level security issues!!)

HAPPY HUNTING!!

