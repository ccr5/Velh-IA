FROM node:15.2.1-alpine3.12 as builder

WORKDIR /app

COPY ["./package.json", "yarn.lock", "tsconfig.json", "/app/"]

RUN yarn

RUN mkdir src

COPY "./src/" "/app/src/"

RUN yarn build

FROM node:15.2.1-alpine3.12 as prod

WORKDIR /app
ENV NODE_ENV=production

COPY --from=builder "/app/dist/" "/app/dist/"
COPY --from=builder "/app/package.json" "/app/"
COPY --from=builder "/app/yarn.lock" "/app/"

RUN yarn

RUN yarn add ts-node tsconfig-paths

COPY ["tsconfig.json", "/app/"]

CMD ["yarn", "prod"]
