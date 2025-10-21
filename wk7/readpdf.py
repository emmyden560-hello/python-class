import PyPDF2

input_file = "Endline.pdf"
output_file = "output.txt"


with open(input_file, "rb") as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)

    with open(output_file, "w", encoding = "utf-8") as out:
        for page_num, page in enumerate(reader.pages, start = 1):
            text = page.extract_text()
            if text: 
                out.write(text + "\n")
            print(f"Extracted text from page {page_num}")
        else:
            print(f"no text found in page {page_num}")


'1.count words'
new_input = "output.txt"
new_output = "stringmanipulation.txt"

with open(new_input, "r", encoding = "utf-8") as file:
    content = file.read()

words_count = len(content.split())
print("Number of words:", words_count)

' 2. count characters'

char_count = len(content)
print("Number of characters:", char_count)


'3. create list of maximum 10 words from the document'
import random

lis = content.split()
new_list = []
random_lis = random.choice(lis) 
for x in lis:
    new_list.append(x)
    if len(new_list) == 10:
        break
print(new_list)

'4. count the number of times the word "the" occurs in the document'

lists = content.split()
counts = lists.count("the")
print("number of 'the':", counts)

'5. list out words that end with "-ound"'

lis = content.split()
new_list = []
for x in lis:
    if x.endswith('ound'):
        new_list.append(x)
        break
print(new_list)


