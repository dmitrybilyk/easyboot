package com.learn.easyboot.camel.hello;

import org.apache.camel.builder.RouteBuilder;
import org.springframework.stereotype.Component;

@Component
public class HelloRestRoute extends RouteBuilder {

    @Override
    public void configure() throws Exception {
        restConfiguration().host("localhost").port(8707);
        from("timer:hello?period={{timer.period}}")
                .setHeader("id", simple("${random(6,9)}"))
                .to("rest:get:example/{id}")
                .log("${body}");
    }
}
