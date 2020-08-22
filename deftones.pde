import gab.opencv.*;

OpenCV opencv;


int width = 1000;
int height = 1000;

int intervalCount = 100;
int ellipseSize = 7;

int marginSize = 60;


PImage img,canny;
PImage new_image;

PImage final_image;

String filename = "cicada";

void setup()
{
  size(1000,1000);
  background(0);
  
  img = loadImage(filename+".jpg");
  opencv = new OpenCV(this,img);
  opencv.findCannyEdges(20,75);
  canny = opencv.getSnapshot();
  
  new_image = new PImage(100,100);
  final_image = new PImage(100,100);
}

void draw()
{
  

  final_image = reduceImage(canny);
  

  

  
  
//  image(canny,0,0);
  

//  scale(0.1); //moved up to scale(10) in the reduceImage function
  int icount = 0;
  for(int i=marginSize;i<(width-marginSize);i+=(width/intervalCount))
  {
    int jcount = 0;
    for(int j=marginSize;j<(height-marginSize);j+=(height/intervalCount))
    {
      
 //    print(brightness(final_image.get(icount,jcount)));
     if(brightness(final_image.get(icount,jcount))>0)
        ellipse(i,j,ellipseSize,ellipseSize);
        
     jcount++;
    }
    icount++;
  }
  
//    image(new_image,0,0);
}


PImage reduceImage(PImage input_image)
{
  input_image.resize(1000,1000);
  int[][] output_array = new int[100][100];
  
  for(int i=0;i<100;i++)
  {
    for(int j=0;j<100;j++)
    {
      output_array[i][j] = input_image.get(i*10,j*10);
    }
  }
  

  
  for(int i=0;i<100;i++)
  {
    for(int j=0;j<100;j++)
    {  
      int pix_val = input_image.get(i*10,j*10);
      if(brightness(pix_val)>0)
        new_image.set(i,j,pix_val);
 //     print(brightness(pix_val)+ "\n");
    }
  }
  
 // new_image.resize(1000,1000);
 //scale(10);
  
//  image(new_image,0,0);
  return new_image;



  
  
//  return output_image;
}
