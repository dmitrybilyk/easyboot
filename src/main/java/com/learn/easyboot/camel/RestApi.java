package com.learn.easyboot.camel;

import org.apache.camel.Exchange;
import org.apache.camel.Processor;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.model.rest.RestBindingMode;
import org.springframework.stereotype.Component;

import javax.ws.rs.core.MediaType;

import static java.net.HttpURLConnection.HTTP_NO_CONTENT;
import static java.net.HttpURLConnection.HTTP_OK;
import static org.apache.camel.Exchange.HTTP_QUERY;
import static org.apache.camel.LoggingLevel.INFO;
import static org.apache.camel.model.rest.RestParamType.header;
import static org.apache.camel.model.rest.RestParamType.query;

@Component
public class RestApi extends RouteBuilder {

    @Override
    public void configure() {
        rest("/api/").description("Teste REST Service")
                .id("api-route")
                .post("/bean")
                .produces(MediaType.APPLICATION_JSON)
                .consumes(MediaType.APPLICATION_JSON)
                // .get("/hello/{place}")
                .bindingMode(RestBindingMode.auto)
                .type(MyBean.class)
                .enableCORS(true)
                // .outType(OutBean.class)

                .to("direct:remoteService");

        from("direct:remoteService").routeId("direct-route")
                .tracing()
                .log(">>> ${body.id}")
                .log(">>> ${body.name}")
//					 .transform().simple("blue ${in.body.name}")
                .process(new Processor() {
                    @Override
                    public void process(Exchange exchange) throws Exception {
                        MyBean bodyIn = (MyBean) exchange.getIn()
                                .getBody();

                        ExampleServices.example(bodyIn);

                        exchange.getIn()
                                .setBody(bodyIn);
                    }
                })
                .setHeader(Exchange.HTTP_RESPONSE_CODE, constant(201));

		rest()
				.get("/status")
				.description("Gets the status of the service")
				.outType(Integer.class)
				.responseMessage().code(HTTP_NO_CONTENT).message("If the service is working properly").endResponseMessage()
				.to("direct:getStatus");

		from("direct:getStatus")
				.routeId("GET@/status")
				.log(INFO, "Status called");


		rest()
				.get("v3/users")
				.description("Gets all users")
				.param().name("testParam").type(header).description("Test Param").endParam()
//				.param().name(HEADER_AUTHORIZATION).type(header).description("Authorization header").endParam()
				.responseMessage().code(HTTP_OK).message("The list of all users").endResponseMessage()
//				.responseMessage(UNAUTHORIZED_MESSAGE_DEFINITION)
				.outType(User[].class)
				.produces(MediaType.APPLICATION_JSON)
				.to("direct:getUsers");

		from("direct:getUsers").routeId("GET@/v3/users")
//				.process(this::verifyAuthorizationToken)
//				.removeHeaders("*", HEADER_AUTHORIZATION, TRACE_HEADERS_PATTERN)
//				.to(AuthorizationRouteBuilder.URI_AUTHORIZE_UNRESTRICTED_WITH_ABAC)
				.process(new Processor() {
					@Override
					public void process(Exchange exchange) throws Exception {
						System.out.println("debug");
					}
				})
				.process(this::validateTestParam)
				.to(UserRouteBuilder.URI_GET_ALL_USERS);
    }

	private void validateTestParam(Exchange exchange) {
		String testParam = exchange.getIn().getHeader("testParam", String.class);
		if (testParam.contains("test")) {
			throw new RuntimeException("Wrong param");
		}
	}
}