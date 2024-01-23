package com.learn.easyboot.bases.exceptions;

import java.io.IOException;

public class SomeUsefulContext {
    public void someAction(int value) throws MyCustomException{
        if (value == 0) {
            throw new MyCustomException("value is " + 0);
        }
        System.out.println(value);
    }
}
