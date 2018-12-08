"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

questions_file = open('questions.txt','r')
questions_and_answers = [line.strip() for line in questions_file.readlines()]
questions_file.close()

question_and_answer_dictionary = []
for line in questions_and_answers:
    line_separated = line.split('=')
    question = f'{line_separated[0]}='
    answer = line_separated[1]
    answer_given = input(question)
    question_and_answer_dictionary.append({'question': question, 'answer': answer, 'answer_given': answer_given})


correct_answers = 0
for question_answer in question_and_answer_dictionary:
    if question_answer['answer'] == question_answer['answer_given']:
        correct_answers += 1

write_file = open('result.txt', 'w')
write_file.write('Your final score is {}/{}.'.format(correct_answers,len(question_and_answer_dictionary)))
write_file.close()
