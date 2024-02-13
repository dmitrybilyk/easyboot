package com.learn.easyboot;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.orm.jpa.vendor.Database;
import org.springframework.stereotype.Component;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;

@ConfigurationProperties(prefix = "easy")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Component
//@Component("easyProperties")
public class EasyProperties {
    private String param1;

    private DatabaseProperties database = new DatabaseProperties();

    @Data
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    public static class DatabaseProperties {
        @NotNull
        private Database type = Database.POSTGRESQL;
        @NotEmpty
        private String driver = "org.postgresql.Driver";
        @NotEmpty
        private String address = "jdbc:postgresql://localhost:5432/";
//        @Value("${easy.database.dbName}")
        private String dbName = "easy";
        @Value("${easy.database.username}")
        private String username;
        @Value("${easy.database.password}")
        private String password;
    }
}
