import cv2
import numpy as np



''' Inverse Transform formula is:
      s=L-1-r
      s=pixel of output image
      r=pixel of input image
      pixel value ranges from [0,L-1]
    Usage: To generate the photographic negative. 
    
'''
##############################################################################
def inverse_transform(path):
    L=255
    img=cv2.imread(path,0)
    grayimage=cv2.imread(path,0) 
    n,m=img.shape

    for i in range(0,m,1):
        for j in range(0,n,1):
           r=img[j,i]
           s=L-r
           s=abs(round(s))
           grayimage[j,i]=s
                 

    print "Original Image is:",img
    print "\n"
    print "Log Transformed Image is:",grayimage


    cv2.imshow('Original_Image',img)
    cv2.imshow('Inverse_Transformed_Image',grayimage)
    cv2.imwrite('InverseTransformed_image.jpg',grayimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##############################################################################

filename="disc.jpg"
inverse_transform(filename)


