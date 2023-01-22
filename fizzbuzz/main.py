# Sample application created by Brenno Leal 

def is_fizz(n: int):
  ''' Check if the number is Fizz '''
  return (n % 3) == 0

def is_buzz(n: int):
  ''' Check if the number is Buzz '''
  return (n % 5) == 0


def fizz_buzz(n: int):
  ''' Simple FizzBuzz Function based on the following requirements: 
  - For multiples of three print “Fizz” instead of the number and
  - For the multiples of five print “Buzz”.
  - For numbers which are multiples of both three and five print “FizzBuzz”
  '''
  
  if is_fizz(n) and is_buzz(n):
    print('FizzBuzz')
  elif is_fizz(n):
    print('Fizz')
  elif is_buzz(n):
    print('Buzz')  
  else: 
    print(n)

def lambda_handler(event, context):

  print(event)
  print(context)

  for i in range(100):
    fizz_buzz(i+1)