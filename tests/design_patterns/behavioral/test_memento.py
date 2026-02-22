import unittest

from src.python_algorithms.design_patterns.behavioral.memento import NumObj, Transaction


class MementoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.num_obj = NumObj(-1)

    def test_num_obj(self):
        # TODO: write some assertions
        a_transaction = Transaction(True, self.num_obj)
        try:
            for i in range(3):
                self.num_obj.increment()
                # print(num_obj)
            a_transaction.commit()
            # print('-- committed')
            for i in range(3):
                self.num_obj.increment()
                # print(self.num_obj)
            self.num_obj.value += 'x'  # will fail
            # print(self.num_obj)
        except Exception:
            a_transaction.rollback()
            # print('-- rolled back')


        try:
            self.num_obj.do_stuff()
        except Exception:
            print('-> doing stuff failed!')
            import sys
            import traceback
            traceback.print_exc(file=sys.stdout)
