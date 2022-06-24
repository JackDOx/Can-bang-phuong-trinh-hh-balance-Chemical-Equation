#def balance():
#cân bằng



import re
from smtplib import OLDSTYLE_AUTH
# tách chất / Get Chemical substances
def getChem(chem):
    firstEChem = []
    x = re.findall("[A-Z][a-z]?[1-9]?[1-9]?", chem)
    x.sort()
    for f in range(len(x)):
        s = re.findall("[A-Z][a-z]?", x[f])
        s = str(s[0])
      
        firstEChem.append(s)
        
    return firstEChem

# funtion() tách hệ số/ Get chemical value//
def getValue(chem):
    firstEValue = []
    x = re.findall("[A-Z][a-z]?[1-9]?[1-9]?", chem)
    x.sort()
    for f in range(len(x)):
        h = re.findall("[0-9][0-9]?", x[f])
        try:
            h = int(h[0])
        except:
            h = 1

        firstEValue.append(h)
    return firstEValue




#test a value convertable to int
def into(dun):
    try:
        dun = int(dun)
        return True
    except:
        return False

"""
Logic:
MgCl2 -> [Cl, Mg] + [2, 1]
aMgCl2 + bKOH -> cMg(OH)2 + dKCl
a[Cl, Mg] + b[H, K, O] -> c[H, Mg, O] + d[Cl, K]
a[2, 1]   + b[1, 1, 1] -> c[2, 1, 2]  + d[1, 1]

check position of Mg in KOH, Mg(OH)2 and KCl
-> a[Cl, Mg] + b[H, K, O] -> c[Cl, Mg] + d[H, K, O]
   a[2, 1]   + b[1, 1, 1] -> c[1, 1]  + d[2, 1, 2]
   find a b c d.
"""

print("\nQuang Duy Do J.DO\n")
print("CÂN BẰNG PHƯƠNG TRÌNH HÓA HỌC CÓ 2 CHẤT THAM GIA PHẢN ỨNG VÀ 1-2 SẢN PHẨM/ Blanace chemical equation\n")
print("Hướng dẫn:")
print("   - Gõ từng chất một bằng cách bấm nút <Enter>/ Type each subtance by pressing <Enter>\n   - Nếu chất đó có dấu ngoặc vd: Ba(OH)2 thì gõ thành BaO2H2, Chú ý ko có dấu cách giữa các chất\n if the subtance contain() ex: Ba(OH2), then type BaO2H2\n   - Nếu chỉ có 3 chất tham gia, <Enter> sau khi điền chất thứ 3")


# 1stE

firstE = input("\nNhập chất đầu tiên: ")
op = []
op.extend(firstE)
op.append(None)
op.insert(0, None)
fec = getChem(firstE)
fev = getValue(firstE)


# 2ndE

secondE = input(firstE + " + ")
sec = getChem(secondE)
sev = getValue(secondE)


# 3rdE
thirdE = input(firstE + " + " + secondE + " -> ")
thc = getChem(thirdE)
thv = getValue(thirdE)


# 4thE

fourthE = input(firstE + " + " + secondE + " -> " +  thirdE + " + ")
foc = getChem(fourthE)
fov = getValue(fourthE)


# def balance()


# a.NaOH + b.HCl -> c.NaCl + d.H2O
# e = a + b if na in fec and sec
# f = c + d if na in thc and foc

try:
    if fourthE == "":
        for a in range(1,32):
            for b in range(1,32):
                for c in range(1, 32):
                    e = []
                    f = []
                    g = []
                    h = []
                    for x in range(len(fec)):
                        try:
                            i = sec.index(fec[x]) # search position of Na in second E
                            o = sev[i]
                            mo = a*fev[x] + b*sev[i]
                            e.append(mo)
                            
                        except: # ramaining first E
                            mi = a*fev[x]
                            e.append(mi)

                        ma = thc.index(fec[x])
                        mo = c*thv[ma]
                        g.append(mo)

                    for x in range(len(sec)):
                        if sec[x] not in fec:
                            mp = b*sev[x]
                            f.append(mp)
                            mc = thc.index(sec[x])
                            md = c*thv[mc]
                            g.append(md)
                    if e+f == g:
                        fe = a
                        se = b
                        te = c

                        break
                if e+f == g:
                    fe = a
                    se = b
                    te = c

                    break
            if e+f == g:
                fe = a
                se = b
                te = c

                break

    
    else:
        for a in range(1, 17):
            for b in range(1, 50):
                for c in range(1, 50):
                    for d in range(1, 22):
                        e = []
                        f = []
                        g = []
                        h = []
                        for x in range(len(fec)):
                            try:
                                i = sec.index(fec[x]) # search position of Na in second E
                                o = sev[i]
                                mo = a*fev[x] + b*sev[i]
                                e.append(mo)

                            except: # ramaining first E
                                mi = a*fev[x]
                                e.append(mi)
                            #third E    
                            try:
                                u = thc.index(fec[x])
                                try:
                                    j = foc.index(fec[x])
                                    iu = c*thv[u]+ d*fov[j]
                                    g.append(iu)
                                except:
                                    g.append(c*thv[u])

                            except:
                                hm = foc.index(fec[x])
                                p = d*fov[hm]
                                g.append(p)

                        # Remaining second E and search them in third E and fourth E
                        for x in range(len(sec)):
                            if sec[x] not in fec:
                                mp = b*sev[x]
                                f.append(mp)
                                try:
                                    l = thc.index(sec[x])
                                    try:
                                        mv = foc.index(sec[x])
                                        mj = c*thv[l] + d*fov[mv]
                                        h.append(mj)

                                    except:
                                        h.append(c*thv[l])

                                except:
                                    lm = foc.index(sec[x])
                                    h.append(d*fov[lm])
                        if e == g and f == h:
                            fe = a
                            se = b
                            te = c
                            foe = d
                            break
                    if e == g and f == h:
                        fe = a
                        se = b
                        te = c
                        foe = d
                        break
                if e == g and f == h:
                    fe = a
                    se = b
                    te = c
                    foe = d
                    break
            if e == g and f == h:
                fe = a
                se = b
                te = c
                foe = d
                break

    if fourthE == "":
        if fe >30 and se > 30  and te > 30:
            print("KO thể cân bằng -  vô nghiệm/ Error no result")
        else:
            print("Result:")
            print(fe, se, te)
            print(str(fe) + firstE + " + " + str(se) + secondE + " -> " + str(te) + thirdE + "\nNice :3")
    else:
        if fe >15 and se > 48 and te> 48:
            print("KO thể cân bằng -  vô nghiệm/ Error no result")
        else:
            print("Result:")
            print(fe, se, te, foe)
            print(str(fe)+firstE + " + " + str(se)+secondE + " -> " +  str(te)+thirdE + " + " + str(foe)+fourthE + "\nNice :3")
except:
    print("Lỗi phương trình, kiểm tra lại!/ Check your chemical substances again")


# Jack Do___
