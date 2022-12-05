total1=0
total=0
with open("4.input") as f:
    line1=[]
    a=[]

    for line in f:
        line = line.rstrip('\n')
        line1= line.split(",")

        x=(line1[0])
        y=(line1[1])
        a=x.split("-")
        b=y.split("-")
        i=int(a[0])
        j=int(a[1])+1
        k=int(b[0])
        l=int(b[1])+1

        g1=[]
        g2=[]
        a1=[]
        for m in range (i,j):
           g1.append(m)
        #print(g1)
        for n in range (k,l):
            g2.append(n)
        #print(g2)
        a1 = list(set(g1) & set(g2))
        #print('a1', a1)
        leng1=len(g1)
        leng2=len(g2)
        lena1=len(a1)
        #print('g1 len', leng1, 'len g2', leng2, 'len comm', lena1)
        if((leng1>leng2) & (leng2==lena1)) or ((leng2>leng1) & (leng1==lena1)) or ((leng1==leng2) & (leng1==lena1)):

            total += 1
        if(lena1>0):
            total1 += 1
print('fully overlap count', total)
###part two #########
print('total Over lap count',total1)
