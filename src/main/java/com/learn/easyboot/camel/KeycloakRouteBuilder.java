package com.learn.easyboot.camel;

import com.google.common.base.Strings;
import com.google.common.collect.Iterables;
//import com.zoomint.encourage.common.exceptions.database.EntityNotFoundDatabaseException;
//import com.zoomint.encourage.common.model.search.SearchTemplate;
//import com.zoomint.encourage.common.model.search.SearchTemplateList;
//import com.zoomint.encourage.framework.data.model.Activities;
//import com.zoomint.encourage.framework.data.model.QmApplication;
//import com.zoomint.encourage.model.search.ClientConversationSearch;
//import com.zoomint.keycloak.clienttokenprovider.ClientTokenProvider;
//import com.zoomint.keycloak.lib.common.rest.exceptions.NotFoundException;
//import com.zoomint.keycloak.lib.common.rest.paging.PageRequest;
//import com.zoomint.keycloak.provider.api.client.KeycloakApiProviderClient;
//import com.zoomint.keycloak.provider.api.client.exceptions.KeycloakApiProviderClientException;
//import com.zoomint.keycloak.provider.api.dto.Group;
//import com.zoomint.keycloak.provider.api.dto.UserInfo;
//import com.zoomint.keycloak.provider.api.dto.UserLookup;
//import com.zoomint.keycloak.provider.api.dto.UserProfileInfo;
//import com.zoomint.keycloak.users.api.provider.client.UsersClient;
import org.apache.camel.Exchange;
import org.apache.camel.RuntimeCamelException;
import org.apache.camel.builder.RouteBuilder;
import org.jetbrains.annotations.NotNull;
//import org.keycloak.representations.idm.RoleRepresentation;
import org.springframework.stereotype.Component;
import org.springframework.util.Assert;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

//import static com.zoomint.encourage.framework.data.routes.AuthorizationRouteBuilder.AUTH_USER;

@Component
public class KeycloakRouteBuilder extends RouteBuilder {
	public static final String URI_LOAD_ALL_KC_USERS = "direct:loadAllKcUsers";
	public static final String URI_LOAD_KC_USERS_BY_FULLTEXT = "direct:loadKcUserByFullText";
	public static final String URI_LOAD_KC_USER_BY_ID = "direct:loadKcUserById";
	public static final String URI_LOAD_KC_USERS_BY_IDS = "direct:loadKcUsersByIds";
	public static final String URI_LOAD_KC_GROUPS_BY_FULLTEXT = "direct:loadKcGroupsByFullText";
	public static final String URI_LOAD_KC_GROUP_BY_ID = "direct:loadKcGroupById";
	public static final String URI_LOAD_KC_USER_INFO = "direct:loadKcUserInfo";

	public static final String ACCESS_TOKEN_HEADER = "accessToken";
	public static final String USER_ID_HEADER = "userId";
	public static final String SEARCH_TEMPLATES = "templates";

//	private final ClientTokenProvider clientTokenProvider;
//	private final KeycloakApiProviderClient keycloakClient;
//	private final KeycloakApiProviderClient keycloakApiProviderClient;
//	private final UsersClient usersClient;

	public KeycloakRouteBuilder(
//			ClientTokenProvider clientTokenProvider, KeycloakApiProviderClient keycloakClient,
//                                KeycloakApiProviderClient keycloakApiProviderClient, UsersClient usersClient
	) {
//		this.clientTokenProvider = clientTokenProvider;
//		this.keycloakClient = keycloakClient;
//
//		this.keycloakApiProviderClient = keycloakApiProviderClient;
//		this.usersClient = usersClient;
	}

	@Override
	public void configure() {
//		from(URI_LOAD_KC_USER_BY_ID).routeId("loadKcUserById")
//				.choice().when(header("userId").isEqualTo("me"))
//					.setBody().exchange(exchange -> exchange.getProperty(AUTH_USER, User.class))
//					.endChoice()
//				.otherwise()
//					.setBody().header(USER_ID_HEADER)
//					.transform().body(String.class, this::loadKeycloakUserById)
//					.transform().body(User.class, this::loadEffectiveRoles)
//					.removeHeaders("*") // remove headers from previous request
//				.end()
//		;
//
//		from(URI_LOAD_KC_USERS_BY_IDS).routeId("loadKcUserByIds")
//				.setBody().header("userIds")
//				.transform().body(List.class, this::findAllByIds)
//				.removeHeaders("*") // remove headers from previous request
//		;

		from(URI_LOAD_ALL_KC_USERS).routeId("loadAllKcUsers")
				.transform().body(Exchange.class, this::loadKeycloakUsersFiltered)
		;

//		from(URI_LOAD_KC_USERS_BY_FULLTEXT).routeId("loadKcUserByFullText")
//				.transform().body(String.class, this::loadKeyCloakUsersByFullText)
//		;
//
//		from(URI_LOAD_KC_GROUPS_BY_FULLTEXT).routeId("loadKcGroupsByFullText")
//				.setBody().header("name")
//				.transform().body(String.class, this::loadKeyCloakGroupsFullText)
//		;

//		from(URI_LOAD_KC_GROUP_BY_ID).routeId("loadKcGroupById")
//				.setBody().header("groupId")
//				.transform().body(String.class, this::loadKeyCloakGroup)
//		;
//
//		from(URI_LOAD_KC_USER_INFO).routeId("loadKcUserInfo")
//				.setBody().header(ACCESS_TOKEN_HEADER)
//				.transform().body(String.class, this::getUserInfo)
//		;
//
	}
//
//	private List<Group> loadKeyCloakGroupsFullText(String fullText) {
//		return keycloakClient.findGroupsFulltext(
//				clientTokenProvider.getRealm(),
//				clientTokenProvider.getAccessTokenString(),
//				fullText,
//				// todo: get the value from the frontend
//				100
//		);
//	}
//
//	private Group loadKeyCloakGroup(String groupId) {
//		if (Strings.isNullOrEmpty(groupId)) {
//			throw new IllegalArgumentException("Group id must be not null!");
//		}
//		return keycloakClient.getGroup(clientTokenProvider.getRealm(), clientTokenProvider.getAccessTokenString(), groupId)
//				.orElseThrow(EntityNotFoundDatabaseException::new);
//	}

