package com.learn.easyboot.multithreading.deadlock;

public class DeadlockWaitingHimSelf {
    public static void main(String[] args) {
        deadlock();
    }

    public static void deadlock() {
        try {
            Thread t = new Thread(DeadlockWaitingHimSelf::deadlock);
            t.start();
            t.join();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}