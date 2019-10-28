# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:45:45 2019

@author: Ujjaini Das
"""
import tbapy
import pandas as pd

tba = tbapy.TBA("MtsQ8UR2BsMQ03giTxFXqNbP61OyHF1Sy9VNNKbK8UjtBfr8NQfYF7Gbs7XrDkoA")

alliances = tba.event_alliances('2019txdel')

print(alliances)
