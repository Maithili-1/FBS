from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, person):
        self.person = person

    @abstractmethod
    def cal_toll(self):
        pass

class TwoWheeler(Vehicle):
    def cal_toll(self):
        toll = 20

        if self.person > 2:
            toll += (self.person - 2) * 10

        return toll

class ThreeWheeler(Vehicle):
    def cal_toll(self):
        toll = 30

        if self.person > 3:
            toll += (self.person - 3) * 20

        return toll

class FourWheeler(Vehicle):
    def cal_toll(self):
        toll = 40

        if self.person > 4:
            toll += (self.person - 4) * 40

        return toll


class HeavyVehicle(Vehicle):
    def cal_toll(self):
        toll = 60

        if self.person > 6:
            toll += (self.person - 6) * 100

        return toll


while True:
    print(f"\n----TOLL---\n1. Two Wheeler\n2. Three Wheeler\n3. Four Wheeler\n4. Heavy Vehicle\n5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 5:
        print("Thank you")
        break
    
    if ch < 1 or ch > 4:
        print("Invalid choice!")
        continue

    persons = int(input("Enter number of persons: "))
    
    if persons <= 0:
        print("Invalid number of persons!")
        continue
        
    if ch == 1:
        vehicle = TwoWheeler(persons)

    elif ch == 2:
        vehicle = ThreeWheeler(persons)

    elif ch == 3:
        vehicle = FourWheeler(persons)

    elif ch == 4:
        vehicle = HeavyVehicle(persons)

    total = vehicle.cal_toll()

    print("Total Toll Amount: Rs.", total)
