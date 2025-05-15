file = open("mybio.txt", "a")
file.write("Nama: Nino\n")
file.write("Hobi: Main game")

bio = open("mybio.txt", "r")
print(bio.read())