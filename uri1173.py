

n = [0,0,0,0,0,0,0,0,0,0]
ni = int(input())

for i in range(len(n)):
    n[i] = ni
    ni = ni *  2
    print(f'N[{i}] = {n[i]}')


'''SAIDA
N[0] = 1 
N[1] = 2 
N[2] = 4 
N[3] = 8 
N[4] = 16
N[5] = 32
N[6] = 64
N[7] = 128
N[8] = 256
N[9] = 512
'''










