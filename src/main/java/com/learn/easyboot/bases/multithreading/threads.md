50 questions:
http://www.journaldev.com/1162/java-multi-threading-concurrency-interview-questions-with-answers#thread-safety


The base means for concurrency are is the java.lang.Thread class.
A Thread executes an object of type java.lang.Runnable

Runnable is an interface which defines the run() method. This method is called
by the Thread object and contains the work which should be done. Therefore the
"Runnable" is the task to perform. The Thread is the worker who is doing
this task.

Process is a separate unit of work. It cant interact directly with other processes.
It shares data only via operation system. There are situations when process is quite
free, but it can't share this free memory with other processes. Thread can do this.
Thread is a 'lightweight' process. By default java application runs in single process
- thread. But you can adjust the application in order to optimize the memory usage.
Threads can share objects between each other. Tasks are divided into small subtasks
and could be performed in parallel.

Threads have their own call stack, but can also access shared data.
Therefore you have two basic problems, visibility and access problems.

A visibility problem occurs if thread A reads shared data which is later changed
by thread B and thread A is unaware of this change.

An access problem can occur if several thread access and change the same shared data
at the same time. Java provides locks to protect certain parts of the code to be
executed by several threads at the same time. The simplest way of locking a certain
method or Java class is to define the method or class with the synchronized
keyword.

The synchronized keyword in Java ensures:

    that only a single thread can execute a block of code at the same time

    that each thread entering a synchronized block of code sees the effects
    of all previous modifications that were guarded by the same lock

Synchronization is necessary for mutually exclusive access to blocks of and for
reliable communication between threads.

You can use the synchronized keyword for the definition of a method.
This would ensure that only one thread can enter this method at the same time.
Another threads which are calling this method would wait until the first thread
leaves this method.

public synchronized void critical() {
  // some thread critical stuff
  // here
}


You can also use the synchronized keyword to protect blocks of code within a method.
This block is guarded by a key, which can be either a string or an object.
This key is called the lock. All code which is protected by the same lock
can only be executed by one thread at the same time.

Volatile

If a variable is declared with the volatile keyword then it is guaranteed that
any thread that reads the field will see the most recently written value.
The volatile keyword will not perform any mutual exclusive lock on the variable.
All fields are cached in thread. In order to get actual data
(directly from register of memory) we use volatile.

Atomic operation

An atomic operation is an operation which is performed as a single unit of work
without the possibility of interference from other operations.


 The i++ operation first reads the value which is currently stored in i
 (atomic operations) and then it adds one to it  (atomic operation).
 But between the read and the write the value of i might have changed.

Since Java 1.5 the java language provides atomic variables, e.g. AtomicInteger
or AtomicLong which provide methods like getAndDecrement(), getAndIncrement()
and getAndSet() which are atomic.

The Java memory model guarantees that each thread entering a synchronized block of
code sees the effects of all previous modifications that were guarded by the same lock.


For all mutable fields, e.g. Arrays, that are passed from the outside to the
class during the construction phase, the class needs to make a defensive-copy
of the elements to make sure that no other object from the outside still
can change the data


Defensive Copies

You must protect your classes from calling code. Assume that calling
code will do its best to change your data in  way you didn't expect it.
While this is especially true in case of immutable data it is also true
for non-immutable data which you still not expect that this data is
changed outside your class.

To protect your class against that you should copy data you receive and
only return copies of data to calling code.



Thread pools with the Executor Framework

Thread pools manage a pool of worker threads. The thread pools contains
a work queue which holds tasks waiting to get executed.

A thread pool can be described as a collection of Runnable objects (work queue)
and a connections of running threads.

These threads are constantly running and are checking the work query for new work.
If there is new work to be done they execute this Runnable. The Executors class itself
provides a method, e.g. execute(Runnable r) to add a new Runnable object
to the work queue.


Futures and Callables

 In case you expect your threads to return a computed result you can use
 java.util.concurrent.Callable.
 The Callable object allows to return values after completion.

The Callable object uses generics to define the type of object which is returned.


Deadlock

A concurrent application has the risk of a deadlock. A set of processes are
deadlocked if all processes are waiting for an event which another process
in the same set has to cause.

For example if thread A waits for a lock on object Z which thread B holds and
thread B waits for a lock on object Y which is hold be process A then these two
processes are locked and cannot continue in their processing.

When working with Threads, it’s also possible to change the priority of a Thread.
In the Java Virtual Machine, the Thread scheduler, use a priority-based scheduling.
So if a Thread enters in Runnable state with a higher priority
than the running Thread, the new Thread will run and the current running
thread will be returned to Runnable state and waits for its turn. But this
behavior is not guaranteed and is completely depending on the virtual machine
you are working on.
So, do not rely on thread priorities, just use them to improve efficiency of your program.

 If you don’t specify a priority, the used priority, will be the priority of
 the current Thread.
 With help of yield() static method you can give an opotunity to other threads to run.
 (you turn current thread to Runnable (waiting for run) state). Also if you don't
 set a priority, the priority of current thread will be set to new  thread.
 But in practise you don't have to rely on priorities. They really unpredictable.



 Thread lifecycle:

