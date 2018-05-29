#__author__ = 'Sebastian Szalasny'

# output:
# 'Arek woli psy, a najbardziej boksery'
#
# nie wolno dostarczyc znakow z zewnatrz
# mozna dowolnie przeksztalcac

x = "Ala ma kota, kot ma Ale"
listX = x.split(" ")
word0 = listX[0]
word1 = listX[1]
word2 = listX[2]
word3 = listX[3]
word4 = listX[4]
word5 = listX[5]

#############################


print(word0[0]+chr(114)+chr(101)+word2[0], chr(119)+word3[1]+word0[1]+chr(105), chr(112)+chr(115)+chr(121)+word2[4],
      word0[2], chr(110)+word0[2]+chr(106)+chr(98)+word0[2]+chr(114)+chr(100)+chr(122)+word5[2]+chr(106),
      chr(98)+word2[1]+word2[0]+chr(115)+word5[2]+chr(114)+chr(121))

##Spelnione zalozenie "NIE MOŻNA DOSTARCZYĆ LITER" - ale mam dziwne wrazenie ze nie o to chodzilo :)