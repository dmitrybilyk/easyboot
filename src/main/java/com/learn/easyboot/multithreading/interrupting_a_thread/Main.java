package com.learn.easyboot.multithreading.interrupting_a_thread;

import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread workerThread = new Thread(() -> {
            while (!Thread.currentThread().isInterrupted()) {
//                try {
                    IntStream.range(0, 10000000).forEach(System.out::println);
//                    Thread.sleep(3000);
//                } catch (InterruptedException e) {
////                    System.out.println("interrupt exception");
//                    throw new RuntimeException(e);
//                }
                // Long running task
//                IntStream.range(0, 100).forEach(System.out::println);
            }
            System.out.println("Thread is interrupted and exiting.");
        });

        workerThread.start();

        // we let it work for 1 second
        Thread.sleep(1000);

        // Later in the code, we can stop the thread by interrupting it
//        try {
            workerThread.interrupt();
//        } catch (RuntimeException e) {
//            System.out.println("Runtime exception");
//        }
    }
}
