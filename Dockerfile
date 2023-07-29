FROM python:3.10-slim-buster
COPY .  /local-alexa
WORKDIR /local-alexa
RUN  apt-get -y update;  apt-get install -y ffmpeg
RUN pip3 install --upgrade pip; pip3 install openai-whisper
RUN pip3 install setuptools-rust
CMD whisper "sample-1.mp3" --model tiny --language English