from django import forms
from django.forms import ModelForm
from cric.models import Team


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


# class PlayerForm(ModelForm):
#     name = forms.CharField(
#         label='',
#         required=True,
#         widget=forms.TextInput(
#             attrs={"placeholder": "Player Name", }
#         ),
#     )

#     class Meta:

#         model = Player
#         fields = ['name']


# # Creating a form to add an article.
# #
