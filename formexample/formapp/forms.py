from django import forms

from .models import Person


# class HelloWorldForm(forms.Form):
#     name = forms.CharField(required=False, label="Say Hello")
#     awesome = forms.BooleanField(label="Are they awesome?")

#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if not name.lower().startswith('b'):
#             raise forms.ValidationError("Wait a second, %s doesn't start with B!" % name)
#         return name


class HelloWorldForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'awesome')

        # Can specify a lot of form settings here
        # widgets, labels etc

    def save(self, commit=True):
        """
        This method is unique to ModelForms

        Override the default save method to ensure that people are only
        saved as awesome if their name starts with b
        """
        person = super(HelloWorldForm, self).save(commit=False)

        if not person.name.lower().startswith('b'):
            person.awesome = False

        if commit:
            person.save()

        return person


