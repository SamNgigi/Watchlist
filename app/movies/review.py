class Review:
    all_reviews = []

    def __init__(self, movie_id, review_title, imageurl, review):
        """
        Defining properties for our object
        """
        self.movie_id = movie_id
        self.review_title = review_title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        """
        Method to save reviews
        """
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        """
        Method to clear review list
        """
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls, id):
        response = []
        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)
        return response
