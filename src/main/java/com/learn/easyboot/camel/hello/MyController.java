package com.learn.easyboot.camel.hello;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.security.SecureRandom;

@RestController
public class MyController {
  @GetMapping(value = "/example/{id}")
  public String getRandomString(@PathVariable("id") Integer id) {
    return "Got " + randomString(id);
  }
  String randomString(int len) {
    String AB = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    SecureRandom rnd = new SecureRandom();
    StringBuilder sb = new StringBuilder(len);
    for (int i = 0; i < len; i++)
      sb.append(AB.charAt(rnd.nextInt(AB.length())));
    
    return sb.toString();
  }
}