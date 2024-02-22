package com.learn.easyboot;

import com.learn.easyboot.dao.repositories.BookRepository;
import com.learn.easyboot.dao.repositories.UserRepository;
import com.learn.easyboot.models.entities.Book;
//import org.easy.auto.GreeterAutoConfiguration;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.Arrays;

@SpringBootApplication
//@SpringBootApplication(exclude = GreeterAutoConfiguration.class)
@EnableJpaRepositories("com.learn.easyboot.dao.repositories")
@EntityScan("com.learn.easyboot.models.entities")
@EnableConfigurationProperties(EasyProperties.class)
//@ComponentScan
//@ComponentScan("com.learn.easyboot.controllers")
// @Import(AppConfig.class)
public class EasyBootApplication {

	@Autowired
	private PasswordEncoder passwordEncoder;

	public static void main(String[] args) {
		SpringApplication.run(EasyBootApplication.class, args);
	}

	@Bean
	public CommandLineRunner run(BookRepository bookRepository, UserRepository userRepository) throws Exception {
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

//			User user = new User();
//			user.setId(1L);
//			user.setUsername("db-user");
//			user.setPassword(passwordEncoder.encode("password"));
//			userRepository.save(user);
		};
	}

}
