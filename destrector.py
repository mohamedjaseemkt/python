class employee:
    def __init__(self):
        print("employee created....")

    def __del__(self):
        print("destrected called.")

def create_object():
    print("making object..")
    obj = employee()
    print("function ended.")
    return obj

print("calling create_object() function...")
obj = create_object()
print("programme ended...")
