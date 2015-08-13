## MelbDjango School - Lesson Five

Class Based Views & ModelForms

---

## WIFI

Common Code / cc&20!4@

---

## A brief look at OO

- Object Oriented Programming
- Software development methodology
- A way to describe data and its interactions in code
- Objects are things - Any-things
- Concept first goes back to the 60s
- Popularised by the Smalltalk language in the early 1980s
- Became a dominant programming methodology with the introduction of C++, Visual FoxPro and Delphi
- Python, Java, Javascript, Ruby, Perl, Lisp (to name a few) - All incorporate OO concepts

---

## Classes

- A Class defines an object
- What sort of object? - Anything!

---

## A Car

![](http://www.wellclean.com/wp-content/themes/artgallery_3.0/images/car3.png)

---

## A Person

![](http://vignette2.wikia.nocookie.net/kimpossible/images/8/86/Placeholder_person.png)

---

## A Car Person

![](http://beakerhead.com/wp-content/uploads/2014/04/art-car-parade.jpg)

---

## Properties of Python classes

- Attributes
- Methods
- Bases (For managing inheritance)

---

## Attributes

- Describe the object
  - Car - Engine, Wheels, Seats, Doors...
  - Person - Head, Eyes, Arms, Legs...

---

## Methods

- Describe what the object can do
  - Car - Drive, Turn, Stop
  - Person - Walk, Run, Talk

---

## Classes in Python

- Define a basic Vehicle
  - Attributes: Engine, Wheels
  - Methods: Drive, Stop

```
class DefaultVehicle:
    engine = '4 Cylinder'
    wheels = 4

    def drive(self):
        pass

    def stop(self):
        pass
```

---

## Inheritance

- Define a Tank using our DefaultVehicle class as a base

![](http://www.incredible-adventures.com/tanks/drive-tank-001.jpg)

---

## Tank Class

- In addition to DefaultVehicle a tank has a turret and can shoot
- Engine and wheels values are also different

  ```
  class Tank(DefaultVehicle):
      engine = 'Massive' # Try googling for "tank engine"
      wheels = 20
      turret = 'Large calibre'

      def shoot(self):
          pass
  ```

- Tank __overloaded__ the engine and wheels with its own values
- Tank still has drive and stop capabilities as they are implied by inheriting from the parent class DefaultVehicle

  ```
  tank = Tank()
  tank.drive() # From parent (super) class DefaultVehicle
  tank.stop()  # From parent (super) class DefaultVehicle
  tank.shoot()
  ```


---

## Another class example

### Person

```
class Person:
    head = 'large'
    eyes = 2
    arms = 2
    legs = 2

    def walk(self):
        pass

    def run(self):
        pass

    def talk(self):
        pass
```

---

## Mix it up

### What sort of object will this code produce?

  ```
  class VehiclePerson(DefaultVehicle, Person):
      pass
  ```

- Remember that the attributes and methods of both __superclasses__ are implied by this definition
- Attributes and methods can be overloaded in this new class just like any other

---

### Something like this?

![](http://beakerhead.com/wp-content/uploads/2014/04/art-car-parade.jpg)

---

## What have I created?

  ```
  freak_of_nature = VehiclePerson()
  freak_of_nature.drive()
  freak_of_nature.walk()
  freak_of_nature.run()
  freak_of_nature.stop()
  freak_of_nature.talk()
  ```

---

## OO Jargon

### __Inheritance__

- Objects inherit everything from their parent (super) class
- Tank inherited wheels, engine, drive() and stop() from DefaultVehicle

---

## OO Jargon

### __Multiple Inheritance (Mixins)__

- VehiclePerson class is a combination of DefaultVehicle and Person

---

## OO Jargon

### __Overloading__

- Tank replaced its superclass' attributes wheels and engine with its own values

---

## OO Jargon

### __Polymorphism__

- Different behaviour depending on the type of object the code is interacting with
- Out of scope for this presentation
- Python implements it's own take on this concept

---

## HTML Forms

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
