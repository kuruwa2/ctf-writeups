from Crypto.Util.number import *
import itertools

def BFI(ab, cd):
    a, b = ab
    c, d = cd
    if abs(a*c-b*d) < a*d+b*c:
        x = (abs(a*c-b*d), a*d+b*c)
    else:
        x = (a*d+b*c, abs(a*c-b*d))
    if abs(a*d-b*c) < a*c+b*d:
        y = (abs(a*d-b*c), a*c+b*d)
    else:
        y = (a*c+b*d, abs(a*d-b*c))
    return [x, y]

def ADD(A, B):
    res = set()
    for i, j in itertools.product(A, B):
        x, y = BFI(i, j)
        res.add(x)
        res.add(y)
    return list(res)

def MUL(A, m):
    b = bin(m)[3:][::-1]
    res = A
    for i in b:
        res = ADD(res, res)
        if i == '1':
            res = ADD(res, A)
    return res

#(p - 2167)**2 + (q - 326)**2 = 9806283809265063566758033718824510148074879605625613522260326142727071525485782252114823738593491179948424510243140176650710740796725421816662574964276347592615939391555797849486315592564554137934538251062439262517676686394984856092767504693553844269313567643006209487604087552159988706608989852232600173305577554380894550328685411262027693100930016206665063909994060539842194048629173836080139658119167462275726935530236306206291208468554102639740084971199502048875561304040781889
c = 4162530708599733880152079445465251228233279193332479686305881911338677676462717745422675499193934855607678519559969518766182082072739790163376599982394630098413003117921382004385054651203710170268877074243207458165942762410479903173324353258065154511643544253863693746603809470766247869470549574622108284898305056998895447377459757443253158327187005891952567743297659176064479721212951686714200266747613462203038160283534793851102484042496527964609356275391559879857476645830630615
e = 65537
assert (29 * 73 * 2101442973337 * 48339667240549 * 2401761848466304940603366829278102880689)**7 == 9806283809265063566758033718824510148074879605625613522260326142727071525485782252114823738593491179948424510243140176650710740796725421816662574964276347592615939391555797849486315592564554137934538251062439262517676686394984856092767504693553844269313567643006209487604087552159988706608989852232600173305577554380894550328685411262027693100930016206665063909994060539842194048629173836080139658119167462275726935530236306206291208468554102639740084971199502048875561304040781889
ab1 = [(2, 5), (3, 8), (559124, 1337469), (1225282, 6843855), (14179542195764409592, 46911644946482547815)]

ab7 = []
for i in ab1:
    ab7.append(MUL([i], 7))

pq = ab7[0]
for j in ab7[1:]:
    pq = ADD(pq, j)
for p, q in pq:
    if p % 2 == 0 and isPrime(p+2167) and isPrime(q+326):
        print(p+2167, q+326)
    elif isPrime(p+326) and isPrime(q+2167):
        print(q+2136, p+326)

p = 2069300450612496435205391896401107009246050974259373265950125261564356857107601939343348838849659112510303072841948141971071753437773678030474040372840544359451314111776603431854580925395608161633036805971174618586256614667084951120026883859
q = 2350378576816931159716220696327428530030445953500426917016301739518586044818934876556500063751062992664346891106558660161917135735168998001444707385674514342933330108128573720721076102795812019947101380097684476445486243801522044091145079231
print(long_to_bytes(pow(c, inverse(e, (p-1)*(q-1)), p*q)))

#CCTF{Congrats_Y0u_5OLv3d_x**2+y**2=z**7}
