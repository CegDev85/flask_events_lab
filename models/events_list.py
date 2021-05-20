# from threading import Event
from models.event import *



event1 = Event("14/02/2021","Valentines Paintball.","2","My Kitchen","2 lovers pelting each other with paintballs at close range.")
event2 = Event("18/12/2021","Buy your spouse the perfect gift.","15","Jacks shop of giant Dessert Lizards","Xmas is close, Its time to think outside the box.")
events = [event1,event2]

def add_new_event(event):
    events.append(event)