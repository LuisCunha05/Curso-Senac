class Cart:
    def __init__(self):
        self.data = {}

    def add(self, name:str, quantity:int = 0, price:float = None) -> int:
        if name in self.data:
            self.data[name]['quantity'] += quantity
            return self.data[name]['quantity']
        else:
            if not price:
                raise ValueError(f"Price must be provided for a new product '{name}'.")
            self.data[name] = {'price': price, 'quantity': quantity}
            return self.data[name]['quantity']

    def sub(self, name:str, quantity:int = 1) -> int:
        if name in self.data:
            self.data[name]['quantity'] -= quantity
            if(self.data[name]['quantity'] <= 0):
                del self.data[name]
                return 0
            return self.data[name]['quantity']
        else:
            print(f"{name} not in data.")

    def getTotalValue(self) -> float:
        return sum(item['price'] * item['quantity'] for item in self.data.values())

    def getTotalAmount(self) -> int:
        return sum(item['quantity'] for item in self.data.values())

    def show(self):
        for name, details in self.data.items():
            print(f"{name}: quant: {details['quantity']} e price: {details['price']:.2f} R$")

    def clearAll(self):
        """Removes all items in the cart"""
        self.data.clear()