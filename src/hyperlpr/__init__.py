name = "hyperlpr_python_pkg"
import sys
from .hyperlpr import LPR
import os


def HyperLPR_plate_recognition(
    Input_BGR, minSize=30, charSelectionDeskew=True, region="CH"
):
    folder = os.path.join(os.path.split(os.path.realpath(__file__))[0], "models")
    PR = LPR(folder)
    return PR.run(Input_BGR, minSize, charSelectionDeskew)
