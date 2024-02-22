package com.learn.easyboot.configuration.security;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@Profile("db-security")
public class DBSecurityConfig {
   @Bean 
   public PasswordEncoder passwordEncoder() { 
      return new BCryptPasswordEncoder(); 
   } 

   @Bean
   public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
      http
              .csrf().disable()
              .authorizeRequests().antMatchers("/register**")
              .permitAll() .anyRequest().authenticated()
              .and()
              .formLogin() .loginPage("/login")
              .permitAll()
              .and()
              .logout() .invalidateHttpSession(true)
              .clearAuthentication(true) .permitAll();
      return http.build();
   }
}