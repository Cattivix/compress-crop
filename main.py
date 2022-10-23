from PIL import Image
import os 


## CHANGE THIS IF CHANGING IMAGE DIRECTORY (do NOT remove 'r')
## program stops if there is a folder inside the directory
path =r'C:\Users\cattg\Pictures\MoviesPictures'




## counters
n_images = 0
n_compressedimages = 0
n_croppedimages = 0

blackRGB = (10, 10, 10)


## move to image directory
os.chdir(path)


## loop in image directory
for file in os.scandir(path):
    print(file.name)
    ## open the image and create a copy to work on, to avoid corrupting the original
    img_og = Image.open(file.name)
    img = img_og.copy()
    n_images+= 1

    ##get image size
    w, h = img.size 
    print(h,w)

    ## compress + save file routine, has to run every iteration

    new_name = file.name[:(len(file.name) - 4)] + '_compressed.png'
    img.resize([w, h], Image.Resampling.LANCZOS, reducing_gap = 3.0)
    img.save(new_name)
    n_compressedimages+= 1 
    print('compressed ' + file.name)



    ##crop + save file routine, has to check if image has black borders
    
    img_data = list(img.getdata())


    current_line = 0
    blackline = True

    for i in range(int(0.25 * h)):


        for y in range(w):


            if all(img_data[y][i] <= blackRGB[i] for i in range(3)):    
                blackline = True

            else:
                blackline = False
                break
            
        if blackline == True:
            current_line =+ 1
            img_data[w:]
        else:
            break

    print(current_line)
            
            


    ##for x in img_data[0:w]:
    ## print(x)



    ## show image
    ##Image.open(image.name).show()



    ## !!!!DELETE ORIGINAL FILE!!!!
    ##os.remove(file.name)



print("Number of images:", n_images)
print("Number of compressed images:", n_compressedimages)
print("Number of cropped images:", n_croppedimages)
