kata = input('kata : ')

reversedKata = "".join(reversed(kata))

if kata == reversedKata:
    print("kata palindrom")
else:
    print("bukan kata palindrom")
    


# input_str = input("Masukkan sebuah string: ")

# input_str = input_str.lower()

# if input_str == input_str[::-1]:
#     print("Palindrome")
# else:
#     print("Bukan Palindrome")
