package com.learn.easyboot.bases.preply.serge;

public class ChildMain extends Main{
    static {
        System.out.println("static block child"); //1
    }

    {
        System.out.println("block child"); //2
    }

    public ChildMain() {
        System.out.println("message from constructor child"); //3
    }

    public final static String SOME_CONSTANT = "ABC";
    private String a;

    public static void main(String[] args) {
        ChildMain main = new ChildMain();
    }

    private static void print(String request){
        System.out.println(request);
    }
}
