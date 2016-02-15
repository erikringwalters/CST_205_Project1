#Project by Erik Ring-Walters
#GitHub repo = https://github.com/erikringwalters/CST_205_Project1
#GitHub may not be up to date because I still am having a hard time pushing
#Project takes the median pixel from nine images and makes a new clean image from that.
#Much help from Leticia Domingues.

#Shows path to images on my computer.
pics = [makePicture("C:\\Users\\Erik\\Desktop\\project1ImagesCST205\\1.png"),
 makePicture("C:\\Users\\Erik\\Desktop\\project1ImagesCST205\\2.png"),
 makePicture("C:\\Users\\Erik\\Desktop\\project1ImagesCST205\\3.png"),
 makePicture("C:\\Users\\Erik\\Desktop\\project1ImagesCST205\\4.png"),
 makePicture("C:\\Users\\Erik\\Desktop\\project1ImagesCST205\\5.png"),
 makePicture("C:\\Users\\Erik\\Desktop\\project1ImagesCST205\\6.png"),
 makePicture("C:\\Users\\Erik\\Desktop\\project1ImagesCST205\\7.png"),
 makePicture("C:\\Users\\Erik\\Desktop\\project1ImagesCST205\\8.png"),
 makePicture("C:\\Users\\Erik\\Desktop\\project1ImagesCST205\\9.png")]

#Uses getHeight and getWidth built-in's to get the height and width of the first image. (will be used later)
width = getWidth(pics [0])
height = getHeight(pics [0])
#creates variable for final image
finalPic = makeEmptyPicture(width, height)
#receives pixels of every image
for y in range(0, height):
  for x in range(0, width):
    pixels = [getPixel(pics[0],x,y),
     getPixel(pics[1],x,y), 
     getPixel(pics[2],x,y),
     getPixel(pics[3],x,y), 
     getPixel(pics[4],x,y), 
     getPixel(pics[5],x,y),
     getPixel(pics[6],x,y),
     getPixel(pics[7],x,y),
     getPixel(pics[8],x,y)]
#receives blue values of every pixel  
    bluePixels = [getBlue(pixels[0]),
      getBlue(pixels[1]),
      getBlue(pixels[2]),
      getBlue(pixels[3]),
      getBlue(pixels[4]),
      getBlue(pixels[5]),
      getBlue(pixels[6]),
      getBlue(pixels[7]),
      getBlue(pixels[8])]
#receives green values of every pixel    
    greenPixels = [getGreen(pixels[0]),
      getGreen(pixels[1]),
      getGreen(pixels[2]),
      getGreen(pixels[3]),
      getGreen(pixels[4]),
      getGreen(pixels[5]),
      getGreen(pixels[6]),
      getGreen(pixels[7]),
      getGreen(pixels[8])]
#receives red values of every pixel      
    redPixels = [getRed(pixels[0]),
      getRed(pixels[1]),
      getRed(pixels[2]),
      getRed(pixels[3]),
      getRed(pixels[4]),
      getRed(pixels[5]),
      getRed(pixels[6]),
      getRed(pixels[7]),
      getRed(pixels[8])]
      
#Sorts pixel color values in numerical order. 
    bluePixels = sorted(bluePixels)  
    redPixels = sorted(redPixels)
    greenPixels = sorted(greenPixels)
#New variable getting pixels for new image    
    pixel = getPixel(finalPic,x,y)
#variable makes new color for each pixel for new image    
    newColor = makeColor(redPixels[4], greenPixels[4], bluePixels[4])
#sets to the new variable above    
    setColor(pixel,newColor)
#Displays final picture    
show(finalPic)
repaint(finalPic)