mvn spring-boot:run -Drun.arguments=--DdbType=MONGO

or
vmoptions>>>
-DdbType=MONGO


### run with docker
docker run -p 8080:8080 --name myeasy -t learn/easyboot/spring-boot-starter-parent:latest
