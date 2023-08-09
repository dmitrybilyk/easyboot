FROM openjdk:17
WORKDIR /app
COPY ./target/easyboot-starter-0.0.1-SNAPSHOT.jar /app
ENV VAR1=value1
RUN echo "The ENV variable value is $VAR1"
EXPOSE 8708
CMD ["java", "-jar", "easyboot-starter-0.0.1-SNAPSHOT.jar"]