package com.learn.easyboot.bases.preply.serge;

import lombok.AllArgsConstructor;
import org.jetbrains.annotations.NotNull;

@AllArgsConstructor
class Person implements Comparable<Person> {
    private String name;


    @Override
    public int compareTo(@NotNull Person o) {
//        return (a,b)-> a.compareTo();
        return 0;
    }


//    @Override
//    public int hashCode() {
//        return super.hashCode();
//    }
//
//    @Override
//    public boolean equals(Object obj) {
//        return super.equals(obj);
//    }

    @Override
    public String toString() {
        return super.toString();
    }
}