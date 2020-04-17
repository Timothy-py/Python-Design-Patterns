## FACTORY DESIGN PATTERN  
### Definition :
Define an interface for creating an object, but defer object instantiation to run time.
The factory method is based on a single function written to handle our object 
creation task. We execute it, passing a parameter that provides information about 
what we want, and, as a result, the wanted object is created.
### Use case :
In the software world, the Django web framework uses the factory method pattern for creating
the fields of a web form. The forms module, included in Django, supports the
creation of different kinds of fields (for example, CharField, EmailField, and so on.)