package com.learn.easyboot.bases.multithreading.way_to_thread_safety.synchronized_keyword;

import lombok.Getter;
import lombok.Setter;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.stream.IntStream;

@Getter
@Setter
public class SynchronizedMethods {

    private int sum = 0;

    public synchronized void calculate() {
        setSum(getSum() + 1);
    }

    // standard setters and getters

    public static void main(String[] args) throws InterruptedException {
        ExecutorService service = Executors.newFixedThreadPool(3);
        SynchronizedMethods summation = new SynchronizedMethods();

        IntStream.range(0, 1000)
                .forEach(count -> service.submit(summation::calculate));
        service.awaitTermination(1000, TimeUnit.MILLISECONDS);
        service.shutdown();
        System.out.println(summation.getSum());
    }

}