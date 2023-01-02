import java.io.*;

public class BlockSyncDemo {
	public static void main(String[] args) {
		// Object of Line class that is shared
        // among the threads.
        Line obj = new Line();
  
        // creating the threads that are
        // sharing the same Object.
        Train train1 = new Train(obj);
        Train train2 = new Train(obj);
  
        // threads start their execution.
        train1.start();
        train2.start();
	}
}

class Line
{
    // It's better to get lock on the  final field so that it's object is not changed and synchronization is
    //not get broken
    private final Object mutator = new Object();

    public void getLine()
    {
        synchronized(mutator) {
        for (int i = 0; i < 3; i++)
        {
            System.out.println(i);
            try
            {
                Thread.sleep(1000);
            }
            catch (Exception e)
            {
                System.out.println(e);
            }
        }
        // try
        //     {
        //         Thread.sleep(100);
        //     }
        //     catch (Exception e)
        //     {
        //         System.out.println(e);
        //     }
        }
    }

    public synchronized void getLine2() {
        synchronized(mutator) {
            System.out.println("getLine2");
        }
     }
}   

  
class Train extends Thread
{
    // reference to Line's Object.
    Line line;
  
    Train(Line line)
    {
        this.line = line;
    }
  
    @Override
    public void run()
    {
        line.getLine();
        line.getLine2();
    }
}