//package com.learn.easyboot.services.security;
//
//import java.util.Optional;
//
//import com.learn.easyboot.dao.repositories.UserRepository;
//import com.learn.easyboot.models.entities.AppUser;
//import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.security.core.userdetails.UserDetails;
//import org.springframework.security.core.userdetails.UserDetailsService;
//import org.springframework.security.core.userdetails.UsernameNotFoundException;
//import org.springframework.security.provisioning.UserDetailsManager;
//import org.springframework.stereotype.Service;
//
//@Service
//public class SecurityUserDetailsService implements UserDetailsService {
//   @Autowired
//   private UserRepository userRepository;
//
//   @Override
//   public UserDetails loadUserByUsername(String username)
//   throws UsernameNotFoundException {
//      AppUser user = userRepository.findByUsername(username)
//         .orElseThrow(() -< new UsernameNotFoundException("User not present"));
//         return user;
//   }
//   public void createUser(UserDetails user) {
//      userRepository.save((AppUser) user);
//   }
//}
//
