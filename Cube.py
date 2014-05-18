#mae esto es una prueba para ver si esto sirve



#draw cube
import sys, math, pygame
yellow=(255,238,0)									  
blue=(0,107,179)
darkBlue=(24,41,131)
lightBlue=(0,157,226)
fuchsia=(255,0,128)
purple=(147,17,126)
orange=(255,153,51)
lightRed=(227,0,79)
red=(227,0,35)
pink=(225,0,122)
lightGreen=(151,190,13)
green=(0,145,54)
white=(255,255,255)
black=(0,0,0)
class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)

    def rotateX(self, angle):
        """ Rotates the point around the X axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        y = self.y * cosa - self.z * sina
        z = self.y * sina + self.z * cosa
        return Point3D(self.x, y, z)

    def rotateY(self, angle):
        """ Rotates the point around the Y axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        z = self.z * cosa - self.x * sina
        x = self.z * sina + self.x * cosa
        return Point3D(x, self.y, z)

    def rotateZ(self, angle):
        """ Rotates the point around the Z axis by the given angle in degrees. """
        rad = angle * math.pi / 180
        cosa = math.cos(rad)
        sina = math.sin(rad)
        x = self.x * cosa - self.y * sina
        y = self.x * sina + self.y * cosa
        return Point3D(x, y, self.z)

    def project(self, win_width, win_height, fov, viewer_distance):
        """ Transforms this 3D point to 2D using a perspective projection. """
        factor = fov / (viewer_distance + self.z)
        x = self.x * factor + win_width / 2
        y = -self.y * factor + win_height / 2
        return Point3D(x, y, 1)

class Simulation:
    def __init__(self, win_width = 640, win_height = 480):
        pygame.init()

        self.screen = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("3D Wireframe Cube Simulation (http://codeNtronix.com)")

        self.clock = pygame.time.Clock()

        self.vertices = [
            Point3D(-1,-1,-1),
            Point3D(-1,1,-1),
            Point3D(1,1,-1),
            Point3D(1,-1,-1),
            Point3D(-1,1,1),
            Point3D(1,1,1),
            Point3D(1,-1,1),
            Point3D(-1,-1,1)
            ]

        self.vertices2 = [
            Point3D(-1,-1,-1),
            Point3D(-1,0,-1),
            Point3D(0,0,-1),
            Point3D(0,-1,-1),
            Point3D(-1,0,0),
            Point3D(0,0,0),
            Point3D(0,-1,0),
            Point3D(-1,-1,0)
            ]


        self.vertices3 = [
            Point3D(0,-1,-1),
            Point3D(0,0,-1),
            Point3D(1,0,-1),
            Point3D(1,-1,-1),
            Point3D(0,0,0),
            Point3D(1,0,0),
            Point3D(1,-1,0),
            Point3D(0,-1,0)
            ]

        # Define the vertices that compose each of the 6 faces. These numbers are
        # indices to the vertices list defined above.
        self.faces = [(0,1,2,3),(0,1,4,7),(4,5,6,7),(7,6,3,0),(5,6,3,2)]
        


        self.angleX, self.angleY, self.angleZ = 0, 0, 0

    def run(self):
        """ Main Loop """
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:       
                    sys.exit()

            self.clock.tick(50)
            self.screen.fill((0,0,0))

            # Will hold transformed vertices.
            t = []
            

            for v in self.vertices:
                # Rotate the point around X axis, then around Y axis, and finally around Z axis.
                r = v.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
                # Transform the point from 3D to 2D
                p = r.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
                # Put the point in the list of transformed vertices
                t.append(p)
                x, y = int(p.x), int(p.y)
                self.screen.fill((255,255,255),(x,y,2,2))


             

            for f in self.faces:
                pygame.draw.line(self.screen, (255,255,255), (t[f[0]].x, t[f[0]].y), (t[f[1]].x, t[f[1]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[1]].x, t[f[1]].y), (t[f[2]].x, t[f[2]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[2]].x, t[f[2]].y), (t[f[3]].x, t[f[3]].y))
                pygame.draw.line(self.screen, (255,255,255), (t[f[3]].x, t[f[3]].y), (t[f[0]].x, t[f[0]].y))


           
           #speed which dice moves on each axis:
            self.angleX += 4
            self.angleY += 4
            self.angleZ += 4

            pygame.display.flip()

if __name__ == "__main__":
    Simulation().run()
