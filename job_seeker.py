import os
import json
import pathlib
from pathlib import PosixPath
from dotenv import load_dotenv
import docx2txt
from openai import OpenAI
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

##### Parse information about job. Only works on XING
load_dotenv()

job_link = "https://www.xing.com/jobs/berlin-senior-data-scientist-121127739?sc_o=jobs_your_jobs_saved_jobs_job_click&ijt=jb_12"

req = Request(job_link, headers={'User-Agent': 'Mozilla/5.0'})
job_page = urlopen(req).read()

soup = BeautifulSoup(job_page, 'html.parser')
paragraphs = soup.find_all('script')

b = json.loads(paragraphs[0].contents[0])

job_title           = BeautifulSoup(b["title"], features="html.parser").get_text()
job_description     = BeautifulSoup(b['description'], features="html.parser").get_text()
job_industry        = BeautifulSoup(b['industry'], features="html.parser").get_text()
job_employmentType  = BeautifulSoup(b['employmentType'], features="html.parser").get_text()


## Parse information about my CV #####
cv_dir = os.environ['CV_DIR'] + r"/CV Deutschland v8 DEU.docx"
# cv_dir = PosixPath(cv_dir)
my_cv = docx2txt.process(cv_dir)
my_cv = my_cv.replace('\n', ' ')


## Ask ChatGPT to write a cover letter for the job based on the CV
client = OpenAI(
    api_key = os.environ['OPEN_AI_KEY']
)

response = client.chat.completions.create(
  model="gpt-4-turbo",
  #response_format={ "type": "json_object" },
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Der folgende Text ist eine Stelleanzeige, auf die ich mich bewerben möchte. Bitte filtere mir die wichtiste Keywords hearus, die unbedingt in meine Bewerbung enthalten sein müssen, damich ich größtmögliche Identifikation mit dem Internehmen bzw. der ausgeschriebenen Position herstelle."},
      {"role": "user", "content": " ".join(job_title + job_description + job_industry + job_employmentType)},
      {"role": "user", "content": "Das hier it mein Lebenslauf " + my_cv},
      {"role": "user", "content": "Bitte schreib eine kurze und professionelle Anschreiben zu diese Stelle bassiert in meinem Lebenslauf. Ich kann ab dem 1 August anfangen. Betont wie mein bisherige Erfahrung in mein Lebenslauf beweist die Wichtiste Keyboards. Zeigt motivation und betont meine Soft-Skills"},
      {"role": "user", "content": "Korregiert die Grammatik und umschreiben als deutsche muttersprachler. Maximal 10 Wörter pro Satz. Finde an passenden Stellen geeeignete Synonime, die den Text noch professioneller wirken lassen."},
  ]
)

print("type", type(response.choices[0].message.content))
print(response.choices[0].message.content)

file_name = job_title[:20] + ".txt"
print("Output saved as:", file_name)

with open(file_name, 'w', encoding='utf-8') as file:
    # Write the string to the file
    file.write(response.choices[0].message.content)