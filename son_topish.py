import random


def top_user(x=15):
    print(f"men {x}gacha son o'yladim siz taxmin qilib ko'ring:")
    taxmin = random.randint(1, x)
    taxminlar = 0
    while True:
        taxminlar += 1
        taxminl = int(input("taxminingizni kiriting:"))
        if taxmin > taxminl:
            print("topolmadingiz.men o'ylagan son kattaroq!.yana urunib ko'ring")
        elif taxmin < taxminl:
            print("topolmadingiz.men o'ylagan son kichikroq!")
        else:
            break
    print(f"To'g'ri!. Siz {taxminlar} taxmin bilan topdingiz!")
    return taxminlar


def top_pc(x=15):
    print(f"siz {x} gacha son o'ylang topishga harakat qilaman")

    taxminlar = 0
    input("o'ylagan bo'lsangiz biror tugmani bosing")
    quyi = 0
    yuqori = x
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(
            f"siz {taxmin} sonini o'yladingiz, agar to'g'ri bo'lsa(t), kattaroq bo'lsa (+) kichikroq bo'lsa (-)".lower())
        if javob == "+":
            quyi = taxmin + 1
        elif javob == "-":
            yuqori = taxmin - 1
        else:
            break
    print(f"men {taxminlar} taxmin bilan topdim")
    return taxminlar


def play(x=15):
    yana = True
    while yana:
        taxminlar_user = top_user(x)
        taxminlar_pc = top_pc(x)

        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va  yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        elif taxminlar_user == taxminlar_pc:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))


play()
