Java Memory model is divided on:

Stack memory:
Memory is allocated for methods executed in the thread, primitives and references on objects used in this thread.
If Stack memory is overfilled then StackOverFlow exception is occurring.

Heap memory:
Objects which has references on them are stored here. Instance members are here. Consists of:
- Young generation
- Survival space
- Old generation
- Perm Space 
- Metaspace