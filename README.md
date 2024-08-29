# Time-Series-Analysis

This repository is dedicated to exploring and understanding Time Series Analysis.  
Here, I am performing noise checking and filtering the noise using a Simple Moving Average.  
For noise checking, I used statistical methods.  

Here are all the steps:
The mean (𝜇) is calculated using the following formula:

$$
\mu = \frac{1}{N} \sum_{i=1}^{N} x_i
$$

This formula represents the average of a set of values.
2. **Calculate the Standard Deviation (𝜎):**  
   The standard deviation (𝜎) is calculated as:  
   $$
   \sigma = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \left( x_i - \mu \right)^2}
   $$
