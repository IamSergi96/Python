def arithmetic_arranger(problems, display_results = False):
  #max numbers of problems
  if len(problems) >5:
    return "Error: Too many problems."
  #lists
  first_line=[]
  second_line=[]
  dash_line=[]
  result_line=[]
  #rules:
  for problem in problems:
    operand1, operator, operand2 = problem.split()
    if not operand1.isdigit() or not operand2.isdigit():
      return "Numbers must only contain digits."
    if len(operand1)>4 or len(operand2)>4:
      return "Error: Numbers cannot be more than four digits."
    if operator not in ("+","-"):
      return "Error: Operator must be '+' or '-'."
    #lines for each problem:
    max_length = max(len(operand1), len(operand2))
    first_line.append(operand1.rjust(max_length +2))
    second_line.append(operator + operand2.rjust(max_length +1))
    dash_line.append("-"*(max_length+2))
    #calculate if display is True
    if display_results:
      results = str(eval(problem))
      result_line.append(results.rjust(max_length+2))
  #combine to a single text
  single_text_problems = "\n".join(first_line + [""] + second_line + [""] + dash_line)
  if display_results:
      single_text_problems += "\n" + "\n".join(result_line)
  return single_text_problems

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
