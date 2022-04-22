FROM python:3.7.13-bullseye          

WORKDIR /flask_app                

COPY requirements.txt .               

RUN pip install -r requirements.txt  

COPY ./flask_app .            
CMD ["python","app.py"]               