#Will create 2 classes: song and artist. The object of song will be used as a data member for artist

class Song():
    def __init__(self,name,artist,album,genre,duration):
        name = formatName(name)
        artist = formatName(artist)
        album = formatName(album)
        genre = formatName(genre)
        duration = formatName(duration)

        self.name = name
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration
    
class Artist():
    def __init__(self,name,song):
        name = formatName(name)
        self.name = name
        self.songs = {song.name:song}
    
    #Add song to the artist's collection
    def add_song(self,song):

        self.songs.update({str(song.name) : song})


'''Defining all the required functions'''

def input_choice():
    '''
    Documentation for the input_choice()
    Takes an input and makes sure exceptions are handled
    '''
    count =0
    while(count<5): #Will tolerate maximum of 5 incorrect entries
        try:
            choice = int(input("\nChoose an option (1,2 or 3): "))
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


'''All required functions defined'''

#Extracting information from file
f = open("Songs.txt","r")
f.readline() #As the document starts with a header
playlist = {}

#Formatting and storing the information in the dictionary
for line in f:
    info = list(line[:-1].split(','))
    if(len(info)==5):
        song = Song(info[0],info[1],info[2],info[3],info[4])
        #If the artist is not in the playlist, add the artist and the song
        if song.artist not in playlist.keys():
            artist = Artist(song.artist,song)
            playlist[artist.name] = artist
        #If the artist is already in the playlist, add the song to the artist's collection
        else:
            playlist[song.artist].add_song(song)

f.close()
count = 0
while(1):
    if count >4:
      print("Too many unsuccessful attempts. Exiting the session\n")
    
    print("--- User Menu ---")
    print("1. Search for a Song by Title")
    print("2. Search for all Songs by an Artist")
    print("3. Exit")

    choice = input_choice()

    if choice == 1:
        status = False
        song_name = input("Enter the song title: ")
        song_name = formatName(song_name)
        for artist,artist_obj in playlist.items():
                for title,song in artist_obj.songs.items():
                    if title == song_name:
                        print(f"Found: {song.name} by {song.artist} ,Genre: {song.genre}, Album: {song.album}\n")
                        status = True
                        break

        if status == False:
            print("Song not found!\n")
    
    elif choice == 2:
        artist_name = input("Enter the artist name: ")
        artist_name = formatName(artist_name)
        if artist_name not in playlist.keys():
            print("Artist not found!\n")

        else:
            artist_obj = playlist[artist_name]
            print(f"Searching for songs by artist: {artist_obj.name}")
            for title,song in artist_obj.songs.items():
                print(f"Found: {title} (Genre: {song.genre}, Album: {song.album}, Duration: {song.duration})")
            print("\n")
            
    
    elif choice == 3:
        print("Exiting... Goodbye!")
        exit()
    
    else:
        count +=1
        print("Invalid choice. Please try again.")
    
