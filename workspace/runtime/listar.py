#for imageName in os.listdir(path): 
            #inputPath = os.path.join(path, imageName) 
        #img = Image.open(inputPath) 
        #text = pt.image_to_string(img, lang ="eng") 
        #imagePath = imagePath[0:-4]

import os
for _, _, j in os.walk('/workspace'):
    print(j)
