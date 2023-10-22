

/***********************************************************************************

* Tufts Electric Racing Team Temperature Sensor Test Code

* 10-9-2023

**********************************************************************************/

#include "U8glib.h" ////U8g lib
#include <math.h>

​

U8GLIB_SH1106_128X64 u8g(U8G_I2C_OPT_NONE);  // I2C / TWI 

​

void prepare(void) 

{

  u8g.setFont(u8g_font_6x10);

  u8g.setFontRefHeightExtendedText();

  u8g.setDefaultForegroundColor();

  u8g.setFontPosTop();

}

​

//draw lines

void draw_line(void)

{

   int i; 

   u8g.setDefaultForegroundColor();

   u8g.firstPage();  

   do 

   {

     for(i = 4;i<u8g.getHeight();i+=4)

     { 

        u8g.drawHLine(0,i,u8g.getWidth());

     } 

     for(i = 4;i<u8g.getWidth();i+=4)

     { 

        u8g.drawVLine(i,0,u8g.getHeight());

     }

   }while(u8g.nextPage());   

   delay(1000);

   for(i = 0;i<=32;i+=2) //X from 0~128 

   {

      u8g.firstPage();  

      do 

      {

        u8g.drawLine(i, 0, 0, 127);

        u8g.drawLine(i*2, 0, 0, 127);

        u8g.drawLine(i*3, 0, 0, 127);

        u8g.drawLine(i*4, 0, 0, 127);

        u8g.drawLine(u8g.getWidth()-i, 0, 127, 127);

        u8g.drawLine(u8g.getWidth()-i*2, 0, 127, 127);

        u8g.drawLine(u8g.getWidth()-i*3, 0, 127, 127);

        u8g.drawLine(u8g.getWidth()-i*4, 0, 127, 127);

        u8g.drawLine(u8g.getWidth()/2+i, 0, 63, 127);

        u8g.drawLine(u8g.getWidth()/2+i*2, 0, 63, 127); 

        u8g.drawLine(u8g.getWidth()/2-i, 0, 63, 127);

        u8g.drawLine(u8g.getWidth()/2-i*2, 0, 63, 127);       

      }while(u8g.nextPage());       

   } 

}

​

void setup() 

{

    prepare();

    Serial.begin(9600);

    draw_line();

    delay(500);

}

​

float resKnown = 3000; //Change if using a different resistor.

float v0 = 5; // Change if using a different voltage

​

void loop(void)

{

    float voltWeRead = analogRead(A4);

    float thermistor = (v0 * resKnown)/(v0 - (v0 * voltWeRead/1023.0)) - resKnown;

    float temp = Calculate_Temp(thermistor);

  

    u8g.firstPage();

    do {

      draw(temp);

    } while (u8g.nextPage());

    //Delay before repeating the loop.

    delay(100);

}

​

void draw(float temp)

{c

    // u8g.print(temp);

    u8g.drawStr(20, 40, "temperature");

    u8g.setPrintPos(30, 50);

    u8g.print(temp);
}

​

float Calculate_Temp(float R)

{

  float A = 3.9083E-3;

  float B = -5.775E-7;

  float T;

  R = R / 1000;       // "We multiplied resistance with 1000 in ADC() function. So need to divide with 1000.""

  // T = (0.0-A + sqrt((A*A)-4.0*B*(1.0-R)))/2.0*B;

  // Break equation in small pieces

  T = 0.0 - A;

  T += sqrt((A * A) - 4.0 * B * (1.0 - R));

  T /= (2.0 * B);

  float tempC = T;             // Actual temperature value

  Serial.print("Temp: ");

  Serial.println(tempC);

  return tempC;

}

