
initial = int(input())
mux = initial
number = int(input())

while (number != -1):
   
    number = int(input())

    if initial>number:
        mux = initial
        initial = initial

    elif initial<number:
        mux = number
        initial = number
print(mux)


