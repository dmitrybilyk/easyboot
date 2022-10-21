package com.learn.easyboot.conditions;

import com.learn.easyboot.dao.JdbcUserDAO;
import com.learn.easyboot.dao.MongoUserDAO;
import com.learn.easyboot.dao.UserDAO;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Conditional;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan
public class AppConfig
{
    @Bean
    @DatabaseType("MYSQL")
//    @Conditional(MySQLDatabaseTypeCondition.class)
    public UserDAO jdbcUserDAO(){
        return new JdbcUserDAO();
    }

    @Bean
    @DatabaseType("MONGO")
//    @Conditional(MongoDbTypePropertyCondition.class)
    public UserDAO mongoUserDAO(){
        return new MongoUserDAO();
    }
}