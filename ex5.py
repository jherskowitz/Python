my_name = 'J Herskowitz'
my_age = 40 # unfortunately true
my_height = 71 # inches
my_weight = 185 # lbs (I wish)
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black and Gray'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got % s eyes and % s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
