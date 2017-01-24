import re

from Tkinter import *
from sgmllib import SGMLParser
import urllib2, urllister, mysgml
class App:
    
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()


        self.w = Label(master, text="enter key: ")
        self.w.pack(side=LEFT)

        self.v=StringVar()
        
        #grafikh yposthrixh ths ergasiaas,sygkekrimena to para8yro emfanishs
        self.widget = Entry(master, width = 20, fg="blue", textvariable=self.v)
        self.widget.pack(side=LEFT)

        
        self.button = Button(master, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=BOTTOM)
        
        self.sear = Button(master, text="Search", command=self.search)
        self.sear.pack(side=LEFT)
        b="http://www.python.org"
        f = urllib2.urlopen(b)
        htmlSource = f.read()
        f.close()

        self.myparser = mysgml.MyParser()
        self.myparser.parse(htmlSource)
        self.teliko={}
        urls=self.myparser.get_hyperlinks()
        data=self.myparser.get_data()
        descr=self.myparser.get_descriptions()
        self.bananasplit(b)

        #trexoume mono ta 20 prwta stoixeia gia logous pou
        #prokyptoun apo ta xronika plaisia ths exetashs
        for d in  range(35):
            if re.match("http", urls[d])!=None:
                print urls[d]
                self.bananasplit(urls[d])
    

    #gia peretairo leptomereies watch this : http://www.youtube.com/watch?v=2B6bnUVbUWw
    #h synarthsh ayth (empneysmenh apo thn sxedon omonymh synathsh ths pytho(split).
    #kaleitai gia na anoixei ola ta links pou periexontai sthn  arxikh selida anazhthshs
    #meta afairei oles tis koina xrhsimopoioumenes kai epexergazontai lai mpainoun sto lexiko pou
    #exei gia kleidia tis lexeis kai ws value mia lista pleiadwn!pou h ka8e pleiada exei mesa
                #to zeygos url kai ari8mo emfanisewn se ayto to url
    def bananasplit(self, urls):
        foo = urllib2.urlopen(urls)
        htmlS = foo.read()
        foo.close()
        myparser = mysgml.MyParser()
        myparser.parse(htmlS)
        
        data=myparser.get_data()
        
        data=data.lower()
        m=re.sub("\n",'',  data)
        q=re.sub("\t",'',  m)
        z=re.sub("[,.:!;?()/\<>-]",'',  q)
        p=z.split(' ')
        dictio={}

        for i in range(len(p)):
            flag=0
            if  p[i] !='.' and p[i] !=',' and p[i] !='the' and p[i] !='' and p[i] != 'a' and p[i] != 'and' and p[i]!='but' and p[i] !='or' and p[i] != 'in' and p[i]!='by' and p[i]!='is' and p[i]!='of' and p[i] !='to' and p[i]!='on' :

                key=dictio.keys()
                for k in range(len(key)):
                    if key[k]==p[i]:flag=1

                    
                if flag==0: dictio[p[i]]=1
                else: dictio[p[i]]=dictio[p[i]]+1

        lista=dictio.keys() 
        for j in range(len(lista)):
            
            if self.teliko.has_key(lista[j])==0:
                self.teliko[lista[j]]=[(urls, dictio[lista[j]])]
            else :
                self.teliko[lista[j]].append((urls, dictio[lista[j]]))
        #print self.teliko


#h search den exei paraxeno onoma alla h mageia krybetai sthn epilogh twn metablhtwn!!!!
#afou parei to string pouj edwsse o xrhsths,diatrexei th lista twn kleidiwn tou telikou mas dictionairy
#otan brei oti atyh h lexh yparxei thn bazei mesa se ena allo dictionary ton anana
#o ananas exei to url ws kleidi kai ton ari8mo emfanisewn sto url ws value,h xrhsimothta
#tou anana erxetai otan mpoun perissoteres apo mia lexeis ggiati tote 8 apsaxnei ekei na brei an
#yparxei kleidi me to url ths trexousaas lexhs,an nai tou allazei to value kai meta erxetai h banana kai
#h guantanamera me to passion fruit na symplhrwsoun to tropiko skhniko,afou h guantanamera
#einai lop gia na broume ola ta urls kai meta sth banana na ypologizoume to pososto emfanishs tou sundiasmo sth selida
         
    def search(self):
        stri=self.v.get()
        stri=stri.lower()
        lists=stri.split(' ')
        anana = {}
        print lists
        banana=0.0
        keys=self.teliko.keys()
        for i in range(len(lists)):
            
            for k in range(len(keys)):
                m=re.match('"', lists[i])
                
                if m!=None :
                    b=re.sub('"', '', lists[i])
                    p=re.compile(b)
                    if p.search(keys[k]) !=None:
                        if len(anana.keys()) == 0 :
                            for g in range(len(self.teliko[keys[k]])):
                                anana[self.teliko[keys[k]][g][0]]=self.teliko[keys[k]][g][1]

                        else:
                            nana = anana.keys()
                            for g in range(len(self.teliko[keys[k]])):
                                for t in range(len(nana)):
                                    if self.teliko[keys[k]][g][0]==nana[t] :
                                        anana[nana[t]]=self.teliko[keys[k]][g][1]+anana[nana[t]]
                                    



                            

                
                if keys[k]==lists[i]:
                    if len(anana.keys()) == 0 :
                        for g in range(len(self.teliko[keys[k]])):
                            anana[self.teliko[keys[k]][g][0]]=self.teliko[keys[k]][g][1]
                            
                    else:
                        nana = anana.keys()
                        for g in range(len(self.teliko[keys[k]])):
                            for t in range(len(nana)):
                                if self.teliko[keys[k]][g][0]==nana[t] :
                                    anana[nana[t]]=self.teliko[keys[k]][g][1]+anana[nana[t]]
                                    


        passionfruit=anana.keys()
        
        for guantanamera in range(len(passionfruit)):
            banana=(anana[passionfruit[guantanamera]])+0.0
            anana[passionfruit[guantanamera]]=banana/len(lists)

        print anana


        
root = Tk()

app = App(root)          

root.mainloop()
