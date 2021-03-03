FROM mysql

ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_PASSWORD root

WORKDIR /src
CMD mysql -u root -p < /data/script.sql