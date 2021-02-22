# URL Shortner

## Requirements/ Expected Functionality
The expected features and supported capabilities will be as follows:
1. A user can supply a url that they want shortened, and then after submitting it they will receive a short url which includes the base url and the hash/short value.
2. On a separate page a user can submit a url they want shortened and the hash/short value they want for it, if it is already taken, let the user know.
3. A user should be able to hit one of the provided short urls and be redirected to the original url.

## Project Architecture:
- As per above mentioned requirements, I have created 2 independent services for requirement point 1 and point 2.
- TinyURLapp Folder contains the Django App for Requirement 1
- CustomURLapp Folder contains the Django App for Requirement 2
- Advantage: 
1. Individual App Reusability for other projects
2. Less complex debugging and Testing
3. Flexible and Scalable (Each application can be scaled independently)  


## Tech Stack
1. Python/Django
2. PostgreSQL Database (AWS RDS Instance)


