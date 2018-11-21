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

### Build of container


```
docker build -t python-selenium-app .
```

### Params
There are a three argv

```
"subject" - subject of mail
"from" - email of sender
"driver" - driver what will be use for checking, default driver is google
```

### Start test

```
docker run -it --rm --name run python-selenium-app
```