#**Programming challenge for Perception team member in Kopernikus**

main.py is the main python file. <br />
imaging_interview.py contains image comparision functions

**Question & Answers**

• What did you learn after looking on our dataset? <br />
It seems like image data from security or surveillance cameras.

• How does you program work?<br />
Assumption: All cameraID seemed to have different positions and scenes. And thus the images are completely diferrent for each CameraID. Thus I only need to do similarity comparision for images of same CameraID. So, I sorted the file list in ascending order and used a dictionary to compute number of images in each cameraID. This will help me to separate images from differenet cameraIDs
At first I wrote a "brute force" program that checks similarity comparision for all possible combinations of image pairs of each cameraID. But this is very computaionally expensive. So, later I optimized the code and used hashmap to quickly compare one image with all others and stores unique hash values for each "range of score". The images that had duplicate values were removed.

• What values did you decide to use for input parameters and how did you find these values?<br />
My input parameters are: <br />
min_contour_area = 250 <br />
gaussian_blur_radius_list = [1,3,5,7,9,11] <br />
These values were found by analysis of first few image samples (trial/error method)<br />

• What you would suggest to implement to improve data collection of unique cases in future?<br />
Maintain an image registry. Establish a central registry or database that keeps track of collected images and their unique identifiers. This registry can be periodically checked to ensure that new images are not duplicates of existing ones.<br />
Collect images from multiple sources. <br />
Leverage machine learning algorithms. <br />

• Any other comments about your solution? <br />
An image in the dataset was corrupted so I deleted it from my local dataset. <br />
