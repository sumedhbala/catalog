FROM python:3.7.1

RUN pip install black jsbeautifier

RUN mkdir -p /tmp

CMD ["black", "/tmp"]
