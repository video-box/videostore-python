from src.Movie import Movie


class RegularMovie(Movie):
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def determine_amount(self, days_rented):
        this_amount = 2
        if days_rented > 2:
            this_amount += (days_rented - 2) * 1.5

        return this_amount

    def determine_frequent_renter_points(self, days_rented):
        return 1
