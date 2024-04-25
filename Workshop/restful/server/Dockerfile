FROM   ubuntu:18.04
RUN    apt-get update && apt-get install -y python3 python3-pip
RUN    pip3 install flask
RUN    mkdir descriptions
COPY   descriptions/* descriptions
COPY   restserver.py /src/restserver.py
RUN    chmod +x /src/restserver.py
EXPOSE 8080
CMD    ["/src/restserver.py"]
