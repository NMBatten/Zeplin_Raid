from graphics import *
from random import randrange

class Explosion:

    def __init__( self , win , size , xpos , ypos ):

        self.win = win
        self.clist = [ "red" , "orange" , "dark orange" , "orange red" , "yellow" ]
        self.ypos = ypos + 2
        self.xpos = xpos
        self.explos = []
        self.size = size
        self.draw( 20 + ( self.size ) )
        self.tval = 0
        
    def drawCircle( self ):
        x = self.xpos + randrange( -self.size , self.size ) / 2
        y = self.ypos + randrange( -self.size , self.size ) / 2
        c = Circle( Point( x , y ) , randrange( 1 , 3 ) )
        color = self.clist[ randrange( 0 , 5 ) ]
        c.setFill( color )
        c.setOutline( color )
        c.draw( self.win )
        self.explos.append( c )

    def draw( self , num ):
        for i in range( num ):
            self.drawCircle()
        
    def undraw( self ):
        for circle in self.explos:
            circle.undraw()
        
    def update( self ):

        self.undraw()
        self.size = int( self.size + 1 )
        self.draw( 30 - self.tval )
            
        self.tval = self.tval + 1    
        if self.tval > 12:
            self.undraw()
