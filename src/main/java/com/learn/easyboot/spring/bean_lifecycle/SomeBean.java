package com.learn.easyboot.spring.bean_lifecycle;

import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

@Component
public class SomeBean {
    @PostConstruct
    public void initMethod() {
        System.out.println(" in init method");
    }

    @PreDestroy
    public void destroyMethod() {
        System.out.println(" in destroy method");
    }
}
