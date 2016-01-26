import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story 3", "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
    "http://ia.media-imdb.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SY317_CR5,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?v=JcpWXaA2qeg")
avatar_movie = media.Movie("Avatar", "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
    "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SY317_CR0,0,214,317_AL_.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
synchronicity = media.Movie("Synchronicity", "A physicist who invents a time machine must travel back to the past to uncover the truth about his creation and the woman who is trying to steal it.",
    "http://ia.media-imdb.com/images/M/MV5BMTc2NDAyOTc4MV5BMl5BanBnXkFtZTgwNjE4Mjk0NzE@._V1_SX214_AL_.jpg", "https://www.youtube.com/watch?v=E1el06Ic5Ts")
game_of_thrones = media.Movie("Game of Thrones", "While a civil war brews between several noble families in Westeros, the children of the former rulers of the land attempt to rise up to power. Meanwhile a forgotten race, bent on destruction, return after thousands of years in the North.",
    "http://ia.media-imdb.com/images/M/MV5BMTYwOTEzMDMzMl5BMl5BanBnXkFtZTgwNzExODIzNzE@._V1_SX214_AL_.jpg",
    "https://www.youtube.com/watch?v=IxI8aPISq8I")

movies = [toy_story, avatar_movie, synchronicity, game_of_thrones]
fresh_tomatoes.open_movies_page(movies)
