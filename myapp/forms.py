from django import forms
from .models import Article, Comment
from django.contrib.auth import authenticate
from django import forms


# class AuthenticationForm(forms.Form):
#     username = forms.CharField(max_length=254)
#     password = forms.CharField(label="Password", widget=forms.PasswordInput)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')
#         if username and password:
#             self.user = authenticate(username=username, password=password)
#             if self.user is None:
#                 raise forms.ValidationError("Incorrect username/password")
#         return cleaned_data

class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError("Incorrect username/password")
            self.cleaned_data['user'] = self.user
        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your comment here...',
                'rows': 4,
            }),

        }
class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter content',
                'rows': 5
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'