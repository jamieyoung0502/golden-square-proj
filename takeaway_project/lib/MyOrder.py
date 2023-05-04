from twilio.rest import Client
import lib.keys
from datetime import datetime, timedelta

# client = Client(lib.keys.acccount_sid, lib.keys.auth_token)
# message = client.messages.create(
#     body= f"your food will arrive at ",
#     from_= lib.keys.twilio_number,
#     to= lib.keys.customer_number
# )

class MyOrder():
    
    def __init__(self):
        self.order = []

    def add_to_order (self, dish):
        self.order.append(dish)

    def remove_from_order(self, dish):
        # remove a dish from the order
        self.order.remove(dish)
    
    def view_my_order(self):
        # return a nice readable list of all dishes and prices with a grand total at the bottom
        total = 0
        my_order_list = []
        print (total)
        for item in self.order:
            my_order_list.append(item.format_dish())
            total += (float(item.price))
        total = "{:.2f}".format(total)
        return my_order_list + [f"TOTAL = {str(total)}"]



    def clear_order(self):
        self.order = []
    

    def place_order(self):
        # sends the user a text message saying order will be with you in 45 mins
        now = datetime.now()
        delivery_time = now + timedelta(minutes=45)
        delivery_text = f"your food will arrive by {delivery_time.hour}: {delivery_time.minute}",
        client = Client(lib.keys.acccount_sid, lib.keys.auth_token)
        message = client.messages.create(
        body= delivery_text,
        from_= lib.keys.twilio_number,
        to= lib.keys.customer_number)
        return "Your order has been placed"



