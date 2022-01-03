# syntax=docker/dockerfile:1
FROM node:16 AS base
COPY front front
WORKDIR /front

# add `/front/node_modules/.bin` to $PATH
ENV PATH /front/node_modules/.bin:$PATH
# install application dependencies
RUN npm install

FROM base AS prod
CMD ["npm", "run", "build"]

FROM base AS dev
CMD ["npm", "start"]

