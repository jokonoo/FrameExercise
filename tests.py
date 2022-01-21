import unittest
from frame import frame


class TestFrame(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(frame(['Small', 'frame'], '~'), "~~~~~~~~~\n~ Small ~\n~ frame ~\n~~~~~~~~~")
        self.assertEqual(frame(['Create', 'this', 'kata'], '+'), '++++++++++\n+ Create +\n+ this   +\n+ kata   '
                                                                 '+\n++++++++++')
        self.assertEqual(frame(['This is a very long single frame'], '-'), '------------------------------------\n- '
                                                                           'This is a very long single frame '
                                                                           '-\n------------------------------------')
        self.assertEqual(frame(
            [' Create a frame!', '          __     __', '         /  \\~~~/  \\', '   ,----(     ..    )',
             '  /      \\__     __/', ' /|         (\\  |(', '^  \\  /___\\  /\\ |', '   |__|   |__|-..'], '*'),
            "*************************\n*  Create a frame!      *\n*           __     __   *\n*          "
            "/  \\~~~/  \\  *\n*    ,----(     ..    ) *\n*   /      \\__     __/  *\n*  /|         (\\  "
            "|(    *\n* ^  \\  /___\\  /\\ |     *\n*    |__|   |__|-..     *\n*************************")

    def test_multiple_spaces(self):
        self.assertEqual(frame(['Test', 'Small', 'Words'], '.', 2), '...........\n.  Test   .\n.  Small  .\n.  Words  '
                                                                    '.\n...........')
        self.assertEqual(frame(['Test', 'Small', 'Words'], '.', 0), '.......\n.Test .\n.Small.\n.Words.\n.......')
        self.assertEqual(frame(['Test', 'Small', 'Words'], '.', -2), '...........\n.  Test   .\n.  Small  .\n.  Words  '
                                                                     '.\n...........')
        self.assertEqual(frame(['Test', 'Small', 'Words'], '.', -1.5),
                         '...........\n.  Test   .\n.  Small  .\n.  Words  '
                         '.\n...........')

    def test_long_characters(self):
        self.assertEqual(frame(['Test', 'Small', 'Words'], '??'),
                         '??????????????????\n?? Test         ??\n?? Small        ??\n?? Words        '
                         '??\n??????????????????')
        self.assertEqual(frame(['Test', 'Small', 'Words'], '???'), '???????????????????????????\n??? Test             '
                                                                   '   ???\n??? Small               ???\n??? Words   '
                                                                   '            ???\n???????????????????????????')


if __name__ == '__main__':
    unittest.main()
