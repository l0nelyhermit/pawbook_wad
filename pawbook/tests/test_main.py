from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from django.template.defaultfilters import slugify

# Valid Registration Details
valid_registration_details = {
    "username": "noobmaster69",
    "password": "test",
    "email": "noobmaster69@gmail.com"
}
# Valid User Profile Details
valid_user_profile_details = {
    "firstName": "Steve",
    "lastName": "Rogers",
    "age": 99,
    "bio": "What's up name",
    "location": "Glasgow",
    "profilePicture": "default.jpg"
}

# Valid Add Listing Details
valid_add_listing_details = {
    "breed": "Siberian Husky",
    "petName": "Lucky",
    "description": "Active,Friendly,Listens Well",
    "petAge": 11,
    "cost": 100,
    "petImage": "cat.jpg"
}
# Valid post details
valid_post_detail = {
    "PostTitle": "Cute Adorable Husky",
    "postDescription": "13 years old husky in the house!",
}
# valid contact us form details
valid_contact_us_detail = {
    "first_name": "John",
    "last_name": "Wick",
    "email": "John_wick@continental.com",
    "message": "You killed my dog!"
}



def register(cli):
    cli.client.post(reverse('pawbook:register'), valid_registration_details,
                    content_type='application/x-www-form-urlencoded')

def login(cli):
    return cli.client.login(username=valid_registration_details['username'],
                        password=valid_registration_details['password'])

def register_and_login(cli):
    register(cli)
    login(cli)


def add_contact(cli):
    cli.client.post(reverse('pawbook:contact'),valid_contact_us_detail,
                content_type='application/x-www-form-urlencoded')

def add_post(cli):
    cli.client.post(reverse('pawbook:posts'),valid_post_detail,
                content_type = 'application/x-www-form-urlencoded')

def add_listing(cli):
    cli.client.post(reverse('pawbook:listings'),valid_add_listing_details,
                content_type = 'application/x-www-form-urlencoded')


