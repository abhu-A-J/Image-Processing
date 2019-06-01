
import cv2
import numpy as np


img1=cv2.imread('Plantation.png')


#=================================================================================================#
def blend_transparent(face_img, overlay_t_img):
    
    overlay_img = overlay_t_img[:,:,:3] 
    overlay_mask = overlay_t_img[:,:,3:]  

 
    background_mask = 255 - overlay_mask


    overlay_mask = cv2.cvtColor(overlay_mask, cv2.COLOR_GRAY2BGR)
    background_mask = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)

 
    face_part = (face_img * (1 / 255.0)) * (background_mask * (1 / 255.0))
    overlay_part = (overlay_img * (1 / 255.0)) * (overlay_mask * (1 / 255.0))

     
    return np.uint8(cv2.addWeighted(face_part, 255.0, overlay_part, 255.0, 0.0))

#=================================================================================================#



#=================================================================================================#

def zone_overlay(zone,count,filename):
   
   if(zone=='A'):
     img=cv2.imread(filename,-1)
     overlay_image=cv2.resize(img,(50,50))
     rows,cols,channels=overlay_image.shape
     for i in range(0,count,1):
        shift_right=i*60
        img1[250:rows+250,300+shift_right:cols+300+shift_right] = blend_transparent(img1[250:rows+250,300+shift_right:cols+300+shift_right], overlay_image)
       

   if(zone=='D'):
     img=cv2.imread(filename,-1)
     overlay_image=cv2.resize(img,(50,50))
     rows,cols,channels=overlay_image.shape
     for i in range(0,count,1):
        shift_right=i*35  
        img1[160:rows+160,490+shift_right:cols+490+shift_right] = blend_transparent(img1[160:rows+160,490+shift_right:cols+490+shift_right], overlay_image)
        

   if(zone=='C'):
      img=cv2.imread(filename,-1)
      overlay_image=cv2.resize(img,(40,40))
      rows,cols,channels=overlay_image.shape
      for i in range(0,count,1):
         shift_right=i*35 
         img1[160:rows+160,240+shift_right:cols+240+shift_right] = blend_transparent(img1[160:rows+160,240+shift_right:cols+240+shift_right], overlay_image)
         


   if(zone=='B'):
      img=cv2.imread(filename,-1)
      overlay_image=cv2.resize(img,(40,40))
      rows,cols,channels=overlay_image.shape
      
      k=0
      for i in range(0,count,1):
          
          if(i<2):
             shift_right=i*45
             img1[190:rows+190,120+shift_right:cols+120+shift_right] = blend_transparent(img1[190:rows+190,120+shift_right:cols+120+shift_right], overlay_image)
            
          else:
              j=1
              shift_down=j*30
              shift_right=k*45
              img1[190+shift_down:rows+190+shift_down,80+shift_right:cols+80+shift_right] = blend_transparent(img1[190+shift_down:rows+190+shift_down,80+shift_right:cols+80+shift_right], overlay_image)
              k=k+1
             
      
#=======================================================================================================#

def plant(zone,count,file_name):
    zone_overlay(zone,count,file_name)
    cv2.imwrite('Result_image.png',img1)
    cv2.imshow('Result_image.png',img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#=========================================================================================================#

plant('A',3,'morningglory.png')
