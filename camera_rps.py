
from itertools import count
from re import T
from typing_extensions import Self
import cv2
import time
from keras.models import load_model
import numpy as np
import random


class RPS: 


    def __init__(self):
        self.computer_wins = 0
        self.user_wins = 0
        self.tools = ["rock", "paper", "scissors", "none"]    

    def get_prediction(self): 
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        return self.tools [np.argmax(prediction)]
       


    def countdown(self): 

        start_time = time.time()
        while True:
        
            if time.time()-start_time == 1:
                print ("3...")
            if time.time() -start_time== 2:
                print ("2...") 
            if time.time() - start_time== 3:
                print ("1...")
            if time.time() -start_time == 4:
                print ("GO!")
            if time.time() -start_time == 5: #give them a second 
                break



    def get_computer_choice(self, choices):
        
        return choices [random.randint (0,2)]


    def get_winner (self):
            
        if self.computer_wins == 3:
            return "Computer is first to 3 wins! You are beyond saving. GAME OVER"
        if self.user_wins == 3:
            return "You are first to 3 wins! CONGRATULATIONS!!!! YOU WIN FOR REAL"

        self.countdown()

        choices = ["rock", "paper", "scissors"] #in this list index 0 beats 1 beats 2 beats 0; used to index computer choice and describe wins/losses
        user = self.get_prediction()
        #user = "rock" it crashes even with this, so I guess its the call 
        computer = self.get_computer_choice (choices)
       
        print (f"You chose {user} and computer chose {computer}!")

        
        if user == computer: #if its a draw
            print ("Draw! Don't give up!")
            return self.get_winner ()
        if choices.index (user) +1 == choices.index (computer) or choices.index(user)-2 == choices.index (computer): #describes the relationship in comment above (0 bearts 1 beats 2 beats 0)
            self.computer_wins +=1
            print ("Computer Wins!") 
            return self.get_winner ()
        else: 
            self.user_wins +=1
            print ("User wins!")
            return self.get_winner()




def play_RPS ():
    print ("playing Game")
    game = RPS ()

    print (game.get_winner())


play_RPS()


##if i want to do it this way then i should quit option 
#try moving countdown somewhere else!
#resizing error is because 