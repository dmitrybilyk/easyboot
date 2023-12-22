package com.learn.easyboot.streams.reduce;

import com.google.common.collect.ImmutableList;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.stream.Collectors;

import static java.util.stream.Collectors.collectingAndThen;
import static java.util.stream.Collectors.counting;
import static java.util.stream.Collectors.groupingBy;
import static java.util.stream.Collectors.maxBy;
import static java.util.stream.Collectors.minBy;
import static java.util.stream.Collectors.partitioningBy;
import static java.util.stream.Collectors.teeing;
import static java.util.stream.Collectors.toList;

public class GroupBy {
    public static void main(String[] args) {
//        List<String> givenList = Arrays.asList("a", "bb", "cccy", "dd");
////        List<String> result = givenList.stream()
////                .collect(collectingAndThen(toList(), ImmutableList::copyOf));
//
//        Map<Integer, List<String>> groupedByLength = givenList.stream().collect(groupingBy(String::length));
//        List<String> partitioned = givenList.stream().collect(partitioningBy(s -> s.length() > 1))
//                .get(true);
//
////        HashMap<String, Integer> result = givenList.stream().collect(teeing(
////                minBy(Integer::compareTo), // The first collector
////                maxBy(Integer::compareTo),
////                (e1, e2) -> {
////                    HashMap<String, Integer> map = new HashMap();
////                    map.put("MAX", e1.get());
////                    map.put("MIN", e2.get());
////                    return map;
////                }));// Receives the result from those collectors and combines them
//
//
        List<Employee> employeeList = Arrays.asList(
                new Employee(1, "A", 100),
                new Employee(2, "B", 200),
                new Employee(3, "C", 200),
                new Employee(4, "D", 400));

//        System.out.println(employeeList.stream().collect(groupingBy(Employee::getSalary)));
//        System.out.println(employeeList.stream().collect(teeing((Collectors.maxBy(Comparator.comparing(Employee::getSalary))),
//                Collectors.maxBy(Comparator.comparing(Employee::getSalary)), employeeList)));
//
//        HashMap<String, Employee> result = employeeList.stream().collect(
//                Collectors.teeing(
//                        Collectors.maxBy(Comparator.comparing(Employee::getSalary)),
//                        Collectors.minBy(Comparator.comparing(Employee::getSalary)),
//                        (e1, e2) -> {
//                            HashMap<String, Employee> map = new HashMap();
//                            map.put("MAX", e1.get());
//                            map.put("MIN", e2.get());
//                            return map;
//                        }
//                ));
//
//        System.out.println(result);


    }
}


    @Getter
    @Setter
    @AllArgsConstructor
    @ToString
    class Employee {
        private int a;
        private String b;
        private Integer salary;
    }