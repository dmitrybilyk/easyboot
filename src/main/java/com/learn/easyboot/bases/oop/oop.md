3......... Which principles of OOP do you know?
a) Abstraction
Abstraction is the process of modeling real world objects into programming language.
Hence interfaces and abstract classes are just two techniques used in this process.
We don't show the implementation details to the appUser, but just show him what he needs.
It's kind of 'details hiding'.

b) Encapsulation.
It's kind of data hiding. It's the process of binding together the code and data it manipulates.
It's the hiding of some important data with providing the interface to manipulate it in secure way.

c) Inheritance.
inheritance is the ability of a class to inherit data and behaviors from another class.
Note that only public and protected members of the superclass are inherited by
the subclass. The subclass can freely add new members to extend features of the superclass.
Inheritance is for reusing code. Using inheritance promotes the maintainability of the code.
Another reason for implementing inheritance is for the purpose of extensibility

What is association:
Association defines how objects are related to each other, know each other and use each other's functionality.
Two forms of association:
- composition - It is a “belongs-to” type of association. it's 'has-a' relationship
- aggregation - also 'has-a' relationship but here objects could exist independently

d) Polymorphism.
Polymorphism means ‘many forms’. In OOP, polymorphism means a type can point to
different object at different time. In other words, the actual object to which
a reference type refers, can be determined at runtime.

Polymorphism is a robust feature of OOP. It increases the re-usability,
flexibility and extensibility of code. Take the above example for instance:
Re-usability: the teach() method can be re-used for different kinds of objects as
long as they are sub types of the Animal interface.
Flexibility: the actual object can be determined at runtime which allows the code
run more flexibly.
Extensibility: when we want to add a new kind of Animal, e.g. Snake, we just pass
an object of Snake into the teach() method without any modification.

4......... In which forms inheritance could be implemented in Java?

In Java, inheritance can be implemented in three forms:
- A class inherits another class
- A class implements another interface
- An interface inherits another interface

5......... Which types of Polymorphism exist in Java?
1) static - methods overloading
2) dynamic - methods overriding