class Mobile:
    def company(self):
        pass

class Android(Mobile):
    def company(self):
        return "Android"

class Apple(Mobile):
    def company(self):
        return "Apple"

class MobileFactory:
    @staticmethod
    def create_mobile(type):
        if type == 'android':
            return Android()
        else:
            return Apple()

m = Mobile()
m1 = MobileFactory.create_mobile("android")
m2 = MobileFactory.create_mobile("apple")

print(m1.company())
print(m2.company())