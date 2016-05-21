RA = []
# crie um arquivo listaRA.txt contendo o RA dos alunos
f = open("listaRA.txt")
for l in f:
    RA.append(l.rstrip())
f.close()

# preencha essa lista com o nome das funcoes
EXS = ['EX01', 'EX02', 'EX03']

fw = open("Corretor.py","w")
print >>fw, "from Gabarito import *"
for ra in RA:
    print >>fw, '''
import Respostas.ra%s as ra%s

print %s,
    ''' %(ra,ra,ra)

    for ex in EXS:
        print >>fw, '''
try:
    print int(G%s()==ra%s.%s()),
except:
    print 0,
        ''' % (ex,ra,ex)
    print >>fw, 'print'
fw.close()

