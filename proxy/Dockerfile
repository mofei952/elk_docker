FROM docker.io/centos:7.4.1708

RUN yum install -y epel-release
RUN yum install -y nginx

ADD nginx.conf /etc/nginx/nginx.conf
ADD elk_docker.conf /etc/nginx/conf.d/elk_docker.conf

USER root

#CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]
CMD ["nginx", "-g", "daemon off;"]