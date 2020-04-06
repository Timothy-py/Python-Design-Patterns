## The Bridge Pattern
### Definition
The bridge pattern is a design pattern used in SE that is meant  
to "decouple an abstraction from its implementation so that the  
two can vary independently". Furthermore, it is a structural  
design pattern that divides business logic or huge class into  
separate class hierarchies that can be developed independently. One  
of these hierarchies(the Abstraction) will get a reference to an  
object of the second hierarchy(implementation).  
It is used mainly for implementing platform independent feature.

### Real-world example
i.  Device drivers

### Use-cases
Using the bridge pattern is a good idea when you want to share an  
implementation among multiple objects. Basically, instead of  
implementing several specialized classes, defining all that is  
required within each class, you can define the following special components:  
    i.  An abstraction that applies to all the classes
    ii. A separate interface for the different objects involved. 