from graphics import *

class DispBar:
    """A class that displays progess via a graphical green and red bar"""

    def __init__( self, win, posx, posy, height, length, numrange ):

        """Sets up the Bar

        win        The graphics window to display on
        posx       The x value of the center of the desired bar (in pixels)
        posy       The y value of the center of the desired bar (in pixels)
        height     The height of the desired bar (in pixels)
        length     The length of the desired bar (in pixels)
        numrange   The desired range of display for the bar
        """      

        height = int(height/2)
        self.topyval = posy + height
        self.lowyval = posy - height

        self.height = height
        self.length = length
        
        self.greenrect = Rectangle( Point( (posx + self.length), (self.topyval)), Point( (posx - self.length), (self.lowyval)))
        self.greenrect.setFill( 'green' )
        self.redrect = Rectangle( Point( (posx + self.length), (self.topyval)), Point( (posx + self.length), (self.lowyval)))
        self.redrect.setFill( 'red' )
        self.greenrect.draw( win )
        self.redrect.draw( win )
        self.win = win
        self.numrange = numrange
        self.posx = posx
        self.posy = posy
        self.ratio = length / numrange
    
    def update( self, val, posx, posy ):
        
        """Updates the Display Bar

        val        The progress of the bar expressed as an integer
        posx       The new x position of the bar
        posy       The new y position of the bar
        """

        distance = int( val*self.ratio )
        self.greenrect.undraw()
        self.redrect.undraw()

        topyval = posy + self.height
        lowyval = posy - self.height

        self.greenrect = Rectangle( Point( (posx + self.length), (topyval)), Point( (posx - self.length), (lowyval)))
        self.greenrect.setFill( 'green' )
        self.redrect = Rectangle( Point( (posx + (self.length - (2 * distance))), (topyval)), Point( (posx + self.length), (lowyval)))
        self.redrect.setFill( 'red' )
        self.greenrect.draw( self.win )
        self.redrect.draw( self.win )



if __name__ == '__main__':
    win = GraphWin( 'testing' )
    dbar = DispBar( win, 50, 50, 10, 20, 10 )
    for i in range( 1, 6 ):
        p = win.getMouse()
        dbar.update( (i*2), (p.getX()), (p.getY()))
    win.getMouse()
    win.close()
        
        
        
