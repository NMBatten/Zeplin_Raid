#by Nathan Batten
#last edited 6/10/21
#notes:
#fix SPAAG rap-around issues
from graphics import *
from zeppelin import Zeppelin
from explosion import Explosion
from bomb import Bomb
from gun import Gun, SPAAG
from bullet import Bullet
from random import randrange
from dispbar import DispBar

class BackGround:

    def __init__( self ):

        self.win = GraphWin( "Use Arrow keys to move" , 600 , 300 , autoflush = False )
        self.win.setBackground( "Sky Blue" )
        self.widthval = 1500
        self._makeClouds()
        
        self.prevx = -150
        self.x = 0
        self.y = 0
        self.win.setCoords( self.prevx , 0 , self.prevx + 300 , 300 )
        self.dispPos()
        self.bomblist = []
        self.exlist = []
        self.gunlist = []
        self.bullets = []
        self.balloons = []
        self.lives = 3
        self.life = self.lives     
        self.zep = Zeppelin( self.win , Point( 0 , 150 ) )
        self.directioncheckval = False
        self._setupGuns( 30 )
        self.bombs = 0
        self.bomblimit = 100
        self.bombsout = False
        self.dbombbar = DispBar( self.win, (self.prevx + 20), 285, 10, 20, self.bomblimit )
        self.dlivesbar = DispBar( self.win, (self.prevx + 20), 250, 10, 20, self.lives )
        
        

    def run( self ):

        self.win.getMouse()

        while True:

            #self.y = -0.10
            key = self.win.checkKey()
            if key == "Up":
                self.y = 0.5
            elif key == "Down":
                self.y = -0.75
            elif key == "Right":
                self.x = self.x + 0.25
            elif key == "Left":
                self.x = self.x - 0.25
            elif key in  ["f",'F']:
                self.makeBomb()
            elif key in [ "q",'Q']:
                self.endmessage = 'You Quit |o|'
                break
            endval = self.update()
            if endval:
                for i in range( 13 ):
                    for e in self.exlist:
                        e.update()
                    update( 30 )
                break

        t = Text( Point( self.prevx + 150, 150 ), self.endmessage )
        t.draw( self.win )
        self.win.getMouse()
        self.win.close()

    def update( self ):

        point = self.zep.getPos()
        zx = point.getX()
        zy = point.getY()
        if zy > 290:
            if self.y > 0:
                self.y = 0
        if zy < 3:
            self._destroy()
            return True
        if self.x > 1:
            self.x = 1
        if self.x < -1:
            self.x = -1
        if self.x == 0:
            self.directioncheckval = True
        elif self.directioncheckval:
            if self.x < 0:
                direction = 1
            else:
                direction = 0
            self.zep.finSwitch( point, direction )

        for e in self.exlist:
            e.update()
            if e.tval > 12:
                self.exlist.remove(e)
            
        alivebomb = []
        for bomb in self.bomblist:
            by = bomb.UpdateBomb()
            if by <= 0:
                bx = bomb.UndrawBomb()
                e = Explosion( self.win, 7, bx, 0 )
                self.exlist.append(e)
                for gun in self.gunlist:
                    if gun.IsIn( bx ):
                        e = Explosion( self.win, 12, bx, 0 )
                        self.exlist.append(e)
                        self.gunlist.remove( gun )
            else:
                alivebomb.append(bomb)
        self.bomblist = alivebomb
        
        if not self.gunlist:
            self.endmessage = "You Win '\o/'"
            return True

        self._FireShots( zx )

        for bullet in self.bullets:
            bpos = bullet.update()
            xp = bpos.getX()
            yp = bpos.getY()
            if ( abs( zx - xp) < 8 ) and ( abs( zy - yp ) < 3 ):
                deathval = self.hit()
                if deathval:
                    self._destroy()
                    return True
                self.bullets.remove( bullet )
                bullet.undraw()
            elif yp > 300:
                self.bullets.remove( bullet )
            if xp < 0:
                bullet.pro.move( self.widthval, 0 )
            elif xp > self.widthval:
                bullet.pro.move( -self.widthval, 0 )

        for balloon in self.balloons:
            if balloon.under( zx, zy ):
                self._destroy()
                return True
                
        
        if self.bombsout and not self.bomblist:            
            self.endmessage = 'You ran out of bombs :('
            return True

        self.prevx += self.x
        update( 45 )
        self.win.setCoords( self.prevx , 0 , self.prevx + 300 , 300 )
        self.zep.move( self.x , self.y )
        if self.zep.getPos().getX() >= self.widthval:
            self.zep.move( -self.widthval, 0 )
            self.prevx = -150
        elif self.zep.getPos().getX() < 0:
            self.zep.move( self.widthval, 0 )
            self.prevx = self.widthval - 150
        self.dispPos()
        self.dbombbar.update( self.bombs, (self.prevx + 20), 285 )
        self.dlivesbar.update( self.lives - self.life, (self.prevx + 20), 250 )
        
        if zy < 150:
            self.y = 0
        else:
            self.y = -0.10
        
    def dispPos( self ):

        try:
            self.t.undraw()
        except:
            pass
        self.t = Text( Point( self.prevx + 20 , 270 ) , f"x: {round(self.prevx + 150 , 4)}" )
        self.t.setSize( 7 )
        self.t.draw( self.win )

    def hit( self ):

        self.life = self.life - 1

        if self.life <= 0:
            self._destroy()
            return True
        else:
            return False

    def makeBomb( self ):

        if self.bombs <= self.bomblimit:

            x = self.zep.getPos().getX()
            y = self.zep.getPos().getY()
            b = Bomb( Point( x, y-4 ), self.x, self.win )
            self.bomblist.append( b )
            self.bombs += 1
        else:
            self.bombsout = True

    def _setupGuns( self, num ):

        for i in range( num ):

            if randrange( 0 , 2 ) == 0:
                g = SPAAG( Point( randrange( 35, self.widthval - 15 ), 0), self.win, 0 )
            else:
                g = Gun( Point( randrange( 35, self.widthval - 15 ), 0), self.win )
            self.gunlist.append(g)

    def _FireShots( self, xpos ):

        for gun in self.gunlist:

            gx = gun.getXPos()
            if abs(xpos - gx) < 200:
                if gun.getType() == 'mobile':
                    if xpos - gx < 0:
                        gun.move( -0.65 )
                    else:
                        gun.move( 0.65 )
                    
                if gun.update():
                    x, y = self._getTrajectory( gx, gun.getType() )
                    b = gun.fire( x, y )
                    self.bullets.append(b)
            else:
                if gun.getType == 'mobile':
                    if abs(xpos - gx) < 500:
                        if (xpos - gx < 0):
                            if self.x >= 0:
                                moveval = -1
                            else:
                                moveval = 1
                        else:
                            if self.x < 0:
                                moveval = 1
                            else:
                                moveval = -1
                    else:
                        if self.x >= 0:
                            moveval = 1
                        else:
                            moveval = -1
                    gun.move( moveval )
            if gx > self.widthval:
                gun.move( -self.widthval )
            elif gx < 0:
                gun.move( self.widthval )

    def _getTrajectory( self, xpos, guntype ):

        p = self.zep.getPos()
        px = p.getX()
        py = p.getY()
        xval = py // 50
        xdifference = px - xpos + self.x * 25 *(py//75)#improve current mobile guns accuracy
        
        yval = xdifference // 100
        return xval, yval
        
        
    def _makeClouds( self ):

        numclouds = randrange( 10, 25 ) #length of colorist 7
        colorlist = [ 'Alice Blue', 'White', 'Cadet Blue', 'Dark Gray', 'White', 'Ghost White', 'Light Steel Blue', 'White' ]
        for i in range( numclouds ):
            rx = randrange( 0, self.widthval )
            ry = randrange( 50, 300 )
            color = colorlist[ randrange( 0, 7 ) ]
            rect = Rectangle( Point( rx, ry ), Point( rx + 25 + randrange( -10, 25 ), ry + 25 + randrange( -10, 15 ) ) )
            rect.setOutline( color )
            rect.setFill( color )
            rect.draw( self.win )

    def _destroy( self ):

        self.life = 0
        p = self.zep.getPos()
        self.zep.UndrawZep()
        e = Explosion( self.win, 10, p.getX(), p.getY() - 3 )
        self.exlist.append( e )
        self.endmessage = "You Died! '/o\'"
        self.dlivesbar.update( self.lives - self.life, (self.prevx + 20), 250 )
        