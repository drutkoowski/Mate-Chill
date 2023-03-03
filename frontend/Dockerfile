FROM node:lts-alpine
RUN npm install -g npm
COPY ./frontend/package.json ./
RUN npm i --silent
COPY ./frontend .
