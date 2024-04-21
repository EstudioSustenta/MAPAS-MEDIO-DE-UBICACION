# -*- coding: utf-8 -*-

import sys

# Agrega la ruta del paquete al path de Python
ruta_libreria = "Q:/09 SISTEMAS INFORMATICOS/GIS_PYTON/SOPORTE_GIS/LIBRERIA"
sys.path.append(ruta_libreria)
import MAPAS
reload(MAPAS)

MAPAS()


