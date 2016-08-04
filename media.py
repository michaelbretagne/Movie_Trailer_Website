import webbrowser

class Video():  # Class parent Video. As Class Movie ans Class TvShow as childs
	def __init__(self, title, storyline, poster_image, trailer_youtube, year_release):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.year_release = year_release

class Movie(Video):  # Class Movie. Child of the parent class Video
	def __init__(self, title, storyline, poster_image, trailer_youtube,year_release,
				runing_time, movie_rating):
		Video.__init__(self, title, storyline, poster_image, trailer_youtube, year_release)
		self.runing_time = runing_time
		self.movie_rating = movie_rating

class TvShow(Video):  # Class TvShow. Child of the parent class Video
	def __init__(self, title, storyline, poster_image, trailer_youtube,year_release,
				runing_time, movie_rating, number_of_seasons):
		Video.__init__(self, title, storyline, poster_image, trailer_youtube, year_release)
		self.runing_time = runing_time
		self.movie_rating = movie_rating
		self.number_of_seasons = number_of_seasons
		
		