package com.learn.easyboot.camel;

import com.fasterxml.jackson.databind.ObjectMapper;
//import com.zoomint.encourage.common.model.user.UserProfileInfoList;
import org.apache.camel.Exchange;
import org.apache.camel.Processor;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.component.jackson.JacksonDataFormat;
import org.apache.camel.spi.DataFormat;
import org.jetbrains.annotations.NotNull;
import org.springframework.stereotype.Component;

import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.function.Function;

import static org.apache.camel.LoggingLevel.INFO;
import static org.apache.camel.builder.AggregationStrategies.flexible;
import static org.springframework.util.StringUtils.hasText;

@Component
public class UserRouteBuilder extends RouteBuilder {

	public static final String URI_GET_ALL_USERS = "direct:wsAllUsers";
	public static final String URI_SINGLE_USER = "direct:wsSingleUser";
	public static final String URI_GET_USERS_BY_DETAILS = "direct:wsUsersByDetails";
	private static final int PARAMETER_DETAIL_MINIMAL_LENGTH = 2;

	private final ObjectMapper objectMapper;

	public UserRouteBuilder(ObjectMapper objectMapper) {
		this.objectMapper = objectMapper;
	}

	@Override
	public void configure() {

		DataFormat jsonAny = new JacksonDataFormat(objectMapper, Object.class); //NOPMD

		from(URI_GET_ALL_USERS)
				.log(INFO, "Getting all users")
				.log("${body}")
				.to(KeycloakRouteBuilder.URI_LOAD_ALL_KC_USERS)
				.log(INFO, "Getting all users: ${body}")
				.process(new Processor() {
					@Override
					public void process(Exchange exchange) throws Exception {
						System.out.println("put a breakpoint here");
					}
				})
//				.transform().body(users -> Map.of("_embedded", Map.of("users", users)))
				.process(new Processor() {
					@Override
					public void process(Exchange exchange) throws Exception {
						System.out.println("put a breakpoint here");
					}
				})
				.setProperty("USERS_MAP").body()
				.transform().body(Map.class, UserRouteBuilder::getRoles)
				.process(new Processor() {
					@Override
					public void process(Exchange exchange) throws Exception {
						System.out.println("put a breakpoint here");
					}
				})
				.setBody().exchangeProperty("USERS_MAP")
				.process(new Processor() {
					@Override
					public void process(Exchange exchange) throws Exception {
						System.out.println("put a breakpoint here");
					}
				})
				.filter(exchange -> {
					List<User> users = exchange.getIn().getBody(List.class);
					return users.get(0).getEmail() != null;
				})
				.enrich(URI_SINGLE_USER, flexible(User.class).storeInProperty("SINGLE_USER"))
				.process(new Processor() {
					@Override
					public void process(Exchange exchange) throws Exception {
						System.out.println("put a breakpoint here");
					}
				})
				.marshal(jsonAny)
		;

		from(URI_SINGLE_USER)
				.log(INFO, "Getting single user")
				.setBody(exchange -> User.builder().userId("singleUserId").build())
//				.marshal(jsonAny)
		;

//		from(URI_GET_USERS_BY_DETAILS)
//				.log(DEBUG, "Getting users by details")
//				.setBody().exchange(exchange -> exchange.getIn().getHeader("text"))
//				.process().body(String.class, this::verifyValidTextHeader)
//				.to(KeycloakRouteBuilder.URI_LOAD_KC_USERS_BY_FULLTEXT)
//				.log(DEBUG, "Getting users: ${body}")
//				.transform().body(List.class, UserProfileInfoList::new)
//				.marshal(jsonAny)
//		;
	}

	@NotNull
	private static List<Role> getRoles(Map usersMap) {
		return Collections.singletonList(Role.builder().build());
	}

	private void verifyValidTextHeader(String textHeader) {
		if (!hasText(textHeader)) {
			throw new IllegalArgumentException("Parameter 'text' must be present and must not be empty.");
		}
		if (textHeader.length() < PARAMETER_DETAIL_MINIMAL_LENGTH) {
			throw new IllegalArgumentException("Parameter 'text' must have at least 2 characters.");
		}
	}
}
