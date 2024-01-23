package com.learn.easyboot.bases.interfaces_vs_abstract_classes.package_for_interface;

public interface SomeInterface {
    public static final int fieldInInterface = 30;
    void intPrint();
    default void printDefault() {
        System.out.println("some default");
    }
}
