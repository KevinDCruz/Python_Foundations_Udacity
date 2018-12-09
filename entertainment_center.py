import Movie_reviews
import fresh_tomatoes
toy_story = Movie_reviews.Movie(
    "Toy Story",
    "Boys and his toys that come to life",
    "https://images-na.ssl-images-amazon.com/images/I/51K8r9COEQL.jpg",
    "https://www.youtube.com/watch?v=LDXYRzerjzU")

#print("Trailer link: "+ toy_story.trailer_youtube_url)

avatar = Movie_reviews.Movie(
    "Avatar",
    "Marine on an alien planet",
    "http://www.gstatic.com/tv/thumb/v22vodart/3542039/p3542039_v_v8_ac.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print("Avatar Storyline: ", avatar.storyline)
#avatar.show_trailer()

queen = Movie_reviews.Movie(
    "Bohemian Rhapsody",
    "Story of Freddie Mercury",
    "http://www.gstatic.com/tv/thumb/v22vodart/15444050/p15444050_v_v8_as.jpg",
    "https://www.youtube.com/watch?v=mP0VHJYFOAU")

#print("Movie name: ",queen.title)
#queen.show_trailer()

Supernatural = Movie_reviews.TV(
    "Supernatural",
    "Sam and Dean are brothers who hunt Monsters",
    "https://images-na.ssl-images-amazon.com/images/I/51-vKSdEy%2BL.jpg",
    "https://www.imdb.com/title/tt0460681/")

#print("IMDB Link: ", Supernatural.imdb)



conjuring = Movie_reviews.Movie("Conjuring","Exorcisms of Ed and Lorriaine Warren",
    "http://www.gstatic.com/tv/thumb/v22vodart/9379266/p9379266_v_v8_ag.jpg",
    "https://www.youtube.com/watch?v=k10ETZ41q5o")

wild_west = Movie_reviews.Movie("The Good, the Bad and the Ugly",
    "A bounty hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.",
    "http://www.gstatic.com/tv/thumb/v22vodart/4161/p4161_v_v8_aq.jpg",
    "http://www.gstatic.com/tv/thumb/v22vodart/4161/p4161_v_v8_aq.jpg")

comedy = Movie_reviews.Movie("Baby's Day Out",
    "Baby Bink couldn't ask for more; he has adoring (if somewhat sickly-sweet) parents, he lives in a huge mansion, and he's just about to appear in the social pages of the paper.",
    "http://www.gstatic.com/tv/thumb/v22vodart/15781/p15781_v_v8_aa.jpg",
    "http://www.youtube.com/watch?v=UUx66hhznjA")

#movies = [toy_story, avatar, queen, conjuring, wild_west, comedy]
#fresh_tomatoes.open_movies_page(movies=[toy_story, avatar, queen, conjuring, wild_west, comedy])
print(Movie_reviews.Movie.VALID_RATINGS)