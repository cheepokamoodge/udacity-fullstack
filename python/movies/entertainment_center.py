from movies import media
from movies import fresh_tomatoes

# Porta dos Fundos is a Brazilian comedy YouTube channel. It is the 4th most-subscribed
# channel in Brazil, and 49th overall, with over 13 million subscribers as of June 2017
# The following program displays a webpage with my top 6 best episodes

# All episodes selected here have the option to display English subtitle

# Generate the instances of class Movie which takes as arguments :
# movie_title -- The Title of the episode
# movie_storyline -- A brief description of the episode
# poster_image -- A link for the images related to each episode
# trailer_youtube -- the you tube link for the related episode

top1 = media.Movie ('The 10 Commandments',
                    'Moses just received the 10 commandments from god, but he is having a hard time making the hebrew '
                    'people believe in him',
                    'https://github.com/marcelobrandao/udacity-fullstack/blob/master/python/movies/imgs/top1.jpg?raw'
                    '=true',
                    'https://youtu.be/eLawrQ1KQno?cc_load_policy=1&cc_lang_pref=en')

top2 = media.Movie ('Emoticon',
                    'In order to date nowadays on must understand Emoticons Language',
                    'https://github.com/marcelobrandao/udacity-fullstack/blob/master/python/movies/imgs/top2.jpg?raw'
                    '=true',
                    'https://www.youtube.com/watch?v=1UptRVmFtMg')

top3 = media.Movie ('Wonder Twins in HR Department',
                    'Wonder Twins are on the Justices League HR department, but things dont turn well for Zen',
                    'https://github.com/marcelobrandao/udacity-fullstack/blob/master/python/movies/imgs/top3.jpg?raw'
                    '=true '
                    '@._V1_UX182_CR0,0,182,268_AL_.jpg',
                    'https://www.youtube.com/watch?v=GY9Aiieerrk')

top4 = media.Movie ('Living Alone',
                    'Living alone for the first time as not as easy as it looks.',
                    'https://github.com/marcelobrandao/udacity-fullstack/blob/master/python/movies/imgs/top4.jpg?raw'
                    '=true',
                    'https://www.youtube.com/watch?v=71nbCHS1B8Q')

top5 = media.Movie ('Brazilian Justice',
                    'Brazilian Justice is not always so blind',
                    'https://github.com/marcelobrandao/udacity-fullstack/blob/master/python/movies/imgs/top5.jpg?raw'
                    '=true',
                    'https://www.youtube.com/watch?v=NdIqyc-jSSs')

top6 = media.Movie ('Creative Meeting',
                    'Jesus and God on a creative meeting',
                    'https://github.com/marcelobrandao/udacity-fullstack/blob/master/python/movies/imgs/top6.jpg?raw'
                    '=true',
                    'https://www.youtube.com/watch?v=YTlQ_2SaQmM')

# Group the instances of Movie into a lit
movies = [top1, top2, top3, top4, top5, top6]

# Pass the list as an argumento the the function open_movies_page which generates a pre defined HTML file.
fresh_tomatoes.open_movies_page (movies)
