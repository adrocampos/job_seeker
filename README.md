# job_seeker
Tool for writing motivation letters with ChatGPT based on a job description. This script automates the process of generating a cover letter tailored to a specific job listing on XING, using the user's CV and the OpenAI API to generate personalized content. You can start from here and then perfonalize your motivation letter to the position.

## Script description

1. It scrapes the job page using urllib and extracts relevant information using BeautifulSoup.
2. It parses job information such as title, description, industry, and employment type.
3. It specifies the directory of the user's CV and extracts text from it using docx2txt.
4. It initiates a conversation with the OpenAI API to generate a cover letter for the job. The conversation involves providing context about the job and the user's CV, and requesting the AI to write a professional cover letter.
5. It prints the generated cover letter and saves it to a text file named after the job title.

## Installation
Create a python3 environment and install the following dependencies:

- annotated-types==0.7.0
- anyio==4.4.0
- beautifulsoup4==4.12.3
- certifi==2024.2.2
- distro==1.9.0
- docx2txt==0.8
- h11==0.14.0
- httpcore==1.0.5
- httpx==0.27.0
- idna==3.7
- numpy==1.26.4
- openai==1.30.3
- pydantic==2.7.1
- pydantic_core==2.18.2
- python-dotenv==1.0.1
- sniffio==1.3.1
- soupsieve==2.5
- tqdm==4.66.4
- typing_extensions==4.12.0