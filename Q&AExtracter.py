import re
import docx2txt

#1.Extracting Question and Answer pair to a list
import pandas as pd

my_text = docx2txt.process("RawDataFile.docx")
pattern = re.compile(r'[\.\?][a-zA-Z" "0-9\,\']*\?[a-zA-Z" "0-9\,\']*[\.\?]') #https://regex101.com/ to test

matches = pattern.finditer(my_text)

pairs = []

for match in matches:
    pairs.append(match.group(0)[2:])
    # print(match.group(0)[2:])

# print(pairs)

#2.Seperate questions and Answers

questions = []
answers = []

for sentence in pairs:
    qIndex = sentence.find("?")
    questions.append(sentence[0:qIndex+1].lstrip())
    answers.append(sentence[qIndex+1:].lstrip())
    # print(qIndex)

##Printing the results
# print(len(questions),len(answers))

# for i in range(0,len(questions)):
#     print(questions[i])
#     print(answers[i])

#3.Creating a dataframe with Questions and Answers as Columns

df = pd.DataFrame({'Questions':questions,
                   'Answers':answers})
print(df.shape)

