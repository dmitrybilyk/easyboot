FROM openjdk:17.0-jdk-slim as build
WORKDIR /workspace/app
ADD maven/@project.build.finalName@.jar application.jar
RUN mkdir -p target/dependency && (cd target/dependency; jar -xf /workspace/app/application.jar)

FROM adoptopenjdk/openjdk11:latest
VOLUME /tmp
ARG DEPENDENCY=/workspace/app/target/dependency
COPY --from=build ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY --from=build ${DEPENDENCY}/META-INF /app/META-INF
COPY --from=build ${DEPENDENCY}/BOOT-INF/classes /app
EXPOSE 8108
ENTRYPOINT ["java","-cp","app:app/lib/*","com.learn.easyboot.EasyBootApplication","--logging.config=classpath:logback-docker.xml"]
