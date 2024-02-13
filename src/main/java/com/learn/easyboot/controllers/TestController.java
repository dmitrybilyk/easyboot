package com.learn.easyboot.controllers;

import com.learn.easyboot.EasyProperties;
import com.learn.easyboot.dao.UserDAO;
import com.learn.easyboot.models.Human;
import org.easy.auto.Greeter;
import org.springframework.beans.BeansException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.core.env.Environment;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDateTime;

@RestController
public class TestController implements ApplicationContextAware {

    @Autowired
    private Environment env;

    @Autowired
    private EasyProperties easyProperties;

//    @Autowired
//    private Greeter greeter;

    @Value("#{someBean.name}")
    private String someBeanName;
    @Value("${params.parameter2}")
    private String parameter2;
    @Value("${params.parameter1}")
    private Integer parameter1;
    @Value("${params.noneexisting:defaultValue}")
    private String noneExisting;
    private ApplicationContext applicationContext;

    @Qualifier("jdbcUserDAO")
    @Autowired(required = false)
    private UserDAO userDAO;

    @Value("${params.parameter2}")
    private String name;

    @GetMapping("/get")
    public Human getHuman() {
//        System.out.println(greeter.greet());
//        EasyProperties easyProperties = (EasyProperties) applicationContext.getBean("easyProperties");

//        userDAO.getAllUserNames().forEach(System.out::println);
        return Human.builder()
                .name("some name2 - " + name + parameter2 + someBeanName + noneExisting +
                env.getProperty("params.parameter2") + parameter1)
                .now(LocalDateTime.now())
                .build();
    }

    @GetMapping("/get/error")
    public Human getHumanWithError() {
        EasyProperties easyProperties = (EasyProperties) applicationContext.getBean("easyProperties");
        throw new RuntimeException("some exception");
//        userDAO.getAllUserNames().forEach(System.out::println);
//        return Human.builder().name("some name2 - " + name + parameter2 + someBeanName + noneExisting +
//                env.getProperty("params.parameter2") + parameter1).build();
    }

    @Override
    public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
        this.applicationContext = applicationContext;
        System.out.println(applicationContext.getApplicationName());
    }
}