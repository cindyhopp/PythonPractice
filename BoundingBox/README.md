This was the final assignment as part of the Programming Fundamentals for Geographic Sciences course. 

The aim for this assignment was to write a command line application that will determine whether the given points in a CSV file are inside or outside a bounding box. 

Files include:
* [bbox.py](https://github.com/cindyhopp/PythonPractice/blob/main/BoundingBox/bbox.py): module that creates a class to define the bounding box of given points
* [filter.py](https://github.com/cindyhopp/PythonPractice/blob/main/BoundingBox/filter.py): module with command line program that assesses whether points from the location.csv or geolocation.csv are contained in the bounding boxes specified in bounds.csv

The following files were provided by the instructor:
* bounds.csv: contains four bounding boxes
* bounds.prj: contains the CRS of the bounding boxes encoded in WKT
* geolocation.csv: contains coordinates
* geolocation.prj: contains CRS of the geolocation.csv encoded in WKT
* location.csv: contains coordinates
* location.prj: contains CRS of the location.csv encoded in WKT
* bbox_test.py: test case for the BoundingBox class from bbox.py
* source-data.pgkg: GeoPackage dataset containing the points and bounding boxes, for visual aid
