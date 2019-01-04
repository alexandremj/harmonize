import sys
from notes import Notes

def main():
    print('Welcome to Harmonize!')
    
    if len(sys.argv) < 2:
        print('help text - no arguments')
        exit()

    if sys.argv[1].casefold() == 'help':
        print("help text")
        exit()
    
    tonic = Notes[sys.argv[1]]
    print(tonic)

if __name__ == "__main__":
    main()