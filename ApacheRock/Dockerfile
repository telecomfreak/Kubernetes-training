FROM ubuntu

# Install Apache and the required modules
#
ENV  DEBIAN_FRONTEND=noninteractive
RUN  apt-get update && apt-get install -y apache2 libapache2-mod-php php-mysql

# Exchange the default index.html by our own index.php
#
RUN  rm /var/www/html/index.html
COPY index.php /var/www/html/index.php

# Take care that logging information is sent to stdout/stderr
#
RUN  rm /var/log/apache2/access.log /var/log/apache2/error.log
RUN  ln -s /dev/stdout /var/log/apache2/access.log
RUN  ln -s /dev/stderr /var/log/apache2/error.log

# Environment variables used by index.php
#
# ENV  DBSERVER=mysqlserver
# ENV  DBUSER=guru00
# ENV  DBPASS=helsinki00
# ENV  DBNAME=rockdisc

CMD  ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
