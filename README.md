# Python-Alpine docker image with selenium

Allowed open pages with chrome, make some screens for tests

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Need to be installed docker

```
docker -v
Docker version 18.06.1-ce, build e68fc7a
```

### Installing


```
docker build -t python-selenium-app .
```

### Start test

```
docker run -it --rm --name run python-selenium-app
```