import cv2
import numpy as np

'''
Usage: When an image is displayed on CRT display,power law transform by gamma=2.5 happens,
       thus image appears dark( see difference between Input and CRT_output)

       Thus gamma correction is done by a factor of gamma=(1/2.5)=0.4
       At the end,when it displayed the images appears correctly.
    
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
        
        
def power_law_transform(input_mat,const,gamma):
    
    
    m=len(input_mat[0])
    n=len(input_mat)
    scaling_factor=get_scaling_factor(const,gamma)

    grayimage=input_mat
    

    for i in range(0,m,1):
        for j in range(0,n,1):
           r=input_mat[j,i]
           s=const*(r**gamma)
           if(gamma>1):
               s=s/scaling_factor
           if(gamma<1):
               s=s*scaling_factor

           
           s=abs(round(s))
           grayimage[j,i]=s
                 
    
    return grayimage

###############################################################################

def CRT_correction(filename):
    
    input_img=cv2.imread(filename,0)
    print "Input Image is:",input_img,"\n"
    cv2.imshow("Input Image",input_img)
    cv2.imwrite("InputImage.jpg",input_img)

   

    input_img=cv2.imread(filename,0)
    CRT_output=power_law_transform(input_img,1,2.5)
    print "CRT_Output:",CRT_output,"\n"
    cv2.imshow("CRT Output for Input",CRT_output)
    cv2.imwrite("CRTOutputForInput.jpg",CRT_output)

    input_img=cv2.imread(filename,0)
    gamma_corrected_image=power_law_transform(input_img,1,0.4)
    print "Gamma Corrected Image:",gamma_corrected_image,"\n"
    cv2.imshow("Gamma Corrected Image",gamma_corrected_image)
    cv2.imwrite("GammaCorrectedImage.jpg",gamma_corrected_image)
    
    input_img=cv2.imread(filename,0)
    final_out=power_law_transform(gamma_corrected_image,1,2.5)
    print "Final Output",final_out,"\n"
    cv2.imshow("Final Output",final_out)
    cv2.imwrite("FinalOutput.jpg",final_out)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


################################################################################
_file="disc.jpg"
CRT_correction(_file)   
    
