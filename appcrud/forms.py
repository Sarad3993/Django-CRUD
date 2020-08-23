from django import forms
from appcrud.models import Students


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__' # actual form fields where we want input from the user 
        # we can also specify each fields separately instead of using __all__

