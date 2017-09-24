import os
__all__=[]
for filename in os.listdir(os.path.dirname(__file__)):
    if  filename.startswith("A") and filename.endswith(".txt"):
        __all__.append(filename)

print __all__