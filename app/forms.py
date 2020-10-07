from django import forms


class MainForm(forms.Form):
    """
    Класс формы на главной странице сайта
    """
    name = forms.CharField(label='', max_length=128,
                           widget=forms.TextInput(attrs={'placeholder': 'Имя'})
                           )
    email = forms.EmailField(label='', max_length=128,
                             widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))