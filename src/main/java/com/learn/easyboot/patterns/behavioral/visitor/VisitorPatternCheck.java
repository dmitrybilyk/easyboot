
public class VisitorPatternCheck {
	public static void main(String[] args) {
		QuickCar quickCar = new QuickCar();
		quickCar.name = "quick car";
		quickCar.messageOfQuickCar = "- quick message";
		quickCar.speed = 100;

		Visitor visitor = new NameChangerVisitor();
		quickCar.accept(visitor);
		System.out.println(quickCar.name);

	}
}

abstract class Car {
	String name;
	int speed;
	abstract void accept(Visitor visitor);
}

class QuickCar extends Car {
	public String messageOfQuickCar;
	void printMessageOfQuickCar() {
		System.out.println(messageOfQuickCar);
	}
	void accept(Visitor visitor) {
		visitor.visitQuickCar(this);
	}
}

class SlowCar extends Car {
	public String messageOfSlowCar;
	void printMessageOfSlowCar() {
		System.out.println(messageOfSlowCar);
	}
	void accept(Visitor visitor) {
		visitor.visitSlowCar(this);
	}
}

interface Visitor {
	void visitQuickCar(QuickCar car);
	void visitSlowCar(SlowCar car);
}

class ImproveSpeedVisitor implements Visitor {
	public void visitQuickCar(QuickCar car) {
		car.speed += 20;
	}
	public void visitSlowCar(SlowCar car) {
		car.speed += 20;
	}
}


class NameChangerVisitor implements Visitor {
	public void visitQuickCar(QuickCar car) {
		car.name += car.messageOfQuickCar + "-changed";
	}
	public void visitSlowCar(SlowCar car) {
		car.name += car.messageOfSlowCar + "-changed";
	}
}