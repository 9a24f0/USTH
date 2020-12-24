# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:23:26 2018

@author: phuonglh

To run xfeatures2d.SURF_create:
    pip install opencv-python==3.4.2.17
    pip install opencv-contrib-python==3.4.2.17

"""

import cv2
import numpy as np
from skimage.transform import integral_image
#from skimage.feature import haar_like_feature

# function for rescale original images in different scales
def RescaleImage(imageFile, NoOfScale):
    #read input file
    img = cv2.imread(imageFile,cv2.IMREAD_GRAYSCALE)
    # print(img.shape)
    #rescale image by NoOfScale 
    listImgs = []
    
    for i in range(NoOfScale):
        img1 = cv2.resize(img, None, fx = 1/(2**i), fy = 1/(2**i))
        listImgs.append(img1)
        
    # return the list of images
    return listImgs

# xpos, ypos: horizontal and vertical cordinates of a point
def RescalePoint(xpos,ypos,NoOfScale):
    listPoints = []
    for i in range(NoOfScale):
        x = round(xpos/(2**i))
        y = round(ypos/(2**i))
        listPoints.append([x,y])
    return listPoints

# compute the RAW features
def computeRAW(listImgs, listPoints, W):
    RawFeature = []
    for scale in range(len(listImgs)):
        for j in range(-W,W+1):
            for k in range(-W,W+1):
                x = listPoints[scale][0]
                y = listPoints[scale][1]               
                #print("i ",i, " y+j,x+k", y,x, "image size ",listImgs[i].shape, "\n",)
                RawFeature.append(listImgs[scale][y+j,x+k])
    return RawFeature

# def compute_raw_multiscale(imgsAtScales, p, no_scale, W):
#     feaVec = []
#     for scale in range(0, no_scale):
#         x = p.x/
#         for i in range(-W,W+1):
#             for j in range(-W,W+1):
#                 feaVec.append(imgsAtScales[scale][pScaled.y+j,pScaled.x+i])
#     return feaVec

# compute the SUB features
def computeSignedSUB(listImgs, listPoints, W):
    SUBFeature = []
    for i in range(len(listImgs)):
        x = listPoints[i][0]
        y = listPoints[i][1]
        for j in range(-W,W+1):
            for k in range(-W,W+1):                            
                SUBFeature.append(listImgs[i][y+j,x+k].astype(np.int16)-listImgs[i][y,x].astype(np.int16))
    return SUBFeature

# compute the SUB features
def computeUnsignedSUB(listImgs, listPoints, W):
    SUBFeature = []
    for i in range(len(listImgs)):
        x = listPoints[i][0]
        y = listPoints[i][1] 
        for j in range(-W,W+1):
            for k in range(-W,W+1):                           
                SUBFeature.append(np.abs(listImgs[i][y+j,x+k].astype(np.int16)-listImgs[i][y,x].astype(np.int16)))
    return SUBFeature

# compute the SURF features
def computeSURF(listImgs, listPoints, W):
    SURFFeature = []
    surf = cv2.xfeatures2d.SURF_create(extended=1)
    kps, des = surf.detectAndCompute(listImgs[0],None)
    print(des.shape)
    #t = cv2.xfeatures2d_SURF
    #t.compute(listImgs[0],kps,des)

# compute the GAUSSIAN SUB descriptors
def computeGaussianSUB(listImgs, listPoints, gausSigma, Ng):
    GAUSSSUBFeature = []
    for i in range(len(listImgs)):
        xOff = np.random.normal(0,gausSigma,Ng)
        xOff = np.int16(xOff)
        yOff = np.random.normal(0,gausSigma,Ng)
        yOff = np.int16(yOff)
        x = listPoints[i][0]
        y = listPoints[i][1]
        for p in range(Ng):            
            GAUSSSUBFeature.append(listImgs[i][y+yOff[p],x+xOff[p]].astype(np.int16)-listImgs[i][y,x].astype(np.int16))
    return GAUSSSUBFeature

# compute the GAUSSIAN SUB descriptors
def computeUnsignedGaussianSUB(listImgs, listPoints, gausSigma, Ng):
    GAUSSSUBFeature = []
    for i in range(len(listImgs)):
        xOff = np.random.normal(0,gausSigma,Ng)
        xOff = np.int16(xOff)
        yOff = np.random.normal(0,gausSigma,Ng)
        yOff = np.int16(yOff)
        x = listPoints[i][0]
        y = listPoints[i][1]
        for p in range(Ng):            
            GAUSSSUBFeature.append(np.abs(listImgs[i][y+yOff[p],x+xOff[p]].astype(np.int16)-listImgs[i][y,x].astype(np.int16)))            
    return GAUSSSUBFeature

# compute the HAAR-LIKE descriptors
# Nh HAAR-LIKE features of random size and position are extracted inside each of the D windows, leading to Nh x D features
# the 4-type is used
def computeHAARLIKE(listImgs, listPoints, W, Nh, maxSizeHAAR):
    HAARFeature = []
    #print("len ",len(listImgs),"\n Points")
    # print(listPoints)
    # print("\n")
    for i in range(len(listImgs)):
        # compute the integral image
        ii = integral_image(listImgs[i])
        #print("Scale ",i, "size ", ii.shape," point ", listPoints[0][0],"\n")
        for j in range(Nh):
            # generate the position of the random
            x = np.random.randint(-W,W) + listPoints[i][0]
            y = np.random.randint(-W,W) + listPoints[i][1]
            size = np.random.randint(0,maxSizeHAAR)
            # calculate the 4-type 
            
            HAARFeature.append(2*ii[y,x+size]+2*ii[y-size,x] + 2*ii[y+size,x]+2*ii[y,x-size] - ii[y-size,x+size] - 4*ii[y,x] - ii[y+size,x-size] - ii[y+size,x+size]-ii[y-size,x-size])                
    return HAARFeature


# Dau vao diem: x: chieu ngang, y: chieu doc
inputF = "egfr_F_R_oly_2X_1.tif"
D = 5 # number of scale
W = 8 # window size is 2W+1

listImgs = RescaleImage(inputF,D)
for img in listImgs:
    h,w = img.shape[:2]
    print("size ", h, " : ", +w)

listPoints = RescalePoint(504,343,D)
for i in range(len(listPoints)):
    print("Point count at scale ",i," ",listPoints[i])
raw = computeRAW(listImgs, listPoints, W)
print(w)
#uSub = computeUnsignedSUB(listImgs, listPoints, W)
#print("size of uSub vector",len(uSub))
#sSub = computeSignedSUB(listImgs, listPoints, W)
#surf = computeSURF(listImgs, listPoints, W)

#gausSigma, Ng = 1, 100
# print(np.random.normal(0,gausSigma,Ng))
#gSub = computeGaussianSUB(listImgs, listPoints, gausSigma, Ng)
#print(gSub)

#computeHAARLIKE(listImgs,listImgs, W, Nh = 8, maxSizeHAAR =5)

#print(raw)
#print(uSub)
#print(sSub)
#print(surf)
#img = cv2.imread(inputF)
#int_img = integral_image(img)
#cv2.imshow("title",int_img)
#cv2.waitKey(0)