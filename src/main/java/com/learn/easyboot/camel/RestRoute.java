package com.learn.easyboot.camel;


import org.apache.camel.builder.RouteBuilder;
import org.springframework.stereotype.Component;
import org.apache.camel.model.rest.RestBindingMode;

/**
 * A Camel route that calls the REST service using a timer
 * <p/>
 * Use <tt>@Component</tt> to make Camel auto detect this route when starting.
 */
@Component
public class RestRoute extends RouteBuilder {

	@Override
	public void configure() throws Exception {

		restConfiguration().component("servlet").bindingMode(RestBindingMode.auto);

		rest().path("/rest").consumes("application/json").produces("application/json")
				.get("{name}").to("bean:serviceBean?method=hello(${headers.name})")

				 .post().type(User.class).outType(User.class)  
				 .to("bean:serviceBean?method=response");
		} 
		 

}