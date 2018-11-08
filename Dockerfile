FROM python:3.7-alpine3.8

# update apk and install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

#make workdir and copy project
WORKDIR /code
COPY . .

# install requirements
RUN pip install -r requirements.txt
