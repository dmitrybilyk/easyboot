package com.learn.easyboot.bases.multithreading.java_concurrent_package.executor_service.executor_interface;

import java.util.concurrent.Executor;


public class ExecutorDemo {
	public static void main(String[] args) {
		Executor executor = new ExecutorImpl();
		executor.execute(new RunnableImpl());
	}
}

class ExecutorImpl implements Executor {
	public void execute(Runnable runnable) {
		new Thread(runnable).start();
	}
}

class RunnableImpl implements Runnable {
	public void run() {
		System.out.println("Running something");
	}
}