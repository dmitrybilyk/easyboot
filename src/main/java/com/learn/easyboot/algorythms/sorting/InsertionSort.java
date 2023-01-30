
public class InsertionSort {

	public static void main(String[] args) {
		int[] array = {3, 2, 6, 1, 0, 2};
		insertionSort(array);
	}

	public static void insertionSort(int[] array) {

	    for (int j = 1; j < array.length; j++) {
	        int current = array[j];
	        int i = j-1;
	        while ((i > -1) && (array[i] > current)) {
	            array[i+1] = array[i];
	            i--;
	        }
	        array[i+1] = current;
	    }

	    for (int i = 0; i < array.length; i++) {
	    	System.out.println(array[i]);
	    }
	}
}
