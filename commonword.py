import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl


ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input('Enter the URL:')
data=dict()
lis=list()
html=urllib.request.urlopen(url,context=ctx)
soup=BeautifulSoup(html,'html.parser')
for j in soup(['script','style']):
    j.extract()
text=soup.get_text()
a=text.split()
for i in a:
    l=i.strip().upper()
    data[l]=data.get(l,0)+1
for k,v in data.items():
    lis.append((v,k))
lis=sorted(lis,reverse=True)
count=0
for m,n in lis:
    if len(n)>2:
        count=count+1
        if count<=5:
            print('Word:',n , ' Frequency:',m)
