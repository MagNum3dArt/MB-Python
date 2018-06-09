from pyfbsdk import *
import time

print time.localtime()

print time.strftime('%X %x')

class YesInit:
    def __init__(self):
        self.timer = time.strftime('%X %x')

class NoInit:
    timer = time.strftime('%X %x')


obj=YesInit()
print obj.timer


obj1=NoInit()
#obj1.__init__()
print obj1.timer




class fruits:
     def __init__(self,w,n=0):
          self.what = w
          self.numbers = n
 
f1 = fruits("apple",150)
f2 = fruits("pineapple")
 
print (f1.what,f1.numbers)
print (f2.what,f2.numbers)


class Building:
     def __init__(self,w,c,n=0):
          self.what = w
          self.color = c
          self.numbers = n
          self.mwhere(n)
 
     def mwhere(self,n):
          if n <= 0:
               self.where = "epsent"
          elif 0 < n < 100:
               self.where = "small stock"
          else:
               self.where = "main stock"
 
     def plus(self,p):
          self.numbers = self.numbers + p
          self.mwhere(self.numbers)
     def minus(self,m):
          self.numbers = self.numbers - m
          self.mwhere(self.numbers)
 
m1 = Building("docs", "white",50)
m2 = Building("docs", "broun", 300)
m3 = Building("cirpich","white")
subject1 = exams('Geolog', 200)
 
print (m1.what,m1.color,m1.where)
print (m2.what,m2.color,m2.where)
print (m3.what,m3.color,m3.where)
 
m1.plus(500)
print (m1.numbers, m1.where)

class exams:
    def __init__(self,p,s=0):
        self.predmet = p
        self.stoimost = s
        self.jadnost_prepoda(s)
 
    def jadnost_prepoda(self,s):
        if  s <= 0:
            self.jadnost_prepoda = 'Gooooood!!!'
        elif 0 < s <= 400:
            self.jadnost_prepoda = 'Norm'
        elif 400 < s < 500:
            self.jadnost_prepoda = 'So So'
        else:
            self.jadnost_prepoda = 'Bith!!!'
 
subject1 = exams('Geology', 200)
subject2 = exams('Geometry', 999)
subject3 = exams('Math')

print (subject1.predmet,subject1.stoimost,subject1.jadnost_prepoda)
print (subject2.predmet,subject2.stoimost,subject2.jadnost_prepoda)
print (subject3.predmet,subject3.stoimost,subject3.jadnost_prepoda)

pTime = FBTime( 0, 0, 0, 60)
FBPlayerControl().Goto(pTime)

def SetKeyValue( pTime, pValue, pAnimationNode ):
  if len(pAnimationNode.Nodes) == 0:
    pAnimationNode.KeyAdd(pTime,pValue)
  else:
    for lNode in pAnimationNode.Nodes:
      SetKeyValue( pTime, pValue, lNode )

def SetKey( pTime, pAnimationNode ):
  if len(pAnimationNode.Nodes) == 0:
    pAnimationNode.FCurve.KeyInsert(pTime)
  else:
    for lNode in pAnimationNode.Nodes:
      SetKey( pTime, lNode )

def DoForAllChildren( lModel, cTime ):
  SetKey( cTime, lModel.AnimationNode )
  for lChild in lModel.Children:
    DoForAllChildren(lChild, cTime)

lModels = FBModelList()
FBGetSelectedModels(lModels)

for lModel in lModels:
  DoForAllChildren(lModel,pTime)
  
  
  
plotOptions = FBPlotOptions()
plotOptions.ConstantKeyReducerKeepOneKey=False
plotOptions.UseConstantKeyReducer = False
plotOptions.PlotAllTakes = False
plotOptions.PlotOnFrame  = True
plotOptions.PlotPeriod   = FBTime( 0, 0, 0, 1,)


FBSystem().CurrentTake.PlotTakeOnSelected( plotOptions )
