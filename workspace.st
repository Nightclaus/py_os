randint secret_number
print secret_number

while secret_number == secret_number do
  input "What is your guess " = user_guess
  if user_guess == secret_number then
    repeat 4 times
      print "You Win"
    endrepeat
    end
  endif
  if user_guess < secret_number then
    print "Higher"
  else
    print "Lower"
  endif
endwhile