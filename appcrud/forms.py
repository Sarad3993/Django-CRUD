from django import forms
from appcrud.models import Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__' # u can also pass each fields separately instead of using __all__

