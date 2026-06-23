

# Q1 = Create a Python script that opens a file called lyrics.txt and prints the file pointer's current position using tell() before and after reading the first 10 characters.


# Open file in read mode
# Step 1: Write to file (create/overwrite)
file = open("lyrics.txt", "w")
file.write("Hello this is a sample lyrics file")
file.close()

# Step 2: Now read the file
file = open("lyrics.txt", "r")

print("Position before reading:", file.tell())

data = file.read(10)

print("Position after reading:", file.tell())

file.close()

# Q2 = Write a function read_next_line(filename) that opens a file, moves the file pointer to the 20th byte using seek(), and prints the next line from that position.<br><br><em><strong>Hint:</strong> Use seek(20) before calling readline().</em>


def read_next_line(filename):
    #open file in read mode
    file = open(filename,"r")

    #move file pointer to 20th byte
    file.seek(20)

    #read and print the next line from that position
    line = file.readline()
    print(line)

    file.close()

    #example usage
    read_next_line("lyrics.txt")

# Q3 = Simulate a Zomato-style order history: create a file orders.txt with at least 5 lines (each line is an order). Write a script that reads and prints each order line-by-line using a loop, and after reading each line, prints the file pointer's position using tell().


#create file with 5 orders
file =open("orders.txt","w")

file.write("order 1: pizza margherita\n")
file.write("order 2:burger combo\n")
file.write("order3: biryani special\n")
file.write("order 4: pasta alfredo\n")
file.write("order 5: ice cream sundae\n")

file.close()

# Q4 = Given a file called playlist.txt containing song names (one per line), write code to jump to the start of the third song using seek() and readline(), then print only that song's name.<br><br><em><strong>Constraint:</strong> Do not read the whole file into memory at once.</em>

# Step 1: Create playlist.txt
file = open("playlist.txt", "w")

file.write("Tum Hi Ho\n")
file.write("Kesariya\n")
file.write("Believer\n")
file.write("Perfect\n")
file.write("Shape of You\n")

file.close()

# Step 2: Open the file for reading
file = open("playlist.txt", "r")

# Skip first song
file.readline()

# Skip second song
file.readline()

# Get position of third song
position = file.tell()

# Move pointer to that position
file.seek(position)

# Read and print the third song
third_song = file.readline()

print("Third song:", third_song.strip())

file.close()




