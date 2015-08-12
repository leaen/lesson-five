### MelbDjango School - Lesson Four

Django Forms & Testing

---

### WIFI

Common Code / cc&20!4@

---

### HTML Forms

- One of the ways users can interact with your application
- Data entered by the user is sent to the server for processing
- Always surrounded by `<form>...</form>` (in valid HTML)
- text, radio, file, select, textarea, submit, etc.

---

### Reminder: GET vs POST

- Forms are submitted via GET or POST

- Quick reminder:
  - Using GET puts the form content in the URL (no passwords!)
  - Use POST for anything that changes the database

---

### Django Forms

- Django helps with the rendering and processing of HTML forms

- There are two different types of forms provided:
  - `django.forms.Form`
  - `django.forms.ModelForm`

- Using Django Forms simplifies the use of HTML forms
- Helps your create more secure web applications
- By convention we create our forms in `forms.py`

---

### Quick example

- Imagine a HTML form that looks like this:

```
<form method="POST">
  <input type="text" name="name" value="">
  <input type="submit" value="Say Hello">
</form>
```

---

![](http://i.imgur.com/hPT22Is.png)

---

### Quick example

We can create a very simple Django form:

```
from django import forms

class HelloWorldForm(forms.Form):
    name = forms.CharField()
```

---

### Quick Example

And update our template to include the form:

```
<form method="POST">
  {{ form.as_p }}
  <input type="submit" value="Say Hello">
</form>
```

---

### Quick Example

Finally in our view we can do something like:

```
def hello_world(request):
    form = HelloWorldForm()
    return render(request, 'django_form.html', {
        'form': form,
    })
```

---

![](http://i.imgur.com/uIXpMdI.png)

---

### Rendering Forms

- Django provides three helper functions for rendering forms:
  - {{ form.as_table }}
  - {{ form.as_p }}
  - {{ form.as_ul }}
- You need to provide the "wrapper" yourself
- Don't forget a submit button!

---

![](http://i.imgur.com/xLqvIOW.png)

---

### Manually Rendering Our Form

- You can also manually render the form by directly accessing the fields:

```
{{ form.non_field_errors }}
<form method="POST">
  {{ form.name.errors }}
  <label for="{{ form.name.id_for_label }}">Name:</label>
  {{ form.name }}
  <input type="submit" value="Say Hello">
</form>
```

- There's a helper `{{ form.name.label_tag }}` to render the label tag for you

---

### Form Fields

- When you're creating a form you need to define it's fields
- Each Field has it's own validation logic and `Widget` (form element)
- All fields have these arguments (and some others):
  - `required` (True by default)
  - `initial_data`
  - `label`
  - `help_text`

---

### Field Example

- Let's update our form field to change the label and make it optional

```
from django import forms

class HelloWorldForm(forms.Form):
    name = forms.CharField(label="Say Hello", required=False)
```

---

# Form Fields

- BooleanField, CharField, ChoiceField, TypedChoiceField, DateField, DateTimeField, DecimalField, DurationField, EmailField, FileField, FilePathField, FloatField, ImageField, IntegerField, IPAddressField, GenericIPAddressField, MultipleChoiceField, TypedMultipleChoiceField, NullBooleanField, RegexField, SlugField, TimeField, URLField, UUIDField, ComboField, MultiValueField, SplitDateTimeField, ModelChoiceField, ModelMultipleChoiceField

---

### CharField

- So, there's a whole bunch of different field types, let's look at a few

- CharField is a generic text input field
- It takes two optional arguments for validation
  - `max_length`
  - `min_length`

```
class HelloWorldForm(forms.Form):
    name = forms.CharField(label="Say Hello", required=True)
```

```
<p>
  <label for="id_name">Say Hello:</label>
  <input id="id_name" name="name" type="text">
</p>
```

---

### BooleanField

- True / False field represented as a Checkbox
- Want to accept `False` values? Use `required=False`

```
class HelloWorldForm(forms.Form):
    name = forms.CharField(required=True, label="Say Hello")
    awesome = forms.BooleanField(label="Are they awesome?")
```

```
<p>
  <label for="id_name">Say Hello:</label>
  <input id="id_name" name="name" type="text">
</p>
<p>
  <label for="id_awesome">Are they awesome?</label>
  <input id="id_awesome" name="awesome" type="checkbox" />
</p>
```

---

Our form earlier was broken, does anyone know why?

---

![](http://i.imgur.com/IZ19HPU.png)

---

### CSRF

- When using POST you need to include `{% csrf_token %}` within your form
- Provides protection against Cross Site Request Forgery
  - Where another site submits a form to your site
- Can be disabled on a per view (or project wide) basis
  - Think carefully before disabling!
- https://docs.djangoproject.com/en/1.8/ref/csrf/

---

### Form Validation

- All the default form fields have validation included
  - `URLField` checks that it's a valid URL
  - `DateField` makes sure it's a date
  - `SlugField` checks that there are only letters, numbers, underscores, and hyphens

---

### Adding Custom Validation

- You can easily write your own validators
- Validators accept the submitted value as an argument and raise `ValidationError` if it fails

```
from django.core.exceptions import ValidationError

def validate_name_starts_with_b(value):
    if not value.lower().startswith('b'):
        raise ValidationError('%s does not start with "b"' % value)
```

---

### Cleaning Fields

- Another way you can validate your form is to use `clean()` or `clean_<fieldname>()`
- Raise `ValidationError` on failure
  - `clean()` must return the full `cleaned_data` dictionary
  - `clean_<fieldname>()` returns the value of that field

```
class HelloWorldForm(forms.Form):
    name = forms.CharField(required=True, label="Say Hello")
    awesome = forms.BooleanField(label="Are they awesome?")

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.lower().startswith('b'):
            raise forms.ValidationError("Wait a second, your name doesn't start with B!")
        return name
```

---

### Using Forms in Views

- Normally we'll send our data back to the same view that the form came from
- This means we add a check to see if the form was submitted then:
  - populate the form with the data from the request
  - or create a blank form
- Calling `is_valid()` does all our validation and tells us if there are errors
- Once things are validated you can access the data with `cleaned_data`

---

### Hello World

```
def django_example(request):
    if request.method == 'POST':
        form = HelloWorldForm(request.POST)
        if form.is_valid():
            return render(request, 'django_form.html', {
                'form': form,
                'name': form.cleaned_data['name']
            })
    else:
        form = HelloWorldForm()

    return render(request, 'django_form.html', {
        'form': form,
    })
```
