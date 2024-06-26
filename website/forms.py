from django import forms
from .models import Architect


class ArchitectForm(forms.ModelForm):
    class Meta:
        model = Architect
        fields = [  "architect_id", 
                    "first_name", "last_name", 
                    "fathers_name", "nickname", 
                    "gender",  "birth_location_id", 
                    "date_of_birth", "date_of_death",
                    'biography']
        