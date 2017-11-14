

class Video():
	"""base class for movies and tv_shows..."""
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration


class Movie(Video):
	"""used to store movie data"""
	def __init__(self, title, duration, storyline, poster_image, youtube_trailer, release_date):
		'''called the parent class's constructor to do the common initial thing'''
		super(Movie, self).__init__(title, duration)
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer
		self.release_date = release_date


class Tv_Show(Video):
	"""used to store tv_show data"""
	def __init__(self, title, duration, storyline, poster_image, youtube_trailer, season, episode, tv_station):
		'''called the parent class's constructor to do the common initial thing'''
		super(Tv_Show, self).__init__(title, duration)
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer
		self.season = season
		self.episode = episode
		self.tv_station = tv_station
		
		
		


