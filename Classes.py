#This is to create all the classes 
#CUSTOMER Class
class customer:
    def __init__(self, key, verb, event_time, last_name, adr_city, adr_state):
        self.key = key
        self.verb = verb
        self.event_time = event_time
        self.last_name = last_name
        self.adr_city = adr_city
        self.adr_state = adr_state


# SITE_VISIT Class
class siteVisit:
    def __init__(self, key, verb, event_time, customer_id, tags):
        self.key = key
        self.verb = verb
        self.event_time = event_time
        self.customer_id = customer_id
        self.tags = tags


# IMAGE Class
class image:
    def __init__(self, key, verb, event_time, customer_id, camera_make, camera_model):
        self.key = key
        self.verb = verb
        self.event_time = event_time
        self.customer_id = customer_id
        self.camera_make = camera_make
        self.camera_model = camera_model


# ORDER Class
class order:
    def __init__(self, key, verb, event_time, customer_id, total_amount):
        self.key = key
        self.verb = verb
        self.event_time = event_time
        self.customer_id = customer_id
        self.total_amount = total_amount
