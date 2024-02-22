package com.learn.easyboot.dao.repositories;

import com.learn.easyboot.models.entities.AppUser;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<AppUser, Long> {

    AppUser findByUsername(String username);
}