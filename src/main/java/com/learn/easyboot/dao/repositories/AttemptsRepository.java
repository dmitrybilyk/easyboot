package com.learn.easyboot.dao.repositories;

import java.util.Optional;

import com.learn.easyboot.models.entities.Attempts;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository; 

@Repository 
public interface AttemptsRepository extends JpaRepository<Attempts, Integer> { 
   Optional<Attempts> findAttemptsByUsername(String username);
}