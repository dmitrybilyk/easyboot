package com.learn.easyboot.multithreading.way_to_thread_safety.reentrant.stamped_lock;

import lombok.Getter;
import lombok.Setter;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.StampedLock;
import java.util.stream.IntStream;

@Getter
@Setter
public class StampedLockCounter {
    private int counter;
    private StampedLock lock = new StampedLock();
    public void incrementCounter() {
        long stamp = lock.readLock();
        try {
            counter++;
        } finally {
            lock.unlock(stamp);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        ExecutorService service = Executors.newFixedThreadPool(3);
        StampedLockCounter reentrantLockCounter = new StampedLockCounter();

        IntStream.range(0, 1000)
                .forEach(count -> service.submit(reentrantLockCounter::incrementCounter));
        service.awaitTermination(1000, TimeUnit.MILLISECONDS);
        service.shutdown();
        System.out.println(reentrantLockCounter.getCounter());
    }
}
