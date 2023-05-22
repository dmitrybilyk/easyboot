package com.learn.easyboot;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in) ;

        System.out.println("input first number : ");
        int x = scanner.nextInt();
        System.out.println("input second number : ");
        int y = scanner.nextInt();
        int binary = Integer.parseInt(Integer.toBinaryString(x+y));
        System.out.println(binary);



    }
}
