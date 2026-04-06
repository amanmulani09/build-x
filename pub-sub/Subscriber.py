
class Subscriber:
    
    def __init__(self,name:str):
        self.name = name
        
    def consume(self,message:str):
        print(f"{self.name} received : {message}")