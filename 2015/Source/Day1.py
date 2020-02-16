# Imports
import os # Need OS for checking if file exists

# Global Variables
# InputFile = None

if __name__ == '__main__':
    # global InputFile
    Path2File = '.\\..\\Inputs\\Day1_Input.txt'
    EnablePartTwo = 0

    FloorNumber = 0
    CharacterPosition = 0
    if os.path.exists(Path2File):
        InputFile = open(Path2File, mode='r', encoding='utf-8', errors='strict')
        a = InputFile.read()
        for i in a:
            if EnablePartTwo == 1:
                CharacterPosition = CharacterPosition + 1
            if i == '(':
                FloorNumber = FloorNumber+1
            elif i == ')':
                FloorNumber = FloorNumber-1;
            else:
                print("Error Detected")
                exit(1)
            if EnablePartTwo == 1:
                if FloorNumber < 0:
                    print(CharacterPosition)
                    exit(0)
        print(FloorNumber)
    else:
        print('Could not find input file')
