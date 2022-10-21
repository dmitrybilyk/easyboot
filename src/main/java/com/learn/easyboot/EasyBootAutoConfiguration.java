package com.learn.easyboot;

import com.learn.easyboot.conditions.MongoDbTypePropertyCondition;
import com.learn.easyboot.conditions.MySQLDatabaseTypeCondition;
import com.learn.easyboot.dao.JdbcUserDAO;
import com.learn.easyboot.dao.MongoUserDAO;
import com.learn.easyboot.dao.UserDAO;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Conditional;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableConfigurationProperties
@ComponentScan
public class EasyBootAutoConfiguration
{
//    @Bean
////    @DatabaseType("MYSQL")
////    @Conditional(MySQLDatabaseTypeCondition.class)
//    public UserDAO jdbcUserDAO(){
//        return new JdbcUserDAO();
//    }
//
//    @Bean
////    @DatabaseType("MONGO")
//    @Conditional(MongoDbTypePropertyCondition.class)
//    public UserDAO mongoUserDAO(){
//        return new MongoUserDAO();
//    }
}