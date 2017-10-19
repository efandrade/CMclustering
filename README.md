# CMclustering

This contains several functions used to implement unsupervised learning algorithm k-means clustering as well as a weighted version of k-means clustering where the coordinates have a weight (or mass) associated with them.

<<<<<<< HEAD
Functions: 

### normalize
Returns normalizes data set from 0 to 1

### threshBackground
Returns coordinated from a given data set that have weighted (mass) values above some specified threshold

### initialCentroids
Returns the position of a specified number of centroids located on randoms points of the given data

### centroidIdx
Returns and index for which centroid is closest to each point with or without a weighted value factored in

### newCentroid
Returns new centroid locations calculated from the center of mass for the points assigned to their respective original centroid

=======
### Prerequisites

You will need to have the following libraries installed:
* numpy
* random

### Installing

Download CMclustering.py script and load

```
import CMclustering
```

### Using pycpselect

Functions: 

* **normalize** - Returns normalized data set from 0 to 1

* **threshBackground** - Returns coordinated from a given data set that have weighted (mass) values above some specified threshold

* **initialCentroids** - Returns the position of a specified number of centroids located on randoms points of the given data

* **centroidIdx** - Returns an index labeling which centroid is closest to each point with or without a weighted value factored in

* **newCentroid** - Returns new centroid locations calculated from the center of mass for the points assigned to their respective original centroid
>>>>>>> 0b802186cd56a3025aefeebebb0e87b862d57860
