
# def double(num):
#     result =num * 2
# #     print(result)
# # double(6)
# VotingAgeRequirement = 18
# UnacceptedAgeToVote = 12
# VotingForm = eval(input('Enter your present age:'))
# if VotingForm >= VotingAgeRequirement:
#     print('congratulation!you are qualified to vote')
# elif  VotingForm <= VotingAgeRequirement:
#   print('Opps!looks like you are too young too young to vote')
# import time
# print("This is the timer")
# # Ask to Begin
# start = input("Would you like to begin Timing? (y/n): ")
# if start == "y":
#     timeLoop = True
# if start == "n":
#     timeLoop = False
# # Variables to keep track and display
# Sec = 0
# Min = 0
# # Begin Process
# timeLoop = start
# while timeLoop:
#     Sec += 1
#     print(str(Min) + " Mins " + str(Sec) + " Sec ")
#     time.sleep(1)
#     if Sec == 60:
#         Sec = 0
#         Min += 1
#         print(str(Min) + " Minute")
#         break
#
#
#
# double(6)
VotingAgeRequirement = 18
UnacceptedAgeToVote = 12
VotingForm = eval(input('Enter your present age:'))
if VotingForm >= VotingAgeRequirement:
    print('congratulation!you are qualified to vote')
elif  VotingForm <= VotingAgeRequirement:
 print('Opps!looks like you are too young too young to vote')

