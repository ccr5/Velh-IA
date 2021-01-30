FROM node:10 AS ui-build
WORKDIR /usr/src/app
COPY . ./velhia.web/
RUN cd velhia.web && yarn && yarn build

# FROM node:10 AS server-build
# WORKDIR /usr/src/app
# COPY api/ ./api/
# RUN cd api && npm install && npm run build

FROM node:10
WORKDIR /usr/src/app/
COPY --from=ui-build /usr/src/app/velhia.web/build ./velhia.web/build
# COPY --from=server-build /usr/src/app/api/dist ./
RUN npm install -g serve

# EXPOSE 3000

CMD ["serve"]