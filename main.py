import sys
from notes import Notes
from harmonic_field import HarmonicField

HELP_TEXT = """ usage: python main.py tonic scale_1 scale_2 ... scale_n
                where:
                    tonic - the tonic chord of the scales
                    
                    scales currently supported:
                        mj - major scale
                        min - minor natural scale"""

def main():
    if len(sys.argv) < 2:
        print(HELP_TEXT)
        exit()
    
    tonic = Notes[sys.argv[1]]
    field = HarmonicField(tonic)

    for command in sys.argv[2:]:
        command = command.casefold()

        if command == 'help':
            print(HELP_TEXT)
            exit()
        elif command == 'mj':
            field.major_scale()
        elif command == 'min':
            field.minor_natural_scale()

if __name__ == '__main__':
    main()