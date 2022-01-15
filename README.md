# Linear_Regression_Curve
Uses Image processing to create a linear regressive curve fit of data taken from a image file. The app also extracts the function of the fitted curve.

Motivation:
While working in an R&D lab an engineer was using old data acquisition software from an electronic transducer signal. The setup had not been used in years and the technician who set the data test bench up had retired. The engineer brought it to me and asked if I could use excel or MatLAB to find the function that fit the messy data. I used that software, but decided it would be fun to make a little app that could solve all kinds of function types. I also wanted brush up on my python knowledge and make a cool little app. This is the result of that conversation. 

Details: The data used for this app demonstration work well with linear, quadratic, and polynomial curve fits. The using the correct guess parameters the app linear curve fit is able to come up with semi-accuracte predictions, but when using the logarithmic base function the curve fit is unable to find a good prediction function. This is because the data does not follow a easily discovered logarithmic function. 

Switching data: The image used to extract data must have a unique or easily identified color. If using your own data, switch the data set in lines 12-17 in the app or lines 11-16 from the jupyter notebook. Use lines 38-39 from the app code or line 29-30 from the jupyter notebook to find the unique pixel color values in your image so you can extract the relevant pixel locations. 

Link to app code: https://github.com/BenPortz/Linear_Regression_Curve_Fit/blob/main/main.py
Link to jupyter notebook: https://github.com/BenPortz/Linear_Regression_Curve_Fit/blob/main/Linear_regression_curve_app.ipynb
