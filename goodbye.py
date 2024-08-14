import inflect
def main():
    goodbye=[]
    while True:
        try:
            user_input= input("Name:")
            goodbye.append(user_input)
        except EOFError:
            break
    print(f"goodbye goodbye, to {adieu} ")


main()