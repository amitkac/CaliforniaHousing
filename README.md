


[![License](https://poser.pugx.org/ali-irawan/xtra/license.svg)](https://poser.pugx.org/ali-irawan/xtra/license.svg)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-373/)


# Visualizing California housing dataset on open-map API
 Before you go ahead with the setup, check this cool image out. This is the magic of ` Holoviews -Bokeh` plot.
 
![](img/Screen2.png)


## Table of contents
* [General info](#general-info)
* [Prerequisites](#technologies)
* [Setup](#setup)
* [Sample output](#sample-output)

## General info
This is a simple modular python code that uses open street maps to plot lat-long of California housing dataset. 
The output is rendered instantly on your default browser and a html file is saved in your directory as `CaliPlot.html` page to visualize it later.
Also, the plot be saved as `.svg` or `.png`. 

So, what exactly is Akaike Information Criteria (AIC)? especially AIC_c (AIC corrected). For that, check out these cool resources:
*  Wikipedia- (https://en.wikipedia.org/wiki/Akaike_information_criterion)
*  Data Science- (https://www.statisticshowto.datasciencecentral.com/akaikes-information-criterion/)

The overall basic idea is to estimate the given distribution parameters using **MLE**, plot the corresponding pdf, and then find out how close is the estimated ditribution close to real distribution using the AIC metric.
	
## Technologies
Project is created with:
* python: 3.x
* Holoviews-bokeh: install with ```python $conda install holoviews ```
* Pandas: install with ```$conda install pandas```
* six, tarfile
* Scipy 
* Numpy
	
## Setup
To run this project, download the repository to any folder. Open the folder and run the following commands from command line:
```
$python3 mainCaliCall.py 


By default, it will read 1<sup>st</sup> column, and will skip 1<sup>st</sup> row as a header. Here is the sample cmd:



## Sample output

The output `Bokeh Plot` as an `.html` should look like the below image,  with all the distribution plots. Now, don't forget to try `Pan`, `Box Zoom`, and **my favorite** ` Wheel Zoom`.  Check out the cool `.gif` below, where wheel zooming the data changes all the fitted distributions, and thus removing the need to recode your data.






