import Movie_reviews

toy_story = Movie_reviews.Movie(
    "Toy Story",
    "Boys and his toys that come to life",
    "https://images-na.ssl-images-amazon.com/images/I/51K8r9COEQL.jpg",
    "https://www.youtube.com/watch?v=LDXYRzerjzU")

print("Trailer link: "+ toy_story.trailer_youtube_url)

avatar = Movie_reviews.Movie(
    "Avatar",
    "Marine on an alien planet",
    "http://www.gstatic.com/tv/thumb/v22vodart/3542039/p3542039_v_v8_ac.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

print("Avatar Storyline: ", avatar.storyline)
#avatar.show_trailer()

queen = Movie_reviews.Movie(
    "Bohemian Rhapsody",
    "Story of Freddie Mercury",
    "http://www.gstatic.com/tv/thumb/v22vodart/15444050/p15444050_v_v8_as.jpg",
    "https://www.youtube.com/watch?v=mP0VHJYFOAU")

print("Movie name: ",queen.title)
queen.show_trailer()

Supernatural = Movie_reviews.TV(
    "Supernatural",
    "Sam and Dean are brothers who hunt Monsters",
    "https://images-na.ssl-images-amazon.com/images/I/51-vKSdEy%2BL.jpg",
    "https://www.imdb.com/title/tt0460681/")

print("IMDB Link: ", Supernatural.imdb)