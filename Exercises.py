from datetime import datetime
import os
#1- 
class Exercise00:
    #2- # Static field
    STUDENT_NAME = "shery"
    #3-
    @staticmethod
    def deadline(format_string):
        # Create a datetime object for November 15th, 2023 at 09:00
        d = datetime(2023, 11, 15, 9, 0)
        # Return formatted string based on the argument
        return d.strftime(format_string)
    #4-properties 
    """A readable but not writable property"""
    def __init__(self, text):
            self._txt = text              # Store the full string in a private variable

    @property
    def txt(self):
        """Return first 17 characters of text plus '...'"""
        return self._txt[:17] + "..."
    #5- Format strings
    def format(self, mode):
        if mode == "order":
            # Reorder: 3rd → 1st, 2nd → 2nd, 1st → 3rd
            return "{2} - {1} - {0}"

        elif mode == "dict":
            # Dictionary-based formatting
            # {x:.1f} → format x with 1 digit after decimal
            # {y:.4f} → format y with 4 digits after decimal
            return "x, y = ({x:.1f}, {y:.4f})"
    # 6. Generator for listing files
    def listfiles(self, path=".", filetype=None):
        """
        Generator that yields file paths from the given directory and subdirectories.
        If filetype is given (e.g. '.py'), only files with that extension are listed.
        """
        for root, dirs, files in os.walk(path):
            for file in files:
                if filetype is None or file.endswith(filetype):
                    yield os.path.join(root, file)
    #7
    def collatz(x):
        # Check if input is a positive integer
        if not isinstance(x, int) or x <= 0:
            return ([], 0)
    
        seq = [x]
    
        # Generate the Collatz sequence until reaching 1
        while x != 1:
            if x % 2 == 0:
                x = x // 2
            else:
                x = 3 * x + 1
            seq.append(x)
    
    # The stopping time is the number of terms in the sequence
    # (i.e. index of 1), which equals the sequence length
        return (seq, len(seq))
# 8. Function object behavior
    def __init__(self, text=""):
            self._txt = text
    def __call__(self, **kwargs):
        # Sort keyword arguments alphabetically
        sorted_items = sorted(kwargs.items())
        # Format each pair as "key = value"
        lines = [f"{key} = {value}" for key, value in sorted_items]
        # Join them with newline characters
        return "\n".join(lines)
#9
        # 9. Base64 encoding when object is converted to string
    def __str__(self):
        if not self._txt:
            return ""
        
        # Base64 alphabet
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        
        # Convert text to binary string
        binary_str = ''.join(f"{ord(c):08b}" for c in self._txt)
        
        # Split into 6-bit chunks
        chunks = [binary_str[i:i+6] for i in range(0, len(binary_str), 6)]
        
        # Convert chunks to Base64 characters
        base64_chars = ""
        for chunk in chunks:
            if len(chunk) < 6:
                chunk = chunk.ljust(6, '0')  # pad with zeros
            index = int(chunk, 2)
            base64_chars += alphabet[index]
        
        # Pad with '=' to make length multiple of 4
        while len(base64_chars) % 4 != 0:
            base64_chars += "="
        
        return base64_chars


    




#2- Calling  Static field 
print(Exercise00.STUDENT_NAME)
#3-calling deadline function 
print(Exercise00.deadline("Hours %H:Miniute %M Day Month Year %d.%m.%Y"))  # Output: 09:00 15.11.2023
print(Exercise00.deadline("Day Month Year %d.%m.%Y Hours %H:Miniute %M"))  # Output: 15.11.2023 09:00
#4- Calling A readable but not writable property
ex = Exercise00("abcdefghijklmnopqrstuvwxyz")
print(ex.txt)
#5 Format strings
ex = Exercise00("test string")

# (a) Order-based formatting
print(ex.format("order").format("third", "second", "first"))
# Expected: first - second - third

# (b) Dictionary-based formatting
print(ex.format("dict").format(x=41.123, y=71.091))
# Expected: x, y = (41.1, 71.0910)
# 6 Generator
ex = Exercise00("Generator")
print("\nAll files in current folder:")
#All files for f in ex.listfiles(filetype="") 
for f in ex.listfiles(filetype=".py"):
    print(f)
#7 loops
# 7. Collatz
print(Exercise00.collatz(12))       # ([12,6,3,10,5,16,8,4,2,1], 10)
print(Exercise00.collatz(3.1415))   # ([], 0)
print(Exercise00.collatz(1))        # ([1], 1)
#8 
# 8. Function object behavior
ex = Exercise00("Function object behavior")
print(ex(c=None, a=1, d=4, b='2'))
#9 .
ex1 = Exercise00("Hello")
print(str(ex1))
ex2 = Exercise00("Python!")
print(str(ex2))







'''
1- compile  main1.cpp  file and   compile  sourcefile.cpp  file 
g++ Exercise.py  Exercise
2- run program 
./Exercise

'''


'''
A- 
| Step | Current `x` | Even/Odd | Next value   |
| ---- | ----------- | -------- | ------------ |
| 1    | 12          | even     | 12 / 2 = 6   |
| 2    | 6           | even     | 6 / 2 = 3    |
| 3    | 3           | odd      | 3×3 + 1 = 10 |
| 4    | 10          | even     | 10 / 2 = 5   |
| 5    | 5           | odd      | 3×5 + 1 = 16 |
| 6    | 16          | even     | 16 / 2 = 8   |
| 7    | 8           | even     | 8 / 2 = 4    |
| 8    | 4           | even     | 4 / 2 = 2    |
| 9    | 2           | even     | 2 / 2 = 1    |
[12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
B- 
Exercise00.collatz(3.1415)
if not isinstance(x, int) or x <= 0:    True 
    return ([], 0)
output
([], 0)
C-
Exercise00.collatz(1)
        seq = [x]  =  seq = [1] 
        while x != 1: // false
 output
([1], 1)


'''
