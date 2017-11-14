import media
import fresh_tomatoes

'''Create a Movie Object（Toy Story）'''
toy_story = media.Movie('Toy Story', 110, 
			'A story about a boy\'s toys', 
			'http://www.impawards.com/1995/posters/toy_story_ver1_xlg.jpg', 
			'https://www.youtube.com/watch?v=KYz2wyBy3kc', 
			'1995')

'''Create a Movie Object（Avatar）'''
avatar = media.Movie('Avatar', 130, 
		     'Aliens fight against aggressors from earth to protect their home', 
		     'http://www.impawards.com/2009/posters/avatar_xlg.jpg', 
		     'https://www.youtube.com/watch?v=5PSNL1qE6VY', 
		     '1995')

'''Create a Tv_Show Object（Breaking Bad-Season1-Episode1）'''
breaking_bad_s1e1 = media.Tv_Show('Breaking Bad', 45, 'Pilot', 
	'https://i.pinimg.com/736x/a4/b9/de/a4b9de044d3967643e70a87827523ef2--breaking-bad-poster-jesse-pinkman.jpg', 
				  'https://www.youtube.com/watch?v=HhesaQXLuRY', 1, 1, 'Sony Pictures')

'''Create a Tv_Show Object（Breaking Bad-Season1-Episode2）'''
breaking_bad_s1e2 = media.Tv_Show('Breaking Bad', 45, 'Cat\'s in the bag', 
	'https://i.pinimg.com/736x/a4/b9/de/a4b9de044d3967643e70a87827523ef2--breaking-bad-poster-jesse-pinkman.jpg', 
				  'https://www.youtube.com/watch?v=HhesaQXLuRY', 1, 2, 'Sony Pictures')

'''Create a list for toy_story and avatar'''
movies = [toy_story, avatar]

'''Create a list for breaking_bad_s1e1 and breaking_bad_s1e2'''
tv_shows = [breaking_bad_s1e1, breaking_bad_s1e2]

'''call the open_movies_page method to create a html page'''
fresh_tomatoes.open_movies_page(movies, tv_shows)
