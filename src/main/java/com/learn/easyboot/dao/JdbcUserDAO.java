package com.learn.easyboot.dao;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Repository;

import java.util.Arrays;
import java.util.List;

//@Repository
//@Primary
public class JdbcUserDAO implements UserDAO
{
    @Override
    public List<String> getAllUserNames()
    {
          System.out.println("**** Getting usernames from RDBMS *****");
          return Arrays.asList("Siva","Prasad","Reddy");
    }
}