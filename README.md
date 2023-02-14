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


## To-do:
- **Password-Reset**
- **Search Function**
- **Implementing Rest-Api**
- **Moderators Implementation For Banning User and Manage All Posts**

## Preview
## Signup 
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/106817606/218756154-4b922ae0-a270-4d98-95d0-063d736ed97c.png">

## Login
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/106817606/218756213-c66f86ca-1976-41c0-b237-0a06667caa0f.png">

## Posts 
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/106817606/218755936-533406dc-735e-4ea4-970c-ab9017656a3a.png">
<img width="1280" alt="image" src="https://user-images.githubusercontent.com/106817606/218756064-79930393-c6f9-4a4c-82d5-1d2087ed2731.png">



## Contributing
If you would like to contribute to this project, please submit a pull request or open an issue on GitHub.
