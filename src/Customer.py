class Customer:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statement(self):
        total_amount = 0.0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"

        for rental in self.rentals:
            this_amount = 0.0
            movie_type = rental.get_price_code()

            if movie_type == "REGULAR":
                this_amount += 2
                if rental.get_days_rented() > 2:
                    this_amount += (rental.get_days_rented() - 2) * 1.5

            elif movie_type == "NEW_RELEASE":
                this_amount += rental.get_days_rented() * 3

            elif movie_type == "CHILDRENS":
                this_amount += 1.5
                if rental.get_days_rented() > 3:
                    this_amount += (rental.get_days_rented() - 3) * 1.5

            frequent_renter_points += 1

            if movie_type == "NEW_RELEASE" and rental.get_days_rented() > 1:
                frequent_renter_points += 1

            result += "\t" + rental.getMovie().getTitle() + "\t" + str(this_amount) + "\n"

            total_amount += this_amount

        result += "You owed " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points\n"

        return result
