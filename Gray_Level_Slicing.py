import cv2
import numpy as np



''' Gray Level Slicing is:
      
    Usage: Highlight a particular section of image by making background dark;
           Or can keep background constant and boost the region of concern.
    
'''

##############################################################################
def gray_level_slicing(path,rL,rH):
    
    img=cv2.imread(path,0)
    grayimage=cv2.imread(path,0)
    
    n,m=img.shape
    
    r1=rL
    r2=rH
    for i in range(0,m,1):
        for j in range(0,n,1):
           r=img[j,i]
           
           if(r>=r1 and r<=r2):
               s=255
           else:
               s=0
              
           grayimage[j,i]=s
         
                

    print "Original Image is:",img
    print "\n"
    print "Gray Level Sliced image with zero background:",grayimage
   


    cv2.imshow('Original_Image',img)
    
    cv2.imshow('Gray Level Sliced image',grayimage)
    cv2.imwrite('GrayLevel_Sliced.jpg',grayimage)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##############################################################################

filename="smiley.jpg"
gray_level_slicing(filename,0,30)

'''paramters include: lower and higher of gray level which are region of concern
'''
