# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /home/luizademelo/tp2-cloud

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the entire project
COPY . .

# Set Flask environment variables
ENV FLASK_APP=app.app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Run the Flask app
CMD ["flask", "run"]
