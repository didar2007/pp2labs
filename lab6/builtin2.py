def count_case(text):
    upper = 0
    lower = 0
    
    for i in text:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
            
    print("Upper: ")
    print("Lower: ")
    
count_case("Python Didar Kalabayev")