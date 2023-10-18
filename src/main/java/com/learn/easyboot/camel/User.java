package com.learn.easyboot.camel;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import lombok.Singular;

import java.util.HashSet;
import java.util.Set;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(onlyExplicitlyIncluded = true)
@JsonIgnoreProperties(ignoreUnknown = true)
public class User {
	String username;
	@EqualsAndHashCode.Include
	String userId;
	String firstName;
	String lastName;
	String agentId;
	String sourceId;
	String email;
	/**
	 * Set of secondary user emails, in addition to main user email.
	 */
	@Builder.Default
	Set<String> secondaryEmails = new HashSet<>();
	/**
	 * Single phone extension of the user.
	 *
	 * @deprecated use {@link #phoneExtensions} instead.
	 */
	@Deprecated
	String phoneExtension;
	/**
	 * List of all user phone extensions
	 */
	@Builder.Default
	Set<String> phoneExtensions = new HashSet<>();
	boolean enabled;
	@Singular
	Set<Role> roles;
	/**
	 * Set of group IDs, not group name or group path
	 */
	Set<String> groups;
	String mainGroupId;
	String scorecardId;
	Set<String> usersTeams;
	long created;
	String locale;
	String timezone;
}
