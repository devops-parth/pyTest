FROM python
EXPOSE 8080
COPY . /app
WORKDIR /app
CMD [ "python","c29.py" ]