from question_class import Question


questions_prompts = [
  "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange \n\n",
  "What color are bananas?\n(a)Blue\n(b) Yellow\n\n",
  "What color are strawberries?\n(a)Yellow\n(b)Purple"
]

question = [
  Question(questions_prompts[0], "a"),
  Question(questions_prompts[1], "b"),
  Question(questions_prompts[2], "b")
]

def run_quiz(question_list):
  score = 0
  for q in question_list:
    answer = input(q.prompt)
    if answer == q.answer:
      score += 1
  print("You got", str(score), "/", str(len(question_list)))

run_quiz(question)