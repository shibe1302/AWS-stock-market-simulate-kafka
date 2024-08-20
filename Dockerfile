FROM python:3.10.14-slim
WORKDIR /app 

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 

COPY . .

#CMD ["flask","--app","home.py","run","-h","localhost","-p","6969"]
CMD ["python3","home.py"]
#docker container run -d -p 3007:5000 python-flask:shiba1
