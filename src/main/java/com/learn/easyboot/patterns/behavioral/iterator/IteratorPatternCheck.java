import java.util.List;
import java.util.ArrayList;


public class IteratorPatternCheck {
	public static void main(String[] args) {
		CarsCollection carsCollection = new CarsCollectionImpl();
		Iterator iterator = carsCollection.iterator();
		while(iterator.hasNext()) {
			System.out.println(iterator.next());
		}
	}
}


class Car {
	private String name;
	public Car(String name) {
		this.name = name;
	}

	@Override
	public String toString() {
		return "car - " + name;
	}
}

interface Iterator {
	boolean hasNext();
	Car next();
}

class CarsIterator implements Iterator {
	private int currentPosition;
	CarsCollection cars = new CarsCollectionImpl();
	public CarsIterator() {
		cars.add(new Car("Opel"));
		cars.add(new Car("Honda"));
	}
	public boolean hasNext() {
		return currentPosition < cars.size();
	}
	public Car next() {
		Car car = cars.get(currentPosition);
		currentPosition++;
		return car;
	}
}

interface CarsCollection {
	Iterator iterator();
	void add(Car car);
	Car get(int index);
	int size();
}

class CarsCollectionImpl implements CarsCollection {
	List<Car> carsList = new ArrayList();
	public Iterator iterator() {
		return new CarsIterator();
	}

	public void add(Car car) {
		carsList.add(car);
	}

	public Car get(int index) {
		return carsList.get(index);
	}

	public int size() {
		return carsList.size();
	}
}