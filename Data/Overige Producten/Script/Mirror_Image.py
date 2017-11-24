from PIL import Image
import glob
import os

def main():
    
    imagePath = '/home/m4dmuffin/Desktop/BBox-Label-Tool/Images/001/{0:06d}.JPG'
    imageSaveLocation = '/home/m4dmuffin/Desktop/Mirror Images/Images/'

    labelPath = '/home/m4dmuffin/Desktop/BBox-Label-Tool/Labels/001/{0:06d}.txt'
    labelSaveLocation = '/home/m4dmuffin/Desktop/Mirror Images/Labels/'
   
    start = 3001
    end  = 3500
    
    width = 1242

    for i in range(start, end):
        #Read Image
        imageObj = Image.open(imagePath.format(i))
        mirroredImage = imageObj.transpose(Image.FLIP_LEFT_RIGHT)

        #Mirror Image 
        imageName = imagePath.format(i)[-10:]
        fullpath = os.path.join(imageSaveLocation, 'mirrored_'+imageName)
        
        #Save Image
        mirroredImage.save(fullpath)

        #Read Label
        labelName = labelPath.format(i).split('/')[-1]
        labelName = "mirrored_" + labelName
        print(labelPath)
        with open(labelPath.format(i), 'r') as labelObj:
           with open(labelSaveLocation + labelName, 'w') as mirroredLabel:
                print(labelObj)
                for line in labelObj:
                    print(line)
                    wordList = line.split(' ')
                    x1 = width - int(wordList[2])
                    x2 = width - int(wordList[0])
  

                    mirroredLabel.write("{} {} {} {} {}".format(x1, wordList[1], x2, wordList[3], wordList[4]))
              
   
if __name__ == '__main__':
    main()
    
