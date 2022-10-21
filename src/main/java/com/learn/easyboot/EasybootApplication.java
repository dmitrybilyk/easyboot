package com.learn.easyboot;

import com.learn.easyboot.conditions.AppConfig;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Import;

@SpringBootApplication
@Import(AppConfig.class)
public class EasybootApplication {

	public static void main(String[] args) {
		SpringApplication.run(EasybootApplication.class, args);
	}

}
