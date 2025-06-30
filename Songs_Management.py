### This programm allow developers to interact with a database of songs efficiently.

## Song class to store single song's attributes
class Song:
    # Constructor to define song data
    def __init__(self,title,artist,album,genre,duration):
        title= formatName(title)
        artist = formatName(artist)
        album = formatName(album)
        genre = formatName(genre)
        duration = formatName(duration)

        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration

    # Return song attributes as dictionary
    def song_dict(self):
        return {
            "title":self.title,
            "artist":self.artist,
            "album":self.album,
            "genre":self.genre,
            "duration":self.duration
        }
    

## Database class for managing playlists and songs
class database:
    # Constructor to empty playlist
    def __init__(self):
        self.playlist = {}

    # Load songs from a specified file to the playlist
    def Load_File(self,file_name):
        try:
            with open(file_name,"r") as file:
                file.readline()
                for line in file:
                    song_attributes = line.strip().split(',')
                    if len(song_attributes) == 5:
                        # Create a Song object
                        song = Song(song_attributes[0],song_attributes[1],song_attributes[2],song_attributes[3],song_attributes[4])
                        # Add the song to the playlist under the artist's name
                        if song.artist not in self.playlist:
                            self.playlist[song.artist] = []
                        self.playlist[song.artist].append(song)
            print(f"Songs loaded from {file_name}.\n")
        except :
            print("File not found!\nTaking back to main menu...\n")
        

    # Display the database in the formatted form
    def display(self):
        print("Song Database:\n")
        print("Title".ljust(30),"Artist".ljust(30),"Genre".ljust(20))
        print("="*80)
        for artist in self.playlist:
            songs = self.playlist[artist]
            for s in songs:
                print(s.title.ljust(30), s.artist.ljust(30), s.genre.ljust(20))
        return

    # Delete the song based on artist and song title from the database
    def delete(self,artist,title):
        if artist in self.playlist:
            for song in self.playlist[artist]:
                if song.title == title:
                    self.playlist[artist].remove(song)
                    if not self.playlist[artist]:
                        del self.playlist[artist]
                    return True
            print("Song not found")
        else:
            print("Artist Not Found")
        return False
    
    # Modify a song's attributes based on artist and title
    def modify(self,artist,title):
        if artist in self.playlist:
            for song in self.playlist[artist]:
                if song.title == title:
                    print("Current Details:")
                    print(song.song_dict())
                    # Prompt for new attributes, allowing empty input to keep current values
                    album = input("Enter new album (or press Enter to keep current): ")
                    if album:
                        song.album = album
                    genre = input("Enter new genre (or press Enter to keep current): ")
                    if genre:
                        song.genre = genre
                    duration = input("Enter new duration (or press Enter to keep current): ")
                    if duration:
                        song.duration = duration
                    return True
            print("Song not found")
        else:
            print("Artist Not Found")
        return False


def input_choice():
    '''
    Documentation for the input_choice()
    Takes an input and makes sure exceptions are handled
    '''
    count =0
    while(count<5): #Will tolerate maximum of 5 incorrect entries
        try:
            choice = int(input("\nChoose an option (1,2,3,4 or 5): "))
        except:
            print("Invalid input!")
        else:
            return choice
        finally:
            count += 1
    if count>=5 :
        print("Too many incorrect inputs, please try after sometime.")
        exit()


def formatName(name):
    '''
    Documentation for formatName()
    This function will remove any leading or trailing whitespaces.
    It also converts the name to tite case.
    '''
    #Removing any single or double quotes
    name = name.strip()
    name = name.strip("'")
    name = name.strip('"')
    name = name.strip()
    return name.title()


# Function to display Developer's menu->
def menu():
    print("Developer Menu:")
    print("1. Load Song Data")
    print("2. View Song Database")
    print("3. Delete a Song")
    print("4. Modify a Song")
    print("5. Exit\n")


db = database()
while True:
    menu() #displaying the menu
    choice = input_choice() # choosing an option
    #match case for choice selection
    
    if choice == 1: # Load song data
        file_name = input("Enter the file name to load songs: ")
        db.Load_File(file_name)

    if choice == 2: # View song database
        db.display()
        
    elif choice == 3: # Delete a song
        artist = input("Enter the artist's name of the song to delete: ")
        name = input("Enter the title of the song to delete: ")
        artist = formatName(artist)
        name = formatName(name)
        if db.delete(artist,name):
            print(f"Deleted {name} by {artist} from the database.")
        
    elif choice == 4: # Modify a song
        artist = input("Enter the artist's name of the song to modify: ")
        title = input("Enter the title of the song to modify: ")
        artist = formatName(artist)
        title = formatName(title)
        if db.modify(artist,title):
            print(f"Modified {title} by {artist}.")
        
    elif choice == 5: # Exiting the programm
        print("Exiting the application. Goodbye!\n")
        break
        
    else : # Handle invalid options
        print("Please choose option from the menu!")
    print()
