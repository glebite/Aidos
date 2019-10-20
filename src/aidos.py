# aidos.py
import os
import logging

LOG_FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"

class Aidos():
    def __init__(self, run_name):
        self.run_name = run_name
        self.setup_logger()

    def setup_logger(self):
        logging.basicConfig(format=LOG_FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
        self.log = logging.getLogger(self.run_name)

    def declare_test(self, test_title):
        self.log.info("TEST_DESCRIPTION: {}".format(test_title))

    def test_step(self, step_description):
        self.log.info("STEP: {}".format(step_description))

    def declare_result(self, test_result):
        self.log.info("RESULTS: {}".format(test_result))

                      
def main():
    """
    main
    """
    return

if __name__ == "__main__":
    main()
