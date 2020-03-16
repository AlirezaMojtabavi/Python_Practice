def tedad_maghsoom_elayh(adad):
    count = 0
    for i in range(1,adad+1):
        if adad%i == 0:
            count= count+1
    return count

init = int(input())
tme_init = tedad_maghsoom_elayh(init)
tme_mux = tme_init
num_mux = init

i = 1
while i != 20 :
    number = int(input())
    tme_num = tedad_maghsoom_elayh(number)
    if tme_num > tme_mux:
        tme_mux = tme_num
        num_mux = number
    elif tme_num == tme_mux:
        if number > num_mux :
            tme_mux = tme_num
            num_mux = number
        else:
            tme_mux = tme_mux
            num_mux = num_mux
    i = i + 1
print(num_mux,'',tme_mux)