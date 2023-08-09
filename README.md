https://www.baeldung.com/solid-principles
Barbara Liskov!!!

mvn clean install
docker build -t easy07:1.1.1 .
docker run -p 8707:8707 --name exec07 easy07:1.1.1

git checkout another_container
mvn clean install
docker build -t easy08:1.1.1 . -f Dockerfile08
docker run -p 8708:8708 --name exec08 easy08:1.1.1

