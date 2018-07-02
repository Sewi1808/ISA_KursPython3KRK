class FlowerShop:
    def __init__(self):
        self.flower_dict = {"": []}


class Flower:
    def __init__(self, f_type):
        self.f_type = f_type


class Bouquet:
    def __init__(self, f_value, f_type):
        self.f_value = f_value
        self.f_type = f_type


class Bill:
    def __init__(self, f_price, f_count):
        self.f_price = f_price
        self.f_count = f_count

    def evaluate(self):
        return self.f_price * self.f_count



rose = Flower("Rose")
b1 = Bouquet(12, rose.f_type)
set0 = FlowerShop({"Rose": [10, 120]})
set1 = FlowerShop({"Tulip": [15, 150]})
bill0 = Bill(set0.flower_dict["Rose"][0], set0.flower_dict["Rose"][1])
bill1 = Bill(10, 5)

print("b1:\n", b1.f_type, b1.f_value)
print("rose:\n", rose.f_type)
print("set0", set0.flower_dict)
print("set1", set1.flower_dict)
print("bill0:\n", bill0.evaluate())
print("bill0:\n", bill1.evaluate())
