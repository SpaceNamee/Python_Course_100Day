alphabet = "abcdefghijklmnopqrstuvwxyz"


# def encoder(word: str, shift: int) -> str:
#     word = word.lower()
#     rez = ''
#     for i in word:
#         if i in alphabet:
#             j = alphabet.index(i)
#             j += shift
#             j %= len(alphabet)
#             # if j > len(alphabet):
#             #     j = j - len(alphabet)
#             # rez += alphabet[j]
#         else:
#             rez += i
#     return rez
#
#
# def decoder(word: str, shift: int) -> str:
#     word = word.lower()
#     rez = ''
#     for i in word:
#         if i in alphabet:
#             for j in range(len(alphabet)):
#                 if alphabet[j] == i:
#                     j -= shift
#                     rez += alphabet[j]
#                     break
#         else:
#             rez += i
#         return rez

def caesar(message: str, shift: int, work_mode):
    word = message.lower()
    rez = ''
    if work_mode == 0:
        shift *= (-1)
    for i in word:
        if i in alphabet:
            j = alphabet.index(i)
            j += shift
            j %= len(alphabet)
            # if j > len(alphabet):
            #     j = j - len(alphabet)
            rez += alphabet[j]
        else:
            rez += i
    return rez

while True:
    message = input("Enter a message: ")
    shifts = int(input("Enter a number of shifts: "))
    mode = int(input("Enter decoder(0) or encoder(1) mode: "))

    if mode == 0:
        rez = caesar(message, shifts, mode)
        print(f"Your decoded message: {rez}")
    elif mode == 1:
        rez = caesar(message, shifts, mode)
        print(f"Your encode message: {rez}")
    else:
        print("Invalid input.")
