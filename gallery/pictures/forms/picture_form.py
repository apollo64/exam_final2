from django.forms import forms
from ..models.Picture import Picture


class PictureUploadForm(forms.ModelForm):
    title = forms.CharField(
        label='Заголовок',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        })
    )

    picture = forms.ImageField(label='Картинка', required=False, type='jpg' 'jpeg' 'png')

    class Meta:
        model = Picture
        include = ["title", "picture"]

