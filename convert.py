# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s


#functions
def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

#input + convert to float
mph = input("Input speed in mph: ")
output = input("Do you want to convert to \n 1) kph \n 2) ft/s \n 3) m/s? \n: ")
mph = float(mph)

#Outputs
if output == "1":
    print("Speed in kph is", mph_to_kph(mph))
elif output == "2":
    print("Speed in ft/s is", mph_to_fts(mph))
elif output == "3":
    print("Speed in m/s is", mph_to_ms(mph))
elif output:
    print("Please retry and select a correct answer.")
