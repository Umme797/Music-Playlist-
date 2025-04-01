# MUSIC PLAYLIST

class Playlist:
    def __init__(self):
        self.vibes = ["happy", "sad", "energetic", "relaxed"]
        self.happy_songs = ["Let's Go Crazy by Prince", "I Got You (I Feel Good) by James Brown", "Good as Hell by Lizzo"]
        self.sad_songs = ["Let Her Go", "Take me to Church", "Someone Like me"]
        self.energetic_songs = ["Brazil la la la", "Waka Waka by Shakira", "Ms Jackson by BOB"]
        self.relaxed_songs = ["Perfect by Ed Sheeran", "Fly me to Moon", "Beautiful Girl by Sean Kingston"]
        self.playlist = self.create_playlist()



    def create_playlist(self):
        return {vibe: songs for vibe, songs in zip(self.vibes, [self.happy_songs, self.sad_songs, self.energetic_songs, self.relaxed_songs])}



    def display_playlist(self):
        mood = input("How are you feeling today? Enter your mood/genre: ").lower()
        try:
            print("Here's your genre playlist: ")
            for song in self.playlist[mood]:
                print(song)
        except KeyError:
            print("Sorry, the mood is not available in the playlist.")


    def update_playlist(self):
        mood = input("Choose genre you want to update or add: ").strip()
        if not mood:
            print("Invalid input. Please enter a non-empty string.")
            return
        if mood in self.playlist:
            print("This mood exists in the playlist. Add your own songs to update the genre.")
        else:
            print("This mood is new. Add your songs to the new genre.")
        songs = input("Enter songs for mood genre (Separate song names by comma): ").split(",")
        self.playlist[mood] = songs
        print("The mood and its songs have been added to the playlist.")



    def remove_vibes(self):
        vibes_to_remove = input("Enter the genre you want to remove: ")
        try:
            del self.playlist[vibes_to_remove]
            print("Genre & its songs have been removed from the playlist")
        except KeyError:
            print("Genre not found in the playlist.")


def main():
    playlist = Playlist()
    while True:
        print("\n1. Display Playlist")
        print("2. Update Playlist")
        print("3. Remove Vibes")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            playlist.display_playlist()
        elif choice == "2":
            playlist.update_playlist()
        elif choice == "3":
            playlist.remove_vibes()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
