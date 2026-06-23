# Q1 = Create a Python class called User with attributes username and email, then create an object and print its details.
class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

# Create an object
user1 = User("vivek7573", 22)

# Print details
print("Username:", user1.username)
print("Age:", user1.age)

# Q2 = Build a single inheritance example where a class Influencer inherits from User and adds a followers attribute; create an Influencer object and print all its details.
# Parent Class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# Child Class
class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers

# Create an Influencer object
inf1 = Influencer("techguru", "techguru@gmail.com", 50000)

# Print details
print("Username:", inf1.username)
print("Email:", inf1.email)
print("Followers:", inf1.followers)

# Q3 = Demonstrate multilevel inheritance by creating a class VerifiedInfluencer that inherits from Influencer and adds a badge attribute; create a VerifiedInfluencer object and display all its properties.

# Grandparent Class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


# Parent Class
class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


# Child Class (Multilevel Inheritance)
class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge


# Create a VerifiedInfluencer object
v1 = VerifiedInfluencer(
    "vivek7573",
    "vivek7573@gmail.com",
    50000,
    "Blue Tick"
)

# Display all properties
print("Username:", v1.username)
print("Email:", v1.email)
print("Followers:", v1.followers)
print("Badge:", v1.badge)

# Q4 = Implement multiple inheritance by creating a class BrandPartner that inherits from both Influencer and a new class Brand (with attribute brand_name); create a BrandPartner object and print the username, followers, and brand_name.

# First Parent Class
class Influencer:
    def __init__(self, username, followers):
        self.username = username
        self.followers = followers

# Second Parent Class
class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name

# Child Class (Multiple Inheritance)
class BrandPartner(Influencer, Brand):
    def __init__(self, username, followers, brand_name):
        Influencer.__init__(self, username, followers)
        Brand.__init__(self, brand_name)

# Create a BrandPartner object
bp = BrandPartner("vk", 9603, "one8")

# Print details
print("Username:", bp.username)
print("Followers:", bp.followers)
print("Brand Name:", bp.brand_name)


# Q5 = Refactor your VerifiedInfluencer class to include a method display_profile() that prints details in the format used on Instagram profiles (username, followers in K/M, badge status).<br><br><em><strong>Hint:</strong> Use a helper function to format large follower counts, e.g., 1500 as '1.5K'.</em>

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge

    # Helper function to format followers
    def format_followers(self):
        if self.followers >= 1_000_000:
            return f"{self.followers / 1_000_000:.1f}M"
        elif self.followers >= 1_000:
            return f"{self.followers / 1_000:.1f}K"
        else:
            return str(self.followers)

    # Display profile like Instagram
    def display_profile(self):
        print("===== Instagram Profile =====")
        print("Username:", self.username)
        print("Followers:", self.format_followers())
        print("Badge Status:", self.badge)
        print("============================")


# Create object
v1 = VerifiedInfluencer(
    "vivek7573",
    "vivek7573@gmail.com",
    1500,
    "Blue Tick"
)

# Display profile
v1.display_profile()