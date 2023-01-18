"""Define bounding box

Class with functions defining the bounding box of given points.
Comments are provided throughout this module to guide the methodology.
"""

__author__ = 'Cindy Lu'

from os import environ
# change the file path when necessary
environ['PROJ_LIB'] = 'C:\\Users\\W0475753\\.conda\\envs\\prog5000\\Library\\share\\proj'

import csv
import os
import pyproj


class BoundingBox:
    """Class representing the bounding box of a geometry 
    with 2 known points
    """

    def __init__(self, id:str, xmin: float, ymin: float, 
    xmax: float, ymax: float, crs:pyproj):
        """identifier, point coordinates (X, Y) as float data type for
        the bottom left corner (xmin, ymin) and top right corner (xmax, 
        ymax), and CRS of the geometry as pyproj data type
        """
        self.id = id
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self.crs = crs
    
    # Define a class method to pass in class parameters
    @classmethod
    def from_file(cls, filepath, id:str):
        """The method retrieves the parameters for the class
        from a given csv file
        """
        with open (filepath,'r') as csv_file:
            reader = csv.reader(csv_file)
            # skip over the header line in the csv file
            next(reader)
            # retrieve coordinates of 2 points
            for i in reader:
                if i[0] == id:
                    xmin = i[1]
                    ymin = i[2]
                    xmax = i[3]
                    ymax = i[4]
            # retrieve corresponding '.prj' file 
            # based on name of the csv file
            name = os.path.splitext(filepath)[0]
            prj_filepath = name + '.prj'
        with open(prj_filepath, 'r') as prj_file:
            # read the CRS from wkt format in the file
            crs_wkt = prj_file.read()
            crs = pyproj.CRS.from_wkt(crs_wkt)
        return cls(id, xmin, ymin, xmax, ymax, crs)
            
    def transform_to(self, target_crs:pyproj):
        """Apply CRS transformation on the bounding box CRS to 
        another given CRS (target_crs)
        """
        # the transformation is applied only when the targe_crs is
        # different from the bounding box CRS
        if self.crs != target_crs:
            transformer = pyproj.Transformer.from_crs(self.crs, target_crs)
            self.xmin, self.ymin = transformer.transform(self.xmin, self.ymin)
            self.xmax, self.ymax = transformer.transform(self.xmax, self.ymax)
            self.crs = target_crs

    def contains(self, x: float, y: float):
        """Verify if a given point is within the bounding box"""
        if (float(self.xmin) <= x <= float(self.xmax) 
            and float(self.ymin) <= y <= float(self.ymax)):
            return True
        else:
            return False


if __name__ == "__main__":

    None