- !New! is the thread state for a thread which was created but has not yet started.
- !Ready!. Thread scheduling decides when the thread could actually start
- A thread in the !runnable! state is executing from the JVM point of view but in
fact it may be waiting for some resources from the operating system.
- !Timed waiting! is a thread state for a thread waiting with a specified waiting time.
A thread is in the timed waiting state due to calling one of the following methods with
a specified positive waiting time:


    Thread.sleep(sleeptime)
    Object.wait(timeout)
    Thread.join(timeout)
    LockSupport.parkNanos(timeout)
    LockSupport.parkUntil(timeout)

- A thread is in the !waiting! state due to the calling one of the following
methods without timeout:


    Object.wait()
    Thread.join()
    LockSupport.park()


Note, that thread in the waiting state is waiting for another thread to perform
a particular action. For example, a thread that has called Object.wait() on
an object is waiting for another thread to call Object.notify() or Object.notifyAll()
on that object.

- Thread is in the !blocked! state while waiting for the monitor lock to enter a
synchronized block or method or to reenter a synchronized block or method after
calling Object.wait().


Java provides three methods that threads can use to communicate with each other:
wait, notify, and notifyAll. These methods are defined for all Objects (not just Threads).
The idea is that a method called by a thread may need to wait for some condition to be
satisfied by another thread; in that case, it can call the wait method, which causes its
thread to wait until another thread calls notify or notifyAll.




Thread Methods:

- static sleep(long millis)

Causes the currently executing thread to sleep (temporarily cease
execution) for the specified number of milliseconds.
The thread does not lose ownership of any monitors.

- static yield()

A hint to the scheduler that the current thread is willing to yield
its current use of a processor. The scheduler is free to ignore this
hint.

- join(long millis)

/**
     * Waits at most {@code millis} milliseconds for this thread to
     * die. A timeout of {@code 0} means to wait forever.
     *
     * <p> This implementation uses a loop of {@code this.wait} calls
     * conditioned on {@code this.isAlive}.

     @throws  InterruptedException
          *          if any thread has interrupted the current thread. The
          *          <i>interrupted status</i> of the current thread is
          *          cleared when this exception is thrown.


- interrupt()
* Interrupts this thread.


From Object:

- wait()

tells the calling thread to give up the monitor and go to sleep until some
other thread enters the same monitor and calls notify( ).

- notify()

wakes up the first thread that called wait() on the same object.



A thread pool manages the pool of worker threads, it contains a queue that
keeps tasks waiting to get executed.
We can specify the number of threads that will be alive when we create
ThreadPoolExecutor instance and we can limit the size of thread pool and
create our own RejectedExecutionHandler implementation to handle the jobs
that can’t fit in the worker queue.




Callable interface.
java.util.concurrent.Callable interface in concurrency package that is similar
to Runnable interface but it can return any Object and able to throw Exception.
Callable interface use Generic to define the return type of Object.
Executors class provide useful methods to execute Callable in a thread pool.
Since callable tasks run in parallel, we have to wait for the returned Object.
Callable tasks return java.util.concurrent.Future object. Using Future we can
find out the status of the Callable task and get the returned Object.
It provides get() method that can wait for the Callable to finish and then
return the result.

Future provides cancel() method to cancel the associated Callable task.
There is an overloaded version of get() method where we can specify the
time to wait for the result, it’s useful to avoid current thread getting
blocked for longer time. There are isDone() and isCancelled() methods to
find out the current status of associated Callable task.

What if we want to override some of the methods of Future interface, for example
overriding get() method to timeout after some default time rather than waiting
indefinitely, in this case FutureTask class comes handy that is the base
implementation of Future interface.
FutureTask is base concrete implementation of Future interface and provides
asynchronous processing. It contains the methods to start and cancel a
task and also methods that can return the state of the FutureTask as whether
it’s completed or cancelled. We need a callable object to create a future
task and then we can use Java Thread Pool Executor to process these asynchronously.


Fork join framework.

ForkJoinPool - it's a wrapper for ExecutorService. The number of threads in pool could be changed. And
you don't have to shutdown completed pool, because all it's threads are deamons.


ForkJoinTask
This is an abstract class for creating tasks that run within a ForkJoinPool. The Recursiveaction and
RecursiveTask are the only two direct, known subclasses of ForkJoinTask. The only difference between
these two classes is that the RecursiveAction does not return a value while RecursiveTask does have a
return value and returns an object of specified type.
In both cases, you would need to implement the compute method in your subclass that performs the main
computation desired by the task.
The ForkJoinTask class provides several methods for checking the execution status of a task. The isDone()
method returns true if a task completes in any way. The isCompletedNormally() method returns true if a task
completes without cancellation or encountering an exception, and isCancelled() returns true if the task was
cancelled. Lastly, isCompletedabnormally() returns true if the task was either cancelled or encountered an
exception.



Difference between Fork/Join Framework And ExecutorService

The main difference between the Fork/Join and the Executor frameworks is the work-stealing algorithm.
Unlike the Executor framework, when a task is waiting for the finalization of the sub-tasks it has
created using the join operation, the thread that is executing that task (called worker thread )
looks for other tasks that have not been executed yet and begins its execution. By this way, the
threads take full advantage of their running time, thereby improving the performance of the application.

