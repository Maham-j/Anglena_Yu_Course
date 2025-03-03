'''Create a program to help the user type faster.

Give him a word and ask him to write it five times at each time.Check how many seconds it took the user

to type the word at each round.Show how many mistakes were made and show a chart with typing speed evolution during the 5 rounds.'''




import time
import matplotlib.pyplot as plt

time_list = []
mistakes = 0
string='typing speed check'
input('Press Enter to Continue')

for i in range(5):
    time_took = []
    start_time = time.time()
    sentence = input('Type sentence given above:')
    end_time = time.time()
    time_taken = end_time - start_time
    time_took.append(time_taken)
    time_list.append(time_took)
    print('Execution time:',(time_took))
    
    if sentence != string:
        mistakes += 1
print('Mistakes u have made maham :( =',mistakes)
print("Now let's see your evolution")
time.sleep(3)   							#so that it will take 3 seconds to load the chart

custom_colors = ['red', 'green', 'grey', 'orange', 'purple']
x = [1,2,3,4,5]
y = time_list 
legend=['1','2','3','4','5']						#so that no float value occurs on x-axis
plt.bar (x ,y,color = custom_colors )
plt.xticks(x,legend)
plt.xlabel ('Attempts')
plt.ylabel ('Seconds')
plt.title('Your Typing Evolution')
plt.show()
    









