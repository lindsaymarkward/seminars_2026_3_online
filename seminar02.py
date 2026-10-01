"""
Write a program that asks the user for a low and high number,
until the high is higher than the low.
while high is lower than the low
Then print n smiley faces :)
where n is a random number between low and high inclusive.

<priming read - get some input>
while <input is bad>
    print error message
    <same as the priming read again - get some input>
do next thing now that you know the input is valid

while is not until
"""
import random

low = int(input("enter low number: "))
high = int(input("enter high number: "))
while high <= low:
    print("error")
    high = int(input("enter high number: "))
print(":)" * random.randint(low, high))

