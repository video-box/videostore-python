class Rental:
    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def get_title(self):
        return self.movie.get_title()

    def determine_amount(self):
        return self.movie.determine_amount(self.days_rented)

    def determine_frequent_renter_points(self):
        return self.movie.determine_frequent_renter_points(self.days_rented)
