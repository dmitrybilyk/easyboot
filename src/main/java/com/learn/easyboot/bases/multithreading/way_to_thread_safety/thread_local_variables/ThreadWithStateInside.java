package com.learn.easyboot.bases.multithreading.way_to_thread_safety.thread_local_variables;

import java.util.Arrays;
import java.util.List;

public class ThreadWithStateInside extends Thread {
    
    private final List<String> letters = Arrays.asList("a", "b", "c", "d", "e", "f");
    
    @Override
    public void run() {
        letters.forEach(System.out::println);
    }
}