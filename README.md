# Time Series Analysis

This repository is dedicated to exploring and understanding Time Series Analysis. Here, I am performing noise checking and filtering the noise using a Simple Moving Average. For noise checking, I used statistical methods.

## Steps

1. **Calculate the Mean (𝜇):**

   The mean (\(\mu\)) is calculated using the following formula:

   $$
   \mu = \frac{1}{N} \sum_{i=1}^{N} x_i
   $$

   This formula represents the average of a set of values.

2. **Calculate the Standard Deviation (𝜎):**

   ![Equation](https://quicklatex.com/cache3/32/ql_86135f0a811484b2cbe5ab66c03dce32_l3.png)

3. **Define Threshold and Identify Noisy Points** <br>

   Let's assume that the threshold value is 3 so   <br>
   Theshold Value= 3 X 𝜎

5. **Identify noisy points by checking if the absolute difference from the mean exceeds the threshold or not :**

$$
\left| x_i - \mu \right| > \text{Threshold}
$$

Example: 

The data are : accx = [10, 12, 11, 13, 100, 12, 11, 12, 14, 13]

Step 1:  
![Equation](https://quicklatex.com/cache3/32/ql_c02a2e9c84fd97b69d30a546c3b1bb32_l3.png) <br>Step 2: 


![Equation](https://quicklatex.com/cache3/40/ql_bf0ea75995523d019a59304f0da09f40_l3.png)

Step 3: 
We use a threshold of 3 standard deviations:

![Equation](https://quicklatex.com/cache3/09/ql_0c29d3bb6138e5dbe132a43763b8b209_l3.png) <br> Step 4: 

Identify noisy points by checking if the absolute difference from the mean exceeds the threshold:
![Equation](https://quicklatex.com/cache3/63/ql_2517bb34518cf45b9d1a60f96d171b63_l3.png)

