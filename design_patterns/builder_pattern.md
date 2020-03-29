## Builder Design Pattern
### Definition
It is a creational pattern.
It is used when we want to create an object that is composed of multiple parts  
and the composition needs to be done step by step. The object is not complete  
unless all its parts are fully created.  
  
### Difference between Factory and Builder Design Pattern  
1.  Factory pattern creates an object in a single step, whereas a builder pattern  
creates an object in a multiple steps, and almost through the use of a director.  
2.  Factory pattern returns a created object immediately whereas in the builder  
pattern, the client code explicitly asks the director to return the final object  
when it needs it.  

### Use Cases
i. Content Management System e.g. WordPress
ii. Fast food restaurants for preparing meals
iii. HTML and dynamic SQL query generator