# Docker

[![Deploy to Docker Cloud](https://files.cloud.docker.com/images/deploy-to-dockercloud.svg)](https://cloud.docker.com/stack/deploy/?repo=https://github.com/fossasia/query-server)

* Get the latest version of docker. See the [official site](https://docs.docker.com/engine/installation/) for installation info for your platform.

* Install the latest version of docker-compose. Windows and Mac users should have docker-compose by default as it is part of Docker toolbox. For Linux users, see the
[official guide](https://docs.docker.com/compose/install/).

* Run `docker` and in terminal to see if they are properly installed.

* Clone the project and cd into it.

```bash
git clone https://github.com/fossasia/query-server.git && cd query-server
```

* In the terminal window, run `docker build -t query-server:latest .` to build badgeyay's docker image. This process can take some time.

* After build is done, run `docker run -d -p 7001:7001 query-server` to start the server.
