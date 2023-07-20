package com.learn.easyboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
//@ComponentScan
//@ComponentScan("com.learn.easyboot.controllers")
// @Import(AppConfig.class)
public class EasyBootApplication {

	public static void main(String[] args) {
		SpringApplication.run(EasyBootApplication.class, args);
	}

}
