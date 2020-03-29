## Prototype Design Pattern
### Definition
The prototype design pattern helps with creating object clones. In its simplest version,  
this pattern is just a clone() function that accepts an object as input parametr and  
returns a clone of it. In Python, this can be done using the copy.deepcopy() function.  

### Use cases
i.  The prototype pattern is useful when we have an existing object that needs to stay  
untouched, and we want to create an exact copy of it, allowing changes in some parts  
of the copy.