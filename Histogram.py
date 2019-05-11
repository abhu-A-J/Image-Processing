import cv2
import numpy as np
import matplotlib.pyplot as plt



''' Histogram:Finding the dynamic range of pixel values
    
'''

##############################################################################
def histogram_evaluation(path):

    rmax=0
    rmin=255
    
    img=cv2.imread(path,0)
    grayimage=cv2.imread(path,0)
    ravel_arr=img.ravel()
    n,m=img.shape

    for i in range(0,m,1):
        for j in range(0,n,1):
            r=img[j,i]
            if(r>rmax):
                rmax=r
            if(r<rmin):
                rmin=r
    
    
    plt.subplot(2,1,1)
    plt.imshow(img,cmap='gray')
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(2,1,2)
    plt.hist(ravel_arr,256,[0,255],rwidth=0.6)
    plt.title('Histogram')
    plt.xlabel('Gray Level, rk')
    plt.ylabel('Number of pixels, nk')
    plt.xlim(xmin=rmin,xmax=rmax)
    plt.show()
    
    

##############################################################################

filename="doggy.png"
histogram_evaluation(filename)
