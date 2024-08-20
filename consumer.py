from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json

class GetDataStream:
  def __init__(self):
    self.consumer = KafkaConsumer('shibe1',
        bootstrap_servers=['18.212.134.208:9092'], #add your IP here
        value_deserializer=lambda x: loads(x.decode('utf-8')))
    self.currentData=2000

    
  def get_data(self):
    for c in self.consumer:
        print("csm --- "+str(c.value))
        self.currentData=c.value
        break
  def get_current_data(self):
     self.get_data()
     return self.currentData
  