	private Collection<User> loadKeycloakUsersFiltered(final Exchange exchange) {
		log.debug("Getting all users from Keycloak");
//		try {
//			final Stream<User> usersStream = getAllNonServiceAccountUsers();
//			final User currentUser = exchange.getProperty(AUTH_USER, User.class);
//			if (userHasPermission(currentUser, Activities.INTERACTIONS_FULL_VIEW)) {
//				final List<User> allUsers = usersStream.toList();
//				log.debug("Got {} users from Keycloak (service account users was filtered out)", allUsers.size());
//				return allUsers;
//			} else if (userHasPermission(currentUser, Activities.INTERACTIONS_AGENT_VIEW) ||
//					userHasPermission(currentUser, Activities.INTERACTIONS_GROUP_VIEW)) {
//				final List<String> evaluateGroupIds = new ArrayList<>();
//				if (userHasPermission(currentUser, Activities.INTERACTIONS_GROUP_VIEW)) {
//					currentUser.getUsersTeams().forEach(userTeamId ->
//							fillGroupsWithSubGroups(userTeamId, evaluateGroupIds));
//				}
//
//				final List<String> searchTemplateAgentIds = new ArrayList<>();
//				addAbacIds(exchange, evaluateGroupIds, searchTemplateAgentIds);
//				final List<User> filteredUsers;
//				if (evaluateGroupIds.isEmpty()) {
//					filteredUsers = getUsersWithNoGroups(usersStream, currentUser, searchTemplateAgentIds);
//					log.debug("Got {} users from Keycloak (with ABAC users and no service account user)", filteredUsers.size());
//				} else {
//					filteredUsers = getUsersWithGroups(usersStream, currentUser, searchTemplateAgentIds, evaluateGroupIds);
//					log.debug("Got {} users from Keycloak (with ABAC users and groups and no service account user)", filteredUsers.size());
//				}
//				return filteredUsers;
//			} else {
//				log.debug("Got nothing from the Keycloak for this filter request");
//				return Collections.emptyList();
//			}
//		} catch (KeycloakApiProviderClientException e) {
//			log.error("Error when getting all users in Keycloak: {}", e.getMessage());
//			throw new RuntimeCamelException(e);
//		}
		return Collections.singletonList(User.builder().build());
	}

//	@NotNull
//	private static List<User> getUsersWithGroups(Stream<User> usersStream, User currentUser, List<String> searchTemplateAgentIds,
//																							 List<String> evaluateGroupIds) {
//		return usersStream.filter(user -> user.getUserId().equals(currentUser.getUserId()) ||
//				searchTemplateAgentIds.contains(user.getUserId()) ||
//				evaluateGroupIds.contains(user.getMainGroupId())).collect(Collectors.toList());
//	}
//
//	@NotNull
//	private static List<User> getUsersWithNoGroups(Stream<User> usersStream, User currentUser, List<String> searchTemplateAgentIds) {
//		return usersStream.filter(user -> user.getUserId().equals(currentUser.getUserId()) ||
//				searchTemplateAgentIds.contains(user.getUserId())).collect(Collectors.toList());
//	}
//
//	private void fillGroupsWithSubGroups(String userTeamId, List<String> evaluateGroupIds) {
//		evaluateGroupIds.add(userTeamId);
//		loadSubGroups(userTeamId, evaluateGroupIds);
//	}
//
//	private static boolean userHasPermission(User currentUser, Activities interactionsFullView) {
//		return currentUser.getRoles().stream().anyMatch(role -> role.getName().equals(interactionsFullView.name()));
//	}
//
//	@NotNull
//	private Stream<User> getAllNonServiceAccountUsers() {
//		return keycloakClient.getUsers(
//						clientTokenProvider.getRealm(),
//						clientTokenProvider.getAccessTokenString(),
//						PageRequest.of(0, PageRequest.MAX_PAGE_SIZE)
//				).getContent().stream()
//				.filter(user -> !user.getUsername().startsWith("service-account-"));
//	}
//
//	private void addAbacIds(Exchange exchange, List<String> evaluateGroupIds, List<String> searchTemplateAgentIds) {
//		List<SearchTemplate> searchTemplates = exchange.getProperty(SEARCH_TEMPLATES, SearchTemplateList.class).getSearchTemplates();
//		searchTemplates.forEach(searchTemplate -> {
//			final ClientConversationSearch conversationSearch = searchTemplate.getConversationSearch();
//			if (conversationSearch == null) {
//				return;
//			}
//			Set<String> agents = conversationSearch.getUserUUIDs();
//			if ((agents == null || agents.isEmpty()) &&
//					(conversationSearch.getGroupUUIDs() != null && !conversationSearch.getGroupUUIDs().isEmpty())) {
//				conversationSearch.getGroupUUIDs().forEach(userTeamId -> {
//					fillGroupsWithSubGroups(userTeamId, evaluateGroupIds);
//				});
//			} else if (agents != null) {
//				searchTemplateAgentIds.addAll(agents);
//			}
//		});
//	}
//
//	private void loadSubGroups(String userTeamId, List<String> evaluateGroupIds) {
//		evaluateGroupIds.addAll(
//				keycloakClient.getSubGroups(clientTokenProvider.getRealm(),
//								clientTokenProvider.getAccessTokenString(), userTeamId).getContent()
//						.stream()
//						.map(Group::getGroupId)
//						.toList());
//	}
//
//	private List<UserProfileInfo> loadKeyCloakUsersByFullText(String text) {
//		log.debug("Looking for users by text '{}' in Keycloak", text);
//		try {
//			List<UserProfileInfo> users = keycloakClient.findUsersFulltext(
//					clientTokenProvider.getRealm(),
//					clientTokenProvider.getAccessTokenString(),
//					text,
//					// todo: get the value from the frontend
//					100
//			);
//			log.debug("Found {} users in Keycloak who contain text '{}'", users.size(), text);
//			return users;
//		} catch (KeycloakApiProviderClientException e) {
//			log.error("Error when looking for users in Keycloak: {}", e.getMessage());
//			throw new RuntimeCamelException(e);
//		}
//	}
//
//	private User loadKeycloakUserById(String userId) {
//		if (Strings.isNullOrEmpty(userId)) {
//			throw new IllegalArgumentException("User id must be not null!");
//		}
//		return keycloakClient.getUser(clientTokenProvider.getRealm(), clientTokenProvider.getAccessTokenString(), userId)
//				.orElseThrow(EntityNotFoundDatabaseException::new);
//	}
//
//	private User loadEffectiveRoles(final User user) {
//		if (Objects.isNull(user)) {
//			throw new IllegalArgumentException("User must be not null!");
//		}
//		user.getRoles().clear();
//		user.getRoles().addAll(getApplicationRoles(user).stream()
//				.map(roleRepresentation ->
//				new Role(roleRepresentation.getName(), new HashSet<>()))
//				.collect(Collectors.toSet()));
//		return user;
//	}
//
//	private Set<RoleRepresentation> getApplicationRoles(final User user) {
//		final Set<RoleRepresentation> roleRepresentations = new HashSet<>();
//			Arrays.stream(QmApplication.values()).forEach(qmApplication -> {
//				roleRepresentations.addAll(getUserRolesByApplicationName(user.getUserId(), qmApplication.getName()));
//			});
//		return roleRepresentations;
//	}
//
//	private List<RoleRepresentation> getUserRolesByApplicationName(final String userId, final String appName) {
//		try {
//			return usersClient.getEffectiveApplicationRoleMappings(clientTokenProvider.getRealm(),
//					clientTokenProvider.getAccessTokenString(), userId, appName);
//		} catch (NotFoundException ex) {
//			log.debug("Application {} is not enabled", appName);
//		}
//		return Collections.emptyList();
//	}
//
//	private Set<User> findAllByIds(Collection<String> userIds) {
//		if (userIds == null) {
//			throw new IllegalArgumentException("User ids must be not null!");
//		}
//		if (userIds.isEmpty()) {
//			log.debug("Empty lookup of user ids. Will not contact keycloak.");
//			return Set.of();
//		}
//
//		log.debug("Looking for users in keycloak with ids: '{}'", userIds);
//		Set<User> users = new HashSet<>();
//		Iterables.partition(userIds, PageRequest.MAX_PAGE_SIZE)
//				.forEach(userIdsPartition -> users.addAll(
//						keycloakClient.getUsers(
//								clientTokenProvider.getRealm(),
//								clientTokenProvider.getAccessTokenString(),
//								UserLookup.builder().ids(userIdsPartition).build(),
//								PageRequest.of(0, userIdsPartition.size())
//						).getContent()
//				));
//
//		log.debug("Found {} users in keycloak", users.size());
//		return users;
//	}
//
//	private UserInfo getUserInfo(String authorizationToken) {
//		Assert.hasText(authorizationToken, "Authorization token must be included");
//		return keycloakApiProviderClient.getUserInfo(clientTokenProvider.getRealm(), authorizationToken);
//	}
}
