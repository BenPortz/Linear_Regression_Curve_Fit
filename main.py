#import python libraries
import numpy as np
from skimage import io
import cv2 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit
import streamlit as st

st.header("Linear Regression Curve Fit App")
#call the picture that you want to extract data from
url = "https://staff.washington.edu/corey/pine-stats/combinedT.gif"

#extract the RGB pixel values
image = io.imread(url)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
st.image(image)
# st.subheader("This app was made to showcase this feature. The upload image below shows how the app could work if implemented to allow users to input their own .jpeg, .png, and .gif files ")

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#      # To read file as bytes:
#      uploaded_image = uploaded_file.getvalue()
# Check the height of image 
# st.write(image.shape[0])
 # Check the width of image 
# st.write(image.shape[1])
 # Check the number of channels of the image
# st.write(image.shape[2])

#name the image array
image_array = np.array(image)
# image_array.shape

#Extract the data points. In our picture, our data is red so we only extract values that are not black or white. (0,0,0) or (255,255,255)
st.markdown("Pictures are rendered using their RGB values. If we run the following line we can identify the types of colors that are used to create the above data image. Using these values this app is able to extract the data from the picture above.")
st.code("Pixel_Colors = np.unique(image_array.reshape((480*640, 3)), axis=0)")
Pixel_Colors = np.unique(image_array.reshape((480*640, 3)), axis=0)
st.write(Pixel_Colors)
y_arr, x_arr = np.where((image_array[:,:,0] == 0) & (image_array[:,:,1]==0) & (image_array[:,:,2]==255))
points = np.array([x_arr, y_arr])

#Verify the shape of the data. Then flip the data invert the x values to correctly arrange the array.
# points.shape
r_x_arr= x_arr[::-1]

#print the data to ensure that the data was extracted correctly.
Corrected_points = np.array([r_x_arr, y_arr])
plt.scatter(Corrected_points[0, :], Corrected_points[1, :]) 
plt.ylabel('Dependent Variable')
plt.xlabel('Indepdendent Variable')
plt.show()

st.subheader("Function Selection")
st.markdown("The app needs the user to declare a function type for the given data. Ex. Linear, Cubic, Polynomial, Exponential, or Logarithmic.")
st.latex(r''' 
y=  c_0 x^3 +c_1 x^2+c_2 x+c_3
''')

option = st.selectbox(
     'What function best fits the data?',
     ('Linear', 'Quadratic', 'Polynomial', 'Exponential','Logarithmic'))

st.write(option,' selected:')
if option == "Linear":
  st.latex(r'''
  y=  c_0 x+c1
  ''')
  st.markdown("Using a linear function the app is able to come up with similar predictions regardsless of the initial coefficient guesses. The prediction is very accurate from x = 400 to x = 500 ")
  #define the type of equation
  c0 = st.slider('Value of constant C0', min_value=-10, max_value=10, value=4, step=2)
  c1 = st.slider('Value of constant C1', min_value=-5,max_value=5, value=1, step=1)
  c2 = 0
  c3 = 0
  def bpm(x,c0,c1,c2,c3):
    return c0*x +c1+c2+c3

elif option == "Quadratic":
  st.latex(r'''
  y=  c_0 x^2+c_1 x+c_2
  ''')
  st.markdown("When using a quadratic base function the app again is able to find a similar solution regardsless of the initial coefficient guesses. The prediction is accurate for the given data around x = 300 to x = 400 and x = 500 to x = 550")
  #define the type of equation
  c0 = st.slider('Value of constant C0', min_value=-10, max_value=10, value=2, step=2)
  c1 = st.slider('Value of constant C1', min_value=-1.0,max_value=1.0, value=0.04, step=0.01)
  c2 = st.slider('Value of constant C2', -80,80, value=45, step=5)
  c3 = 0
  def bpm(x,c0,c1,c2,c3):
    return c0*x**2+c1*x+c2+c3

elif option == "Polynomial":
  st.latex(r'''
  y=  c_0 x^3+c_1 x^2+c_2 x+c_3
  ''')
  st.markdown("A polynomial function fits the data with high accuracy. The solver is able to use iterative methods to find the accurate data function within the given coefficient guess ranges.")
  #define the type of equation
  c0 = st.slider('Value of constant C0', min_value=-20, max_value=20, value=2, step=2)
  c1 = st.slider('Value of constant C1', min_value=-10,max_value=10, value=1, step=1)
  c2 = st.slider('Value of constant C2', min_value=-10,max_value=10, value=5, step =1)
  c3 = st.slider('Value of constant C3', min_value=-100,max_value=150,value=100, step=10)
  def bpm(x,c0,c1,c2,c3):
    return c0*x**3 +c1*x**2+c2*x**1+c3

elif option == "Exponential":
  st.latex(r'''
  y=  c_0 e^{c_1 x}+c_2
  ''')
  st.markdown("An exponential base function gives interesting results when using different coefficient guesses. Try altering the values to see how the app tries to fit the data when constrained to exponential functions.")
 #define the type of equation
  c0 = st.slider('Value of constant C0', min_value=-10, max_value=10, value=4, step=2)
  c1 = st.slider('Value of constant C1', min_value=-1.0,max_value=1.0, value=0.04, step=0.01)
  c2 = st.slider('Value of constant C2', -80,80, value =80, step =5)
  c3 = 0
  def bpm(x,c0,c1,c2,c3):
    return c0*np.exp(c1*x)+c2+c3
  
else:
  #this block is for Logarithmic functions
  st.latex(r'''
  y=  log(c_0 x)+c_1
  ''')
  st.markdown("Using a logarithmic function results in a inaccurate curve fit with this given data. Notice how using a negative c0 value results in no output since the function is undefined.")

  #define the type of equation
  c0 = st.slider('Value of constant C0', min_value=-2.0, max_value=10.0, value=2.0, step=.1)
  c1 = st.slider('Value of constant C1', min_value=0,max_value=150, value=100, step=10)
  c2 = 0
  c3 = 0
  def bpm(x,c0,c1,c2,c3):
    return np.log(c0*x)+c1+c2+c3

x_data = Corrected_points[0,:]
y_data = Corrected_points[1,:]

y_new = np.zeros(816)
# User input values for guesses
guess_coefficients= [c0,c1,c2,c3]

# st.code("c,cov = curve_fit(bpm,r_x_arr,y_arr,guess_coefficients)")
c,cov = curve_fit(bpm,r_x_arr,y_arr,guess_coefficients)
print(c)
# For C values of [-4.98E-6,5.51E-3,-1.06E0,1.49E2]
# The equation would be y= -.00000498x^3+.00551x^2-1.06x+149 

length = len(x_data)

for i in range(length):
  y_new[i] = bpm(x_data[i],c[0],c[1],c[2],c[3])

fig1=plt.plot(r_x_arr,y_arr)
# st.pyplot(fig1[0].figure)
fig2=plt.plot(r_x_arr,y_new,'r.')
st.pyplot(fig2[0].figure)