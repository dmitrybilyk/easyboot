package com.learn.easyboot.patterns.creational.factory.simple_factory;

public class SimpleFactory {
    public static void main(String[] args) {
        User user = SimpleUserFactory.createUser("good");
    }
}

class User {}

class GoodUser extends User {}
class BadUser extends User {}

class SimpleUserFactory {
    public static User createUser(String param){
        if (param.equals("good")) {
            return new GoodUser();
        } else {
            return new BadUser();
        }
    }
}
