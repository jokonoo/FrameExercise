import unittest
from frame import Frame


class TestFrame(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(Frame(['Small', 'frame'], '~').build_frame(), "~~~~~~~~~\n~ Small ~\n~ frame ~\n~~~~~~~~~")
        self.assertEqual(Frame(['Create', 'this', 'kata'], '+').build_frame(), '++++++++++\n+ Create +\n+ this   +\n+ kata   '
                                                                 '+\n++++++++++')
        self.assertEqual(Frame(['This is a very long single frame'], '-').build_frame(), '------------------------------------\n- '
                                                                           'This is a very long single frame '
                                                                           '-\n------------------------------------')
        self.assertEqual(Frame(
            [' Create a frame!', '          __     __', '         /  \\~~~/  \\', '   ,----(     ..    )',
             '  /      \\__     __/', ' /|         (\\  |(', '^  \\  /___\\  /\\ |', '   |__|   |__|-..'], '*').build_frame(),
            "*************************\n*  Create a frame!      *\n*           __     __   *\n*          "
            "/  \\~~~/  \\  *\n*    ,----(     ..    ) *\n*   /      \\__     __/  *\n*  /|         (\\  "
            "|(    *\n* ^  \\  /___\\  /\\ |     *\n*    |__|   |__|-..     *\n*************************")

    def test_multiple_spaces(self):
        self.assertEqual(Frame(['Test', 'Small', 'Words'], '.', 2).build_frame(), '...........\n.  Test   .\n.  Small  .\n.  Words  '
                                                                    '.\n...........')
        self.assertEqual(Frame(['Test', 'Small', 'Words'], '.', 0).build_frame(), '.......\n.Test .\n.Small.\n.Words.\n.......')
        self.assertEqual(Frame(['Test', 'Small', 'Words'], '.', -2).build_frame(), '...........\n.  Test   .\n.  Small  .\n.  Words  '
                                                                     '.\n...........')
        self.assertEqual(Frame(['Test', 'Small', 'Words'], '.', -1.5).build_frame(),
                         '...........\n.  Test   .\n.  Small  .\n.  Words  '
                         '.\n...........')

    def test_centre(self):
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
