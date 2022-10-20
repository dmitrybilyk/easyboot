package com.learn.easyboot.controllers;

import com.learn.easyboot.models.Human;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController("/humans")
public class TestController {

    @GetMapping("/get")
    public Human getHuman() {
        return Human.builder().name("some name").build();
    }
}