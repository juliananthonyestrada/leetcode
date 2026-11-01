class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.small_spots = small
        self.medium_spots = medium
        self.big_spots = big

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big_spots > 0:
            self.big_spots -= 1
            return True
        if carType == 2 and self.medium_spots > 0:
            self.medium_spots -= 1
            return True
        if carType == 3 and self.small_spots > 0:
            self.small_spots -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)