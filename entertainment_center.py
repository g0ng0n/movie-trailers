import media
import fresh_tomatoes


terminator = media.Movie("Terminator",
                         "http://t1.gstatic.com/images?q=tbn:ANd9GcRHzSaUCOKu1RwS-bfbaUeeo_I1JcBkiuJRjBElvJi7qsHXkUkJ",
                         "https://www.youtube.com/watch?v=lHz95RYUbik")

terminator_the_judgment_day = media.Movie("Terminator 2 - Judgement Day ",
                                          "https://elehti.files.wordpress.com/2012/09/terminator_2_1991_6.jpg",
                                          "https://www.youtube.com/watch?v=aAr8llumKnY")

terminator_genesys = media.Movie("Terminator Genesys",
                                 "http://www.theterminatorfans.com/wp-content/uploads/2015/05/Terminator-Genisys-US-Poster.jpeg",
                                 "https://www.youtube.com/watch?v=62E4FJTwSuc")

#Here we create the movie List with the Movie instances in order to use the open_movies_page method
movies = [terminator,terminator_the_judgment_day,terminator_genesys]

fresh_tomatoes.open_movies_page(movies)