FROM openjdk:17
WORKDIR /app
COPY ./target/easyboot-starter-0.0.1-SNAPSHOT.jar /app
EXPOSE 8707
CMD ["java", "-jar", "easyboot-starter-0.0.1-SNAPSHOT.jar"]