import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;
import java.util.function.Function;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;

public class FutureDemo {

	private static void tryFuture() throws InterruptedException, ExecutionException {
		CallableTask callableTask = new CallableTask();
		ScheduledExecutorService executorService = Executors.newSingleThreadScheduledExecutor();
		Future<String> resultFuture = executorService.schedule(callableTask, 1, TimeUnit.SECONDS);
			// try {
			// 	String result = resultFuture.get();
			// 	System.out.println("Result - " + result);
			// } catch (InterruptedException|ExecutionException ex) {

			// }
		Thread.sleep(6000);
		System.out.println("After some pause");
			System.out.println("Result - " + resultFuture.get());
			System.out.println("After future");
			executorService.shutdownNow();
	}


	public static void main(String... args) throws InterruptedException, ExecutionException {
		tryFuture();
	}

}

class CallableTask implements Callable<String> {
    @Override
    public String call() throws Exception {
    	Thread.sleep(5000);
        return "Returning for future";
    }
}

