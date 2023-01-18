"""Assess and filter if points in a given .csv file are contained  
within a bounding box. The feature CRS is required if different from 
the CRS of the bounding box file, and should be stored as a .prj file
in the same folder directory and same name as the .csv file.

E.g. A 'location.csv' should have a corresponding 'location.prj' file,
and both nested in the same folder directory.
"""

__author__ = 'Cindy Lu'

from os import environ
# change the file path when necessary
environ['PROJ_LIB'] = 'C:\\Users\\W0475753\\.conda\\envs\\prog5000\\Library\\share\\proj'

import argparse
import csv
import os
import pyproj
import bbox


# create an argument parser
parser = argparse.ArgumentParser(
    description = 'Parse user input arguments')

# 2 arguments input by user, see help for description
parser.add_argument('bbox_id', type = str,
    help = 'The identifier of the bounding box')
parser.add_argument('filename', type = str,
    help = 'The filename of the points file, input to include .csv extension')

# parse the arguments
args = parser.parse_args()

# define file location of the bounding box file
bbox_file = 'D:\\PROG5000\\Python\\Assignment3\\bounds.csv'

# ensure the bounding box identifier exists in the bounding box file
try:
    # retrieve the parameters for the bounding box based on bbox_id
    parameter = bbox.BoundingBox.from_file(bbox_file, args.bbox_id)

    # retrieve the CRS file corresponding to the points file
    name = os.path.splitext(args.filename)[0]
    prj_filename = name +'.prj'

    # ensure the points file and its corresponding .prj file is valid
    try:
        # read the CRS from wkt format in the file
        with open(prj_filename, 'r') as prj_file:
            point_crs_wkt = prj_file.read()
            point_crs = pyproj.CRS.from_wkt(point_crs_wkt)

        # apply CRS transformation by calling transform_to() function
        bbox.BoundingBox.transform_to(parameter, point_crs)

        # read the points file and determine whether the points are 
        # inside of the bounding box using the contains() function
        with open(args.filename, 'r') as point_file:
            reader = csv.reader(point_file)
            for i in reader:
                x = float(i[0])
                y = float(i[1])
                point_name = i[2]
                if bbox.BoundingBox.contains(parameter,x,y) is True:
                    print(f'Bounding box {args.bbox_id} contains {point_name}')
                else:
                    pass
    # if points file is not valid, print error message
    except FileNotFoundError:
        print(f'{args.filename} file or corresponding .prj file'
            + f' not found. Please ensure .csv is included in your' 
            + f' input, check spelling or directory.')

# if bounding box is invalid, print error message
except UnboundLocalError:
    print(f'{args.bbox_id} does not exist.')
