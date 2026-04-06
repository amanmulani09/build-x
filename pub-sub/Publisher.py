from Broker import Broker

class Publisher:
    
    def __init__(self, broker: Broker):
        self.broker = broker
        
    def publish(self, topic: str, message: str):
        self.broker.publish(topic, message)