FROM python:latest
RUN pip install boto3
COPY get-mods/* /
WORKDIR /
VOLUME [ "/data" ]
CMD ["python", "main.py"]