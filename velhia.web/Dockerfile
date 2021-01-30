FROM node:10
WORKDIR /usr/src/app
COPY . ./velhia.web/
WORKDIR /usr/src/app/velhia.web
RUN npm install -g serve
RUN yarn && yarn build
cmd serve -s build
EXPOSE 5000