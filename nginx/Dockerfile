# VERSION 1.0
# DESCRIPTION: NGINX on alpine
FROM nginx:1.21-alpine
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 5000
CMD ["nginx", "-g", "daemon off;"]
