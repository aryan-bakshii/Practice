template = 'PHOSBSKBBBFSPPPCCCHN'

conversions = """KO -> H
OK -> P
BO -> C
SH -> V
PC -> F
NK -> N
PH -> K
VH -> S
NN -> S
VC -> P
OF -> O
HH -> S
VP -> K
KP -> O
NP -> F
SS -> V
HP -> S
PS -> F
BV -> P
KS -> H
SO -> H
NF -> N
CO -> V
HK -> F
OO -> N
KN -> F
SP -> V
OP -> S
OV -> V
HO -> V
PK -> N
FF -> N
CV -> S
PP -> B
CF -> P
HF -> B
BN -> C
FH -> S
ON -> K
SN -> N
CP -> N
OB -> O
HC -> F
KH -> P
OS -> S
NS -> C
BK -> H
PB -> P
SV -> F
FV -> C
BC -> K
HS -> N
PF -> V
NC -> N
CH -> H
VF -> H
KK -> B
OH -> K
HB -> C
SC -> B
VK -> C
FP -> C
SK -> N
VO -> K
FB -> S
KB -> N
BS -> S
VS -> C
CN -> K
KF -> F
NB -> O
BB -> C
CS -> C
FC -> K
NO -> B
SB -> C
CB -> N
BP -> S
NV -> H
NH -> N
PV -> K
PO -> C
VB -> O
FK -> P
HV -> O
KC -> S
VV -> O
VN -> H
BH -> K
FS -> O
KV -> K
HN -> P
OC -> B
SF -> V
CC -> F
CK -> P
FO -> C
PN -> K
BF -> C
FN -> O""".split("\n")
print(len(conversions))
maps = {}
template = list(template)

for j in conversions:
    maps[j.split(" -> ")[0]] = j.split(" -> ")[1]

for i in range(0, 9):
    j = 0
    while j <= len(template)-2:
        print(f"j: {j}")
        if template[j]+template[j+1] in maps.keys():
            template.insert(j+1, maps[template[j]+template[j+1]])
            j += 2
        else:
            j += 1

print(template)