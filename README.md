# Instructions to build and run

Open command prompt at online-store folder level

****************************************************************************

To use makefile to run tests (Assumes as installed: python, pip and make)

make

****************************************************************************

Install Python virtual environment dependencies

pip install virtualenv

Create Python virtual environment

python -m virtualenv env

Activate environment

env\Scripts\activate.bat

Install packages into environment

pip install -r requirements.txt

Run tests

pytest -v

****************************************************************************

Run REST API service

python app.py

****************************************************************************

Postman

URL base: http://localhost:5000/v1

****************************************************************************

Swagger/OpenAPI Documentation

http://localhost:5000/v1/swagger/

****************************************************************************

Run as Docker container

docker-compose build -t online-store:latest .

docker run -d -p 5000:5000 online-store
