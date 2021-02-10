FROM ubuntu:focal
MAINTAINER Kuruwa

RUN apt-get update
RUN apt-get install xinetd python3 python3-pip -qy
RUN pip3 install pycrypto
RUN useradd -m HNP
RUN chown -R root:root /home/HNP
RUN chmod -R 755 /home/HNP

CMD ["/usr/sbin/xinetd","-dontfork"]
