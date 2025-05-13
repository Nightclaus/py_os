randint secret_number = 56
print secret_number
input "What is your guess " = user_guess

if user_guess == secret_number then
  print "You Win"
endif
if user_guess < secret_number then
  print "Higher"
endif
if user_guess > secret_number then
  print "Lower"
endif