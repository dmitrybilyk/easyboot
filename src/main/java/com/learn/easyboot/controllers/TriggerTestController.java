package com.learn.easyboot.controllers;

import com.learn.easyboot.models.Human;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class TriggerTestController {

    @GetMapping("/trigger")
    public Human getHuman() {
        RestTemplate restTemplate = new RestTemplate();
        String fooResourceUrl
                = "http://172.17.0.2:8707/easy/get";
        ResponseEntity<Human> response
                = restTemplate.getForEntity(fooResourceUrl, Human.class);
        return response.getBody();
    }
}