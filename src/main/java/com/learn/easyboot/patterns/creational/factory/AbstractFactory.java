package com.learn.easyboot.patterns.creational.factory;

public class AbstractFactory {
    public static void main(String[] args) {
        Client client = new Client(new WinControlsFactory());
        Button button = client.createButton();
        CheckBox checkBox = client.createCheckBox();
        button.click();
        checkBox.tick();
    }
}

class Client {
    private ControlsAbstractFactory abstractFactory;

    public Client(ControlsAbstractFactory abstractFactory) {
        this.abstractFactory = abstractFactory;
    }

    public Button createButton() {
        return abstractFactory.createButton();
    }
    public CheckBox createCheckBox() {
        return abstractFactory.createCheckBox();
    }
}

interface Button {
    void click();
}

class WinButton implements Button {

    @Override
    public void click() {
        System.out.println("win button clicks");
    }
}
class MacButton implements Button {

    @Override
    public void click() {
        System.out.println("mac button clicks");
    }
}

interface CheckBox {
    void tick();
}

class WinCheckBox implements CheckBox {

    @Override
    public void tick() {
        System.out.println("win checkbox ticks");
    }
}

class MacCheckBox implements CheckBox {

    @Override
    public void tick() {
        System.out.println("mac checkbox ticks");
    }
}

interface ControlsAbstractFactory {
    Button createButton();
    CheckBox createCheckBox();
}

class WinControlsFactory implements ControlsAbstractFactory {

    @Override
    public Button createButton() {
        return new WinButton();
    }

    @Override
    public CheckBox createCheckBox() {
        return new WinCheckBox();
    }
}

class MacControlsFactory implements ControlsAbstractFactory {

    @Override
    public Button createButton() {
        return new MacButton();
    }

    @Override
    public CheckBox createCheckBox() {
        return new MacCheckBox();
    }
}