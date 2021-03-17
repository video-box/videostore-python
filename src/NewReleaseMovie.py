from src.Movie import Movie


class NewReleaseMovie(Movie):
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def determine_amount(self, days_rented):
        return days_rented * 3

    def determine_frequent_renter_points(self, days_rented):
        return 2 if days_rented > 1 else 1
