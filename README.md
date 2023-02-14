## Django-User-System

This system provides user registration, login, logout, and a user profile, as well as public and private post creation built with  **_Crispy-Forms_**

## Features 
 - User Registration
 - User Login / Logout
 - Creation Of Posts (Public / Private)


## Usage 

- ```pip install -r requirements.txt```
- ```python manage.py runserver```

## Urls

- **/signup:** Register a new user
- **/login:** Login with an existing user
- **/logout**: Logout the current user
- **/home/:** View a list of all public posts
- **/create-post/**: Create a new post (requires authentication)
- **/update-post/<post-id>**: Update the post
- **/admin:** Access the Django admin site (requires superuser privileges)
