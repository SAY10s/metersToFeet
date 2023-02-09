class Data:
    def metersToFeet(self, m):
        print(f"{m}m are {m * 3.2808}ft")

    def feetToMeters(self, ft):
        print(f"{ft}ft are {ft * 0.3048}m")


data = Data()
data.metersToFeet(30)
data.feetToMeters(30)
