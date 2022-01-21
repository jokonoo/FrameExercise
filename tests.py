import unittest
from frame import frame


class TestFrame(unittest.TestCase):
    def test_basic(self):
        self.assertEquals(frame(['Small', 'frame'], '~'), "~~~~~~~~~\n~ Small ~\n~ frame ~\n~~~~~~~~~")


if __name__ == '__main__':
    unittest.main()
