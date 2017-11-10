

class Video():
	"""base class for movies and tv_shows..."""
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration


class Movie(Video):
	"""docstring for Movie"""
	def __init__(self, title, duration, storyline, poster_image, youtube_trailer, release_date):
		super(Movie, self).__init__(title, duration)
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer
		self.release_date = release_date


class Tv_Show(Video):
	"""docstring for TV_Show"""
	def __init__(self, title, duration, storyline, poster_image, youtube_trailer, season, episode, tv_station):
		super(Tv_Show, self).__init__(title, duration)
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = youtube_trailer
		self.season = season
		self.episode = episode
		self.tv_station = tv_station
		
		
		


