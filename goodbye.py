import inflect
def main():
    goodbye=[]
    p = inflect.engine()
    while True:
        try:
            user_input= input("Name:")
            goodbye.append(user_input)
        except EOFError:
            print()
            break
    formatted_list = p.join(goodbye)
    print("Goodbye, goodbye, to " +formatted_list)
