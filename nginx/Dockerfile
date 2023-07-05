FROM node:alpine AS builder

RUN apk update && apk add git
run git clone https://github.com/kacperpy/secret_website_frontend.git .

WORKDIR /secret_website_frontend

COPY ./secret_website_frontend/package.json ./
COPY ./secret_website_frontend/package-lock.json ./

RUN npm install

COPY ./secret_website_frontend/ ./
RUN npm run build


FROM nginx:alpine

COPY --from=builder /secret_website_frontend/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d