from django import forms

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=30,label='Username')
    password=forms.CharField(max_length=10,label='Password',widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=10,label='Password confirm',widget=forms.PasswordInput)

def clean(self):
    username=self.clean_data['username']
    password=self.clean_data['password']
    confirm=self.clean_data['confirm']
        
    if password and confirm and password != confirm:
        raise forms.ValidationError('Shifre eyni deyil  . ')
    values={
        'username':username,
        'password':password
    }
    return values

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30,label='Username')
    password=forms.CharField(max_length=10,label='Password')