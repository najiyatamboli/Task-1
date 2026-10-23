
from abc import ABC, abstractmethod


# 1. Abstract Passenger Class
class Passenger(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @abstractmethod
    def get_discount(self):
        pass


# 2. Inheritance and Polymorphism
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 10


# 3. Flight Class
class Flight:
    def __init__(self, code, airline, source, destination,
                 seats, base_fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self._seats = seats
        self.base_fare = base_fare

    @property
    def available_seats(self):
        return self._seats

    def reserve_seats(self, count):
        if count > 0 and count <= self._seats:
            self._seats -= count
            return True
        return False

    def display(self):
        print(
            f"{self.code:<10} {self.airline:<12} "
            f"{self.source:<12} {self.destination:<15} "
            f"{self.available_seats:<8} Rs.{self.base_fare}"
        )


# 4. Booking Class
class Booking:
    def __init__(self, booking_id, passenger, flight,
                 tickets, base_total, discount, final_fare):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.tickets = tickets
        self.base_total = base_total
        self.discount = discount
        self.final_fare = final_fare

    def display_summary(self):
        print("\n========== BOOKING SUMMARY ==========")
        print("Booking ID       :", self.booking_id)
        print("Passenger Name   :", self.passenger.name)
        print("Passenger Age    :", self.passenger.age)
        print("Passenger Type   :", type(self.passenger).__name__)
        print("Flight Code      :", self.flight.code)
        print("Airline          :", self.flight.airline)
        print("Source           :", self.flight.source)
        print("Destination      :", self.flight.destination)
        print("Tickets Booked   :", self.tickets)
        print("Base Fare        : Rs.", self.base_total)
        print("Discount         : Rs.", self.discount)
        print("Final Fare       : Rs.", self.final_fare)
        print("Seats Remaining  :", self.flight.available_seats)
        print("=====================================")


# 5. Flight Booking System
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("AI101", "Air India", "Pune", "Delhi", 10, 5000),
            Flight("6E202", "IndiGo", "Mumbai", "Bengaluru", 8, 3500),
            Flight("UK303", "Vistara", "Delhi", "Goa", 5, 4500)
        ]

        self.latest_booking = None
        self.booking_counter = 1000

    # Display flights
    def display_flights(self):
        print("\n================ AVAILABLE FLIGHTS ================")
        print(
            f"{'Code':<10} {'Airline':<12} {'Source':<12} "
            f"{'Destination':<15} {'Seats':<8} Base Fare"
        )
        print("-" * 75)

        for flight in self.flights:
            flight.display()

    # Find flight by code
    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight
        return None

    # Validate booking details
    def validate_details(self, flight, name, age, tickets):
        if flight is None:
            print("Error: Invalid flight code.")
            return False

        if not name.strip():
            print("Error: Name cannot be empty.")
            return False

        if not all(char.isalpha() or char.isspace()
                   for char in name.strip()):
            print("Error: Name must contain letters only.")
            return False

        if age < 1 or age > 120:
            print("Error: Enter a valid age between 1 and 120.")
            return False

        if tickets < 1:
            print("Error: Tickets must be at least 1.")
            return False

        if tickets > flight.available_seats:
            print("Error: Not enough seats available.")
            print("Available seats:", flight.available_seats)
            return False

        return True

    # Calculate fare
    def calculate_fare(self, passenger, flight, tickets):
        base_total = flight.base_fare * tickets
        discount = base_total * passenger.get_discount() / 100
        final_fare = base_total - discount

        return base_total, discount, final_fare

    # Book a flight
    def book_flight(self):
        self.display_flights()

        code = input("\nEnter flight code: ").strip()
        flight = self.find_flight(code)

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter passenger age: "))
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Error: Age and tickets must be numbers.")
            return

        print("\nSelect Passenger Category")
        print("1. Regular Passenger")
        print("2. Student Passenger")

        category = input("Enter category (1 or 2): ").strip()

        if category == "1":
            passenger_class = RegularPassenger
        elif category == "2":
            passenger_class = StudentPassenger
        else:
            print("Error: Invalid passenger category.")
            return

        if not self.validate_details(flight, name, age, tickets):
            return

        passenger = passenger_class(name, age)

        base, discount, total = self.calculate_fare(
            passenger, flight, tickets
        )

        print("\n========== FARE DETAILS ==========")
        print("Tickets          :", tickets)
        print("Fare per ticket  : Rs.", flight.base_fare)
        print("Base Fare        : Rs.", base)
        print("Discount         : Rs.", discount)
        print("Final Fare       : Rs.", total)
        print("==================================")

        confirm = input("Confirm booking? (yes/no): ").strip().lower()

        if confirm != "yes":
            print("Booking cancelled. Seats have not changed.")
            return

        # Change seats only after confirmation
        if not flight.reserve_seats(tickets):
            print("Error: Not enough seats available.")
            return

        self.booking_counter += 1
        booking_id = "BK" + str(self.booking_counter)

        booking = Booking(
            booking_id,
            passenger,
            flight,
            tickets,
            base,
            discount,
            total
        )

        self.latest_booking = booking

        print("\nBooking confirmed successfully!")
        print("Number of tickets booked:", tickets)

        booking.display_summary()

    # View latest booking
    def view_booking(self):
        if self.latest_booking is None:
            print("\nNo confirmed booking found.")
        else:
            self.latest_booking.display_summary()

    # Main menu
    def run(self):
        while True:
            print("\n====== FLIGHT BOOKING APPLICATION ======")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.display_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("Thank you for using Flight Booking Application!")
                break

            else:
                print("Invalid choice. Please select 1-4.")


# 6. Start Application
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()
