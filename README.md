# Basic_Gait_analysis
This project is a basic version for gait analysis using OpenCV and Mediapipe Holistic .
Here we first run the pose estimation on the sources using mediapipe and then compare them.<br>

<h3>1.Introduction</h3>
Gait analysis is the systematic study of animal locomotion, more specifically the study of human motion, using the eye and the brain of observers, augmented by instrumentation for measuring body movements, body mechanics, and the activity of the muscles.<br>
Here we have used the idea for security implementations, where it is possible to pose of two inputs and tell whether it belongs to same person or not as the movement might be similar but their movement rythm will be mostly unique<br>

<h3>2.Installing the Requirements</h3>
We have provided the 'requirements.txt' in this repository. Use the following command to install the requirements from the given file.<br>

'''bash
pip install -r requirements.txt
'''

<h3>3. Executing the program</h3>
In this phase, we have a sequence of instructions to be followed.<br>

<h4>Step1: Execute the main file.</h4>
Execute the 'Gait_analysis.py' from its parent folder either using any code editors or the command terminal.<br>
<h4>Step2: Supply the first input requirement.</h4>
The input given should be in the format of GIF only and also it should have some human motion for pose estimation.<br>
<img src = 'https://user-images.githubusercontent.com/82897100/157450275-c5874e5b-de02-4f9d-8941-91adc2f50c7f.png'></img>

<h4>Step3: Wait for the program to be executed </h4>
Execution generates the required result as csv and graph plots<br>
<img src = 'https://user-images.githubusercontent.com/82897100/157450556-e5d34ed4-10f6-4238-954c-a19b0f29923d.png'></img>

<h4>Step4: Supply next Input requirement as GIF</h4>
This input should also be in the format of GIF only, also it should have some human motion for pose estimation and it should have gif attributes like length, frame rate etc.. nearly similar to the first provided input for the best performance.<br>
<img src = 'https://user-images.githubusercontent.com/82897100/157450275-c5874e5b-de02-4f9d-8941-91adc2f50c7f.png'></img>

<h4>Step5: Wait till execution</h4>
Execution generates another sot of the required result as csv and graph plots<br>
<img src = 'https://user-images.githubusercontent.com/82897100/157450840-05062abd-798f-4cd0-ac40-36e71b418520.png'></img>

<h4>Step6: Gait analysis comes to an end </h4>
With this step we can come to know taht both the gifs belong to the same person or not.<br>
<img src = 'https://user-images.githubusercontent.com/82897100/157450935-918457b4-d252-4bd4-9f9e-71ffca9ffa61.gif'></img>
<img src = 'https://user-images.githubusercontent.com/82897100/157450952-b3cef042-166a-4303-afcf-c83fe9e940d0.gif'></img>
<img src = 'https://user-images.githubusercontent.com/82897100/157451004-c6b9e971-c385-4956-931f-0d390ca20117.png'></img>
<br>

[Note: The credits for the GIF's belong to appropriate creators]
