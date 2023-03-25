FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get install sudo -y
RUN apt-get install curl -y
RUN apt-get install python3 python3-pip -y
WORKDIR /app

COPY main.py requirements.txt /app

RUN sudo ln -s bash /bin/sh.bash
RUN sudo mv /bin/sh.bash /bin/sh

RUN touch ~/.bashrc
# TODO: use the website URL in the future
RUN curl -fsSL https://raw.githubusercontent.com/snowball-lang/snowball/dev/scripts/install.sh | bash -s -- -y
RUN pip install -r requirements.txt
RUN eval "$(docker-machine env default)"


