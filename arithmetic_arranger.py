spacing = " " * 4

def arithmetic_arranger(problems, showAnswer=False):
    row1 = ""
    row2 = ""
    bar = ""
    answers = ""
    arranged_problems = ""

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        splitproblem = problem.split()

        if (splitproblem[1] != '+' and splitproblem[1] != '-'):
            return "Error: Operator must be '+' or '-'."
        if (len(splitproblem[0]) > 4 or len(splitproblem[2]) > 4):
            return "Error: Numbers cannot be more than four digits."
        if (not(splitproblem[0].isnumeric()) or not(splitproblem[2].isnumeric())):
            return "Error: Numbers must only contain digits."

        maxLength = len(max(splitproblem, key=len))

        row1 += splitproblem[0].rjust(maxLength + 2, ' ') + spacing
        row2 += splitproblem[1] + " " + splitproblem[2].rjust(maxLength, ' ') + spacing
        bar += '-' * (maxLength + 2) + spacing

        if (showAnswer):
          if(splitproblem[1] == "+") :
            answer = int(splitproblem[0]) + int(splitproblem[2])
          if(splitproblem[1] == "-") :
            answer = int(splitproblem[0]) - int(splitproblem[2])
          answers += str(answer).rjust(maxLength + 2, ' ') + spacing
  
    arranged_problems += row1.rstrip() + "\n" + row2.rstrip() + "\n" + bar.rstrip()
    if (showAnswer):
      arranged_problems += "\n" + answers.rstrip()
      
    return arranged_problems
