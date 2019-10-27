# AirBnB Barcelona
Ai‌r‌b‌n‌b‌, ‌ ‌I‌n‌c‌.‌ is an online marketplace for arranging or offering lodging, primarily homestays, or tourism experiences. The company does not own any of the real estate listings, nor does it host events; it acts as a broker, receiving commissions from each booking. <i>Extracted from <a href="https://en.wikipedia.org/wiki/Airbnb">Wikipedia</a></i>.

## Project Motivation
Using the recommended <a href="https://www.datasciencecentral.com/profiles/blogs/crisp-dm-a-standard-methodology-to-ensure-a-good-outcome">CRISP-DM</a> methodology on the <a href="https://www.udacity.com/course/data-scientist-nanodegree--nd025">Data Science Nanodegree by Udacity</a>, we analyse the AirBnB Barcelona July 2019 dataset, focusing on the following 3 aspects:

1) Is the price affected by the location?
2) Which locations receive the most reviews? What is the split between accomodation type and its reviews? What's the top reviewed property?
3) Can we predict the mean price or avg reviews based on seasonality?

## Files

* <b><a href="AirBnB-BCN-July2019Extract-Analysis.ipynb">AirBnB-BCN-July2019Extract-Analysis</a></b> jupyter notebook.
* Data files contained within the "data" folder. These files were downloaded from <a href="http://insideairbnb.com/get-the-data.html">insideairbnb.com</a>:

    * <b>calendar.csv</b>: which contains detailed calendar data for listings in Barcelona
    * <b>listings.csv</b>: which contains summary information and metrics for listings in Barcelona (good for visualizations)
    * <b>listings.csv.gz</b>: which contains detailed listings
    * <b>neighbourhoods.csv</b>: which is a list of geo filter, sourced from city or open source GIS files
    * <b>reviews.csv</b>: Summary Review data and Listing ID (to facilitate time based analytics and visualisations linked to a listing).
    * <b>reviews.csv.gz</b>: Detailed Review Data for listings in Barcelona

## Installation
Anaconda, python 3.7, 
pandas, numpy, matplotlib.pyplot, seaborn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import r2_score

## Summary of findings:

### 1) Is the price affected by location?
Yes, it is. Looking at the mean price per neighbourhood group we can see that there are some locations which prices are higher than others:

<img src="assets/mean-price-barrio.png"
     alt="AirBnB Barcelona 2019 - avg price per barrio"
     style="margin-right: 10px;" />

This is also seen when plotted by phisical location:

<img src="assets/price-location-heatmap.png"
     alt="AirBnB Barcelona 2019 - map"
     style="margin-right: 10px;" />

Even when plotting by room type, we also observe certain areas which are "hotter" than others.

<img src="assets/price-location-heatmap-facet.png"
     alt="AirBnB Barcelona 2019 - map by room type"
     style="margin-right: 10px;" />

Being the top 2 locations: Eixample and Gracia.

### 2) Which locations receive the most reviews? What is the split between accomodation type and its reviews? What's the top reviewed property?

The top 3 most reviewed areas are Sants-Montjuic, Eixample and Gracia.

On average, entire homes recieve more reviews than other "room types", having:

* 36 reviews on average per entire home
* 30 reviews on average per private room
* 18 reviews on average per shared room

The listing that has the most reviews is a Private room located in Ciutat Vella with a total of 645 reviews on the dataset, an average of 8 reviews per month and an average price of €50.

### 3) Can we predict the mean price or avg reviews based on seasonality?

Looking at the mean price over time, we can visually see some trends (probably weekends) and a couple of spikes which probably relate to Christmas and Easter holidays.

<img src="assets/mean-price-over-time.png"
     alt="AirBnB Barcelona 2019 - mean price over time"
     style="margin-right: 10px;" />

When we decompose the signal, we can see a little better the different trends within the data:

<img src="assets/mean-price-decompose.png"
     alt="AirBnB Barcelona 2019 - price decompose trend"
     style="margin-right: 10px;" />


Focusing exclusively on time, price and neighbourhood groups, a polynomial linear regression model will give the 75.6% using 50% sample.

<img src="assets/poly-regre-price-time.png"
     alt="AirBnB Barcelona 2019 - mean price Actual vs Predicted"
     style="margin-right: 10px;" />

We could look more in detail about all the features the listings have (such as TV, internet, etc) but with this simple model, we could obtain a simple prediction model that woudn't fall too far from reality.

## Credits
As with anything code related, thanks to stack over flow, dozens of bloggers who write their experience, python documentation online, and of course, google search engine for making access to those only few clicks away.