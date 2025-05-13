set "secret_number" = 56
input "What is your guess" = "user_guess"

if "user_guess" == "secret_number" then
  print "You Win"
endif
if "user_guess" < "secret_number" then
  print "Higher"
endif
if "user_guess" > "secret_number" then
  print "Lower"
endif