#burada kullanıcılardan isim alıyor ve boş veya aynı olmamasını sağlıyor
import random
def isim_secimi():
    global oyuncu1
    global oyuncu2
    oyuncu1=input(10*'-'+'İlk Kahraman'+10*'-'+'\nLütfen Kahramanınızın Adını yazın: ')
    while oyuncu1.strip()== '' or len(oyuncu1)>10:
        oyuncu1=input('Lütfen geçerli bir isim gir: ')
    oyuncu2=input(10*'-'+'İkinci Kahraman'+10*'-'+'\nLütfen Kahramanınızın Adını yazın: ')
    while oyuncu2.strip()== '' or len(oyuncu2)>10:
        oyuncu2=input('Lütfen geçerli bir isim gir: ')
    while oyuncu2.strip() == oyuncu1.strip():
        print(f'{oyuncu1} alındı, lütfen başka bir isim seç!')
        oyuncu2=input(10*'-'+'İkinci Kahraman'+10*'-'+'\nLütfen Kahramanınızın Adını yazın: ')
def oyun(oyuncu1,oyuncu2):
    # oyun yazı turanın sonucuna göre if ve else ile iki farklı doğrultuda gidiyor
    # yazı tura galibinin can barı üstte olsun diye oyunu if else ile ikiye ayırdım
    oyuncu1data = {
        'name':oyuncu1,
        'HP': 100
    }
    oyuncu2data = {
        'name':oyuncu2,
        'HP': 100
    }
    coinflip = random.randint(1,2)
    #saldılar sürekli kullanılacak diye bir fonksiyon olarak tanımladım
    def saldiri(oyuncu_adi,oyuncudatası,hasar):
        hasar=int(hasar)
        if hasar< random.randint(1,100):
            print('saldırı başarılı')
            oyuncudatası['HP']=int(oyuncudatası['HP'])-hasar
        else:
            print(f'ooppsssy {oyuncu_adi} kaçırdı.')
    #oyun sonunda devam etmek istenirse diye
    def oyunSonuMesaji(cevap):
        while cevap!="e" and cevap!="E" and cevap!="h" and cevap!="H":
            cevap=input("lütfen geçerli bir değer gir(e/h): ")
        if cevap=='e' or cevap=="E":
            oyun(oyuncu1,oyuncu2)
        elif cevap=='h' or cevap=="H":
            print('Teşekkürler, yine bekleriz canım')
            exit()   
    def scoreboard(oyuncu1data,oyuncu2data):
        uzunluk=0
        if len(oyuncu1data['name'])>len(oyuncu2data['name']):
            uzunluk=len(oyuncu1data['name'])
        else:
            uzunluk=len(oyuncu2data['name'])
        print(f"{oyuncu1data['name']}{(uzunluk-len(oyuncu1data['name']))*' '} {oyuncu1data['HP']} {int(oyuncu1data['HP']/2)*'|'}")
        print(f"{oyuncu2data['name']}{(uzunluk-len(oyuncu2data['name']))*' '} {oyuncu2data['HP']} {int(oyuncu2data['HP']/2)*'|'}")
        #boyutlandırmanın eşit olması için yukarıdaki boşluk ekleme yapıldı 
    if coinflip==1:
        print(f'yazı tura sonucu {oyuncu1} başlar.')
        scoreboard(oyuncu1data,oyuncu2data)
        #oyuncuların canı tükenmediği sürece saldırılar devam edecek
        while oyuncu1data['HP']>0 and oyuncu2data['HP']>0:
            hasar=input('1 ile 50 aralığında bir değer seçiniz: ')
            while hasar.isdigit()==False or int(hasar)<1 or int(hasar)>50:
                print('giridiğiniz değerler hatalı')
                hasar=input('1 ile 50 aralığında bir değer seçiniz: ')
            saldiri(oyuncu1,oyuncu2data,hasar)
            scoreboard(oyuncu1data,oyuncu2data)
            # saldırı sonucu oyuncunun hpsi tükenirse oyun bitecek sıra rakibe geçmeyecek
            if oyuncu2data['HP']<=0:
                break
            hasar=input('1 ile 50 aralığında bir değer seçiniz: ')
            while hasar.isdigit()==False or int(hasar)<1 or int(hasar)>50:
                print('giridiğiniz değerler hatalı')
                hasar=input('1 ile 50 aralığında bir değer seçiniz: ')
            saldiri(oyuncu2,oyuncu1data,hasar)
            scoreboard(oyuncu1data,oyuncu2data)
        #canlarında biri bitince döngü bitecek ve kimin canı bitmişse ona göre bir kazanan mesajı yayınlanacak
        if oyuncu1data['HP']<=0:
            print('\n',30*'*','\n',int((20-len(oyuncu2))/2)*'*',f'kazanan {oyuncu2}',int((20-len(oyuncu2))/2)*'*','\n',30*'*')
            cevap=input('devam etmek ister misiniz (e/h):')
            oyunSonuMesaji(cevap)
        else:
            print('\n',30*'*','\n',int((20-len(oyuncu1))/2)*'*',f'kazanan {oyuncu1}',int((20-len(oyuncu1))/2)*'*','\n',30*'*')
            cevap=input('devam etmek ister misiniz (e/h):')
            oyunSonuMesaji(cevap)
    #aynı şeyleri yazı turanın diğer tarafı için de yaptım
    else:
        print(f'yazı tura sonucu {oyuncu2} başlar.')
        scoreboard(oyuncu2data,oyuncu1data)
        while oyuncu1data['HP']>0 and oyuncu2data['HP']>0:
            hasar=input('1 ile 50 aralığında bir değer seçiniz: ')
            while hasar.isdigit()==False or int(hasar)<1 or int(hasar)>50:
                print('giridiğiniz değerler hatalı')
                hasar=input('1 ile 50 aralığında bir değer seçiniz: ')
            saldiri(oyuncu2,oyuncu1data,hasar)
            scoreboard(oyuncu2data,oyuncu1data)
            if oyuncu1data['HP']<=0:
                break
            hasar=input('1 ile 50 aralığında bir değer seçiniz: ')
            while hasar.isdigit()==False or int(hasar)<1 or int(hasar)>50:
                print('giridiğiniz değerler hatalı')
                hasar=input('1 ile 50 aralığında bir değer seçiniz: ')
            saldiri(oyuncu1,oyuncu2data,hasar)
            scoreboard(oyuncu2data,oyuncu1data)
        if oyuncu1data['HP']<=0:
            print('\n',30*'*','\n',int((20-len(oyuncu2))/2)*'*',f'kazanan {oyuncu2}',int((20-len(oyuncu2))/2)*'*','\n',30*'*')
            cevap=input('devam etmek ister misiniz (e/h):')
            oyunSonuMesaji(cevap)
        else:
            print('\n',30*'*','\n',int((20-len(oyuncu1))/2)*'*',f'kazanan {oyuncu1}',int((20-len(oyuncu1))/2)*'*','\n',30*'*')
            cevap=input('devam etmek ister misiniz (e/h):')
            oyunSonuMesaji(cevap)
isim_secimi()       
oyun(oyuncu1,oyuncu2)
