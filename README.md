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

   Let's assume that the threshold value is 3 so   
$$
\text{Threshold} = 3 \times \sigma
$$

4. **Identify noisy points by checking if the absolute difference from the mean exceeds the threshold or not :**

$$
\left| x_i - \mu \right| > \text{Threshold}
$$


   
