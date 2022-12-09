package com.learn.easyboot.controllers;

import com.learn.easyboot.dao.UserDAO;
import com.learn.easyboot.models.Human;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController("/humans")
public class TestController {

    @Qualifier("jdbcUserDAO")
    @Autowired(required = false)
    private UserDAO userDAO;

    @GetMapping("/get")
    public Human getHuman() {
        userDAO.getAllUserNames().forEach(System.out::println);
        return Human.builder().name("some name").build();
    }
}