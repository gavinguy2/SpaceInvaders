import pygame
import game_mouse
import spaceinvaders

class PygameApp( game_mouse.Game ):

    def __init__( self, width, height, frame_rate ):

        # title of the application is ""
        game_mouse.Game.__init__( self, "Space Invaders",
                                  width,
                                  height,
                                  frame_rate )
        # create a game instance
        self.mGame = spaceinvaders.SpaceInvaders( width, height )
        return
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        if pygame.K_a in keys:
            self.mGame.moveTurretLeft()
        
        if pygame.K_d in keys:
            self.mGame.moveTurretRight()

        if pygame.K_SPACE in newkeys:
            self.mGame.fireTurret()

        self.mGame.refresh( dt )

        return
    
    def paint( self, surface ):
        self.mGame.draw( surface )
        return

def main():
    pygame.font.init( )
    game = PygameApp( 700, 550, 60 )
    game.main_loop( )
    
if __name__ == "__main__":
    main()
