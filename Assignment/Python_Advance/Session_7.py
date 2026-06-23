# Q1 = Create a class InstaStory with a method share() that prints 'Sharing an image story'. Now create another class WhatsAppStory that overrides share() to print 'Sharing a text status'. Instantiate both and call share() to show method overriding in action.

# Parent Class
class InstaStory:
    def share(self):
        print("Sharing an image story")

# Child Class (Method Overriding)
class WhatsAppStory(InstaStory):
    def share(self):
        print("Sharing a text status")

# Create objects
insta = InstaStory()
whatsapp = WhatsAppStory()

# Call share() method
insta.share()
whatsapp.share()

# Q2 = Build a class Payment with a pay() method that takes amount as a parameter and prints 'Paying amount'. Then, create a subclass UPI that overrides pay() to print 'Paying amount via UPI'. Demonstrate both methods by making objects and calling pay(). 

# Parent Class
class Payment:
    def pay(self, amount):
        print(f"Paying {amount}")

# Child Class
class UPI(Payment):
    def pay(self, amount):
        print(f"Paying {amount} via UPI")

# Create objects
p = Payment()
u = UPI()

# Call pay() method
p.pay(500)
u.pay(500)

# Q3 = Simulate method overloading in Python by creating a class ZomatoOrder with a method add_item(). Use default arguments so that add_item() can be called with just an item name or with item name and quantity. Show both usages with print statements.<br><br><em><strong>Hint:</strong> Python does not support true method overloading, but you can use default or *args parameters.</em>
class ZomatoOrder:
    def add_item(self, item_name, quantity=1):
        print(f"Added {quantity} x {item_name} to the order")

# Create object
order = ZomatoOrder()

# Call with only item name
order.add_item("Pizza")

# Call with item name and quantity
order.add_item("Burger", 3)

# Q4 = Given the following code, fix it so that the Movie class overrides the display() method to show the movie's title and year, instead of just the title:<br><br>class Content:
# def display(self, title):
# print('Title:', title)

# class Movie(Content):
# def display(self, title, year):
# your code here<br><br>Call display() on a Movie object with both title and year.

class Content:
    def display(self, title):
        print("Title:", title)

class Movie(Content):
    def display(self, title, year):
        print("Title:", title)
        print("Year:", year)

# Create Movie object
m = Movie()

# Call display()
m.display("Jawan", 2023)


# Q5 = Use ChatGPT to generate a Python example where a base class Notification has a send() method, and two subclasses (EmailNotification, SMSNotification) override send() to print different messages. Paste the generated code, run it, and write one line explaining how method overriding works in your example.

# Base Class
class Notification:
    def send(self):
        print("Sending a notification")

# Subclass 1
class EmailNotification(Notification):
    def send(self):
        print("Sending an email notification")

# Subclass 2
class SMSNotification(Notification):
    def send(self):
        print("Sending an SMS notification")

# Create objects
email = EmailNotification()
sms = SMSNotification()

# Call send() methods
email.send()
sms.send()