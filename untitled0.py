# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 16:12:07 2021

@author: MADZEROPIE
"""


from PIL import Image


def MedianFilter(image, wwidth, wheight):
    im=image
    width, height = im.size
    edgex, edgey = wwidth//2, wheight//2
    rw=[0]*(wwidth*wheight)
    gw=[0]*(wwidth*wheight)
    bw=[0]*(wwidth*wheight)
    for x in range(edgex, width-edgex):
        for y in range(edgey, height-edgey):
            i=0
            for fx in range(0,wwidth):
                for fy in range(0,wheight):
                    #print(x+fx-edgex,y+fy-edgey)
                    (r,g,b)=image.getpixel((x+fx-edgex,y+fy-edgey))
                    rw[i],gw[i],bw[i]= r, g, b
                    #rw[i]=r
                    i+=1
            #print(rw)       
            rw.sort()
            bw.sort()
            gw.sort()
            j=(wwidth*wheight)//2
            #print(x,y)
            (r,g,b)=image.getpixel((x,y))
            im.putpixel((x,y),(rw[j], gw[j], bw[j]))
            #im.putpixel((x,y),(rw[j], g, b))
    return im

original = Image.open("salt_pepper_noise.jpg") #CHANGE TO ANOTHER IMAGE
mf=MedianFilter(original,3,3)
mf.save("MedianFilter.jpg")
mf.show()