package com.learn.easyboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;

@SpringBootApplication
@EnableJpaRepositories("com.learn.easyboot.dao.repositories")
@EntityScan("com.learn.easyboot.models.entities")
//@ComponentScan
//@ComponentScan("com.learn.easyboot.controllers")
// @Import(AppConfig.class)
public class EasyBootApplication {

	public static void main(String[] args) {
		SpringApplication.run(EasyBootApplication.class, args);
	}

}
