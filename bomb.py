from graphics import *

class Bomb:

    def __init__( self, pos, vel, win ):

        self.oblist = []
        self.pos = pos
        self.vel = vel
        self.win = win
        self._makebomb()
        for ob in self.oblist:
            ob.draw( win )
        self.counter = 0       

    def _makebomb( self ):

        x = self.pos.getX()
        y = self.pos.getY()
        circle = Circle( Point( x, y-1 ), 1 )
        circle.setFill( 'black' )
        self.oblist.append(circle)
        rect = Rectangle( Point( x-1, y-1 ), Point( x+1, y+2 ) )
        rect.setFill( 'black' )
        self.oblist.append( rect )

    def UpdateBomb( self ):

        self.counter += 0.05
        for ob in self.oblist:
            ob.move( self.vel * (1- 0.5 * self.counter), self.counter * -7 )
        return self.oblist[1].getCenter().getY()

    def UndrawBomb( self ):
        for ob in self.oblist:
            ob.undraw()
        return self.oblist[1].getCenter().getX()

if __name__ == '__main__':
    win = GraphWin("testing")
    b = Bomb( Point( 100 , 4), 5, win )
    for i in range( 25 ):
        b.UpdateBomb()
        update(60)
    win.getMouse()
    b.UndrawBomb()
    win.close()

