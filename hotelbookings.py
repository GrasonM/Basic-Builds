from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_booked = False

    def __repr__(self):
        return f"Room {self.room_number} ({self.room_type}) - ${self.price}"

class Booking:
    def __init__(self, room, check_in_date, check_out_date):
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def __repr__(self):
        return f"Booking for Room {self.room.room_number} from {self.check_in_date} to {self.check_out_date}"

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def check_availability(self, check_in_date, check_out_date):
        available_rooms = []
        for room in self.rooms:
            if all(booking.room != room or not (
                    booking.check_in_date < check_out_date and booking.check_out_date > check_in_date)
                   for booking in self.bookings):
                available_rooms.append(room)
        return available_rooms

    def book_room(self, room_number, check_in_date, check_out_date):
        room = next((r for r in self.rooms if r.room_number == room_number), None)
        if room:
            if room in self.check_availability(check_in_date, check_out_date):
                booking = Booking(room, check_in_date, check_out_date)
                self.bookings.append(booking)
                room.is_booked = True
                return booking
            else:
                return f"Room {room_number} is not available for the selected dates."
        else:
            return f"Room {room_number} does not exist."

    def __repr__(self):
        return f"Hotel {self.name} with {len(self.rooms)} rooms"

# Example usage
hotel = Hotel("Grand Plaza")
hotel.add_room(Room(101, "Single", 100))
hotel.add_room(Room(102, "Double", 150))
hotel.add_room(Room(103, "Suite", 200))

print(hotel)

check_in_date = datetime(2024, 6, 20)
check_out_date = datetime(2024, 6, 22)

print("Available rooms:", hotel.check_availability(check_in_date, check_out_date))

booking = hotel.book_room(101, check_in_date, check_out_date)
print(booking)

print("Available rooms after booking:", hotel.check_availability(check_in_date, check_out_date))

#Built with assistance from openai