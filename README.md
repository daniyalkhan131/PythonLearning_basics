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
