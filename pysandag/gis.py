"""
GIS utility functions commonly used at SANDAG.
"""
from osgeo import ogr, osr

# Setup State Plane to WGS Transformation
source = osr.SpatialReference()
source.ImportFromEPSG(2230)

target = osr.SpatialReference()
target.ImportFromEPSG(4326)
transform = osr.CoordinateTransformation(source, target)


def transform_wkt(geom_wkt):
    """
    Transform a well-known text geometry from California
    State Plane Coordinate System (EPSG:2230) to a well-
    known text geometry in Web Mercator Longitude /
    Latitude (EPSG: 4326)

    Args:
        geom_wkt (Well-Known Geometry String): Well-known
            text geometry from California State Plane
            Coordinate System (EPSG:2230)

    Returns:
        string: Extended (PostGIS) well-known text (EWKT)
            geometry in Web Mercator Longitude / Latitude
            (EPSG: 4326)
    """
    geom_binary = ogr.CreateGeometryFromWkt(geom_wkt)
    geom_binary.Transform(transform)
    return "SRID=4326;" + geom_binary.ExportToWkt()
