class Movie():
    """This is the Movie Class where we can create our own movies instances


       Attributes:
           movie_title (str): This is the Movie name attribute
           movie_poster_image_url (str): This is the Poster Image url in order to show it in the html page
           movie_trailer_youtube_url (str): This is the trailer url in order to show it in the html page

       """

    def __init__(self,movie_title,movie_poster_image_url,movie_trailer_youtube_url):
        self.title=movie_title
        self.poster_image_url=movie_poster_image_url
        self.trailer_youtube_url=movie_trailer_youtube_url