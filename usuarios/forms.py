from django import forms
from django.contrib.auth.models import User, Group

class UsuarioCreateForm(forms.ModelForm):
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        label='Nível de acesso'
    )
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            user.groups.clear()
            user.groups.add(self.cleaned_data['grupo'])
        return user

class UsuarioUpdateForm(forms.ModelForm):
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
        label='Nível de acesso'
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        label='Nova senha (opcional)'
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        new_password = self.cleaned_data.get('password')
        if new_password:
            user.set_password(new_password)
        if commit:
            user.save()
            user.groups.clear()
            user.groups.add(self.cleaned_data['grupo'])
        return user
