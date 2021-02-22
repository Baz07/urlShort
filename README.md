# URL Shortner (Deployed on Heroku)

[Go to App!](https://shortner-project.herokuapp.com/)

## Requirements/ Expected Functionality
The expected features and supported capabilities will be as follows:
1. A user can supply a url that they want shortened, and then after submitting it they will receive a short url which includes the base url and the hash/short value.
2. On a separate page a user can submit a url they want shortened and the hash/short value they want for it, if it is already taken, let the user know.
3. A user should be able to hit one of the provided short urls and be redirected to the original url.

## Project Architecture:
- As per above mentioned requirements, I have created 2 independent services for requirement point 1 and point 2.
- "tinyURLapp" Folder contains the Django App for Requirement 1
- "customURLapp" Folder contains the Django App for Requirement 2

#### Advantage of creating 2 independent applications as opposed to creating 1 single application: 
1. You can use each application in any other project [Code Reusability achieved]
2. Testing Application Code, Generate Code Coverage and Debug Code Issues is way less complex than performing all mentioned tasks in a single application
3. Consistent, High Fault Tolerant and Scalable Design [Even if one application/service goes down, you can still use other service without any issue]   


## Tech Stack
1. Python/Django
2. PostgreSQL Database (AWS RDS Instance)
3. HTML/Bootstrap
4. AWS S3 bucket (For Static File Storage) --> In Progress


## How to use the project code? (Please make sure to install all dependencies from requirements.txt file before executing the project)
1. Create a Folder locally on your desktop machine.
2. Initialize git inside the folder using 'git init'
3. From Inside the folder, run "git clone <HTTP or SSL git link>" to clone the repo locally in your desktop
4. Move inside folder 'urlShort' and run "python manage.py runserver" to execute the application locally.
5. To run Test Cases, run 'python manage.py test <App Name>' [Ex: python manage.py test tinyURLapp]
6. For Coverage Testing, run 'coverage run manage.py test <App Name>' and 'coverage html' to check the coverage of each module.

## Git Branch Information
Since I have treated requirement 1 and 2 as an independent services, I have developed requirment 1 via branch 1.0.0 and requirement 2 via branch 2.0.0 to handle major/minor feature enhancement and bug fixes.

