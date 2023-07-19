#### Import necessary libraries
from imaging_interview import draw_color_mask,preprocess_image_change_detection, compare_frames_change_detection
import cv2
import imutils
import os
import time
from itertools import combinations

##Dataset Error: file corrupted c21_2021_03_27__10_36_36.png -> Thus, I deleted it from my image dataset

#### Path of Image dataset
path = "/home/rishabh/Downloads/dataset-candidates-ml/dataset/"

#### Parameters
dim = (640, 480)
min_contour_area= 250 ##value found by analysis of first few image samples
gaussian_blur_radius_list=[1,3,5,7,9,11] ##value found by analysis of first few image samples

def preprocess_path(path):
    file_list = os.listdir(path)
    file_list.sort()
    #print(file_list[0])
    file_list = file_list[1:] #At 0 index, file is .DS_Store Hence starting the indexing from 1
    return file_list
    
#separting images of different camera ID
#Since all cameras have different positions and scenes, we dont need to compare image from one cameraID with a image from other cameraID.
def separate_cameraID(file_list):
    cameraID_images_freq = {}
    for i in range(len(file_list)):
        file = file_list[i].replace('_','-')
        file = file.split('-') #Data format is "{Camera_ID}-{timestamp}""
        if file[0] not in cameraID_images_freq:
            cameraID_images_freq[file[0]] =1
        else:
            cameraID_images_freq[file[0]]+=1
    print(cameraID_images_freq)
    return cameraID_images_freq

#Check all possible combinations of image pairs and compare if they are similar looking. High computational cost but accurate results.
def remove_similar_looking_images_bruteforce(path,dim,min_contour_area,gaussian_blur_radius_list):
    file_list = preprocess_path(path)
    cameraID_images_freq = separate_cameraID(file_list)
    start = time.process_time()
    count = 0
    for key,value in cameraID_images_freq.items():
        print(key)
        files_cameraID = file_list[count:(count+value)] 
        comb = list(combinations(files_cameraID, 2))
        for i in range(len(comb)):
            #print(comb[i][0])
            if os.path.isfile(path+comb[i][0]) and os.path.isfile(path+comb[i][1]):
                prev_frame = cv2.imread(path+comb[i][0]) 
                prev_frame = cv2.resize(prev_frame, dim)
                prev_frame = preprocess_image_change_detection(prev_frame, gaussian_blur_radius_list)
                next_frame = cv2.imread(path+comb[i][1])
                next_frame = cv2.resize(next_frame, dim)
                next_frame = preprocess_image_change_detection(next_frame, gaussian_blur_radius_list)
                score, res_cnts, thresh = compare_frames_change_detection(prev_frame, next_frame, min_contour_area)
    
                if score ==0:
                    os.remove(pathnew+comb[i][1]) 
        count+=value
        
    print(time.process_time() - start)

#Uses a hashmap to quickly compare one image with all others and stores unique hash values for each "range of score"
#Less computational cost and good results.
def remove_similar_looking_images_hashmap(path,dim,min_contour_area,gaussian_blur_radius_list):
    file_list = preprocess_path(path)
    cameraID_images_freq = separate_cameraID(file_list)
    count = 0
    for key,value in cameraID_images_freq.items():
        hash_map = {}
        #cv2.imread(path+"c10-1623871124416.png")
        prev_frame = cv2.imread(path+file_list[count])
        prev_frame = cv2.resize(prev_frame, dim)
        prev_frame = preprocess_image_change_detection(prev_frame, gaussian_blur_radius_list)
        # cv2.imshow('', prev_frame)
        # cv2.waitKey(0)
        for i in range(count,count+value): #len(file_list)
            #print(i)
            next_frame = cv2.imread(path+file_list[i])
            next_frame = cv2.resize(next_frame, dim)
            next_frame = preprocess_image_change_detection(next_frame, gaussian_blur_radius_list)
            score, res_cnts, thresh = compare_frames_change_detection(prev_frame, next_frame, min_contour_area)
            #print("threshold", thresh)
            #print("result", score)
            # print("contours")
            # for c in res_cnts:
            #     #print(cv2.contourArea(c))
            #     print(cv2.contourArea(c))
            
            if score==0:
                os.remove(pathnew+file_list[i])
                continue
            elif len(hash_map) ==0:
                hash_map[int(score)]=i
            elif len(hash_map)>0:
                check = True
                for s in range(int(score)-min_contour_area,int(score)+min_contour_area):
                    if s in hash_map:
                        check=False
                        os.remove(pathnew+file_list[i])
                        break
                if check:
                    hash_map[int(score)]=i
    
        #print(time.process_time() - start)
        count+=value
        print(hash_map)
        print(len(hash_map))
        

#remove_similar_looking_images_bruteforce(path,dim,min_contour_area,gaussian_blur_radius_list)
remove_similar_looking_images_hashmap(path,dim,min_contour_area,gaussian_blur_radius_list)
