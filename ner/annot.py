def annot(ners,fich):
    with open(fich,"r") as f:
        indesc = False
        abs = ""
        for l in f:
            if '<dc:description>' in l:
                i = l.find('<dc:description>')
                l = l[i+16:]
                indesc=True
            if indesc: abs += l.strip() + " "
            if '</dc:description>' in l:
                i = abs.find('</dc:description>')
                abs = abs[:i].strip()
                indesc=False
                break
    for ner in ners:
        i=abs.find(ner)
        if i<0: continue
        a,b=max(0,i-40),min(len(abs),i+40)
        print(ner,i,len(abs),abs[a:b])
        input()

           

ners = set()
with open("/home/xtof/ner.log","r") as f:
    for l in f:
        if l.startswith("FICH"):
            if len(ners)>0: annot(ners,fich)
            fich = l[6:].strip()
            ners.clear()
        elif l.startswith("NER"):
            ss = l.split('"')
            ners.add(ss[1])
