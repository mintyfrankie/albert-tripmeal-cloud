FROM mysql
COPY mysqld.cnf /etc/mysql/conf.d
ADD init-db.sql /docker-entrypoint-initdb.d
RUN chown mysql:mysql /docker-entrypoint-initdb.d/*.sql
RUN chown mysql:mysql /etc/mysql/conf.d/*.cnf
ENV MYSQL_ROOT_HOST=%