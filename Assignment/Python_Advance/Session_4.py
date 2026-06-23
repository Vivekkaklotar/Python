# Q1 = Create a custom exception class called InvalidCouponCodeError for a Zomato-style food ordering app, and raise this exception if a user tries to apply a coupon code that is not in the list of valid codes.

# Custom Exception Class
class InvalidCouponCodeError(Exception):
    pass

# List of valid coupon codes
valid_coupons = ["ZOMATO50", "FOOD20", "SAVE100"]

# Function to apply coupon
def apply_coupon(coupon_code):
    if coupon_code not in valid_coupons:
        raise InvalidCouponCodeError("Invalid coupon code!")
    
    print("Coupon applied successfully!")

# Main Program
try:
    coupon = input("Enter coupon code: ")
    apply_coupon(coupon)

except InvalidCouponCodeError as e:
    print(e)

# Q2 = Write a function add_song_to_playlist(song_name, playlist) for a Spotify-like app that raises a SongAlreadyExistsError (custom exception) if the song is already present in the playlist.<br><br><em><strong>Hint:</strong> Define SongAlreadyExistsError as a user-defined exception class and use the raise keyword inside your function.</em>'''


# Custom Exception Class
class SongAlreadyExistsError(Exception):
    pass

# Function to add song to playlist
def add_song_to_playlist(song_name, playlist):
    if song_name in playlist:
        raise SongAlreadyExistsError(
            f"'{song_name}' already exists in the playlist!"
        )

    playlist.append(song_name)
    print(f"'{song_name}' added successfully.")

# Example Playlist
playlist = ["Believer", "Perfect", "Kesariya"]

try:
    add_song_to_playlist("Believer", playlist)  # Already exists
    # add_song_to_playlist("Shape of You", playlist)  # New song

except SongAlreadyExistsError as e:
    print("Error:", e)

print("Playlist:", playlist)


# Q3 = Simulate a Flipkart-style checkout process where a function process_payment(amount) raises a PaymentFailedError (custom exception) if the amount is less than or equal to zero, and prints 'Payment Successful' otherwise.

class PaymentFailedError(Exception):
    pass

def process_payment(amount):
    if amount <=0:
        raise PaymentFailedError("payment failed: amount must be greater than zero")
    print("payment successful")

try:
    process_payment(500)
    process_payment(0)
except PaymentFailedError as e:
    print(e)

# Q4 = Given the following traceback from a Python program, use ChatGPT to explain in your ownwords what the error means and how you would fix it:<br><br>Traceback (most recent call last):<br> File "main.py", line 8, in <module><br> book_ticket('Avengers', -2)<br> File "main.py", line 4,in book_ticket<br> raise InvalidSeatNumberError('Seat number must be positive')<br>NameError: name 'InvalidSeatNumberError' is not defined


# Define custom exception
class InvalidSeatNumberError(Exception):
    pass

def book_ticket(movie, seat):
    if seat <= 0:
        raise InvalidSeatNumberError('Seat number must be positive')
    print("Ticket booked!")

# Call function
book_ticket('Avengers', -2)
