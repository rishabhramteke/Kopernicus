#**Programming challenge for Perception team member in Kopernikus**

main.py is the main python file

imaging_interview.py contains image comparision functions

Question & Answers

• What did you learn after looking on our dataset?
It seems like data from security or surveillance cameras.
• How does you program work?
Assumption: All cameraID seemed to have different positions and scenes. And thus the images are completely diferrent for each CameraID. Thus I only need to do similarity comparision for images of same CameraID. So, I sorted the file list in ascending order and used a dictionary to compute number of images in each cameraID. This will help me to separate images from differenet cameraIDs
At first I wrote a "brute force" program that checks similarity comparision for all possible combinations of image pairs of each cameraID. But this is very computaionally expensive. So, later I optimized the code and used hashmap 
• What values did you decide to use for input parameters and how did you find these values?
• What you would suggest to implement to improve data collection of
unique cases in future?
• Any other comments about your solution?
