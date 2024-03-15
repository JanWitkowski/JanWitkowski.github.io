from bs4 import BeautifulSoup
import requests
import sys

def scrape_history(language):
    url = f"https://en.wikipedia.org/wiki/{language}_(programming_language)"
    response=requests.get(url)
    his=[]
    if response.status_code==200:
        helpsoup = BeautifulSoup(response.text, 'html.parser')
        headers=helpsoup.find_all(['h1', 'h2', 'h3'])
        hisheader=None    
        for h in headers:
            if "History" in h.text:
                hisheader=h
                break
        if hisheader:
            hlvl=int(hisheader.name[1])
            
            nastel=hisheader.find_next_sibling()
            while nastel:
                if nastel.name[0]=='h' and int(nastel.name[1])==hlvl:
                    break
                if nastel.name[0]=='h' and int(nastel.name[1])==hlvl+1:
                    his.append("## "+nastel.get_text(strip=True))
                if nastel.name[0]=='h' and int(nastel.name[1])==hlvl+2:
                    his.append("### "+nastel.get_text(strip=True))
                
                if nastel.name == 'p':
                    his.append(nastel.get_text(strip=True))
                nastel=nastel.find_next_sibling()
    return his


url = 'https://www.tiobe.com/tiobe-index/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#main page
title=soup.find('h1')
tgt="The TIOBE Programming Community index is"
paragrafy=soup.find_all('p')
opis=None
for e in paragrafy:
    ptext=e.text.strip()
    if ptext.startswith(tgt):
        opis=ptext
        break

if opis==None:
    print("paragraph not found")
    sys.exit(1)

with open('index.md', 'w') as file:
    file.write("---")
    file.write('layout: default')
    file.write('---')
    file.write("# "+title.text+'\n'+opis+'\n')
    file.write("[Link to see the table](tabela.md)")

#collecting the table 
table=soup.find('table')
data=[]
for row in table.find_all('tr'):
    col=row.find_all('td') 
    if len(col)==0:
        col=row.find_all('th')

    col=[el.text.strip().replace('#', '_Sharp') for el in col]
    data.append([el if not el.startswith("Delphi") else "Delphi" for el in col if el])

for row in data:
    row[2]=row[2].replace(" ", "_")

with open('tabela.md', 'w') as file:
    file.write("---")
    file.write('layout: default')
    file.write('---')
    i=0
    for el in data:
        file.write('|')
        if(i==0):
            for le in el:
                if i!=2:
                    file.write(le+'|')
                i=i+1
            file.write('History|\n|----------|----------|-----------------------|---------|--------|---------|\n')
            continue 

        for le in el:
            file.write(le+'|')
        
        file.write("[see history...]("+el[2]+".md)|\n")

#creating subsites
i=0
for row in data:
    if i==0:
        i=i+1
        continue
    language=row[2]
    scrape_history(language)
    
    with open(language+".md", 'w') as file:
        file.write("---")
        file.write('layout: default')
        file.write('---')
        file.write('# History of '+language+'\n')
        his=scrape_history(language)
        if not his:
            file.write(f"Unfortunately we could not find the History of "+language+" programing language. Our most sincere apologies.")
        else:
            for el in his:
                #el=el.replace('#', 'Sharp')
                if not (el.startswith("Due to technical") or el.startswith("In 1999, the first English language mailing")):
                    file.write(el+'\n')
                else:
                    file.write("_ Corrupted text _"+'\n')
        
