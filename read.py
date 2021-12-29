import binascii
import codecs
f = open('πάσο.png', 'rb')
def printk(k, m):
    s = ''
    count = 0
    for i in k:
        s = s + str(i) + m
        count+=1
        if count%16==0:
            s=s + '\n'

    if s[-1] != '\n':
            s = s + '\n'
    print(s)       
byte = f.read(1)
L=[]
l=[]
while byte:
    x = binascii.b2a_hex(byte) #μετατροπή bytes σε δεκαεξαδικούς χαρακτήρες του ascii
    a = str(x) 
    b = a.upper()           #μετατροπή των χαρακτήρων σε string, κεφαλαιοποίηση  των 'γραμμάτων' και ταξινόμηση τους σε λίστα
    L.append(b[2:4])
    c = str(byte)
    
    if len(c)> 4:
        g = c[4:6]
        if g.startswith('0') or g.startswith('1'):      #μετατροπή των byte σε string, τύπωσή τους ανάλογα με το μήκος της 'λέξης' που τα περιγράφει και ταξινόμηση τους σε λίστα
            g = '.'
        elif g == 'a0' or g == '20':
            g = ' '

        l.append(g)
    else:
        h = c[2:3]
        l.append(h)
    
    byte = f.read(1)

printk(L, ' ')
printk(l, '')
f.close()

