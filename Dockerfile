FROM python:3.7

# Set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Add requirements
COPY ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# run server
CMD python app.py