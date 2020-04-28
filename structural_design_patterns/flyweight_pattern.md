## Flyweight Pattern
### Definition
The flyweight design pattern is a technique used to minimize memory usage and improve performance  
by introducing data sharing between similar objects. It is an optimization technique because it  
helps to reduce the overhead of object creation. A flyweight is a shared object that contains  
state-independent, immutable(aka intrinsic) data. The dependent, mutable(aka extrinsic) data should  
not be part of flyweight because this is information that cannot be shared, since it differs per  
object. If flyweight needs extrinsic data, it should be provided explicitly by the client code.

### Use Cases
i. Embedded Systems e.g Phones, Tablets, Game consoles etc.  
ii. Performance-critical applications e.g games, 3-D graphics processing, real-time systems etc.

### Requirements that need to be satisfied to effectively use the flyweight pattern
i. the application needs to use a large number of objects.  
ii. there are so many objects that it's too expensive to store/render them. Once the mutable state  
is removed, many groups of distinct objects can be replaced by relatively few shared objects.  
iii. Object identity is not important for the application.