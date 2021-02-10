FROM ubuntu:focal
MAINTAINER Kuruwa

RUN apt-get update
RUN apt-get install xinetd python3 -qy
RUN useradd -m CoB
RUN chown -R root:root /home/CoB
RUN chmod -R 755 /home/CoB

CMD ["/usr/sbin/xinetd","-dontfork"]
