# Objective: The aim of this assignment is to practice using nested loops in Python.

# Task 1: Your Mood Tracker 
# Simulate a mood tracker that records your mood at three different times of the day 
# (morning, afternoon, evening) for each day of the week. #####need times list######
# Use nested loops to implement this: the outer loop should iterate over the days, #####Days list#####
# and the inner loop should iterate over the times of the day. For each time, 
# randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.####\n######

#Example Outcome: An example would be "On Tuesday afternoon you were sad" "On Tuesday night you were happy" "On Wednesday morning you were tired"

import random
moods = ["Happy", "Sad", "Energetic", "Calm", "Totally Tubular"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
times = ["morning", "afternoon", "evening"]

for day in days:
    for time in times:
        mood = random.choice(moods)
        print(f"On\n{day} {time}, you felt {mood}.")

    