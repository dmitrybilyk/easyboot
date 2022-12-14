package com.learn.easyboot.dao;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Repository;

import java.util.Arrays;
import java.util.List;

//@Repository
//@Primary
public class MongoUserDAO implements UserDAO
{
    @Override
    public List<String> getAllUserNames()
    {
          System.out.println("**** Getting usernames from MongoDB *****");
          return Arrays.asList("Bond","James","Bond");
    }
}