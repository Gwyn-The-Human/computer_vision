# computer_vision
#Project to build a to build a rock-paper-scissors game in which the computer will use compture vision to play against me!


# FIRST MILESTONE 

#Trained a model using https://teachablemachine.withgoogle.com/ to recognise 4 classes (rock, paper, scissors and none) trained on about 3000 images for each class
#The model is saved as keras_model.h5 in this repo. 
#I'll be using the model to build a rock-paper-scissors game in which the computer will use compture vision to play against me! But I will win anyway! 


# SECOND MILESTONE


#wrote a little rock-paper-scissors game; used the random library to randomise computer choice. 
#tried to do something more itneresting with the logic for get_winner than just hard coding "if user == rock and computer #== paper" etc. etc.; instead tried having a list of possible choices, and arranging them so that each item loses to the #left and wins to the right. From this list we can describe how the choices interact by comparing the indexes of the #players' choices in that list. 


# THIRD MILESTONE
#created a new environment:

```
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
_openmp_mutex             5.1                       1_gnu  
absl-py                   1.2.0                    pypi_0    pypi
asttokens                 2.0.8                    pypi_0    pypi
astunparse                1.6.3                    pypi_0    pypi
backcall                  0.2.0                    pypi_0    pypi
ca-certificates           2022.07.19           h06a4308_0  
cachetools                5.2.0                    pypi_0    pypi
certifi                   2022.6.15        py38h06a4308_0  
charset-normalizer        2.1.1                    pypi_0    pypi
debugpy                   1.6.3                    pypi_0    pypi
decorator                 5.1.1                    pypi_0    pypi
entrypoints               0.4                      pypi_0    pypi
executing                 0.10.0                   pypi_0    pypi
flatbuffers               1.12                     pypi_0    pypi
gast                      0.4.0                    pypi_0    pypi
google-auth               2.11.0                   pypi_0    pypi
google-auth-oauthlib      0.4.6                    pypi_0    pypi
google-pasta              0.2.0                    pypi_0    pypi
grpcio                    1.47.0                   pypi_0    pypi
h5py                      3.7.0                    pypi_0    pypi
idna                      3.3                      pypi_0    pypi
importlib-metadata        4.12.0                   pypi_0    pypi
ipykernel                 6.15.1                   pypi_0    pypi
ipython                   8.4.0                    pypi_0    pypi
jedi                      0.18.1                   pypi_0    pypi
jupyter-client            7.3.4                    pypi_0    pypi
jupyter-core              4.11.1                   pypi_0    pypi
keras                     2.9.0                    pypi_0    pypi
keras-preprocessing       1.1.2                    pypi_0    pypi
ld_impl_linux-64          2.38                 h1181459_1  
libclang                  14.0.6                   pypi_0    pypi
libffi                    3.3                  he6710b0_2  
libgcc-ng                 11.2.0               h1234567_1  
libgomp                   11.2.0               h1234567_1  
libstdcxx-ng              11.2.0               h1234567_1  
markdown                  3.4.1                    pypi_0    pypi
markupsafe                2.1.1                    pypi_0    pypi
matplotlib-inline         0.1.6                    pypi_0    pypi
ncurses                   6.3                  h5eee18b_3  
nest-asyncio              1.5.5                    pypi_0    pypi
numpy                     1.23.2                   pypi_0    pypi
oauthlib                  3.2.0                    pypi_0    pypi
opencv-python             4.6.0.66                 pypi_0    pypi
openssl                   1.1.1q               h7f8727e_0  
opt-einsum                3.3.0                    pypi_0    pypi
packaging                 21.3                     pypi_0    pypi
parso                     0.8.3                    pypi_0    pypi
pexpect                   4.8.0                    pypi_0    pypi
pickleshare               0.7.5                    pypi_0    pypi
pip                       22.1.2           py38h06a4308_0  
prompt-toolkit            3.0.30                   pypi_0    pypi
protobuf                  3.19.4                   pypi_0    pypi
psutil                    5.9.1                    pypi_0    pypi
ptyprocess                0.7.0                    pypi_0    pypi
pure-eval                 0.2.2                    pypi_0    pypi
pyasn1                    0.4.8                    pypi_0    pypi
pyasn1-modules            0.2.8                    pypi_0    pypi
pygments                  2.13.0                   pypi_0    pypi
pyparsing                 3.0.9                    pypi_0    pypi
python                    3.8.13               h12debd9_0  
python-dateutil           2.8.2                    pypi_0    pypi
pyzmq                     23.2.1                   pypi_0    pypi
readline                  8.1.2                h7f8727e_1  
requests                  2.28.1                   pypi_0    pypi
requests-oauthlib         1.3.1                    pypi_0    pypi
rsa                       4.9                      pypi_0    pypi
setuptools                61.2.0           py38h06a4308_0  
six                       1.16.0                   pypi_0    pypi
sqlite                    3.39.2               h5082296_0  
stack-data                0.4.0                    pypi_0    pypi
tensorboard               2.9.1                    pypi_0    pypi
tensorboard-data-server   0.6.1                    pypi_0    pypi
tensorboard-plugin-wit    1.8.1                    pypi_0    pypi
tensorflow                2.9.1                    pypi_0    pypi
tensorflow-estimator      2.9.0                    pypi_0    pypi
tensorflow-io-gcs-filesystem 0.26.0                   pypi_0    pypi
termcolor                 1.1.0                    pypi_0    pypi
tk                        8.6.12               h1ccaba5_0  
tornado                   6.2                      pypi_0    pypi
traitlets                 5.3.0                    pypi_0    pypi
typing-extensions         4.3.0                    pypi_0    pypi
urllib3                   1.26.11                  pypi_0    pypi
wcwidth                   0.2.5                    pypi_0    pypi
werkzeug                  2.2.2                    pypi_0    pypi
wheel                     0.37.1             pyhd3eb1b0_0  
wrapt                     1.14.1                   pypi_0    pypi
xz                        5.2.5                h7f8727e_1  
zipp                      3.8.1                    pypi_0    pypi
zlib                      1.2.12               h7f8727e_2  

```
#downloaded RPS-Template and used it to run my keras_model. All good! 


# FOURTH MILESTONE:

#edited RPS-Template for my own use in camera_rps.py to remove while loop because I thought it would be more efficient for #the model to only have to view one image rather than have it continuously cycling through images as the game runs. I #imported numpy and used argmax to return the computer's best estimate of what the user is doing (rock/paper etc.). 

#created countdown function, and added it to my rock paper scissors game from SECOND MILESTONE. Put it all together. 


#seems to run fine but:
#-Sometimes the countdown will skip a number and just say "3,2, GO" or "2,1,GO" (instead of "3,2,1,GO")
#-still need to add a quit option. As it is now you can't escape!!
#-the game usually crashes before getting to the end. 
#-Need to add a git ignore to repo,