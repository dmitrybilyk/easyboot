package com.learn.easyboot;

import com.learn.easyboot.dao.repositories.BookRepository;
import com.learn.easyboot.models.entities.Book;
import org.easy.auto.GreeterAutoConfiguration;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.http.HttpStatus;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

@SpringBootApplication(exclude = GreeterAutoConfiguration.class)
@EnableJpaRepositories("com.learn.easyboot.dao.repositories")
@EntityScan("com.learn.easyboot.models.entities")
@EnableConfigurationProperties(EasyProperties.class)
//@ComponentScan
//@ComponentScan("com.learn.easyboot.controllers")
// @Import(AppConfig.class)
public class EasyBootApplication {

	public static void main(String[] args) {
		SpringApplication.run(EasyBootApplication.class, args);
	}

	@Bean
	public CommandLineRunner run(BookRepository bookRepository) throws Exception {
		return (String[] args) -> {
			Arrays.stream(args).forEach(System.out::println);
			Book book = new Book();
			book.setTitle("Good book1");
			book.setAuthor("Dmytro");
			Book book2 = new Book();
			book2.setTitle("Good book2");
			book2.setAuthor("Dmytro");
			bookRepository.save(book);
			bookRepository.save(book2);
			bookRepository.findAll().forEach(System.out::println);
		};
	}

}
