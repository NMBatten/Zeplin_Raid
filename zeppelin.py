from graphics import *

class Zeppelin:

    def __init__( self , win , point ):

        self.win = win
        x = point.getX()
        y = point.getY()
        self.objects = []
        self.DrawZep( x, y, 0 )        

    def DrawZep( self, x, y, direction ):

        win = self.win
        if not direction:#direction 0 means facing left
            self.fin = Rectangle( Point( x - 6 , y - 6 ) , Point( x - 9 , y + 6 ) )
            self.fin.setOutline( "red" )
            self.fin.setFill( "red" )
            self.fin.draw( win )
        else:
            self.fin = Rectangle( Point( x + 6 , y - 6 ) , Point( x + 9 , y + 6 ) )
            self.fin.setOutline( "red" )
            self.fin.setFill( "red" )
            self.fin.draw( win )
        self.objects.append( self.fin )
        fcircle = Circle( Point( x + 3 , y ) , 6 )
        fcircle.setFill( "blue" )
        fcircle.setOutline( "blue" )
        fcircle.draw( win )
        self.objects.append( fcircle )
        bcircle = Circle( Point( x - 3 , y ) , 6 )
        bcircle.setFill( "blue" )
        bcircle.setOutline( "blue" )
        bcircle.draw( win )
        self.objects.append( bcircle )
        self.rect = Rectangle( Point( x - 6 , y - 6 ) , Point( x + 6 , y + 6 ) )
        self.rect.setFill( "blue" )
        self.rect.setOutline( "blue" )
        self.rect.draw( win )
        self.objects.append( self.rect )

    def move( self , xval , yval ):

        for ob in self.objects:
            ob.move( xval , yval )

    def getPos( self ):

        return self.rect.getCenter()

    def UndrawZep( self ):

        for ob in self.objects:
            ob.undraw()

    def finSwitch( self, point, direction ):        

        self.UndrawZep()
        self.DrawZep( point.getX(), point.getY(), direction )
