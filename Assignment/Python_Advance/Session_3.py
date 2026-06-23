# Q1 = Write a Python function get_song_duration that takes a song name and returns its duration from a predefined dictionary.Use a try-except block to handle the case where the song is not found and print 'Song not found on Spotify!'.

file = open("songs.txt", "w")

file.write("Believer\n")
file.write("Perfect\n")
file.write("Kesariya\n")
file.write("Tum Hi Ho\n")
file.write("Shape of You\n")

file.close()

# Step 2: Function to get song duration
def get_song_duration(song_name):
    songs = {
        "Believer": "3:24",
        "Perfect": "4:23",
        "Kesariya": "4:28",
        "Tum Hi Ho": "4:22",
        "Shape of You": "3:53"
    }

    try:
        duration = songs[song_name]
        print(f"{song_name} duration: {duration}")
    except KeyError:
        print("Song not found on Spotify!")

# Step 3: Test the function
get_song_duration("Believer")
get_song_duration("Despacito")


# Q2 = Simulate a Flipkart order summary calculator that takes price and quantity as input and calculates the total. Use try-except to handle ValueError if the user enters a non-numeric value, and display an error message.
 
# Flipkart Order Summary Calculator

try:
    # Take input from user
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Calculate total
    total = price * quantity

    # Display order summary
    print("\n----- Flipkart Order Summary -----")
    print("Price per item:", price)
    print("Quantity:", quantity)
    print("Total Amount:", total)

except ValueError:
    print("Error: Please enter only numeric values for price and quantity!")

# Q3 = Create a function book_movie_ticket that takes the number of tickets as input and divides a fixed wallet balance by the number of tickets to get the price per ticket. Handle ZeroDivisionError and ValueError using multiple except blocks, and print a different message for each error.<br><br><em><strong>Hint:</strong> Use two separate except blocks for ZeroDivisionError and ValueError.</em>

def book_movie_ticket():
    wallet_balance = 1000  # Fixed wallet balance

    try:
        tickets = int(input("Enter number of tickets: "))

        price_per_ticket = wallet_balance / tickets

        print("Price per ticket:", price_per_ticket)

    except ZeroDivisionError:
        print("Error: Number of tickets cannot be zero!")

    except ValueError:
        print("Error: Please enter a valid numeric value!")

# Call the function
book_movie_ticket()


# Q4 = Given the following buggy code, fix it so that it catches both IndexError and KeyError and prints a custom message 
# for each:
# my_list = [1, 2, 3]

my_list = [1, 2, 3]
my_dict = {'a': 1}

# Handle IndexError
try:
    print(my_list[5])
except IndexError:
    print("Error: List index is out of range!")

# Handle KeyError
try:
    print(my_dict['b'])
except KeyError:
    print("Error: Key not found in dictionary!")




