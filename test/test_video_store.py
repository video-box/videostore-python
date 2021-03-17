from src.ChildrensMovie import ChildrensMovie
from src.NewReleaseMovie import NewReleaseMovie
from src.RegularMovie import RegularMovie
from src.Rental import Rental
from src.RentalStatement import RentalStatement


class TestVideoStore:
    @classmethod
    def setup_class(cls):
        cls.new_release_1 = NewReleaseMovie("New Release 1")
        cls.new_release_2 = NewReleaseMovie("New Release 2")
        cls.childrens = ChildrensMovie("Childrens")
        cls.regular_1 = RegularMovie("Regular 1")
        cls.regular_2 = RegularMovie("Regular 2")
        cls.regular_3 = RegularMovie("Regular 3")

    @staticmethod
    def assert_amount_and_points(rental_statement, expected_amount, expected_points):
        assert expected_amount == rental_statement.get_amount_owed()
        assert expected_points == rental_statement.get_frequent_renter_points()

    def test_single_new_release_statement(self):
        rental_statement = RentalStatement("Customer Name")
        rental_statement.add_rental(Rental(self.new_release_1, 3))
        rental_statement.make_rental_statement()
        self.assert_amount_and_points(rental_statement, 9.0, 2)

    def test_dual_new_release_statement(self):
        rental_statement = RentalStatement("Customer Name")
        rental_statement.add_rental(Rental(self.new_release_1, 3))
        rental_statement.add_rental(Rental(self.new_release_2, 3))
        rental_statement.make_rental_statement()
        self.assert_amount_and_points(rental_statement, 18.0, 4)

    def test_single_childrens_statement(self):
        rental_statement = RentalStatement("Customer Name")
        rental_statement.add_rental(Rental(self.childrens, 3))
        rental_statement.make_rental_statement()
        self.assert_amount_and_points(rental_statement, 1.5, 1)

    def test_multiple_regular_statement(self):
        rental_statement = RentalStatement("Customer Name")
        rental_statement.add_rental(Rental(self.regular_1, 1))
        rental_statement.add_rental(Rental(self.regular_2, 2))
        rental_statement.add_rental(Rental(self.regular_3, 3))
        rental_statement.make_rental_statement()
        self.assert_amount_and_points(rental_statement, 7.5, 3)

    def test_rental_statement_format(self):
        rental_statement = RentalStatement("Customer Name")
        rental_statement.add_rental(Rental(self.regular_1, 1))
        rental_statement.add_rental(Rental(self.regular_2, 2))
        rental_statement.add_rental(Rental(self.regular_3, 3))

        assert "Rental Record for Customer Name\n" + \
               "\tRegular 1\t2.0\n" + \
               "\tRegular 2\t2.0\n" + \
               "\tRegular 3\t3.5\n" + \
               "You owed 7.5\n" + \
               "You earned 3 frequent renter points\n" == rental_statement.make_rental_statement()
