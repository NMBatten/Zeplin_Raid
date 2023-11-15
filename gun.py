from graphics import *
import random
from bullet import Bullet


class Gun:

    def __init__( self , pos , win ):

        self.cannon = Rectangle( Point( pos.getX()-2, pos.getY()), Point( pos.getX()+2, pos.getY()+5))
        self.cannon.setFill( 'black' )
        self.cannon.draw( win )
        self.pos = pos
        self.win = win
        self.type = 'stationary'
        self.shottimer = random.randrange( -10, 11 )

    def update( self ):

        self.shottimer +=1
        if self.shottimer > 75:
            self.shottimer = random.randrange( -5, 5 )
            return True

    def fire( self, directionx, directiony ):

        b = Bullet( self.pos, 3, directiony + (random.randrange( -2,3)/25) , self.win )
        return b

    def IsIn( self, hit ):

        if (hit < self.pos.getX() +5) and (hit > self.pos.getX()-5):

            self.cannon.undraw()
            return True
        else:
            return False

    def getXPos( self ):
        return self.pos.getX()

    def getType( self ):
        return self.type

class SPAAG( Gun ):

    def __init__( self, pos, win, level ):

        """

        pos    the initial position of the gun
        win    the canvas to display the gun in
        level  the difficulty (effectiveness of the gun)
        """
        super().__init__( pos, win )
        self.cannon.undraw()
        self.cannon = Image( Point( pos.getX(), pos.getY() + 2 ), 'T87SPAAG.png' )
        self.type = 'mobile'
        self.level = level
        self.cannon.draw( win )

    def move( self, amount ):

        self.cannon.move( amount , 0 )
        self.pos = Point(self.pos.getX() + amount, self.pos.getY() )
        
        
        

                                             

    
