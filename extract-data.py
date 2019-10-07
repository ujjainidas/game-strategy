
"""This file extracts data using the tbapy library from the Blue Alliance API

@author Ujjaini Das
"""

import tbapy

tba = tbapy.TBA("MtsQ8UR2BsMQ03giTxFXqNbP61OyHF1Sy9VNNKbK8UjtBfr8NQfYF7Gbs7XrDkoA")

event_list = tba.events("2019", keys = True)
print(event_list)
