import sys
import tkinter as tk
import cgitb
import pandas as pd

class Stock_Average:
      
  def __init__(share,name,year_high,year_low, average_price, percentage_growth, peak, price_dif):
    share.name = name
    share.year_high = float(year_high)
    share.year_low = float(year_low)
    share.average_price = average_price
    share.percentage_growth = percentage_growth
    share.peak = peak
    share.price_dif = price_dif
    
# Method definition
    
  def ShareName(sharename):
    print("The Sharename is " + sharename.name)
    
  def AveragePrice(AveragePrice):
    AveragePrice.Total= (AveragePrice.year_high + AveragePrice.year_low)/2  
    print ("The Average price for the year is " + str(AveragePrice.Total))
    share1.average_price = AveragePrice.Total
    
  def PercentageGrowth(PercentageGrowth):
    PercentageGrowth.Total= ((PercentageGrowth.year_high - PercentageGrowth.year_low)/ (PercentageGrowth.year_low)) * 100  
    print ("The Percentage Growth is " + str(int(PercentageGrowth.Total))+ " %")
    share1.percentage_growth = PercentageGrowth.Total

  def HighestPrice(HighestPrice):
     print ("The Highest price for the year is " + str(HighestPrice.year_high))
        
  def LowestPrice(LowestPrice):
     print ("The Lowest price for the year is " + str(LowestPrice.year_low))
    
    
  def HighesttoLowest(Meltdown):
    Meltdown.Week = 0
    Meltdown.HighPoint = Meltdown.year_high
    while Meltdown.HighPoint > Meltdown.year_low:
        if Meltdown.year_high >= 1.0: 
                    Meltdown.HighPoint= (Meltdown.HighPoint -0.01)
                    Meltdown.Week = Meltdown.Week + 1;
        elif Meltdown.year_high < 1.0:
                    Meltdown.HighPoint= (Meltdown.HighPoint -0.005)
                    Meltdown.Week = Meltdown.Week + 1;
                   
    print ("Number of days for the stock to move from highpoint to lowpoint is " + str(Meltdown.Week) + " days or approximately " + str(float (Meltdown.Week /30)) + " Months" ) ;             

    
  def Peak(Peak):
    Peak.Week = 0
    Peak.HighPoint = Peak.year_high
    while Peak.HighPoint > Peak.year_low:
        if Peak.year_high >= 1.0: 
                Peak.HighPoint= (Peak.HighPoint -0.01)
                Peak.Week = Peak.Week + 1;
        elif Peak.year_high < 1.0:
                Peak.HighPoint= (Peak.HighPoint -0.005)
                Peak.Week = Peak.Week + 1;
                 
    print ("Number of days for the stock to move from lowpoint to highpoint is " + str(Peak.Week) + " days or approximately " + str(float (Peak.Week /30)) + " Months" ) ;             
    share1.peak = Peak.Week

  def Pad(sharename):
    print("---------------------------------------------------------------------------------- " )
     
  def PriceDifference(PriceDifference):
    PriceDifference.Sum= (PriceDifference.year_high - PriceDifference.year_low) ;
    print ("The Difference in price for the year is " + str(PriceDifference.Sum ));
    share1.price_dif =   PriceDifference.Sum  

# New Class
class Filewriter(Stock_Average):
   
    def __init__(file,name,year_high,year_low, average_price, percentage_growth, peak, price_dif):
      file.name = name
      file.year_high = float(year_high)
      file.year_low = float(year_low)
      file.average_price = average_price
      file.percentage_growth = percentage_growth
      file.peak = peak
      file.price_dif = price_dif 
      super().__init__(name,year_high,year_low, average_price, percentage_growth, peak, price_dif)      

    def FileOpen(fileopen): 
      f = open("Sharefile.txt", "w")
      
    def FileWrite(fwrite):
      f = open("Sharefile.txt", "a")
      f.write(str(share1.name))
      f.write(',')
      f.write (str(share1.year_high))
      f.write(',')
      f.write (str(share1.year_low))
      f.write(',')
      f.write (str(share1.average_price))
      f.write(',')
      f.write (str(int(share1.percentage_growth)))
      f.write(',')
      f.write (str(share1.peak))
      f.write(',')
      f.write (str(share1.price_dif))
      f.write('\n')
      
      
# Child Class

class Volume(Stock_Average):
   def __init__(volume,name,volume_high,volume_low):
     volume.name = name
     volume.volume_high = float(volume_high)
     volume.volume_low = float(volume_low)
     super().__init__(name,volume_high, volume_low,0,0,0,0)

# Defining objects 


ans=True
share1 = Stock_Average("",0,0,0,0,0,0)
volume1 = Volume("Volume",4230,100)
file1 = Filewriter("",0,0,0,0,0,0)
f = open("Sharefile.txt", "a")

while ans == True:  
    share1.name = input("Enter ShareName:")
    if share1.name == "":
         break
         ans= False
    elif share1.name !="":
            share1.year_high = float(input('Enter Highest Price for 52 weeks: '))
            share1.year_low = float(input('Enter Lowest Price for 52 weeks: '))
            share1.ShareName()
            share1.HighestPrice()
            share1.LowestPrice()
            share1.AveragePrice()
            share1.PriceDifference()
            share1.Peak()
            share1.PercentageGrowth()
            share1.Pad()                     
            file1.FileWrite()
    f.close() 
    f = open("Sharefile.txt", "r")
    print(f.read()) 
    f.close
    



