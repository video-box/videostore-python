class RentalStatement:
    def __init__(self, customer_name):
        self.rentals = []
        self.total_amount = 0
        self.frequent_renter_points = 0
        self.customer_name = customer_name

    def add_rental(self, rental):
        self.rentals.append(rental)

    def make_rental_statement(self):
        self.clear_totals()
        return self.make_header() + self.make_rental_lines() + self.make_summary()

    def clear_totals(self):
        self.total_amount = 0
        self.frequent_renter_points = 0

    def make_header(self):
        return "Rental Record for " + self.get_name() + "\n"

    def make_rental_lines(self):
        rental_lines = ""

        for rental in self.rentals:
            rental_lines += self.make_rental_line(rental)

        return rental_lines

    def make_rental_line(self, rental):
        this_amount = rental.determine_amount()
        self.frequent_renter_points += rental.determine_frequent_renter_points()
        self.total_amount += this_amount
        
        return self.format_rental_line(rental, this_amount)

    @staticmethod
    def format_rental_line(rental, this_amount):
        return "\t" + rental.get_title() + "\t" + "{:.1f}".format(this_amount) + "\n"

    def make_summary(self):
        return "You owed " + str(self.total_amount) + \
               "\n" + "You earned " + \
               str(self.frequent_renter_points) + " frequent renter points\n"

    def get_name(self):
        return self.customer_name

    def get_amount_owed(self):
        return self.total_amount

    def get_frequent_renter_points(self):
        return self.frequent_renter_points
