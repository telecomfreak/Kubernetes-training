FROM ubuntu:18.04
RUN  apt-get update && apt-get install -y python3 python3-pip
RUN  pip3 install requests
COPY restclient.py /src/restclient.py
RUN  chmod +x /src/restclient.py
CMD  ["/src/restclient.py"]
