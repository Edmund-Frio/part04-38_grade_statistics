# Write your solution here

def input_from_user(number_inputs):
  numbers = []
  
  for i in range(len(number_inputs)):
    number = int(number_inputs[i])
    numbers.append(number)
  return numbers
  
def print_statistics(numbers):
  print("Statistics:")
  
def analyze(numbers):
  print()
  
  
    
  

def main():
  while True:
    inputs = input_from_user(input("Exam points and exercises completed: ").split())
    if len(inputs) <= 1:
      break
    print(inputs)
  analyze(inputs)
  print_statistics(inputs)
  
main()