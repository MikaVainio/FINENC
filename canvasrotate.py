# QGIS-kartan kiertäminen ohjelmallisesti

# Määritellään karttaikkuna (canvas)
canvas = iface.mapCanvas()

# Kierretään karttaikkunaa 30 astetta myötäpäivään
canvas.rotate(30)

# Kierretään karttaikkunaa 30 astetta vastapäivään
canvas.rotate(-30)
