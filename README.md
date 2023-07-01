# spatial_pathomics
Spatial pathomics toolbox


## Segmentation and Load  annoation 

First, get the annotation information by, for example, annotating and exporting it to a geojson file in QuPath. Alternatively, consider automated tools [Omni-seg](https://github.com/ddrrnn123/Omni-Seg).

<img src='/doc/demo0.png' align="center" height="200px"> 

## Mask Image

To generate a mask, run
```
python mask_image.py /image.png /annotation.geojson
```

<img src='/doc/demo1.png' align="center" height="200px"> 

## Features extraction in cellprofiler

Open feature_extract.cpproj in CellProfiler, and extract features by loading 'masked_imag.jpg'.

<img src='/doc/demo2.png' align="center" height="200px"> 


## Feature Analysis
