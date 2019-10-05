# AirBnB Barcelona

## Introduction
The first project on the <a href="https://www.udacity.com/course/data-scientist-nanodegree--nd025">Data Science Nanodegree by Udacity</a> consists of analysing a dataset using three initial questions to help the exploration. 


### Steps
The key steps for this project are:
1. Pick a dataset
2. Pose at least three questions related to business or real-world applications of how the data could be used.
3. Create a Jupyter Notebool to prepare, analyze, model and visualize the data.
4. Communicate business insights by creating a Github repository to share code and data wrangling techniques and a blog post to share the questions and insights to non-technical audience.

### The process
The process recommended on the course for this is  <a href="https://www.datasciencecentral.com/profiles/blogs/crisp-dm-a-standard-methodology-to-ensure-a-good-outcome">CRISP-DM</a>, which is an industry standard process for data mining:

* Business Understanding
* Data understanding
* Prepare Data
* Model Data
* Results
* Deploy

### Exploration questions
As part of this project and to help focus the analysis, there are three questions which I'll try to answer using the data avaiable:
1. What makes a listing more profitable?
2. What are the key features that generate better reviews?
3. 

## Quick overview of the content

<i>(TODO - Table of content)</i>

### Chosen Data set: Barcelona AirBnB provided on July 2019

I decided to choose the Barcelona <a href="http://insideairbnb.com/get-the-data.html">AirBnB dataset</a> (with the help of the course's menthor as I couldn't decide!) mainly because I studied there (quite a while ago) and it'd be a really interesting dataset which I could relate to.

### Files
* AirBnB-BCN-July2019Extract-Analysis jupyter notebook
* Data files

#### Data
I opted for creating a folder named "data" with all the different datasets downloaded from AirBnB (some in gz format):

* <b>calendar.csv</b>: which contains detailed calendar data for listings in Barcelona
* <b>listings.csv</b>: which contains summary information and metrics for listings in Barcelona (good for visualizations)
* <b>listings.csv.gz</b>: which contains detailed listings
* <b>neighbourhoods.csv</b>: which is a list of geo filter, sourced from city or open source GIS files
* <b>reviews.csv</b>: Summary Review data and Listing ID (to facilitate time based analytics and visualisations linked to a listing).
* <b>reviews.csv.gz</b>: Detailed Review Data for listings in Barcelona

## CRISP-DM on this dataset

### Business Understanding
AA‌i‌r‌b‌n‌b‌, ‌ ‌I‌n‌c‌.‌ is an online marketplace for arranging or offering lodging, primarily homestays, or tourism experiences. The company does not own any of the real estate listings, nor does it host events; it acts as a broker, receiving commissions from each booking. <i>Extracted from <a href="https://en.wikipedia.org/wiki/Airbnb">Wikipedia</a></i>.

### Data loading and wrangling
With any dataset, we need to explore to find areas where data is missing, incomplete or requires modification (such as data types). This also helps understand the data, what it contains and guide our exploration. As part of this section, I made a decision of which files would be used for the analysis:
* Calendar
* Listings

On this section, I looked for data which was missing or outlyers which could represent incorrect data on pricing as well as correcting data types to help with the analysis.

### Data Analysis



