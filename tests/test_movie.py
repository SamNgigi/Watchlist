#!/usr/bin/env python3.6
import unittest
from app.models import Movie
# Movie = movie.Movie


class TestMovie(unittest.TestCase):
    """
    Test Class to test the behaviours we expect of the Movie class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_movie = Movie(1, "Python is easy",
                               "A thrilling intro Python series",
                               "https://image/tmdb.org/t/p/w500/khsjha27hbs",
                               9.9, 797773)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))
