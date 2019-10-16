class Employees(object):
    def __init__(self, name, rate, hours):
        self.name = name
        self.rate = rate
        self.hours = hours


class Resigned(Employees):
    def __init__(self, name, rate, hours, status):
        self.name=name
        self.rate=rate
        self.hours=hours
        self.status=status
