FROM ubuntu:16.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \ 
      nodejs \
      npm \
      nginx \
      tzdata \
      curl

RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10

RUN npm cache clean && npm install n -g

RUN n stable && ln -sf /usr/local/bin/node /usr/bin/node && n 8.11.1

RUN apt-get purge -y nodejs npm

RUN npm install -g yarn

RUN export DEBIAL_FRONTEND=noninteractive
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata
