# For Loops
# Executes a block of code a fixed number of times

for x in range(1, 11):
    print(x)

for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR!")

for x in range(1, 11, 2):
    print(x)

msg = "I love you"
for x in msg:
    print(x)

for x in range(1, 21):
    if x == 13:
        continue # skips 13
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break # stops the script before printing 13
    else:
        print(x)

## More practice with for loops
# Range

# for number in range(1, 11, 3): # a = start, b = end, c = step
#     print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)

## FizzBuzz test
## Marking numbers divisible by 3 and 5 and annotating their divisibility in the print

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

## High score

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(max(student_scores))

total_exam_score = sum(student_scores)

# print(total_exam_score)

# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
    else:
        pass
print(max_score)
