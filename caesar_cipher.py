# def encript_letter(a,b):
    
#     (ord (a.upper())+shift)
#     return a

# def main():
#     shift = 15
#     letter = "b"
#     print(encript_letter(letter,shift))
#     letter = "w"
#     print(encript_letter(letter,shift))
#     letter = "h"
#     print(encript_letter(letter,shift))
#     print(encript_letter("A",3))
#     print(encript_letter("G",5))
#     print(encript_letter("D",10))
    
    
# if __name__ == '__main__':
#     main()


string = "this is a \"string literal"

def encript_letter(a,b):

    flag = 0
    if ord(a)>= 97 and ord(a)<= 122:
        flag = 1
    return_this = ord(a.upper())+b
    if return_this > 90:
        return_this = return_this -91 + 65
    if return_this < 65:
        return_this = return_this + 26
    return chr(return_this+32*flag)

def is_alphabetic(a):
    if (ord(a)>= 97 and ord(a)<=127) or (ord(a)>=65 and ord(a)<= 90):
        return False
    
def decrypt_letter(a,b):
    flag = 0
    if ord(a) >=97 and ord(a) <=122:
        flag = 1
        return_this = ord(a.upper())- b
    if return_this > 90:
        return_this = return_this -91 + 65
    if return_this < 65:
        return_this = return_this + 26
    return chr(return_this+32*flag)

def main():
    shift = 15
    letter = "b"
    print(encript_letter(letter,shift))
    letter = "w"
    print(encript_letter(letter,shift))
    letter = "h"
    print(encript_letter(letter,shift))
    print(encript_letter("A",3))
    print(encript_letter("G",5))
    print(encript_letter("D",10))
    
    
if __name__ == '__main__':
    main()