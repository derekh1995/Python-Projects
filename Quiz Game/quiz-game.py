# Python Quiz Game

questions = ("1. What's the difference between a Resource Group and a Subscription?",
             "2. What defines VMSS \"Flexible\" orchestration mode?",
             "3. How can a VM get a token to access another Azure resource without stored credentials?",
             "4. What does registering a resource provider (like Microsoft.KeyVault) do?",
             "5. What does a load balancer health probe do?",)

options = (("A) RG = billing boundary, Sub = container",
            "B) Sub = billing/access boundary, RG = container for resources",
            "C) Same thing",
            "D) RG can contain multiple Subs"),
           ("A) No load balancer support",
            "B) Instances behave like individually managed VMs",
            "C) Single instance only",
            "D) Windows-only"),
           ("A) SSH key forwarding",
            "B) Instance Metadata Service (IMDS)",
            "C) Azure AD Connect Sync",
            "D) A stored connection string"),
           ("A) Buys a license",
            "B) Enables the subscription to create resources of that type",
            "C) Auto-creates a resource",
            "D) Grants admin rights to all users"),
           ("A) Encrypts traffic",
            "B) Checks instance health, routes traffic only to healthy ones",
            "C) Auto-scales the VMSS",
            "D) Logs inbound traffic"))

answers = ("B", "B", "B", "B", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("---------------------")
print("       RESULTS       ")
print("---------------------")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" | ")
print()
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" | ")
print()
print()

score = int(score / len(questions) * 100)
print(f"You scored {score}%")
