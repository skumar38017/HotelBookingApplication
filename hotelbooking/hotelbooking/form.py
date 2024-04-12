from django import forms
'''
Django validation and HTML form handling
'''
class UserLogin(forms.Form):
      email=forms.EmailField(label='Enter Email')
      password=forms.CharField(label='Enter Password')

class UserRegister(forms.Form):

      email=forms.EmailField(label='Enter Email',widget=forms.EmailInput(attrs={'class':"form-control",'placeholder':'Enter Email','id':"name"}))

      password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"row g-3 col-12 form-floating form-control",'placeholder':'Enter Password','id':"password"}))
      