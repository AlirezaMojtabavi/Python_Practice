initial = int(input())
age = int(input())
initial_age = age
mux = initial
mux_2 = initial_age

if initial_age > initial:
    mux = initial_age
    mux_2 = initial

while age !=-1 :
    age = int(input())

    if age > mux :
        mux_2 = mux
        mux = age
    elif mux > age and age > mux_2:
        mux_2 = age
        mux = mux

print(mux,'' ,mux_2)
    

