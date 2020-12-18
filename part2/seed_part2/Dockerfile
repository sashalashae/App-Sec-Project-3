FROM python:3.7

RUN pip3 install mysql-connector-python

COPY ./users.csv /users.csv
COPY ./products.csv /products.csv
COPY ./seedoflife.py /seedoflife.py


ENTRYPOINT ["/entrypoint.sh"]
CMD ["mysqld", "--secure-file-priv=/"]