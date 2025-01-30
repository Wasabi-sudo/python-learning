movies = {
    "007" : "10h00",
    "The Grinch" : "14h30",
    "Toys Story" : " 16h30"
}

print(movies)

movie_title = input("What movie you want to see ?")

showtime = movies.get(movie_title)

if showtime == None:
    print("Ce film n'existe pas.")
else:
    print(f"Vous aller voir le film {movie_title} qui sera diffusé à : {showtime}")