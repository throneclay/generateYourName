import validate_email as ve
import whois as ws
import sys
from multiprocessing import Pool

domain=['com','info','me','net']

def serialJudge(rank,name):
    wrong=0
    n=name+'.'+domain[rank]
    #print 'my_rank=',rank,'I get',n
    try:
        w=ws.whois(n)
    except:
        wrong=1
    if wrong==1 or w.domain_name==n:
        wrong=0
        #print rank,'true'
        return 1
    else:
        #print rank,'false'
        return 2

def judgeDomain(name):
    lens=len(domain)
    p = Pool(lens)
    res=[]
    for i in range(lens):
        res.append(p.apply_async(serialJudge, args=(i,name)))
    p.close()
    p.join()
    
    valid=[]
    for r in res:
        valid.append(r.get())
        
    return valid

class judgeName:
   
    def __init__(self):
        self.mail=['gmail','hotmail','outlook','163','126','139']
        
    def judgeEmail(self,name):
        
        valid=[]
        for m in self.mail:
            v=ve.validate_email(name + '@' + m + 'com',verify=True)
            valid.append(v)
        return valid
    
    def printEmail(self,name):
        valid=self.judgeEmail(name)
        colors=[]
        for i in xrange(len(self.mail)):
            if valid[i]==True:
                colors.append(1)
            else:
                colors.append(2)
        return colors
