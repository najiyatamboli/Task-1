
import random

while True:
    print("===== CAB BOOKING CHATBOT =====")
    print("1. Book Ride")
    print("2. Exit")

    menu = input("Select the number: ")

    match menu:
        case "1":
            print("Select Cab Type:")
            print("1. Auto")
            print("2. Sedan")
            print("3. SUV")

            cab = input("Enter your cab choice: ")

            match cab:
                case "1":
                    cab_type = "Auto"
                    rate = 12
                case "2":
                    cab_type = "Sedan"
                    rate = 18
                case "3":
                    cab_type = "SUV"
                    rate = 25
                case _:
                    print("Invalid cab choice")
                    continue

            print("Select Pickup Location:")
            print("1. Pune Station")
            print("2. Swargate")
            print("3. Hinjawadi")

            pickup = input("Enter pickup choice: ")

            match pickup:
                case "1":
                    source = "Pune Station"
                case "2":
                    source = "Swargate"
                case "3":
                    source = "Hinjawadi"
                case _:
                    print("Invalid pickup choice")
                    continue

            print("Select Destination:")

            if source == "Pune Station":
                print("1. Shivajinagar - 5 km")
                print("2. Kothrud - 8 km")
                print("3. Wakad - 10 km")
            elif source == "Swargate":
                print("1. Kothrud - 8 km")
                print("2. Shivajinagar - 5 km")
                print("3. Wakad - 10 km")
            else:
                print("1. Wakad - 10 km")
                print("2. Kothrud - 8 km")
                print("3. Shivajinagar - 5 km")

            destination_choice = input("Enter destination choice: ")

            match source:
                case "Pune Station":
                    match destination_choice:
                        case "1":
                            destination = "Shivajinagar"
                            distance = 5
                        case "2":
                            destination = "Kothrud"
                            distance = 8
                        case "3":
                            destination = "Wakad"
                            distance = 10
                        case _:
                            print("Invalid destination choice")
                            continue

                case "Swargate":
                    match destination_choice:
                        case "1":
                            destination = "Kothrud"
                            distance = 8
                        case "2":
                            destination = "Shivajinagar"
                            distance = 5
                        case "3":
                            destination = "Wakad"
                            distance = 10
                        case _:
                            print("Invalid destination choice")
                            continue

                case "Hinjawadi":
                    match destination_choice:
                        case "1":
                            destination = "Wakad"
                            distance = 10
                        case "2":
                            destination = "Kothrud"
                            distance = 8
                        case "3":
                            destination = "Shivajinagar"
                            distance = 5
                        case _:
                            print("Invalid destination choice")
                            continue

            fare = rate * distance

            print("===== RIDE DETAILS =====")
            print("Cab Type:", cab_type)
            print("Source:", source)
            print("Destination:", destination)
            print("Distance:", distance, "km")
            print("Rate: Rs.", rate, "/km")
            print("Total Fare: Rs.", fare)

            print("1. Confirm & Share OTP")
            print("2. Cancel Ride")

            confirm = input("Enter your choice: ")

            match confirm:
                case "1":
                    otp = random.randint(1000, 9999)
                    print("Your OTP has been shared:", otp)
                    print("Cancellation is not allowed after OTP sharing.")
                    print("Booking Confirmed!")

                case "2":
                    print("Ride cancelled. No OTP was shared.")

                case _:
                    print("Invalid confirmation choice.")

        case "2":
            print("Thank you for using Cab Booking Chatbot. Goodbye!")
            break

        case _:
            print("Invalid choice. Please select 1 or 2.")
