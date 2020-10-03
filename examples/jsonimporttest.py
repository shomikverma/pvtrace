import json
from sys import argv
from tap import Tap

class MyTap(Tap):
    shape: str = 'Box'
    STLfile: str = ''
    dimX: float = 5.0
    dimY: float = 5.0
    dimZ: float = 1.0
    PVedgesLRFB: bool = [False, False, False, False]
    bottomMir: bool = False
    bottomScat: bool = False
    lumophore: str = "Lumogen Red"
    lumophoreConc: int = 200
    waveguideAbs: int = 0.2
    lightPattern: str = "Rectangle Mask"
    lightDimX: float = dimX
    lightDimY: float = dimY
    lightWavMin: int = 400
    lightWavMax: int = 800
    lightDiv: int = 0
    maxRays: int = 1000
    convThres: float = 1e-3
    convPlot: bool = False
    wavMin: int = 300
    wavMax: int = 900
    enclBox: bool = False
    showSim: bool = True
    saveFolder: str = ''
    figDPI: int = 300
    resultsFileName: str = 'LSC_results'
    inputsFileName: str = 'LSC_inputs'



args = MyTap()
args.load(argv[1])
print(args)
