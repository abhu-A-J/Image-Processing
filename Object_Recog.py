#classes and subclasses to import
import cv2
import numpy as np
import os

filename = 'DataFile.csv'



####################################################################

def writecsv(color,shape,(cx,cy)):
    global filename
    #open csv file in append mode
    filep = open(filename,'a')
    # create string data to write per image
    datastr = "," + color + "-" + shape + "-" + str(cx) + "-" + str(cy)
    #write to csv
    filep.write(datastr)
    filep.close()

##################################################################################################

    
###############################################################################################


def color_detect(img,cy,cx):
    pix=img[cy,cx]

    if( (pix[0]>pix[1])and (pix[0]>pix[2])):
        color="Blue"
    elif( (pix[1]>pix[0]) and (pix[1]>pix[2])):
        color="Green"
    else:
        color="Red"

    return color

############################################################################################

def main(path):


 
  out_name=path[:len(path)-4]+"output" 
 

  font = cv2.FONT_HERSHEY_SIMPLEX

                       
  img=cv2.imread(path) 
  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


  ret,thresh=cv2.threshold(gray,127,255,0)

  _,cnt,h=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  if (len(cnt)<=1):      
    print"EMPTY FILE"
    empty=["[ "," ",[" "," ]"]]
    writecsv(*empty)

  for i in range(1,len(cnt),1):
    M = cv2.moments(cnt[i])
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    
    color=color_detect(img,cy,cx)
    centroid="("+str(cx)+","+str(cy)+")" 
    
    
    approx = cv2.approxPolyDP(cnt[i],0.01*cv2.arcLength(cnt[i],True),True)
    x = len(approx)
    
    if(x==3):
               shape="Triangle"
               cv2.putText(img,"Triangle",(cx-30,cy),font,0.5,(0,0,0),2)
               cv2.putText(img,color,(cx-20,cy-20),font,0.5,(0,0,0),2)
               cv2.putText(img,centroid,(cx-40,cy+20),font,0.5,(0,0,0),2)
               
    elif(x==5):
               shape="Pentagon"
               cv2.putText(img,"Pentagon",(cx-30,cy),font,0.5,(0,0,0),2)
               cv2.putText(img,color,(cx-20,cy-20),font,0.5,(0,0,0),2)
               cv2.putText(img,centroid,(cx-40,cy+20),font,0.5,(0,0,0),2)
               
    elif(x==6):
               shape="Hexagon"
               cv2.putText(img,"Hexagon",(cx-30,cy),font,0.5,(0,0,0),2)
               cv2.putText(img,color,(cx-20,cy-20),font,0.5,(0,0,0),2)
               cv2.putText(img,centroid,(cx-40,cy+20),font,0.5,(0,0,0),2)
               
    
    elif(x==4):
               
               x,y,w,h=cv2.boundingRect(cnt[i])
               areacon=cv2.contourArea(cnt[i])
               areabox=w*h
               ratio=(float)(areacon/areabox)
               if(ratio>0.7):
                             shape="Trapezium"
                             cv2.putText(img,"Trapezium",(cx-30,cy),font,0.5,(0,0,0),2)
                             cv2.putText(img,color,(cx-20,cy-20),font,0.5,(0,0,0),2)
                             cv2.putText(img,centroid,(cx-40,cy+20),font,0.5,(0,0,0),2)
                             
               else:
                             shape="Rhombus"
                             cv2.putText(img,"Rhombus",(cx-30,cy),font,0.5,(0,0,0),2)
                             cv2.putText(img,color,(cx-20,cy-20),font,0.5,(0,0,0),2)
                             cv2.putText(img,centroid,(cx-40,cy+20),font,0.5,(0,0,0),2)
                             
    else:
               shape="Circle"
               cv2.putText(img,"Circle",(cx-30,cy),font,0.5,(0,0,0),2)
               cv2.putText(img,color,(cx-20,cy-20),font,0.5,(0,0,0),2)
               cv2.putText(img,centroid,(cx-40,cy+20),font,0.5,(0,0,0),2)
               
               
     
    color='["'+color
    centroid =[str(cx),str(cy)+'"]']
    data=[color,shape,centroid]
    writecsv(*data)

  fp=open(filename,'a')
  fp.write("]")
  fp.close()
  cv2.imshow('image',img)
  cv2.imwrite(out_name+".png",img)    
  cv2.waitKey(0)
  cv2.destroyAllWindows()


#################################################################################
    

#####################################################################################
if __name__ == "__main__":
    global filename
    mypath = '.'
   
    onlyfiles = [os.path.join(mypath,f) for f in os.listdir(mypath) if f.endswith(".png")]
 
    for fp in onlyfiles:
       
        filep = open(filename,'a')
       
        filep.write("["+fp)
       
        filep.close()
      
        data = main(fp)
        print data
        
        filep = open(filename,'a')
    
        filep.write('\n')
       
        filep.close()
