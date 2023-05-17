from django import forms
class Login(forms.Form):
    username=forms.CharField(max_length=15,label="Kullanıcı Adı :",widget=forms.TextInput(attrs={"class" :"form-control"}))
    password=forms.CharField(max_length=20,label="Şifrenizi Giriniz :",widget=forms.PasswordInput(attrs={"class" :"form-control"}))
class Kayıtol(forms.Form):
    username=forms.CharField(max_length=15,label="Kullanıcı Adı :",widget=forms.TextInput(attrs={"class" :"form-control"}))
    password=forms.CharField(max_length=20,label="Şifrenizi Giriniz :",widget=forms.PasswordInput(attrs={"class" :"form-control"}))
    confirmpassword=forms.CharField(max_length=20,label="Şifre Doğrulama :",widget=forms.PasswordInput(attrs={"class" :"form-control"}))
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirmpassword=self.cleaned_data.get("confirmpassword")
        if password and confirmpassword and password!=confirmpassword:
            raise forms.ValidationError("")

        degeler= {
            "username" : username,
            "password" : password
        }
        return degeler