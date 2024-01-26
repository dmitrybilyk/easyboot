package com.learn.easyboot.spring.bean_lifecycle;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.BeanFactoryAware;
import org.springframework.beans.factory.BeanNameAware;
import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.beans.factory.config.BeanPostProcessor;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.stereotype.Component;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

public class SomeBean implements BeanNameAware, BeanFactoryAware, ApplicationContextAware,
        BeanPostProcessor, InitializingBean, DisposableBean {
    private String name;
    private AnotherSomeBean anotherSomeBean;

    public SomeBean() {
        System.out.println("1 - Constructor");
    }

    public void setAnotherSomeBean(AnotherSomeBean anotherSomeBean) {
        System.out.println("2 - Setter");
        this.anotherSomeBean = anotherSomeBean;
    }

    public SomeBean(String name) {
        System.out.println("1 - Constructor Really used with Name");
        this.name = name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("6 - Bean Post Processor - before initialization");
        return BeanPostProcessor.super.postProcessBeforeInitialization(bean, beanName);
    }

    @Override
    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("6 - Bean Post Processor - after initialization");
        return BeanPostProcessor.super.postProcessAfterInitialization(bean, beanName);
    }

    @PostConstruct
    public void initMethod() {
        System.out.println("7 - Post Construct Annotation");
    }

    @PreDestroy
    public void destroyMethod() {
        System.out.println("10 - PreDestroy Annotation");
    }

//    @PostConstruct
    public void customInitMethod() {
        System.out.println("9 - Custom Init Method");
    }

//    @PreDestroy
    public void customDestroyMethod() {
        System.out.println("12 - Custom Destroy Method");
    }

    @Override
    public void setBeanName(String s) {
        System.out.println("3 - Bean name " +  s);
    }

    @Override
    public void setBeanFactory(BeanFactory beanFactory) throws BeansException {
        System.out.println("4 - Bean Factory Aware");
    }

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        System.out.println("5 - Application Context Aware");
    }

    @Override
    public void afterPropertiesSet() throws Exception {
        System.out.println("8 - Initializing Bean - afterPropertiesSet");
    }

    @Override
    public void destroy() throws Exception {
        System.out.println("11 - DisposableBean");
    }
}
