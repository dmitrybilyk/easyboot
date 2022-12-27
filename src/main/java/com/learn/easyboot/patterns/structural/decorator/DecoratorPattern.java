package com.learn.easyboot.patterns.structural.decorator;

public class DecoratorPattern {
	public static void main(String[] args) {
		TShirtProducer tShirtProducer = new WhaterProofTshirtDecorator(
			new ColorfulTshirtDecorator(
				new SimpleTShirtProducer()));
		tShirtProducer.produceTShirt();
	}
}

interface TShirtProducer {
	void produceTShirt();
}

class SimpleTShirtProducer implements TShirtProducer {
	public void produceTShirt() {
		System.out.println("Simple tshirt is produced");
	}
}

class BaseTShirtProducerDecorator implements TShirtProducer {
	protected TShirtProducer tShirtProducer;
	public BaseTShirtProducerDecorator(TShirtProducer tShirtProducer) {
		this.tShirtProducer = tShirtProducer;
	}

	public void produceTShirt() {
		tShirtProducer.produceTShirt();
	}
}

class ColorfulTshirtDecorator extends BaseTShirtProducerDecorator {
	public ColorfulTshirtDecorator(TShirtProducer tShirtProducer) {
		super(tShirtProducer);
	}
	public void produceTShirt() {
		super.produceTShirt();
		System.out.println("Added color");
	}
}


class WhaterProofTshirtDecorator extends BaseTShirtProducerDecorator {
	public WhaterProofTshirtDecorator(TShirtProducer tShirtProducer) {
		super(tShirtProducer);
	}
	public void produceTShirt() {
		super.produceTShirt();
		System.out.println("Added whater proof feature");
	}
}