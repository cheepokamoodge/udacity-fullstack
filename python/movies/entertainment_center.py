from movies import media
from movies import fresh_tomatoes

top1 = media.Movie ('The 10 Commandments',
                            'Moses just received the 10 commandments from god, but he is having a hard time making the hebrew people believe in him',
                            'https://github.com/marcelobrandao/udacity-fullstack/blob/master/python/movies/imgs/top1.jpg?raw=true',
                            'https://youtu.be/eLawrQ1KQno?cc_load_policy=1&cc_lang_pref=en')

top2 = media.Movie ('Emoticon',
                            'In order to date nowadays on must understand Emoticons Language',
                            'https://github.com/marcelobrandao/udacity-fullstack/blob/master/python/movies/imgs/top2.jpg?raw=true',
                            'https://www.youtube.com/watch?v=1UptRVmFtMg')

top3 = media.Movie ('Wonder Twins in HR Department',
                          'Wonder Twins are on the Justices League HR department, but things dont turn well for Zen',
                          'https://github.com/marcelobrandao/udacity-fullstack/blob/master/python/movies/imgs/top3.jpg?raw=true'
                          '@._V1_UX182_CR0,0,182,268_AL_.jpg',
                          'https://www.youtube.com/watch?v=GY9Aiieerrk')

snatch = media.Movie ('Snatch',
                      'A group of up-and-coming hustlers who stumble upon a truck-load of stolen gold bullion are '
                      'suddenly thrust into the high-stakes world of organized crime.',
                      'https://m.media-amazon.com/images/M/MV5BMzEyMTc4NzEyMl5BMl5BanBnXkFtZTgwMzA2OTYzNjM'
                      '@._V1_UX182_CR0,0,182,268_AL_.jpg',
                      'https://www.youtube.com/watch?v=9Jar2XkBboo')

matrix = media.Movie ('The Matrix',
                      'A computer hacker learns from mysterious rebels about the true nature of his reality and his '
                      'role in the war against its controllers.',
                      'https://m.media-amazon.com/images/M'
                      '/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY'
                      '@._V1_UX182_CR0,0,182,268_AL_.jpg',
                      'https://www.youtube.com/watch?v=Q8g9zL-JL8E')

rock_rolla = media.Movie ('The Matrix',
                          'In London, a real-estate scam puts millions of pounds up for grabs, attracting some of the '
                          'citys scrappiest tough guys and its more established underworld types, all of whom are '
                          'looking to get rich quick. While the citys seasoned criminals vie for the cash, '
                          'an unexpected player -- a drugged-out rock n roller presumed to be dead but very much '
                          'alive -- has a multi-million-dollar prize fall into his hands.',
                          'https://m.media-amazon.com/images/M/MV5BMTQ0NTk5Mzk2OV5BMl5BanBnXkFtZTcwMDE3NTE4MQ'
                          '@@._V1_UX182_CR0,0,182,268_AL_.jpg',
                          'https://www.youtube.com/watch?v=F_n0e3d4ruE')

movies = [top1, top2, top3, snatch, matrix, rock_rolla]
fresh_tomatoes.open_movies_page(movies)