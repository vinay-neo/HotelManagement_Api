# Loading from image 
FROM python:3
ENV PYTHONBUFFERED=1
# Changing into container folder app
WORKDIR /app
# Loading local data to container
COPY requirements.txt requirements.txt
# Install  and ugrade pip and requirements
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /app
# Exposing the port
EXPOSE 8000