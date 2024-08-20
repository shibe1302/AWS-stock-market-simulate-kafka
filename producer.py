import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

class DataStream:
  def __init__(self):
    self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'], #change ip here
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
    self.producer.flush()

    
  def send_data(self):
    df = pd.read_csv("indexProcessed.csv")
    out=df[df['Index']=='HSI']
    for x in range(0,len(out)):
        self.producer.send('tp1', value=out.iloc[x].to_dict()['Open'])
        print(out.iloc[x].to_dict()['Open'])
        sleep(3)
    

lmao=DataStream()
lmao.send_data()

    