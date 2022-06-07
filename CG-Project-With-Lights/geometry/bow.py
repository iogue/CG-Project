from geometry.cylinder import CylinderGeometry
from core_ext.mesh import Mesh
from material.surface import SurfaceMaterial
from geometry.handle import HandleGeometry
from core_ext.texture import Texture
from material.texture import TextureMaterial
from material.flat import FlatMaterial


class BowMesh(Mesh):
    def __init__(self):
        geometry = HandleGeometry(height=10, height_segments=10, radius_bottom=0.5, radius_top=0.5)
        geometry1 = CylinderGeometry(radius=0.1,height=9.5,radial_segments=16,height_segments=1)
        
        material = FlatMaterial(texture=Texture(file_name="images/wood.jpeg"), property_dict={"baseColor":[1, 1, 1]})
        self.mesh = Mesh(geometry=geometry,material=material)
        super().__init__(geometry, material)


        material1 = FlatMaterial(texture=Texture(file_name="images/string.jpg"), property_dict={"baseColor":[1, 1, 1]})
        self.mesh1 = Mesh(geometry1, material1)
        self.add(self.mesh1)
        self.rotate_y(1.57)
        self.scale(0.3)