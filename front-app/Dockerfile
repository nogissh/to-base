FROM mypage_vue-webapp-base:latest

COPY . /home/docker/app/

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY ./docker/nginx-app.conf /etc/nginx/sites-available/default

WORKDIR /home/docker/app/
RUN yarn && yarn build

EXPOSE 80
