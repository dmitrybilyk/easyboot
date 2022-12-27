S ingle responsibility - every class should have just single reason to be changed. It's easier to change, test and read such class.
- Class `Book` and Class `PrintSomething` (from the book) should be separate. We can re-use `PrintSomething` btw

O pen/Closed principle - open for extension and Closed for modification
- Instead of modifying existing class we may extend it and change whatever we need

L iskov Substitution principle - We should be able the derived class anywhere we can use it's parent
I nterface Segregation - Should have more interfaces with less responsibility rather than to have single with everything
D ependency inversion principle - Classes should depend on abstractions, not on particular implementations