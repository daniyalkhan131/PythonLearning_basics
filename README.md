# PythonLearning_basics
learn python from starting, all things are defined with comments


Method Resolution Order (MRO)
Whenever you create a class, Python sets a Method Resolution Order, or MRO, for that class, which is the order in which Python will look for methods on instances of that class.
You can programmatically reference the MRO three ways:
• mro_ attribute on the class
• use the mro) method onhhe class
• use the builtin help(cls) method


polymorphism-
1. The same class method works in a similar way for different classes
A common implementation of this is to have a method in a base (or parent) class that is overridden by a subclass. This is called method overriding.
• Each subclass will have a different implementation of the method.
• If the method is not implemented in the subclass, the version in the parent class is called instead.


2.  The same operation works for different kinds of objects
The answer is "special methods"!
Python classes have special (also known as "magic") methods, that are dunders (i.e. double underscore-named).
These are methods with special names that give instructions to Python for how to deal with objects.


+ operator is speacial method called __add__() that get called on the first operand
If the first (left) operand is an instance of int, __add__() does mathematical addition. If it's a string, it does string concatenation.

Therefore, you can declare special methods on your own classes to mimic
the behavior of builtin objects, like so using __len__

The __repr__ method is one of several ways to provide a 
nicer string representation:

Decorators are examples of higher order functions
• Decorators have their own syntax, using "@" (syntactic sugar)

