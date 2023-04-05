#import libraries

import topologicpy
import topologic
from topologicpy.Vertex import Vertex
from topologicpy.Face import Face
from topologicpy.CellComplex import CellComplex
from topologicpy.Cluster import Cluster
from topologicpy.Topology import Topology
from topologicpy.Plotly import Plotly

#create podium

#parameters
podL = 20          #PodiumLength
podW = 60          #PodiumWidth
podWsplit = 4      #PodiumWidthSplit
PodLsplit = 4      #PodiumLengthSplit
podFlrHt = 4       #PodiumFloorHeight
PodNoOfFlr = 4     #No.ofFloors
coreL = 6               #CoreLength         
coreW = 6              #CoreWidth
PodscaleF = 0.5           #PodscaleFactor
altWindowBool = True

# create single floor
sinPodFlr = CellComplex.Box(width=podW, length=podL, height=4, 
                            uSides=podWsplit, vSides=PodLsplit, wSides=1, placement = 'bottom')

# Decomposing the model
DecPodDict = CellComplex.Decompose(sinPodFlr)
# extracting vertical external surfaces from Dictionary
PodExtVerFaces = DecPodDict['externalVerticalFaces']
# PodTopHorFaces = DecPodDict['topHorizontalFaces']
# PodBotHorFaces = DecPodDict['bottomHorizontalFaces']
# PodIntVerFaces = DecPodDict['internalVerticalFaces']
# PodIntHorFaces = DecPodDict['internalHorizontalFaces']

#Window
extWindow = []
# Iterating through all external faces
for eachExtFace in PodExtVerFaces:                                                         
    centre = Topology.Centroid(eachExtFace)                                     #centre of each faces
    extWindow.append(Topology.Scale(eachExtFace, centre, 
                                    x = PodscaleF, y= PodscaleF, z=PodscaleF))                   # scaling external faces

# Subtracting windows from walls
cluPodAper = Cluster.ByFaces(extWindow)
aperExtWall = Topology.Boolean(sinPodFlr, cluPodAper, operation = 'difference', 
                                                   tranDict=True, tolerance= 0.0001)


# Visualise geometry
geo = Plotly.DataByTopology(aperExtWall)
plotfig1 = Plotly.FigureByData(geo)
Plotly.Show(plotfig1, renderer = 'notebook')