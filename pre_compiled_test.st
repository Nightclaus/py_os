randint secret_number = 56
## print secret_number

while secret_number == secret_number do
  input "What is your guess " = user_guess
  if user_guess == secret_number then
    print "You Win"
    end
  endif
  if user_guess < secret_number then
    print "Higher"
  else
    print "Lower"
  endif
endwhile