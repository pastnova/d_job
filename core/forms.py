from django.forms import ModelForm

from core.models import UserProfile, Conference


class UserProfileForm(ModelForm):

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

    class Meta:
        model = UserProfile
        fields = [
            'email',
            'password',
        ]


class CreateConference(ModelForm):

    class Meta:
        model = Conference
        fields = [
            'theme',
            'count_participant',
            'date_start',
            'description'
        ]
