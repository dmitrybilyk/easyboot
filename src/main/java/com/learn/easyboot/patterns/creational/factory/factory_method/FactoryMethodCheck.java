public class FactoryMethodCheck {
	public static void main(String[] args) {
		CoctailMaker coctailMaker;
		String whatClientWants = "milk";
		if (whatClientWants.equals("hot")) {
			coctailMaker = new HotCoctailMaker();
		} else if (whatClientWants.equals("milk")) {
			coctailMaker = new MilkCoctailMaker();
		} else {
			coctailMaker = new ColdCoctailMaker();
		}
		coctailMaker.prepareForMaking();
		Coctail coctail = coctailMaker.makeCoctail();
		System.out.println(coctail.name);
	}
}

abstract class CoctailMaker {
	// could be much more logic common for both types of the product (coctail)
	void prepareForMaking() {
		System.out.println("preparing for making");
	}
	abstract Coctail makeCoctail();
}

class HotCoctailMaker extends CoctailMaker {
	public Coctail makeCoctail() {
		System.out.println("hot coctail is created");
		Coctail coctail = new ColdCoctail();
		coctail.name = "hot coctail";
		return coctail;
	}
}

class ColdCoctailMaker extends CoctailMaker {
	public Coctail makeCoctail() {
		System.out.println("cold coctail is created");
		Coctail coctail = new ColdCoctail();
		coctail.name = "cold coctail";
		return coctail;
	}
}

class MilkCoctailMaker extends CoctailMaker {
	public Coctail makeCoctail() {
		System.out.println("milk coctail is created");
		Coctail coctail = new MilkCoctail();
		coctail.name = "milk coctail";
		return coctail;
	}
}

class Coctail {
	public String name;
}

class HotCoctail extends Coctail {
}

class ColdCoctail extends Coctail {
}

class MilkCoctail extends Coctail {
}