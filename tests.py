import unittest
from frame import Frame, CharLengthError, NotEvenOrOddNumberOfCharacters


class TestFrame(unittest.TestCase):

    def test_init(self):
        self.assertRaises(CharLengthError, Frame, ['Test', 'Frame'], 'XX')
        self.assertRaises(CharLengthError, Frame, ['Test', 'Frame'], 'XXXXX')
        self.assertRaises(NotEvenOrOddNumberOfCharacters, Frame, ['Test', 'Frame'], 'X', centre=True)
        self.assertRaises(NotEvenOrOddNumberOfCharacters, Frame, ['TestTestTest', 'F'], 'X', centre=True)

    def test_basic(self):
        self.assertEqual(Frame(['Small', 'frame'], '~').build_frame(), "~~~~~~~~~\n~ Small ~\n~ frame ~\n~~~~~~~~~")
        self.assertEqual(Frame(['Create', 'this', 'kata'], '+').build_frame(),
                         '++++++++++\n+ Create +\n+ this   +\n+ kata   '
                         '+\n++++++++++')
        self.assertEqual(Frame(['This is a very long single frame'], '-').build_frame(),
                         '------------------------------------\n- '
                         'This is a very long single frame '
                         '-\n------------------------------------')
        self.assertEqual(Frame(
            [' Create a frame!', '          __     __', '         /  \\~~~/  \\', '   ,----(     ..    )',
             '  /      \\__     __/', ' /|         (\\  |(', '^  \\  /___\\  /\\ |', '   |__|   |__|-..'],
            '*').build_frame(),
                         "*************************\n*  Create a frame!      *\n*           __     __   *\n*          "
                         "/  \\~~~/  \\  *\n*    ,----(     ..    ) *\n*   /      \\__     __/  *\n*  /|         (\\  "
                         "|(    *\n* ^  \\  /___\\  /\\ |     *\n*    |__|   |__|-..     *\n*************************")

    def test_multiple_spaces(self):
        self.assertEqual(Frame(['Test', 'Small', 'Words'], '.', 2).build_frame(),
                         '...........\n.  Test   .\n.  Small  .\n.  Words  '
                         '.\n...........')
        self.assertEqual(Frame(['Test', 'Small', 'Words'], '.', 0).build_frame(),
                         '.......\n.Test .\n.Small.\n.Words.\n.......')
        self.assertEqual(Frame(['Test', 'Small', 'Words'], '.', -2).build_frame(),
                         '...........\n.  Test   .\n.  Small  .\n.  Words  '
                         '.\n...........')
        self.assertEqual(Frame(['Test', 'Small', 'Words'], '.', -1.5).build_frame(),
                         '...........\n.  Test   .\n.  Small  .\n.  Words  '
                         '.\n...........')

    def test_centre(self):
        self.assertEqual(Frame(['Test', 'Case'], '#', centre=True).build_frame(),
                         '########\n# Test #\n# Case #\n########')
        self.assertEqual(Frame(['Test1', 'Case1'], '#', centre=True).build_frame(),
                         '#########\n# Test1 #\n# Case1 #\n#########')
        self.assertEqual(Frame(['TestLongCase', 'Checking'], '#', centre=True).build_frame(),
                         '################\n# TestLongCase #\n#   Checking   #\n################')


if __name__ == '__main__':
    unittest.main()
