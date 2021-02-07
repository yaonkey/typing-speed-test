from modules.game import *
import sys, getopt



def main():
    pass


if __name__ == '__main__':
    if len(sys.argv[1:])>1:
        report = False
        sentencefile = 'src/sentences.txt'
        try:
            opts, args = getopt.getopt(sys.argv[1:],"hs:r",["sentences=", "report"])
        except getopt.GetoptError:
            print ('typingspeedtest -s <sentencefile> -r')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print ('typingspeedtest -s <sentencefile> -r')
                sys.exit()
            elif opt in ("-s", "--sentences"):
                sentencefile = arg
            elif opt in ("-r", "--report"):
                report = True
        game = Game(sentencefile, report)
        game.run()
    else:
        Game().run()
