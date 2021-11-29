# STUDIO PICTURESQUE

### 26th Nov. 2021

## Author  
  
[Mwikali](https://github.com/Maryan23)  
  
# Description  
This is a beautiful photo studio that showcases pictures of some of the rarest places on earth.Allows users to search based on category and to view based on locations.
  
##  Live Link  
 
  
## Screenshots 

###### Home page
 
 
## User Story  
  
* View different photos from the galllery 
* Click a single image to expand it and view the details of that photo  
* Search for images by different categories.   
* Copy a link to the photo.  
* Filter photos based on the location.  
  

  
## Setup and Installation  
  
##### Clone the repository:  
 ```bash 
 git@github.com:Maryan23/Studio-Picturesque.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Studio-Picturesque pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source env/bin/activate  
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations gallery
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django==3.2.7](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs  
  
## Support and Contact Information 

Incase of any contributions fork the repo and make any substantial changes.
Incase of any ideas,suggestions or complaints feel free to connect with me on mwikali119@gmail.com 

## License
MIT
Copyright (c) 2021 **Studio-Picturesque**