import arcpy

def exp():
    grupos = ["03 MUN AGS","01 GEOPOLITICO"]
    capas = ["Crecimiento historico de la ciudad de Ags.","Limite municipal","Perimetro de Contencion Urbana 2018"
                 ,"Delegaciones","Centro historico","Zonas de focalizacion urbana"]
    expmapa(grupos,capas)