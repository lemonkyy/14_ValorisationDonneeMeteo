FROM node:25 AS build

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

RUN npm run build

FROM dhi.io/node:25 AS prod

WORKDIR /app

COPY --from=build --chown=node:node /app/.output /app/.output/

ENV NODE_ENV=production

USER node

EXPOSE 3000

CMD [ "node", ".output/server/index.mjs" ]
