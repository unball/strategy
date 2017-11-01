class Player(object):
    target = [0, 0]
    th = 0
    control_option = 0
    
    def __init__(self, strategy):
        self.target = strategy.getTarget()
        self.th = strategy.getTh()
        self.control_option = strategy.getControl_Option()

    def getTarget(self):
        return self.target

    def getTh(self):
        return self.th

    def getControl_Option(self):
        return self.control_option

    def printValues(self):
        print self.target, self.th, self.control_option
