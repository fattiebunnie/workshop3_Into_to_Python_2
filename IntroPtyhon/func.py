# function takes an input and provides u with an output

# print( x )




def calc_avg ( ls ):
    lssum = 0
    for i in ls:
        lssum += i

    avg = lssum / len(ls)
    
    return avg


age = [19, 12, 20, 98]


appleprice = [9000, 8000, 80000, 2000]

avgage = calc_avg(appleprice)
        


print(avgage)
    
