FROM node:16.3.0-alpine AS builder

WORKDIR /secret_website_frontend
COPY ./secret_website_frontend/package.json ./
COPY ./secret_website_frontend/package-lock.json ./
RUN npm install
COPY ./secret_website_frontend/ ./
RUN npm run build


FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /secret_website_frontend/build /usr/share/nginx/html