from django import forms
from django.contrib.auth.models import User
from pawbook.models import UserProfile, PetPedia, Post, Listing
import django.utils.timezone as timeNow


class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    dateJoined = forms.DateField(widget = forms.HiddenInput(), default = timeNow.now())

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("age", "bio", "location", "profilePicture")


class PostForm(forms.ModelForm):
    postTitle = forms.CharField(max_length = 128, help_text = "Enter post title")
    datePosted = forms.DateField(widget = forms.HiddenInput(), default = timeNow.now())
    postImage = forms.ImageField()
    postDescription = forms.CharField(max_length = 128, help_text = "Enter post description")
    likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    dislikes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)

    class Meta:
        model = Post
        fields = ("postTitle", "postImage", "postDescription")


class ListingForm(forms.ModelForm):
    datePosted = forms.DateField(widget = forms.HiddenInput(), default = timeNow.now())
    petName = forms.CharField(max_length = 128, help_text = "Enter the name of the pet for sale")
    breed = forms.ChoiceField(queryset = PetPedia.breed)
    petAge = forms.IntegerField(help_text = "How old is your pet?")
    cost = forms.IntegerField(help_text = "How much does the pet cost?")
    petImage = forms.ImageField()

    class Meta:
        model = Listing
        fields = ("breed", "petName", "petAge", "cost", "petImage")