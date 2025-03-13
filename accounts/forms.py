from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = CustomUser
        # fields = AdminUserCreationForm.Meta.fields + ('age',)
        fields = ('username', 'age', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'age', 'email',)


