# coding: utf-8
from django.forms import ModelForm
from core.models import Conference
from core.models import UserProfile


class UserProfileForm(ModelForm):
    """Форма для создания профиля пользователя."""

    class Meta:
        model = UserProfile
        fields = [
            'surname',
            'name',
            'patronymic',
            'email',
            'password',
            'office',
            'degree',
            'organization',
            'address',
            'phone',
            'personal_data'
        ]


class LoginForm(UserProfileForm):
    """Форма для авторизации."""

    class Meta:
        model = UserProfile
        fields = [
            'email',
            'password',
        ]


class CreateConference(ModelForm):
    """Форма для создания конференции."""

    class Meta:
        model = Conference
        fields = [
            'theme',
            'date_start',
            'description',
            'requirements',
            'count_participant',
            'file'
        ]
