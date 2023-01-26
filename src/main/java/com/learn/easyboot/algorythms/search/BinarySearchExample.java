
public class BinarySearchExample {
	public static void main(String[] args) {
		int[] array = {3, 5, 1, 7, 10};
		binarySearch(array, 7);
	}

	private static void binarySearch(int[] array, int key) {
		int first = 0;
		int last = array.length - 1;
		int mid = (first + last) / 2;

		while(first <= last) {
			if (mid == key) {
			System.out.println("Found at " + mid);
		} else if (mid >= key) {
			System.out.println(mid);
			last = mid;
		} else {
			System.out.println(mid);
			first = mid + 1;
		}
		mid = (first + last) / 2;
		}

		
	}
}