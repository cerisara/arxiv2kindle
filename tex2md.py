import sys
import os.path
import glob

def getText(l):
    l=l.replace('\\citep','')
    l=l.replace('\\cite','')
    return l

def checkFig(l):
    i=l.find('\\includegraph')
    if i>=0:
        j=l.find('{',i)
        if j>=0:
            k=l.find('}',j)
            if k>=0:
                ff=l[j+1:k]
                if ff.lower().endswith(".pdf"):
                    os.system('convert '+ff+" "+ff[0:-4]+".png")
                    ff=ff[0:-4]+".png"
                if os.path.exists(ff): print("\n![img]("+ff+")\n")
                else:
                    ffs=glob.glob(ff+'*')
                    if len(ffs)>1: print("WARNING ambiguous pic",ffs)
                    if len(ffs)>=1: print("\n![img]("+ffs[0]+")\n")

def texfile(tfich):
    with open(tfich,'rb') as f : ls = f.readlines()

    empty=False
    eq=False
    for l in ls:
        l=l.strip()
        if len(l)==0:
            if not empty:
                empty=True
                print("")
            continue
        if l[0]=='\\':
            if eq:
                if l.startswith('\\end{eq'): eq=False
                else: print(l)
            if l.startswith('\\section'):
                print('\n# '+getText(l[9:-1])+'\n')
            elif l.startswith('\\subsection'):
                print('\n## '+getText(l[12:-1])+'\n')
            elif l.startswith('\\subsubsection'):
                print('\n### '+getText(l[15:-1])+'\n')
            elif l.startswith('\\begin{eq'): eq=True
            elif l.startswith('\\input{'):
                i=l.find('{')
                if i>=0:
                    j=l.find('}',i)
                    if j>=0:
                        texfile(l[i+1:j]+'.tex')
                        continue
            # supprime toutes les lignes qui commencent par \
            checkFig(l)
            if not empty:
                empty=True
                print("")
        elif l[0]=='%':
            # supprime toutes les lignes qui commencent par %
            if not empty:
                empty=True
                print(getText(l))
        else:
            print(l)
            empty=False

texfile(sys.argv[1])

