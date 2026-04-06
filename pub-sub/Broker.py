from collections import defaultdict
from typing import Callable, Dict, List, Any

class Broker: 
    
    def __init__(self):
        #topic -> list of subscribers
        self.subscribers: Dict[str, List[Callable[..., Any]]] = defaultdict(list)
        
    def subscribe(self, topic: str, callback: Callable[..., Any]):
        self.subscribers[topic].append(callback)
        
    def publish(self, topic:str, message:str):
        
        if topic not in self.subscribers:
            return 
        
        for cb in self.subscribers[topic]:
            cb(message)