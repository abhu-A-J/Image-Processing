import cv2
import numpy as np
from math import log10


''' Log Transform formula is:
      s=c*log(r+1)
      s=pixel of output image
      r=pixel of input image
    Usage: Expands the darker side and compreses the lighter side
    
'''
##############################################################################
def log_transform(path):
    const=1
    scaling=106 

    
    img=cv2.imread(path,0)
    grayimage=cv2.imread(path,0)
    n,m=img.shape

    for i in range(0,m,1):
        for j in range(0,n,1):
           r=img[j,i]
           s=const*log10(r+1)
           s=s*scaling
           s=abs(round(s))
           grayimage[j,i]=s
                 

    print "Original Image is:",img
    print "\n"
    print "Log Transformed Image is:",grayimage


    cv2.imshow('Original_Image',img)
    cv2.imshow('Log_Transformed_Image',grayimage)
    cv2.imwrite('LogTransformed_image.jpg',grayimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##############################################################################

filename="puppy.jpg"
log_transform(filename)


