import math

data = ['Arsel','Avivah','Daiva',['Wahyu','Wibi']]

def linearsearch(data,i):
    for t in range(len(data)):
        if type(data[t]) == list:
            hasil1 = linearsearch(data[t],i)
            if hasil1 == -1:
                return -1
            else:
                print(f'{i} Ditemukan pada indeks {t} Kolom {hasil1}')
                exit()
        elif data[t] == i:
            return t
    return -1

def jumpSearch (data, x , o) :
    interval = o**0.5
    prev = 0
    for H in range(len(data)):
        if type(data[H]) == list:
            hasil_g = jumpSearch (data[int(H)],x,len(data[int(H)]))
            if hasil_g == -1:
                data[int(H)]="berhasil"
            else:
                print(x ,"ditemukan pada indeks", int(H) , "kolom", hasil_g)
                exit()
    while data[int (min(interval, o) -1)] < x:
        prev = interval
        interval += o**0.5 
        if (prev >= o) :
            return -1
        
    while data[int (prev)]< x:
        prev += 1
        if prev == min(interval, o) :
            return -1
    if data[int(prev)]== x:
        return int(prev)
    return -1



while True:
    print("|=================|")
    print("| 1. linearsearch |")
    print("| 2. jumpSearch   |")
    print("|=================|")

    pilih = input("masukan no yang anda inginkan :")

    if pilih == "1" :
        print(data)
        i = input('Masukan nama yang ingin dicari: ')
        hasil2 = linearsearch(data,i)
        if hasil2 == -1:
            print(f'{i} ditemukan pada indeks {hasil2}')
        else:
            print(f'{i} ditemukan pada indeks {hasil2}')
        exit()
             
    elif pilih == "2" :
            print(data)
            o = len(data)
            # print(f'Arsel','Avivah','Daiva','Wahyu','Wibi')
            x = str(input("masukan nama :"))
            hasil2 = jumpSearch(data,x, o)
            if hasil2 == -1:
                print(x, 'tidak ada')
            else:
                print(x,'ada di indeks ke',hasil2)
            exit()






