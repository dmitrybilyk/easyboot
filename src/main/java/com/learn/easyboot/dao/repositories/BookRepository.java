package com.learn.easyboot.dao.repositories;

import com.learn.easyboot.models.entities.Book;
import org.springframework.data.repository.CrudRepository;

import java.util.List;

public interface BookRepository extends CrudRepository<Book, Long> {
    List<Book> findByTitle(String title);
}