# Instructions to build and run

Create environment
python -m virtualenv env

Activate environment
env\Scripts\activate.bat

Install packages into environment
pip install -r requirements.txt

Run tests
pytest -v

Run REST API service
python app.py

Postman
URL base: http://localhost:5000/v1

Swagger/OpenAPI Documentation
http://localhost:5000/v1/swagger/

# Docker - Not tested as environment was not available.
docker build -t online-store:latest .
docker run -d -p 5000:5000 online-store