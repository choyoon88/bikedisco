# BikeDisco
![amiresponsive](static/images/readme-images/bd-responsive.png)

## Table of Content

1. About

# About

BikeDisco is a public bicycle station application that provides station locations and available number of bicycles on real time across Ireland and UK. Station information is all from [CityBike API](https://api.citybik.es/v2/#net_resource). User can join the website, review specific stations and contact us for feedback and improvements.

# Project Goals
- Give users real time information about the bicycle station in Ireland and UK.
- Enable users to write a review about specific stations and also view other reviews that were written by other users. 

## User Goal
- View into the shared bicycle stations in Ireland and UK on Google Maps.
- Create a review of each stations.
- Edit a review that has been created by themselves. 
- View other reviews that were posted by others.
- Delete their own reviews. 
- Join the website as a member. 
- Update their personal data such as name, email address, phone number etc. 
- Delete their account.
- Contact to the admin by filling out the given form.


# User Experience
## Target Audience

## User Expectations
- Application showing clear purpose.
- Easy interface that allows quick and efficient navigation.

## User Stories


# Database

## Data Models

### User Model
- User model is from Django allauth library and it contains basic information about authenticated user. 

### Post Model

| Name | Field Type | Validation |
| :---:   | :---: | :---: |
| title | CharField | max_length=200, unique=True |
slug | SlugField | max_length=200, unique=True |
author | ForeignKey | on_delete=models.CASCADE, related_name="review_posts" |
updated_on | DateTimeField | auto_now=True |
content | TextField | |
featured_image | CloudinaryField | 'image', default='placeholder' |
created_on | DateTimeField | auto_now_add=True |
status | IntegerField | choices=STATUS, default=1 |
country | CharField | max_length=100, null=True |
city | CharField | max_length=100, null=True |
station_name | CharField | max_length=100, null=True |

### Profile Model

| Name | Field Type | Validation |
| :---:   | :---: | :---: |
user | OneToOneField | on_delete=models.CASCADE, related_name='profile' |
firstname | CharField | max_length=50, blank=True, Default = 'Enter your first name' |
lastname | CharField | max_length=50, blank=True, Default = 'Enter your first name' |
phone_number | PhoneNumberField | blank=True |
email | EmailField | |

### Contact Model

| Name | Field Type | Validation |
| :---:   | :---: | :---: |
name | CharField | max_length=100 |
email | EmailField | |
subject | TextField | |


## Testing


## Validation


## WAVE (Accessibility check)

## Deployment 



## Credits and References

- [CityBikes API Documentation](https://api.citybik.es/v2/#net_resource)
- jQuery
- [Google Maps API](https://developers.google.com/maps/documentation/javascript)
- [Bootstrap 5.3.1](https://getbootstrap.com/docs/5.3/)
- [Django](https://www.djangoproject.com/)
    - [Django Allauto](https://django-allauth.readthedocs.io/en/latest/)
    - [django-active-link](https://valerymelou.com/blog/2020-05-04-how-to-highlight-active-links-in-your-django-website)
- [Google Font](https://fonts.google.com/)
- [Fontawesome](https://fontawesome.com/)
- [Stackoverflow](https://stackoverflow.com/) for browsing related questions