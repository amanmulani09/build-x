from Broker import Broker
from Subscriber import Subscriber
from Publisher import Publisher

broker = Broker()

# create subscriber 
sub1 = Subscriber("user-1")
sub2 = Subscriber("user-2")
sub3 = Subscriber("user-3")

# subscripbe to topic 
broker.subscribe("news",sub1.consume)
broker.subscribe("news",sub2.consume)
broker.subscribe("song",sub3.consume)

# publisher 
pub = Publisher(broker)

pub.publish("news","Breaking news r")

pub.publish("song","dhoom machaleyy")
