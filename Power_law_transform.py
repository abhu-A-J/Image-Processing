import cv2
import numpy as np

''' Power_Law Transform formula is:
      s=c*r^gamma
      s=pixel of output image
      r=pixel of input image
      if (gamma>1): it performs inverse log transform
      if (gamma<1): it performs log transform
      log tranform         : compresses the lighter side of image
      inverse log transform: compresses the darker side of the image
    Usage: used for gamma correction on CRT
    
'''
##############################################################################
def get_scaling_factor(constant,gamma_value):
    if(gamma_value>1):
        temp=(255**gamma_value)*(constant)
        scaling=(temp/255)
    elif(gamma_value<1):
        temp=(255**gamma_value)*(constant)
        scaling=(255/temp)
    else:
        scaling=1

    return scaling

##############################################################################
        
        
def power_law_transform(path,const,gamma):
    
    img=cv2.imread(path,0)
    grayimage=cv2.imread(path,0) 
    n,m=img.shape
    scaling_factor=get_scaling_factor(const,gamma)
    print "Scaling factor will be:",scaling_factor,"\n"
    for i in range(0,m,1):
        for j in range(0,n,1):
           r=img[j,i]
           s=const*(r**gamma)
           if(gamma>1):
               s=s/scaling_factor
           if(gamma<1):
               s=s*scaling_factor

           
           s=abs(round(s))
           grayimage[j,i]=s
                 

    print "Original Image is:",img
    print "\n"
    print "Power Law Transformed Image is:",grayimage


    cv2.imshow('Original_Image',img)
    cv2.imshow('Power_Law_Transformed_Image',grayimage)
    cv2.imwrite('Power_Law_Transformed_image.jpg',grayimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##############################################################################

filename="puppy.jpg"
power_law_transform(filename,1,2.5)
''' parameters include: filename,constant value in relation,gamma value
'''
