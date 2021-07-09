def deter_expo(a):
    for i in range(20, 0, -1):
        '''if(pow(a, 1.0/float(i)) == )'''
        t = pow(a, 1.0/float(i))
        if(t == int(t)):
            return i

inf = 10000
print ("start")
for m in range(2, inf):
    for n in range(2, inf):
        t = n / float(3 * m)
        if(t == int(t)):
            continue
        expo = deter_expo(m * n)
        raw_expo = expo * n / (3 * m)
        if(expo != 1 and expo % 3 != 0 and raw_expo == int(raw_expo)):
            print ("m : %d, n : %d, m*n : %d, m*n : %d^%d 전체 지수 : %d" %( m, n, m * n, pow(m*n, 1.0/expo) ,expo, raw_expo))
