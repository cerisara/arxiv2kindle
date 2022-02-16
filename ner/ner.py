from flair.data import Sentence
from flair.models import SequenceTagger

# load the NER tagger
tagger = SequenceTagger.load('ner')

def parseXML():
    import glob
    d="/home/xtof/arxiv/"
    fs=glob.glob(d+"*.xml")
    for f in fs:
        print("FICH ",f)
        with open(f,"r") as ff:
            indesc = False
            abs = ""
            for l in ff:
                if '<dc:description>' in l:
                    i = l.find('<dc:description>')
                    l = l[i+16:]
                    indesc=True
                if indesc: abs += l.strip() + " "
                if '</dc:description>' in l:
                    i = abs.find('</dc:description>')
                    abs = abs[:i].strip()
                    indesc=False
                    # print(abs)
                    sentence = Sentence(abs)
                    tagger.predict(sentence)
                    for entity in sentence.get_spans('ner'): print("NER",entity)
                    # PB: certaines entites sont loupees, et de nombreuses ne sont pas des modeles
                    abs = ""

# oai-harvest --set "cs" --from 2022-01-01 'http://export.arxiv.org/oai2?verb=Identify' 

parseXML()

