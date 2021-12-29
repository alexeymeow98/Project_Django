from django import forms
from .models import Post, Contact
from django.forms import ModelForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'message']
