##
class Youtube:
    def playvideo(self):
        print("Video is running with....")
        print("Ads will run")
        print("No background play")
        print("Low quality available")
        print("Play back speed (upto 2x)")

    def youtubeMusic(self):
        print("No access to YouTube Music in free version")
    def likes(self):
        print("You can like videos")
    def share(self):
        print("You can share videos with others")
    def comments(self):
        print("You can comment on videos")
    def subscribe(self):
        print("You can subscribe to channels")
    def upload(self):
        print("You can upload your own videos")
    def watchhistory(self):
        print("You can view your watch history")
    def downloads(self):
        print("No access to Downloads in free version")


# Premium version using inheritance
class PremiumYoutube(Youtube):
    def playvideo(self):
        print("Viedo is running with...")
        print("ads free ")
        print("Background run")
        print("High quality ")
        print("Play back speed (upto 3x)")

    def youtubeMusic(self):
        print("Exclusive Music" )
    def downloads(self):
        print("You can download all videos with high quality")


sita = PremiumYoutube()
print("\n sita - PremiumYoutube ")
sita.playvideo()
sita.youtubeMusic()
sita.downloads()
sita.likes()
sita.share()
sita.comments()
sita.subscribe()
sita.upload()
sita.watchhistory()

priya = Youtube()
print("\n sita - Normal User ")
priya.playvideo()
priya.youtubeMusic()
priya.downloads()
priya.likes()
priya.share()
priya.comments()
priya.subscribe()
priya.upload()
priya.watchhistory()
