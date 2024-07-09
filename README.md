# ml_cv
## Problem Solving
### Objective:
Get an appreciation for the candidates communication, logical thinking and problem solving skills under pressure.

### Scenario:
We are capturing conductor images from a small drone. The drone flys along the conductor at a fixed height above it capturing images (one per second) with a camera that points vertically downwards.The drone flys down the conductor at a variable rate (it aims to move at 1 m/s), sometimes slowing down and stopping and sometimes moving faster.  The drone can be affected by the wind as well. We want to get as full as possible coverage of the conductor but want to minimise the number of images we process.  

Here is the information that you have available:

You have the full set of images captured, they each have EXIF data that includes the following:

You know the parameters if the camera capturing the images

You know the drone location (GPS coords and altitude) when it captures the image

the camera angle downwards is assuming to be 90 degrees

You know height of the conductor above ground level

You know the GPS locations of the end points of the conductor

Describe how you would devise an approach to creating the minimum set of images to process.

## MLOps Design Questions
Describe how you would approach designing a processing pipeline that could process a large number of images (1 million) in a single day.

You may use diagrams to support your explanation.

Explain the mechanisms used to scale the compute.

How would you make the design cost effective on days where very few images are required to be processed.

How would you accomodate for “pre-processing” and “post-processing” code in your design.

How would you test the individual components and the pipeline in your design.

How would you design the deployment process to minimise manual operations work. Consider the deployment of application code, models and pipelines.

Important aspects of the machine learning operations process (MLOps) is data management and taxonomy.

Explain how you would go about designing a data management platform using tools you are familiar with for image data, classification and localisation labels.

Explain why it is important to have a data management platform.

Explain why we would want to version control taxonomy, e.g. class labels used for the model.

We train models and keep track of all experiments run in an experiment tracking list.

Sketch a table that shows some of the model attributes/metadata you’d like to keep track of against each model.

Explain why it is important to keep track of experiments.

The following python function iterates through a numpy array and adds 50 to the green channel of each pixel. Explain all the things wrong with the code. Assume the array uses the BGR format.



```def get_greener_image(image_array: np.ndarray) -> np.ndarray:
  for row in image_array:
    for pixel in row:
          pixel[1] += 50
  return image_array
```
## Coding/Testing
### Objective
Clone the given repository and create a new branch for your work

Using the image and single annotation file from the repository, draw the annotation polygon on the image

Create a conductor mask image from the annotation polygon

Write unit tests for your code

### Bonus Objective
Using the image and double annotation file from the repository, merge the annotation polygons so that there is no gap

Draw the merged annotation polygon on the image
