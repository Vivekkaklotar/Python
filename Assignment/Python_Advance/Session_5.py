# Q1 = Create a Python class called Song with attributes title, artist, and duration (in seconds). Use the __init__ method to initialize these attributes and create two Song objects with different values.

# Song class
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

# Creating Song objects
song1 = Song("Shape of You", "Ed Sheeran", 233)
song2 = Song("Blinding Lights", "The Weeknd", 200)

# Displaying song details
print("Song 1:")
print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration, "seconds")

print("\nSong 2:")
print("Title:", song2.title)
print("Artist:", song2.artist)
print("Duration:", song2.duration, "seconds")


# Q2 = Build a class named FoodOrder that represents a Zomato-style order with properties: restaurant_name, items (a list), and total_price. Add a method show_order() that prints the order details in a readable format.

class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def show_order(self):
        print("----- Order Details -----")
        print("Restaurant:", self.restaurant_name)
        print("Items:")
        for item in self.items:
            print("-", item)
        print("Total Price: ₹", self.total_price)
        print("-------------------------")

# Creating an object
order1 = FoodOrder(
    "Pizza Hut",
    ["Margherita Pizza", "Garlic Bread", "Coke"],
    799
)

# Displaying order details
order1.show_order()

# Q3 = Write a Python class called InstagramPost with attributes caption, likes, and comments (a list). Add a method add_comment(comment_text) that appends a new comment to the comments list and increases the likes by 1.

class InstagramPost:
    def __init__(self, caption, likes, comments):
        self.caption = caption
        self.likes = likes
        self.comments = comments

    def add_comment(self, comment_text):
        self.comments.append(comment_text)
        self.likes += 1

    def show_post(self):
        print("Caption:", self.caption)
        print("Likes:", self.likes)
        print("Comments:", self.comments)


# Creating an Instagram post object
post = InstagramPost(
    "Enjoying the beautiful sunset! 🌅",
    100,
    ["Amazing view!", "So beautiful!"]
)

# Adding a new comment
post.add_comment("Wonderful picture!")

# Displaying updated post details
post.show_post()


# Q4 = Given the following code, fix the bug so that the object is created with the correct values:<br><br>class Movie:<br> def __init__(self, title, rating):<br> title = title<br> rating = rating<br><br>m = Movie('Jawan', 4.5)<br>print(m.title, m.rating)<br><br><em><strong>Hint:</strong> Check how instance variables should be assigned inside __init__.</em>


class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating

m = Movie("Jawan", 4.5)
print(m.title, m.rating)