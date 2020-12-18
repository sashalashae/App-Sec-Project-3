FROM mysql:latest

COPY ./migsetup.sql /migsetup.sql

ENTRYPOINT ["/entrypoint.sh"]
CMD ["mysqld", "--secure-file-priv=/"]
#CMD ["--secure-file-priv=/"]
