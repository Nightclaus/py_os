set "secret_number" = 56
set "user_guess" = 90

if "user_guess" == "secret_number" then
  print "You Win"
endif
if "user_guess" < "secret_number" then
  print "Higher"
endif
if "user_guess" > "secret_number" then
  print "Lower"
endif