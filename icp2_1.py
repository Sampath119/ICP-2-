#Author : SampathKumar medam
def full_name():
    try:
        inp_a = str(input("Enter your first_name here:"))
        inp_b = str(input("Enter your last_name here:"))
        if validate_inp(inp_a) and validate_inp(inp_b):
            full_name = inp_a + " " + inp_b
            print(full_name)
            return full_name
        else:
            print("please enter a valid string")
    except Exception as error:
        print("Error occured {}".format(error))

def validate_inp(input_value):

    if input_value != '' and input_value is not None and input_value.isspace() != True and input_value.isnumeric() != True:
        return True
    else:
        return False        

def string_alternative(full_name):
    try:
        inp_1 = full_name
        print(inp_1[::2])
    except Exception as error:
        print("Error occured {}".format(error))

if __name__ == "__main__":
    f = full_name()
    string_alternative(f)       