from Time1 import Time

time1 = Time()
print "The attributes of time are: "
print "time1.hour:", time1.hour
print "time1.minute:", time1.minute
print "time1.second:", time1.second

print "\nCalling method printMilitary:",
time1.printMilitary()
print "\nCalling method printStandard:",
time1.printStandard()

print "\n\nChanging time1's hour attribute..."
time1.hour = 25
print "Calling method printMilitary after alteration:",
time1.printMilitary()
