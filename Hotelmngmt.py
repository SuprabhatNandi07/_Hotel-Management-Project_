print("\n=*=*=* Hotel Reservation System =*=*=*")
class HotelManagementSystem:
    def __init__(self):
        self.rooms = {
            "single": 700,  # price per day
            "double": 1200,  # price per day
            "suite": 1650    # price per day
        }

    def calculate_bill(self, room_type, ac, days):
        base_price = self.rooms.get(room_type.lower())
        if base_price is None:
            raise ValueError("Invalid room type selected.")
        
        ac_charge = 20 if ac else 0
        total_bill = (base_price + ac_charge) * days
        return total_bill

    def add_reservation(self):
        name = input("Enter your Name: ")
        room_type = input("Enter type of room (Single/Double/Suite): ")
        ac = input("Air Conditioned (Yes/No): ").lower() == 'yes'
        days = int(input("Enter number of days: "))

        try:
            total_bill = self.calculate_bill(room_type, ac, days)
            print(f"\nReservation Details:\nName: {name}\nRoom Type: {room_type}\nAC: {'Yes' if ac else 'No'}\nDays: {days}\nTotal Bill: Rs.{total_bill}")
            print("___Thank You___")
        except ValueError as e:
            print(e)

def main():
    hotel_system = HotelManagementSystem()
    while True:
        hotel_system.add_reservation()
        another = input("Do you want to add another reservation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
