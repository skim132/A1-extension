""" Sunwoo kim
    772978633
    skim864
    extension
"""
class Director:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if len(self.name) > 0:
            return f"<Director {self.name}>"
        else:
            return "<Director None>"

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and self.name == other.name)

    def __lt__(self, other):
        return (self.name < other.name)

    def __hash__(self):
        return hash(self.name)

    @property
    def director_full_name(self):
        return self.name

    @director_full_name.setter
    def director_full_name(self, newName):
        self.name = newName


class Genre:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if len(self.name) > 0:
            return f"<Genre {self.name}>"
        else:
            return "<Genre None>"

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and self.name == other.name)

    def __lt__(self, other):
        return (self.name < other.name)

    def __hash__(self):
        return hash(self.name)

    @property
    def genre_name(self):
        return self.name

    @genre_name.setter
    def genre_name(self, newName):
        self.name = newName


class Actor:
    def __init__(self, name=None):
        if (isinstance(name, str) and len(name) > 0):
            self.name = name
        else:
            self.name = None
        self.colleagues = []

    def __repr__(self):
        return f"<Actor {self.name}>"

    def __eq__(self, other):
        return (self.__class__ == other.__class__ and self.name == other.name)

    def __lt__(self, other):
        return (self.name < other.name)

    def __hash__(self):
        return hash(self.name)

    @property
    def actor_full_name(self):
        return self.name

    @actor_full_name.setter
    def actor_full_name(self, newName):
        self.name = newName

    def add_actor_colleague(self, colleague):
        self.colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return (colleague in self.colleagues)


class Movie:
    def __init__(self, titleArg=None, yearArg=None):
        self.movie_title = None
        if (isinstance(titleArg, str) and len(titleArg) > 0):
            self.movie_title = titleArg.strip()
        self.movie_year = None
        if (isinstance(yearArg, int) and yearArg >= 1900):
            self.movie_year = yearArg
        self.movie_description = None
        self.movie_director = None
        self.movie_actors = []
        self.movie_genres = []
        self.movie_runtime_minutes = None

    def __repr__(self):
        return f"<Movie {self.movie_title}, {self.movie_year}>"

    def __eq__(self, other):
        return (
                    self.__class__ == other.__class__ and self.movie_title == other.movie_title and self.movie_year == other.movie_year)

    def __lt__(self, other):
        if self.movie_title == other.movie_title:
            return (self.movie_year < other.movie_year)
        else:
            return (self.movie_title < other.movie_title)

    def __hash__(self):
        return hash(self.movie_title + str(self.movie_year))

    @property
    def title(self):
        return self.movie_title

    @property
    def description(self):
        return self.movie_description

    @property
    def director(self):
        return self.movie_director

    @property
    def actors(self):
        return self.movie_actors

    @property
    def runtime_minutes(self):
        return self.movie_runtime_minutes

    @property
    def genres(self):
        return self.movie_genres

    @property
    def runtime_minutes(self):
        return self.movie_runtime_minutes
    @title.setter
    def title(self, newTitle):
        if (isinstance(newTitle, str) and len(newTitle) > 0):
            self.movie_title = newTitle.strip()

    @description.setter
    def description(self, newDescrip):
        if (isinstance(newDescrip, str) and len(newDescrip) > 0):
            self.movie_description = newDescrip.strip()

    @director.setter
    def director(self, newDirector):
        if (isinstance(newDirector, Director)):
            self.movie_director = newDirector

    @actors.setter
    def actors(self, newActors):
        if (isinstance(newActors, list)):
            self.movie_actors = newActors

    @genres.setter
    def genres(self, newGenres):
        if (isinstance(newGenres, list)):
            self.movie_genres = newGenres

    @runtime_minutes.setter
    def runtime_minutes(self, newRuntime):
        if (isinstance(newRuntime, int)):
            if (newRuntime >= 0):
                self.movie_runtime_minutes = newRuntime
            else:
                raise ValueError('ValueError: Negative runtime value!')

    def add_actor(self, newActor):
        if (isinstance(newActor, Actor) and not newActor in self.movie_actors):
            self.movie_actors.append(newActor)

    def add_genre(self, newGenre):
        if (isinstance(newGenre, Genre) and not newGenre in self.movie_genres):
            self.movie_genres.append(newGenre)

    def remove_actor(self, remActor):
        if (isinstance(remActor, Actor) and remActor in self.movie_actors):
            self.movie_actors.remove(remActor)
        elif (isinstance(remActor, str)):
            for actor in self.movie_actors:
                if actor.actor_full_name == remActor:
                    self.movie_actors.remove(actor)
                    break

    def remove_genre(self, remGenre):
        if (isinstance(remGenre, Genre) and remGenre in self.movie_genres):
            self.movie_genres.remove(remGenre)
        elif (isinstance(remGenre, str)):
            for genre in self.movie_genres:
                if genre.genre_name == remGenre:
                    self.movie_genres.remove(genre)
                    break

""" Implementing the watchlist according to the specification of it"""
class WatchList:
    def __init__(self):
        self.__movies=list()
        self.__ind=0
    @property
    def movie(self):
        return self.__movies
    """get the size of movies"""
    def size(self):
        return len(self.__movies)
    """add the movie that is not in the watchlist"""
    def add_movie(self,movie:Movie):
        if movie not in self.__movies:
            self.__movies.append(movie)
    """remove movie if its in the list else pass it"""
    def remove_movie(self,movie:Movie):
        if movie in self.__movies:
            self.__movies.remove(movie)
        else:
            pass
    """ get the first value in the list"""
    def first_movie_in_watchlist(self):
        if self.size()==0:
            return None
        else:
            return self.__movies[self.__ind]
    """ if index is greater than the size return none
        else return index of it"""
    def select_movie_to_watch(self,index):
        if index>self.size():
            return None
        else:
            return self.__movies[index]
    def __iter__(self):
        return self
    def __next__(self):
        self.__ind += 1
        if self.__ind >= len(self.__movies):
            self.__ind = -1
            raise StopIteration
        else:
            return self.__movies[self.__ind]
watchlist = WatchList()
watchlist.add_movie(Movie("Moana", 2016))
watchlist.add_movie(Movie("Ice Age", 2002))
watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
watchlist.add_movie(Movie("2012",2012))
for i in watchlist:
    print(i)



