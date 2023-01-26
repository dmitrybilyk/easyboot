
public class BubbleSortTry {
	public static void main(String[] args) {
		int[] arrayToSort = {4, 2, 1, 7, 3};
		int length = arrayToSort.length;

		for(int i = 0; i < length - 1; i++) {
			for (int j = 0; j < length - i - 1; j++) {
				if (arrayToSort[j] > arrayToSort[j + 1]) {
					int temp = arrayToSort[j + 1];
					arrayToSort[j + 1] = arrayToSort[j];
					arrayToSort[j] = temp;
				}
			}
		}

		for (int i = 0; i < arrayToSort.length; i++) {
			System.out.println(arrayToSort[i]);
		}

		
	}
}