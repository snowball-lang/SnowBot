FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get install sudo \
    curl python3 python3-pip -y
RUN apt-get update && apt-get -f install && \
    apt-get install -y gcc-9 g++-9 wget curl patchelf vim-common fuse \
        libfuse2 libtool autoconf automake zlib1g-dev libjpeg-dev libpng-dev \
        git libssl-dev sudo cmake make pkg-config cmake-data libglib2.0-dev

WORKDIR /app

RUN apt-get install lsb-release wget software-properties-common gnupg -y
RUN wget https://apt.llvm.org/llvm.sh
RUN chmod +x llvm.sh
RUN sudo ./llvm.sh 14
RUN rm llvm.sh

RUN sudo ln -s bash /bin/sh.bash
RUN sudo mv /bin/sh.bash /bin/sh

RUN touch ~/.bashrc
# TODO: use the website URL in the future
RUN curl -fsSL https://raw.githubusercontent.com/snowball-lang/snowball/dev/scripts/install.sh | bash -s -- -y

RUN eval "$(docker-machine env default)"
RUN chmod 777 ~/.snowball/bin/snowball
