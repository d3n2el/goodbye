import inflect
def main():
    goodbye=[]
    while True:
        try:
            user_input= input("Name:")
            s= goodbye.append(user_input)
        except EOFError:
            break
    print("goodbye, goodbye, to " + ", ".join(goodbye))

main()
