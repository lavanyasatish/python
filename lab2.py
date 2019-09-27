from collections import Counter 
  
data_set = ("Welcome to the world of Gym " 
"This place has been created to provide well and healthy"  
"thought and well explained exercises for selected questions "  
"If you like Gym for Gym and would like to contribute "  
"here is your chance You can write article and mail your article "  
" to contribute at gymtogym org See your article appearing on "  
"the Geeks for Gym main place and help thousands of other Gym people . ")
  
# split() returns list of all the words in the string 
split_it = data_set.split() 
  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
  
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(2) 
  
print(most_occur) 
