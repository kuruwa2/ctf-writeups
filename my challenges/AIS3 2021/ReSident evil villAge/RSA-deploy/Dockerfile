FROM ubuntu:focal
MAINTAINER Kuruwa

RUN apt-get update
RUN apt-get install xinetd python3 python3-pip -qy
RUN pip3 uninstall pycrypto
RUN pip3 install pycryptodome
RUN useradd -m RSA
RUN chown -R root:root /home/RSA
RUN chmod -R 755 /home/RSA

CMD ["/usr/sbin/xinetd","-dontfork"]
