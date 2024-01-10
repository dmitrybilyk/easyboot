package com.learn.easyboot.multithreading.interrupting_a_thread;

import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread workerThread = new Thread(() -> {
            while (!Thread.currentThread().isInterrupted()) {
                try {
                    Thread.sleep(11000);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
                // Long running task
                IntStream.range(0, 100).forEach(System.out::println);
            }
            System.out.println("Thread is interrupted and exiting.");
        });

        workerThread.start();

        // we let it work for 10 seconds
        Thread.sleep(10000);

// Later in the code, we can stop the thread by interrupting it
        workerThread.interrupt();
    }
}
