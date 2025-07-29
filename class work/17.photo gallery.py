#
print("Photo Gallery: ")
gallery = {
    1:"beach.png",
    2:"mountain.jpg",
    3:"party1.jpg",
    4: "selfie.png",
    5:"birthday.png",
    6:"concert.jpg",
    7:"sunset.png",
    8:"tripl.jpg"
}
for i in gallery:
    print(f'{i}.{gallery[i]}')

selected_photos=set(map(int,input("Select photos to share: ").split()))

print("Sharing the following photos:")
for i in selected_photos:
    if 1<=i<=8:
        print(gallery[i])
    else:
        print(f" unable to fetch the image for this id-{i}")


# Select photos to share: 1 2 3 4 23 4
# Sharing the following photos:
# beach.png
# mountain.jpg
# party1.jpg
# selfie.png
# unable to fetch the image for this id-23
