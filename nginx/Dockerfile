FROM node:12.16.1-alpine AS builder


WORKDIR /secret_website_frontend

COPY ./secret_website_frontend/package.json ./
COPY ./secret_website_frontend/package-lock.json ./

RUN npm install --force

COPY ./secret_website_frontend/ ./

RUN npm run build --prod


FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY --from=builder /secret_website_frontend/dist/diploma-secret_website_frontend /usr/share/nginx/html