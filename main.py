import sys
from notes import Notes
from harmonic_field import HarmonicField

def main():
    if len(sys.argv) < 2:
        print('help text - no arguments')
        exit()

    if sys.argv[1].casefold() == 'help':
        print("help text")
        exit()
    
    tonic = Notes[sys.argv[1]]
    field = HarmonicField(tonic)
    print(field.major_natural_scale())

if __name__ == "__main__":
    main()