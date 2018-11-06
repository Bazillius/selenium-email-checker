# Python-Alpine docker image with selenium
Allowed open pages with chrome, make some screens for tests

#Installation
docker build -t python-selenium-app .

#Start test
docker run -it --rm --name run python-selenium-app
