# URL Shortner (Deployed on Heroku)

[Go to App!](https://shortner-project.herokuapp.com/)

## Requirements/ Expected Functionality

### Functional Requirments:
The expected features and supported capabilities will be as follows:
1. A user can supply a url that they want shortened, and then after submitting it they will receive a short url which includes the base url and the hash/short value.
2. On a separate page a user can submit a url they want shortened and the hash/short value they want for it, if it is already taken, let the user know.
3. A user should be able to hit one of the provided short urls and be redirected to the original url.

### Non Functional Requirments:
1. HA (High Availabiltiy) to ensure URL redirection shouldn't fail at any instance.
2. Real time URL Redirection (No Latency)
3. For multiple users accessing the same URL, they all should get the same URL. This will improve API Response Time and requires less storage in DB. [This requirment can be changed according to client since in some situations for multiple users, they might ask to give different short URLs for same long URL]

## Project Architecture:
- As per above mentioned requirements, I have created 2 independent services for requirement point 1 and point 2.
- "tinyURLapp" Folder contains the Django App for Requirement 1
- "customURLapp" Folder contains the Django App for Requirement 2
- Logic to create short URLs is present inside "tinyURLapp" folder

#### Logic to create Short URLs:
1. Assign a unique id to a valid user provided long URL (i.e. use a Hash Map/Table) and encoded the id using base64 conversion to generate short/hash value for Short URL.
2. **My Approach**: We can use Hash Function like Digest or MD5 or SHA256 Algorithm to generate a unique hash of user provided long URL. 
3. Naive Approach: Use "random" and "strings" to randomly generate a new short value and append it with base URL.
4. Use "KGS (Key Generation Service)" which will precompute a random short string and store it in the Database. For each request, KGS will send a unique short string. Advantage would be no need to encode or deal with collisions however this could be a single point of failure in the system.

#### Advantage of creating 2 independent applications as opposed to creating 1 single application: 
1. You can use each application in any other project [Code Reusability achieved]
2. Testing Application Code, Generate Code Coverage and Debug Code Issues is way less complex than performing all mentioned tasks in a single application
3. Consistent, High Fault Tolerant and Scalable Design [Even if one application/service goes down, you can still use other service without any issue]   


## Tech Stack
1. Python/Django
2. PostgreSQL Database (AWS RDS Instance)
3. HTML/Bootstrap
4. AWS S3 bucket (For Static File Storage) --> In Progress
5. Redis Caching System for Requirement 1 --> In Progress


## How to use the project code? (Please make sure to install all dependencies from requirements.txt file before executing the project)
1. Create a Folder locally on your desktop machine. (Recommended: Set up a virtual env)
2. Initialize git inside the folder using 'git init'
3. From Inside the folder, run "git clone <HTTP or SSL git link>" to clone the repo locally in your desktop
4. Run "pip install -r requirements.txt" to install the dependencies
5. Move inside folder 'urlShort' and run "python manage.py makemigrations" and then "python manage.py migrate" for DB Migrations
6. Move inside folder 'urlShort' and run "python manage.py runserver" to execute the application locally.
7. To run Test Cases, run 'python manage.py test <App Name>' [Ex: python manage.py test tinyURLapp]
8. For Coverage Testing, run 'coverage run manage.py test <App Name>' and 'coverage html' to check the coverage of each module.

## Git Branch Information
Since I have treated requirement 1 and 2 as an independent services, I have developed requirment 1 via branch 1.0.0 and requirement 2 via branch 2.0.0 to handle major/minor feature enhancement and bug fixes.

## Database Schema

#### For Requirment 1 [Tiny URL App]

![db_schema1](db_schema1.JPG)


#### For Requirment 2 [Custom URL App]

![db_schema2](db_schema2.JPG)

## Further Improvements
1. Implement Data Parititoning (Ex: hash based paritioning) in case application is handling million/billion requests per sec/min.
2. Implement Load Balancers throughout the design
3. Database Cleaning/Purging (Include a expiration time with each short URL)   
4. Allow a group of users to access a particular URL (Include permission tag along with URL)

