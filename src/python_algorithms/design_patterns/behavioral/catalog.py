"""
A class that uses different static function depending of a parameter passed in init.
Note the use of a single dictionary instead of multiple conditions.
"""


class Catalog:
    """
    Catalog of multiple static methods that are executed depending on an init parameter
    """


    def __init__(self, param):
        # dictionary that will be used to determine which static method is
        # to be executed but that will be also used to store possible param
        # value
        self._static_method_choices = {'param_value_1': self._static_method_1, 'param_value_2': self._static_method_2}

        # simple test to validate param value
        if param in self._static_method_choices.keys():
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        return "executed method 1!"

    @staticmethod
    def _static_method_2():
        return "executed method 2!"

    def main_method(self):
        """
        Will execute either _static_method_1 or _static_method_2 depending on self.param value
        """
        return self._static_method_choices[self.param]()


""" Alternative implementation for different levels of methods """
class CatalogInstance:
    def __init__(self, param):
        """
        Catalog of multiple methods that are executed depending on an init parameter
        """
        self.x1 = 'x1'
        self.x2 = 'x2'
        # simple test to validate param value
        if param in ['param_value_1', 'param_value_2']:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    def _instance_method_1(self):
        return "Value {}".format(self.x1)

    def _instance_method_2(self):
        return "Value {}".format(self.x2)

    def main_method(self):
        """
        Will execute either _instance_method_1 or _instance_method_2 depending on self.param value
        """
        if self.param == 'param_value_1':
            return self._instance_method_1()
        return self._instance_method_2()


class CatalogClass:
    """
    Catalog of multiple class methods that are executed depending on an init parameter
    """

    x1 = 'x1'
    x2 = 'x2'

    def __init__(self, param):
        # simple test to validate param value
        if param in ['_class_method_1', '_class_method_2']:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @classmethod
    def _class_method_1(cls):
        return "Value {}".format(cls.x1)

    @classmethod
    def _class_method_2(cls):
        return "Value {}".format(cls.x2)

    def main_method(self):
        """
        Will execute either _class_method_1 or _class_method_2 depending on self.param value
        """
        if self.param == 'param_value_1':
            return self._class_method_1()
        return self._class_method_2()


class CatalogStatic:
    """
    Catalog of multiple static methods that are executed depending on an init parameter
    """

    def __init__(self, param):
        """
        simple test to validate param value
        :param param:
        """
        if param in self._static_method_choices:
            self.param = param
        else:
            raise ValueError("Invalid Value for Param: {0}".format(param))

    @staticmethod
    def _static_method_1():
        return 'executed method 1!'

    @staticmethod
    def _static_method_2():
        return 'executed method 2!'

    _static_method_choices = {'param_value_1': _static_method_1, 'param_value_2': _static_method_2}

    def main_method(self):
        """
        Will execute either _static_method_1 or _static_method_2 depending on self.param value
        """
        if self.param == 'param_value_1':
            return self._static_method_1()
        elif self.param == 'param_value_2':
            return self._static_method_2()
