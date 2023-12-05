# class Inventory:
#     def __init__(self, capacity):
#         self.__capacity = capacity
#         self.items = []
#
#     def add_item(self, item: str):
#         if self.__capacity > len(self.items):
#             self.items.append(item)
#         else:
#             return "not enough room in the inventory"
#
#     def get_capacity(self):
#         return self.__capacity
#
#     def __repr__(self):
#         result = f"Items: {', '.join(self.items)}."
#         return result + "\n" + f"Capacity left: {self.__capacity - len(self.items)}"


class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        result = ', '.join(self.items)
        return f"Items: {result}.\nCapacity left: {self.__capacity - len(self.items)}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)