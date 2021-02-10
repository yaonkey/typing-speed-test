import getopt
import sys

from modules.game import *

if __name__ == '__main__':
    if len(sys.argv[1:]) >= 1:
        report: bool = False
        debug: bool = False
        sentencefile: str = 'src/sentences.txt'
        help_text: str = 'typingspeedtest -s <sentencefile> -r -d'

        try:
            opts, args = getopt.getopt(sys.argv[1:], "hs:rd", ["sentences=", "report", "debug"])
            for opt, arg in opts:
                if opt == '-h':
                    print(help_text)
                    sys.exit()
                elif opt in ("-s", "--sentences"):
                    sentencefile = arg
                    print(f'{sentencefile=}')
                elif opt in ("-r", "--report"):
                    report = True
                    print(f'{report=}')
                elif opt in ("-d", "--debug"):
                    debug = True
                    print(f'{debug=}')
            game = Game(sentencefile, report, debug)
            game.run()
        except getopt.GetoptError:
            print(help_text)
            sys.exit(2)
    else:
        Game().run()
