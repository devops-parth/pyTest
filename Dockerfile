FROM python
EXPOSE 8080
COPY /var/jenkins_home/workspace/$JOB_NAME/. /app
WORKDIR /app
CMD [ "python","c29.py" ]