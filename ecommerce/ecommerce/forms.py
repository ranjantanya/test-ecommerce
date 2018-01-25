from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class Contact_Form(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Your full name"
                   }
        )
    )

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={"class": "form-control",
                   "placeholder": "Your email"
                   }
        )

    )

    content = forms.CharField(
        widget = forms.Textarea(
            attrs={"class": "form-control",
                   "placeholder": "Your message"
                   }
        )
    )

    def clean_email(self):
       email = self.cleaned_data.get("email")
       if not "gmail.com" in email:
           raise forms.ValidationError("only gmail is accepted")
       return email


from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Enter your username"
                   }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Your password"
                   }
        )

    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        return username


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Enter your username"
                   }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Your password"
                   }
        )

    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Confirm password"
                   }
        )

    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control",
                   "placeholder": "Your email"
                   }
        )

    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username = username)
        if qs.exists():
            raise forms.ValidationError('Username is already taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError('email is already taken')
        return email

    def clean(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("passwords must match")