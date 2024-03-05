from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=225, widget=forms.TextInput(
        attrs={'placeholder': "Your name"}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': "Your email"}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': "What do you want to say?"}))
