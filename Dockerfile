FROM python:3.7-alpine3.8

# update apk and install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# install selenium
RUN pip install selenium==3.14
RUN pip install pyyaml==3.11

#make workdir and copy project
WORKDIR /code
COPY . .
