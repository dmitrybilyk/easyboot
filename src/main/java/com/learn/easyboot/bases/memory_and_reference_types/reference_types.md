Java memory consists of Stack and Heap. Both occupy the RAM.

Stack is quicker and memory allocation happens at
compile time. Stack persists methods and local variables, references to objects.
It frees up quickly at once method is over.

Heap keeps global objects. Memory allocation happens at runtime. It's unlimited in size. It consists of
Young and Old generation. Garbage collector frees up young generation at once.
But in old generation there is some more complicated algorithm.


Reference types:
Strong - usual. When there is no any reference to the object (when it's set to null for instance) 
the object is deleted from memory.
WeakReference - good to load the link to classloader.
GC will remove objects if just weak references are connected to it.
SoftReference - garbage collector will remove objects if there is a lack of memory 
(good for implementing cache).
PhantomReference - helpful if we just want to know if object will be removed now 
and memory will be allocated.

a SoftReference is like a customer that says: I’ll leave my table only when there are no other tables available.
A WeakReference is like someone ready to leave as soon as a new customer arrives.
A PhantomReference is like someone ready to leave as soon as a new customer arrives,
but actually not leaving until the manager gives him permission.