# Base Image to run the app
FROM python:3.10

# Environment variables to connect to the Database "mongodb"
ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=adminroot

# If we specify the WorkDir we don't need to mention the path in CMD command
WORKDIR /home/pyapp


# This command creates Directory in the Container
#RUN mkdir -p /home/app

# This command executes on the host

# Copies all files from localhost to the ".../pyapp" directory in Container
COPY ./pyapp /home/pyapp


# Installs prerequisites to run the App.
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt \
    && pip3 install pymongo

EXPOSE  5000

CMD ["python", "/home/pyapp/pythonmongo.py"]




