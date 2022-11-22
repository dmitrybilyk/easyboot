
public class StatePatternCheckTV {
	public static void main(String[] args) {
		TvSet tvSet = new TvSet();
		tvSet.changeState(new OnState());
		tvSet.showing();

		tvSet.changeState(new OffState());
		tvSet.showing();
	}
}

class TvSet {
	State state;
	public void changeState(State state) {
		this.state = state;
	}
	public void showing() {
		state.action();
	}
}

abstract class State {
	abstract void action();
}

class OnState extends State {
	public void action() {
		System.out.println("Tv is showing");
	}
}

class OffState extends State {
	public void action() {
		System.out.println("Tv is off");
	}
}