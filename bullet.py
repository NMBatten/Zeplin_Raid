from graphics import *

class Bullet:

    def __init__( self , pos , xvel, yvel, win ):

        self.pro = Circle( pos , 1 )
        self.pro.setFill( "black" )
        self.pro.draw( win )
        self.xvel = xvel
        self.yvel = yvel
        self.timelapsed = 0
        
    def update( self ):

        self.pro.move( self.yvel , self.xvel  - (0.001 * self.timelapsed) )
        self.timelapsed += 1
        if self.pro.getCenter().getY() > 300:
            self.pro.undraw()
            return Point( 0 , 305 )
        else:
            return self.pro.getCenter()

    def undraw( self ):
        self.pro.undraw()
