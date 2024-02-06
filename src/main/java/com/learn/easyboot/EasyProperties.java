package com.learn.easyboot;

import lombok.Getter;
import lombok.Setter;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@ConfigurationProperties(prefix = "easy")
@Getter
@Setter
@Component("easyProperties")
public class EasyProperties {
    private String param1;
}
