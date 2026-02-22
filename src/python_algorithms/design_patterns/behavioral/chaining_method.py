class Person(object):
    def __init__(self, name, action):
        """
        Constructor
        :param name:
        :param action:
        """
        self.name = name
        self.action = action

    def do_action(self):
        # print(self.name, self.action.name, end=' ')
        return self.action


class Action(object):
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def set_amount(self, val):
        self.amount = val

    def get_amount(self):
        return self.amount

    def stop(self):
        return 'then stop'

