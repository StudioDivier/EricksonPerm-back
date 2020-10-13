from django import forms
from django.contrib.auth.forms import UsernameField


class MainForm(forms.Form):
    """
    Класс формы на главной странице сайта
    """
    name = forms.CharField(label='', max_length=128,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Имя', 'class': 'inputs-section', 'type': 'text'})
                           )
    email = forms.EmailField(label='', max_length=128,
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'E-mail', 'class': 'inputs-section', 'type': 'email'}))


class UsernameAdmin(UsernameField):

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            'autocapitalize': 'none',
            'autocomplete': 'username',
            'placeholder': 'Логин'

        }
