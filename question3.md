**Question 3**
Download a week of PM2.5 dataset from the OpenAQ website for Delhi. Fill in the missing data with appropriate methods. Use i) the sklearn Random Forest regressor; ii) sklearn Linear regression and iii) Gaussian process regressor to interpolate the PM2.5 values across the space. Use all the available features that you can get from the OpenAQ website or elsewhere (e.g., meteorological variables). Compare the results and prepare a table showing the metrics in K-Fold cross-validation setting.

**Procedure** 
I tried downloading the data set from https:/www.openaq.org/. The dataset parameters are not matching. All the 5 fits failed. 

Trial 2
This Python code uses the requests, json, and pandas libraries to download air quality data for PM2.5 particles from the OpenAQ API for the city of Delhi in India.
The code defines the url and params variables to specify the API endpoint and parameters for the data request. The requests.get() function is used to send a GET request to the API, and the resulting response is checked for success using the response.status_code attribute.
If the response is successful, the JSON data is parsed using the json.loads() function and converted to a Pandas DataFrame using the pd.json_normalize() function. The resulting DataFrame is saved to a CSV file named delhi_pm25.csv using the df.to_csv() method.
If the response is unsuccessful, an error message is printed indicating the HTTP status code.
Notable features of the code include the use of the requests library to interact with the OpenAQ API, the parsing of JSON data into a Pandas DataFrame using pd.json_normalize(), and the saving of the resulting DataFrame to a CSV file using df.to_csv().
It is not specified where the open aqi data is taken from within the code, but it is known that the data pertains to air quality measurements for PM2.5 particles in Delhi, India.

Website used here: https://api.openaq.org/v1/measurements

Link: https://colab.research.google.com/drive/16Cc2EYT4sYoOC8w-XbjcnpuFfy_IxagV?usp=sharing
