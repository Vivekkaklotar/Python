#Q1 = Create a text file named my_fav_songs.txt using Python's open() function in write ('w') mode, and write the names of your 5 favorite songs into it, each on a new line.


# open file in write mode
file = open ("my_fav_songs.txt","w")

#write 5 favorite songs (you can change names)

file.write("tum hi ho\n")
file.write("tuje sochta hu\n")
file.write("lovely\n")
file.write("perfect\n")

#close the file
file.close()

print("FILE CREATED AND SONGS WRITTEN SUCESSFULLY")


#Q2 = Write a Python script that opens the my_fav_songs.txt file in read ('r') mode and prints each song name to the console with its line number (like a playlist).


#open the file in read mode
file = open("my_fav_songs.txt","r")
#read all lines
songs = file.readlines()

#print each song with line number
for index,song in enumerate(songs,start=1):
    print(f"{index}.{song.strip()}")

#close the file
file.close()


#Q3 = Add 2 more song names to my_fav_songs.txt without deleting the existing content, using Python's open() function in append ('a') mode.


#open file in append mode
file = open("my_fav_songs.txt","a")

#add 2 new songs (they will be added at the end)

file.write("wildflower\n")
file.write("tere bin\n")

#close the file
file.close()

print("2 songs added  successfully!")

# Q4 = Build a script that reads all lines from my_fav_songs.txt, counts how many songs are listed, and displays 'Total songs: X' at the end.<br><br><em><strong>Hint:</strong> Use the readlines() method to get all lines as a list and len() to count.</em>


#open file in read mode
file = open("my_fav_songs.txt","r")
# read all lines into a list
songs = file.readlines()
#close the file
file.close()
#count total songs
total_songs = len(songs)

#display result
print("total songs:", total_songs)

