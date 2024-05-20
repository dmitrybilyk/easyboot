package com.learn.easyboot.bases.preply.serge;


import java.util.Set;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {

        Set<Person> persons = new TreeSet<>();
        persons.add(new Person("aaa"));
        persons.add(new Person("ccc"));
        persons.add(new Person("bbb"));
        System.out.println(persons);
    }

}

