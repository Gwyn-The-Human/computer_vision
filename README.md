# computer_vision
#Project to build a to build a rock-paper-scissors game in which the computer will use compture vision to play against me!


#FIRST MILESTONE 

#Trained a model using https://teachablemachine.withgoogle.com/ to recognise 4 classes (rock, paper, scissors and none) trained on about 3000 images for each class
#The model is saved as keras_model.h5 in this repo. 
#I'll be using the model to build a rock-paper-scissors game in which the computer will use compture vision to play against me! But I will win anyway! 


#SECOND MILESTONE


#wrote a little rock-paper-scissors game; used the random library to randomise computer choice. 
#tried to do something more itneresting with the logic for get_winner than just hard coding "if user == rock and computer #== paper" etc. etc.; instead tried having a list of possible choices, and arranging them so that each item loses to the #left and wins to the right. From this list we can describe how the choices interact by comparing the indexes of the #players' choices in that list. 
