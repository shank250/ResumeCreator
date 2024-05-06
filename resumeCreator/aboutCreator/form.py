from django import forms

class UserInputForm(forms.Form):
    user_input = forms.CharField(label='Enter your data', widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))