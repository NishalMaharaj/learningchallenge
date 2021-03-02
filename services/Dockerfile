FROM python:3-onbuild
RUN pip install --upgrade pip
RUN pip3 install dahuffman
RUN pip3 install nameko
CMD ["nameko", "run", "--config", "config.yaml", "learning_challenge"]
