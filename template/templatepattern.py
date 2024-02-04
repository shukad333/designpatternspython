class Connect:
    def initialize(self):
        pass
    def connect(self):
        pass

    def con(self):
        self.initialize()
        self.connect()

class TwoGNetwork(Connect):
    def initialize(self):
        print("init 2g")
    def connect(self):
        print("connect 2g")


class ThreeGNetwork(Connect):
    def initialize(self):
        print("init 3g")
    def connect(self):
        print("connect 3g")

nw = TwoGNetwork()
nw.con()
nw = ThreeGNetwork()
nw.con()
