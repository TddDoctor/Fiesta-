from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    
    Email = forms.EmailField(required=True, label="", widget = forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.IntegerField(required=True, label="", widget = forms.TextInput(attrs={'placeholder': 'Phone'}))
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Message'}))


        