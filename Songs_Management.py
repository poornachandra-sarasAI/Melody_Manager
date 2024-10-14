### This programm allow developers to interact with a database of songs efficiently.

## Song class to store single song's attributes
class Song:
    # Constructor to define song data
    def __init__(self,title,artist,album,genre,duration):
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
        print(file_name)
        try:
            with open(file_name,"r") as file:
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
        except FileNotFoundError:
            print("File not found!\nTaking back to main menu...\n")
        return

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
    choice = int(input("Select an option: ")) # choosing an option
    #match case for choice selection
    match choice:
        case 1: # Load song data
            file_name = input("Enter the file name to load songs: ")
            db.Load_File(file_name)

        case 2: # View song database
            db.display()
        
        case 3: # Delete a song
            artist = input("Enter the artist's name of the song to delete: ")
            name = input("Enter the title of the song to delete: ")
            if db.delete(artist,name):
                print(f"Deleted {name} by {artist} from the database.")
        
        case 4: # Modify a song
            artist = input("Enter the artist's name of the song to modify: ")
            title = input("Enter the title of the song to modify: ")
            if db.modify(artist,title):
                print(f"Modified {title} by {artist}.")
        
        case 5: # Exiting the programm
            print("Exiting the application. Goodbye!\n")
            break
        
        case _: # Handle invalid options
            print("Please choose option from the menu!")
    print()
