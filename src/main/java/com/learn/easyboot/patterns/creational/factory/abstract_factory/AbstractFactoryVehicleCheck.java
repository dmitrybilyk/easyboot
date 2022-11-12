package com.learn.easyboot.patterns.creational.factory.abstract_factory;

public class AbstractFactoryVehicleCheck {
    public static void main(String[] args) {
        String sizeName = "big";
        ShowRunner showRunner = new ShowRunner();
        showRunner.setRaceSizeAbstractFactory(new MiddleSizeRaceAbstractFactory());
        showRunner.configure(sizeName);
        showRunner.runShow();
    }
}

class ShowRunner {
    private RaceSizeAbstractFactory raceSizeAbstractFactory;
    private Car car;
    private MotoBike motoBike;

    public void setRaceSizeAbstractFactory(RaceSizeAbstractFactory raceSizeAbstractFactory) {
        this.raceSizeAbstractFactory = raceSizeAbstractFactory;
    }

    void configure(String sizeName) {
        car = raceSizeAbstractFactory.createCar();
        motoBike = raceSizeAbstractFactory.createMotoBike();
    }

    public void runShow() {
        car.drive();
        motoBike.motoDrive();
    }
}


interface RaceSizeAbstractFactory {
    Car createCar();
    MotoBike createMotoBike();
}

class BigSizeRaceAbstractFactory implements RaceSizeAbstractFactory {

    @Override
    public Car createCar() {
        return new BigCar();
    }

    @Override
    public MotoBike createMotoBike() {
        return new BigMotoBike();
    }
}

class SmallSizeRaceAbstractFactory implements RaceSizeAbstractFactory {

    @Override
    public Car createCar() {
        return new SmallCar();
    }

    @Override
    public MotoBike createMotoBike() {
        return new SmallMotoBike();
    }
}
class MiddleSizeRaceAbstractFactory implements RaceSizeAbstractFactory {

    @Override
    public Car createCar() {
        return new MiddleSizeCar();
    }

    @Override
    public MotoBike createMotoBike() {
        return new MiddleSizeMotoBike();
    }
}

interface Car {
    void drive();
}

class BigCar implements Car {

    @Override
    public void drive() {
        System.out.println("riding a big car");
    }
}

class SmallCar implements Car {

    @Override
    public void drive() {
        System.out.println("riding a small car");
    }
}
class MiddleSizeCar implements Car {

    @Override
    public void drive() {
        System.out.println("riding a middle size car");
    }
}

interface MotoBike {
    void motoDrive();
}

class BigMotoBike implements MotoBike {

    @Override
    public void motoDrive() {
        System.out.println("riding a big motobike");
    }
}

class SmallMotoBike implements MotoBike {

    @Override
    public void motoDrive() {
        System.out.println("riding a small motobike");
    }
}

class MiddleSizeMotoBike implements MotoBike {

    @Override
    public void motoDrive() {
        System.out.println("riding a middle size motobike");
    }
}

