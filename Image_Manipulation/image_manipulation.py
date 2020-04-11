from PIL import Image 
  
def main(): 
    try: 
        ## Relative Path 
        img = Image.open("picture.png") 
        img2 = Image.open("picture2.png") 
        
        width, height = img.size
        width1, height1 = img2.size

        print(" Image width = {}, height= {} ".format( width, height) )
        print(" Image width = {}, height= {} ".format( width1, height1) )

        ## resize
        # img3 = img2.resize((1873, 937))

        # alpha = 0.3

        img4 = img2.copy()

        # This method completely overwrites the image
        # img4.paste(img, (0,0), img)

        img5 = merge(img4, img);

        ## Angle given 
        # img = img.rotate(180)  
          
        ## Saved in the same relative location 
        img5.save("resulting_picture3.png") 
    except IOError: 
        print(IOError)
        pass

## img1 and img2 should be of same size
## img2 will be merged on top of img1
def merge(img1: Image, img2: Image) -> Image:
    width, height = img1.size
    for w in range(0, width):
        for h in range(0, height):
            r1,g1,b1 = img1.getpixel((w,h))
            r2,g2,b2,a2 = img2.getpixel((w,h))
            if filter1(r1,g1,b1,0) < filter1(r2,b2,g2,0.8):
                # img1.putpixel((w,h),(r2,g2,b2,0))
                img1.putpixel( (w,h), ( 
                    ((width-w)//width * r1 + r2 )//2, 
                    ((width-w)//width * g1 + g2 )//2, 
                    ((width-w)//width * b1 + b2 )//2, 0 ) 
                );
    return img1;

def filter1(r,g,b,a):
    if(a>0) :
        return (r+g+b) * a;
    return r+g+b;

def filter2(r,g,b,a):
    if(a>0) :
        return (r+g+b) * a;
    return r+g+b;
  
if __name__ == "__main__": 
    main()