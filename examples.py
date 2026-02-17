import logging
import random

from selfie import selfie

# Set up a logger with custom formatting
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
custom_logger = logging.getLogger(__name__)


@selfie(logger=custom_logger.info)
class TestClassCustomLogger:
    def __init__(self):
        self.number = 0
        self.kv = {"key": 0}
        self.list = [1, 2, 3]

    def increment(self):
        self.number += 1

    def decrement(self):
        self.number -= 1

    def modify_kv(self):
        self.kv["key"] = random.randint(1, 100)

    def modify_list(self):
        self.list[0] = random.randint(10, 99)
        self.list.append(random.randint(10, 99))


@selfie
class TestClassDefaultLogger:
    def __init__(self):
        self.number = 0
        self.kv = {"key": 0}
        self.list = [1, 2, 3]

    def increment(self):
        self.number += 1

    def decrement(self):
        self.number -= 1

    def modify_kv(self):
        self.kv["key"] = random.randint(1, 100)

    def modify_list(self):
        self.list[0] = random.randint(10, 99)
        self.list.append(random.randint(10, 99))


if __name__ == "__main__":
    print("With custom logger")
    test_class_with_logger = TestClassCustomLogger()
    test_class_with_logger.increment()
    test_class_with_logger.decrement()
    test_class_with_logger.modify_kv()
    test_class_with_logger.modify_kv()
    test_class_with_logger.modify_list()

    print("\nWith print as logger")
    test_class_with_print = TestClassDefaultLogger()
    test_class_with_print.increment()
    test_class_with_print.decrement()
    test_class_with_print.modify_kv()
    test_class_with_print.modify_kv()
    test_class_with_print.modify_list()

    print("\nChanges history (flat)")
    print(test_class_with_logger.get_change_history())

    print("\nChanges history (attr)")
    print(test_class_with_logger.get_change_history(format="attr"))
