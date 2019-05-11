import cv2
import numpy as np



''' Contrast Stretching formula is:
      s=(smax-smin)/(rmax-rmin)*(r-rmin)+smin
      s=pixel of output image
      r=pixel of input image
    Usage: Expands the brighter side and compreses the lighter side
    
'''
smax=0
smin=0
rmin=0
rmax=0
##############################################################################
def contrast_stretching(path,low,high):
    
    img=cv2.imread(path,0)
    grayimage=cv2.imread(path,0)
    n,m=img.shape
    global rmax
    global rmin
    global smax
    global smin
    smin=low
    smax=high
    
    for i in range(0,m,1):
        for j in range(0,n,1):
            r=img[j,i]
            if(r>rmax):
                rmax=r
            if(r<rmin):
                rmin=r
    print "Maximum gray level in image:",rmax,"\n"
    print "Minimum gray level in image:",rmin,"\n"
    
          
    
    for i in range(0,m,1):
        for j in range(0,n,1):
           r=img[j,i]
           ratio=float(smax-smin)/float(rmax-rmin)
           s=ratio*(r-rmin)+smin
           s=round(s)
           grayimage[j,i]=s
                

    print "Original Image is:",img
    print "\n"
    print "Contrast_Stretching is:",grayimage


    cv2.imshow('Original_Image',img)
    cv2.imshow('Contrast_Stretched_image',grayimage)
    cv2.imwrite('Contrast_Stretched_image.jpg',grayimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

##############################################################################

filename="lowcontrast.jpg"
contrast_stretching(filename,0,255)


