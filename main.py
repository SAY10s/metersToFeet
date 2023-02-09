class Data:
    units = ["meters", "centimeters", "kilometers", "feet", "inches", "yards"]

    def __init__(self):
        self.inputUnit = 1
        self.inputValue = 0
        self.meters = 0

    def choose_units(self):
        self.inputUnit = int(input("1. Meters\n2. Centimetres\n3. Kilometers\n4. Feet\n5. Inches\n6. Yards\nInsert your unit: "))

    def input_value(self):
        self.inputValue = float(input(f"Insert value in {self.units[self.inputUnit-1]}: "))

    def to_meters(self):
        if self.inputUnit == 1:
            self.meters = self.inputValue
        if self.inputUnit == 2:
            self.meters = self.inputValue * 0.01
        if self.inputUnit == 3:
            self.meters = self.inputValue * 1000
        if self.inputUnit == 4:
            self.meters = self.inputValue * 0.3048
        if self.inputUnit == 5:
            self.meters = self.inputValue * 0.0254
        if self.inputUnit == 6:
            self.meters = self.inputValue * 0.9144

    def count4ever(self):
        while True:
            self.choose_units()
            self.input_value()
            self.to_meters()
            print(self.meters)

calculator = Data()
calculator.count4ever()

