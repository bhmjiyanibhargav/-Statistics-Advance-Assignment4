#!/usr/bin/env python
# coding: utf-8

# # question 01
Q1: What is the difference between a t-test and a z-test? Provide an example scenario where you would
use each type of test.
The main difference between a t-test and a z-test is the way they are used to test a hypothesis about the population mean when the sample size is small or large, respectively.

A t-test is used when the sample size is small (typically less than 30) or when the population standard deviation is unknown. The test statistic used in a t-test is a t-distribution, which has heavier tails than the standard normal distribution used in a z-test. The t-distribution becomes closer to the standard normal distribution as the sample size increases.

A z-test is used when the sample size is large (typically greater than or equal to 30) and the population standard deviation is known. The test statistic used in a z-test is a standard normal distribution.

Here are two example scenarios where we would use each type of test:

Scenario for a t-test: A researcher wants to test if a new medication reduces blood pressure levels. She randomly selects 25 patients from a population and measures their blood pressure levels before and after taking the medication. She wants to know if the average reduction in blood pressure is statistically significant. Since the sample size is small and the population standard deviation is unknown, she should use a t-test to test the hypothesis.

Scenario for a z-test: A marketing manager wants to test if a new ad campaign has increased sales for their product. She collects sales data for the product for a random sample of 500 customers before and after the ad campaign. Since the sample size is large and the population standard deviation is known (or can be assumed to be known), she should use a z-test to test the hypothesis.

In summary, the choice of a t-test or a z-test depends on the sample size and whether the population standard deviation is known or unknown. A t-test is used when the sample size is small or the population standard deviation is unknown, while a z-test is used when the sample size is large and the population standard deviation is known.
# # question 02
Differentiate between one-tailed and two-tailed tests.
A hypothesis test is a statistical method to test whether a sample statistic (such as a sample mean) is significantly different from the hypothesized population parameter (such as a population mean). In hypothesis testing, we typically specify a null hypothesis (H0) and an alternative hypothesis (Ha) to be tested. The null hypothesis usually assumes that there is no significant difference between the sample statistic and the hypothesized population parameter, while the alternative hypothesis assumes otherwise.

One-tailed and two-tailed tests refer to the directionality of the alternative hypothesis.

A one-tailed test is used when we want to test if the sample statistic is significantly greater than or less than the hypothesized population parameter in a specific direction. For example, a one-tailed test can be used to test if a new drug improves the response rate of patients compared to the standard treatment. The null hypothesis would be that there is no significant difference in the response rate between the two treatments, while the alternative hypothesis would be that the response rate for the new drug is significantly greater than that for the standard treatment. In this case, we are only interested in one direction of the alternative hypothesis, i.e., the response rate of the new drug being greater than that of the standard treatment.

A two-tailed test is used when we want to test if the sample statistic is significantly different from the hypothesized population parameter in any direction. For example, a two-tailed test can be used to test if the mean weight of a population is different from a hypothesized value. The null hypothesis would be that there is no significant difference in the mean weight between the population and the hypothesized value, while the alternative hypothesis would be that the mean weight of the population is significantly different from the hypothesized value, either greater or less. In this case, we are interested in both directions of the alternative hypothesis, i.e., the mean weight being greater or less than the hypothesized value.

In summary, a one-tailed test is used when we are interested in only one direction of the alternative hypothesis, while a two-tailed test is used when we are interested in any direction of the alternative hypothesis. The choice of a one-tailed or two-tailed test should be based on the research question and the directionality of the hypothesis.
# # question 03
# 
Explain the concept of Type 1 and Type 2 errors in hypothesis testing. Provide an example scenario for
each type of error.
Type I and Type II errors are two possible mistakes that can occur in hypothesis testing.

Type I error occurs when we reject a true null hypothesis. In other words, we conclude that there is a significant difference between the sample statistic and the hypothesized population parameter when there is actually no significant difference. The probability of committing a Type I error is denoted by α, which is also known as the level of significance.

An example scenario of a Type I error is a medical test for a rare disease. Suppose that the null hypothesis is that the patient does not have the disease, and the alternative hypothesis is that the patient has the disease. If we reject the null hypothesis and conclude that the patient has the disease when in fact the patient does not have the disease, this would be a Type I error.

Type II error occurs when we fail to reject a false null hypothesis. In other words, we conclude that there is no significant difference between the sample statistic and the hypothesized population parameter when there is actually a significant difference. The probability of committing a Type II error is denoted by β.

An example scenario of a Type II error is a clinical trial for a new medication. Suppose that the null hypothesis is that the new medication has no effect on the patients, and the alternative hypothesis is that the new medication has a positive effect on the patients. If we fail to reject the null hypothesis and conclude that the new medication has no effect when in fact the new medication does have a positive effect, this would be a Type II error.

In summary, Type I error is rejecting a true null hypothesis, while Type II error is failing to reject a false null hypothesis. Both Type I and Type II errors can occur in hypothesis testing, and the probabilities of committing each type of error depend on the level of significance and the power of the test. The choice of the level of significance and the power of the test should be based on the research question and the consequences of each type of error.
# # question 4
Explain Bayes's theorem with an example.
Bayes's theorem is a mathematical formula that provides a way to update our beliefs or probabilities based on new evidence or information. It is widely used in Bayesian statistics and machine learning to make predictions and decisions.

Bayes's theorem states that the probability of an event A, given the occurrence of an event B, can be calculated as the product of the conditional probability of B given A and the prior probability of A, divided by the marginal probability of B. This can be written as:

P(A | B) = P(B | A) * P(A) / P(B)

where P(A | B) is the probability of A given B, P(B | A) is the probability of B given A, P(A) is the prior probability of A, and P(B) is the marginal probability of B.

An example scenario where Bayes's theorem can be used is in medical diagnosis. Suppose that a patient has a certain symptom, and we want to know the probability of the patient having a certain disease given the symptom.

Let A be the event that the patient has the disease, and B be the event that the patient has the symptom. Suppose that we know the following probabilities:

The probability of having the disease is 0.01, i.e., P(A) = 0.01.
The probability of having the symptom given that the patient has the disease is 0.9, i.e., P(B | A) = 0.9.
The probability of having the symptom given that the patient does not have the disease is 0.05, i.e., P(B | not A) = 0.05.
Using Bayes's theorem, we can calculate the probability of the patient having the disease given the symptom:

P(A | B) = P(B | A) * P(A) / P(B)

P(A | B) = 0.9 * 0.01 / (0.9 * 0.01 + 0.05 * 0.99)

P(A | B) ≈ 0.15

This means that the probability of the patient having the disease given the symptom is about 15%. In other words, the symptom alone is not a strong indicator of the disease, and further tests or examinations may be needed to confirm the diagnosis.

In this example, Bayes's theorem is used to update our prior belief about the probability of the patient having the disease based on the new evidence of the symptom. The result is a posterior probability that reflects our updated belief.
# # question 05
What is a confidence interval? How to calculate the confidence interval, explain with an example.
A confidence interval is a range of values that is likely to contain the true value of a population parameter (such as a mean or proportion) with a certain level of confidence. It is a way to quantify the uncertainty in our estimate based on a sample of data.

The confidence interval is typically expressed as a range of values, along with a level of confidence (usually in percentage). For example, a 95% confidence interval for the mean height of a population might be (160 cm, 170 cm). This means that we are 95% confident that the true mean height of the population falls within this range.

To calculate a confidence interval, we first need to determine the level of confidence and the sample statistics (such as the sample mean and standard deviation). Then we use a formula that takes into account the sample size, standard error, and the distribution of the sample statistics.

For example, suppose we want to estimate the mean weight of a population of adult male elephants. We take a random sample of 100 elephants and measure their weights. The sample mean weight is 5000 kg, and the sample standard deviation is 1000 kg. We want to calculate a 99% confidence interval for the population mean weight.

To do this, we first calculate the standard error of the mean, which is the standard deviation of the sample divided by the square root of the sample size:

standard error = 1000 / sqrt(100) = 100 kg

Next, we use a table or a statistical software to find the appropriate critical value for the level of confidence and the degrees of freedom (which is the sample size minus one). For a 99% confidence interval and 99 degrees of freedom, the critical value is approximately 2.626.

Finally, we use the following formula to calculate the confidence interval:

confidence interval = sample mean ± (critical value * standard error)

confidence interval = 5000 ± (2.626 * 100) = (4737.4 kg, 5262.6 kg)

This means that we are 99% confident that the true mean weight of adult male elephants falls within the range of 4737.4 kg to 5262.6 kg.

Note that the width of the confidence interval depends on the sample size, the level of confidence, and the variability of the sample data. A larger sample size or a higher level of confidence will result in a wider confidence interval, while a smaller sample size or a lower level of confidence will result in a narrower confidence interval.
# # question 06
Use Bayes' Theorem to calculate the probability of an event occurring given prior knowledge of the
event's probability and new evidence. Provide a sample problem and solution.
Sure, here's an example problem and solution using Bayes' Theorem:

Problem: A factory produces two types of products, A and B. Historically, 60% of the products produced are type A. The factory has a quality control system that can detect defects with 95% accuracy for type A products and 80% accuracy for type B products. If a product is randomly selected and found to be defective, what is the probability that it is type A?

Solution:

Let's define the following events:

A = the product is type A
B = the product is type B
D = the product is defective
We want to find the probability of A given D, which is written as P(A|D).

According to Bayes' Theorem, we can calculate P(A|D) using the following formula:

P(A|D) = P(D|A) * P(A) / P(D)

where:

P(D|A) = the probability of the product being defective given that it is type A (which is 1 - the accuracy rate, or 0.05)
P(A) = the prior probability of the product being type A (which is 0.6)
P(D) = the total probability of the product being defective (which can be calculated using the Law of Total Probability)
To calculate P(D), we need to consider two cases: the product is type A and defective, or the product is type B and defective. So we have:

P(D) = P(D|A) * P(A) + P(D|B) * P(B)

where:

P(D|B) = the probability of the product being defective given that it is type B (which is 1 - the accuracy rate, or 0.2)
P(B) = the prior probability of the product being type B (which is 0.4)
Plugging in the numbers, we have:

P(D) = 0.05 * 0.6 + 0.2 * 0.4 = 0.09

Now we can calculate P(A|D):

P(A|D) = P(D|A) * P(A) / P(D)

P(A|D) = 0.05 * 0.6 / 0.09 = 0.333 (or approximately 33.3%)

Therefore, if a product is randomly selected and found to be defective, the probability that it is type A is about 33.3%.
# # question 07
Calculate the 95% confidence interval for a sample of data with a mean of 50 and a standard deviation
of 5. Interpret the results.
To calculate the 95% confidence interval for a sample of data with a mean of 50 and a standard deviation of 5, we need to use the formula:

CI = X̄ ± Zα/2 * (σ/√n)

where:

CI is the confidence interval
X̄ is the sample mean (which is 50 in this case)
Zα/2 is the critical value of the standard normal distribution at α/2 (where α is the level of significance, which is 0.05 for a 95% confidence interval)
σ is the population standard deviation (which is unknown in this case, so we use the sample standard deviation as an estimate)
n is the sample size
The critical value Zα/2 for a 95% confidence interval is approximately 1.96. So, plugging in the numbers we get:

CI = 50 ± 1.96 * (5/√n)

We don't know the sample size (n) for this problem, so we can't calculate the exact interval. However, we can make some general observations:

As the sample size increases, the confidence interval will become narrower because the standard error of the mean (which is the standard deviation of the sampling distribution of the mean) decreases as n increases.
A 95% confidence interval means that we are 95% confident that the true population mean falls within the interval. In other words, if we took many samples and calculated their confidence intervals using the same method, we would expect 95% of the intervals to contain the true population mean.
The margin of error is given by the second term in the formula (i.e., 1.96 * (5/√n)). This represents the range of values above and below the sample mean that we are 95% confident contains the true population mean.
So, for example, if we had a sample size of 100, we would have:

CI = 50 ± 1.96 * (5/√100) = 50 ± 0.98

This means that we are 95% confident that the true population mean falls within the range of 49.02 to 50.98.
# # question 08
What is the margin of error in a confidence interval? How does sample size affect the margin of error?
Provide an example of a scenario where a larger sample size would result in a smaller margin of error.
The margin of error is the range of values above and below the sample estimate in a confidence interval that we are reasonably confident contains the true population parameter. It is calculated as the product of the critical value of the selected confidence level and the standard error of the sample statistic.

A larger sample size results in a smaller margin of error because it reduces the variability of the sample estimate and increases the precision of the estimate. In other words, the larger the sample size, the more reliable the estimate, and the more confident we can be that it represents the true population parameter.

Here's an example scenario to illustrate this:

Suppose a polling organization wants to estimate the proportion of eligible voters in a state who plan to vote for Candidate A in the upcoming election. They take a random sample of 200 eligible voters and find that 110 of them plan to vote for Candidate A.

To calculate the margin of error, the organization needs to choose a confidence level. Let's assume they choose a 95% confidence level. The critical value for a 95% confidence interval is 1.96.

The organization also needs to calculate the standard error of the sample proportion. The formula for the standard error of the proportion is:

SE = sqrt[(p̂(1-p̂))/n]

where p̂ is the sample proportion, and n is the sample size.

In this case, the sample proportion is 110/200 = 0.55. Plugging this into the formula, we get:

SE = sqrt[(0.55(1-0.55))/200] = 0.0502

So the margin of error is:

ME = 1.96 * 0.0502 = 0.0984

Thus, the 95% confidence interval for the proportion of eligible voters who plan to vote for Candidate A is:

0.55 ± 0.0984, or 0.4516 to 0.6484.

Suppose the organization wants to reduce the margin of error to 0.05 to obtain a more precise estimate of the population parameter. To achieve this, they could increase the sample size. If they increase the sample size to 1000, the standard error of the sample proportion would decrease, and the margin of error would decrease as well. In fact, the margin of error would be:

ME = 1.96 * sqrt[(0.55(1-0.55))/1000] = 0.0229

This means that the 95% confidence interval for the proportion of eligible voters who plan to vote for Candidate A would be much narrower with a larger sample size, which would provide a more precise estimate of the population parameter.
# # question 09
Calculate the z-score for a data point with a value of 75, a population mean of 70, and a population
standard deviation of 5. Interpret the results.
The z-score is a measure of how many standard deviations a data point is away from the population mean. It is calculated as:

z = (x - μ) / σ

where x is the data point, μ is the population mean, and σ is the population standard deviation.

In this case, we have:

x = 75
μ = 70
σ = 5

Plugging these values into the formula, we get:

z = (75 - 70) / 5 = 1

So the z-score for the data point with a value of 75 is 1. This means that the data point is one standard deviation above the population mean.

Interpreting the z-score, we can say that the value of 75 is higher than the population mean by a moderate amount (one standard deviation). This implies that the data point is relatively far away from the center of the distribution, and it may be considered an outlier or unusual observation. We can also use the z-score to calculate the probability of observing a value of 75 or higher under the normal distribution with a mean of 70 and a standard deviation of 5, which can be useful in statistical inference and hypothesis testing.
# # question 10
Q10. In a study of the effectiveness of a new weight loss drug, a sample of 50 participants lost an average
of 6 pounds with a standard deviation of 2.5 pounds. Conduct a hypothesis test to determine if the drug is
significantly effective at a 95% confidence level using a t-test.
We want to test the hypothesis that the mean weight loss for the population of people taking the new drug is significantly different from zero (i.e., there is a significant weight loss effect). We can set up the null and alternative hypotheses as follows:

H0: μ = 0 (there is no significant weight loss effect)
Ha: μ ≠ 0 (there is a significant weight loss effect)

We will use a two-tailed t-test with a significance level of 0.05 (95% confidence level). Since we do not know the population standard deviation, we will use the sample standard deviation as an estimate and use a t-distribution with 49 degrees of freedom (50-1).

The test statistic can be calculated as:

t = (x̄ - μ) / (s / √n)

where x̄ is the sample mean (6 pounds), μ is the null hypothesis population mean (0), s is the sample standard deviation (2.5 pounds), and n is the sample size (50).

Plugging in the values, we get:

t = (6 - 0) / (2.5 / √50) = 13.4164

Using a t-table or a calculator with t-distribution function, we can find the critical t-value for a two-tailed test with 49 degrees of freedom and a significance level of 0.05. This gives us a critical t-value of ±2.0096.

Since our calculated t-value of 13.4164 is greater than the critical t-value of 2.0096, we can reject the null hypothesis and conclude that there is a significant weight loss effect from taking the new drug at a 95% confidence level.

In other words, we can say that we are 95% confident that the true population mean weight loss from taking the new drug is different from zero and that the drug is significantly effective for weight loss.
# # question 11
Q11. In a survey of 500 people, 65% reported being satisfied with their current job. Calculate the 95%
confidence interval for the true proportion of people who are satisfied with their job.
We want to calculate the 95% confidence interval for the true proportion of people who are satisfied with their job based on a survey of 500 people where 65% reported being satisfied.

To calculate the confidence interval, we can use the formula:

CI = p̂ ± z* (sqrt(p̂(1-p̂)/n))

where p̂ is the sample proportion (0.65), z* is the critical z-value for a 95% confidence level (1.96), and n is the sample size (500).

Plugging in the values, we get:

CI = 0.65 ± 1.96 * (sqrt(0.65 * (1-0.65) / 500))

CI = 0.65 ± 0.042

The 95% confidence interval for the true proportion of people who are satisfied with their job is (0.608, 0.692).

This means that we can be 95% confident that the true proportion of people who are satisfied with their job falls within this interval.
# # question 12
Q12. A researcher is testing the effectiveness of two different teaching methods on student performance.
Sample A has a mean score of 85 with a standard deviation of 6, while sample B has a mean score of 82
with a standard deviation of 5. Conduct a hypothesis test to determine if the two teaching methods have a
significant difference in student performance using a t-test with a significance level of 0.01.
To determine if there is a significant difference in student performance between the two teaching methods, we can conduct a two-sample t-test with a significance level of 0.01.

Our null hypothesis is that the means of the two samples are equal (i.e. there is no significant difference in student performance between the two teaching methods). Our alternative hypothesis is that the means of the two samples are not equal (i.e. there is a significant difference in student performance between the two teaching methods).

We can use the following formula to calculate the t-statistic:

t = (x̄1 - x̄2) / (s_pool * sqrt(1/n1 + 1/n2))

where x̄1 and x̄2 are the sample means, s_pool is the pooled standard deviation, n1 and n2 are the sample sizes.

First, we calculate the pooled standard deviation:

s_pool = sqrt(((n1-1)*s1^2 + (n2-1)*s2^2)/(n1+n2-2))

s1 and s2 are the sample standard deviations.

Plugging in the values, we get:

s_pool = sqrt(((296^2)+(395^2))/(30+40-2))

s_pool = 5.34

Next, we can calculate the t-statistic:

t = (85 - 82) / (5.34 * sqrt(1/30 + 1/40))

t = 2.44

The degrees of freedom for the t-distribution can be calculated using the formula:

df = (s1^2/n1 + s2^2/n2)^2 / [(s1^2/n1)^2/(n1-1) + (s2^2/n2)^2/(n2-1)]

Plugging in the values, we get:

df = ((6^2/30) + (5^2/40))^2 / [((6^2/30)^2/(30-1)) + ((5^2/40)^2/(40-1))]

df = 67.33

Using a t-table with 67 degrees of freedom and a significance level of 0.01, the critical t-value is ±2.653.

Since our calculated t-statistic of 2.44 is less than the critical t-value of 2.653, we fail to reject the null hypothesis. This means that we do not have enough evidence to conclude that there is a significant difference in student performance between the two teaching methods.
# # question 13
Q13. A population has a mean of 60 and a standard deviation of 8. A sample of 50 observations has a mean
of 65. Calculate the 90% confidence interval for the true population mean.
To calculate the 90% confidence interval for the true population mean, we can use the formula:

CI = x̄ ± z*(σ/√n)

where x̄ is the sample mean, σ is the population standard deviation, n is the sample size, and z is the critical value from the standard normal distribution for the desired confidence level (90% in this case).

First, we need to find the critical value of z for a 90% confidence level. Using a standard normal distribution table or a calculator, we can find that the critical value is 1.645.

Plugging in the values we have:

CI = 65 ± 1.645*(8/√50)

Simplifying:

CI = 65 ± 2.327

Therefore, the 90% confidence interval for the true population mean is (62.673, 67.327). This means that we are 90% confident that the true population mean lies between 62.673 and 67.327.

Note that the margin of error is ±2.327, which means that we can be 90% confident that the true population mean is within 2.327 units of the sample mean of 65.




# # question 14
Q14. In a study of the effects of caffeine on reaction time, a sample of 30 participants had an average
reaction time of 0.25 seconds with a standard deviation of 0.05 seconds. Conduct a hypothesis test to
determine if the caffeine has a significant effect on reaction time at a 90% confidence level using a t-test.
To determine if caffeine has a significant effect on reaction time using a t-test, first, we need to state the null and alternative hypotheses.

Null Hypothesis: Caffeine has no significant effect on reaction time (µ = 0.25)
Alternative Hypothesis: Caffeine has a significant effect on reaction time (µ ≠ 0.25)

We can use a two-tailed t-test because the alternative hypothesis is non-directional.

Next, we calculate the t-statistic using the formula:

t = (x̄ - µ) / (s / √n)

where x̄ is the sample mean (0.25 seconds), µ is the hypothesized population mean (0.25 seconds), s is the sample standard deviation (0.05 seconds), and n is the sample size (30).

Plugging in the values, we get:

t = (0.25 - 0.25) / (0.05 / √30) = 0 / 0.009144 = 0

The calculated t-statistic is 0.

Next, we need to find the critical t-value at a 90% confidence level with 29 degrees of freedom (30-1). Using a t-distribution table or a calculator, we find the critical t-value to be ±1.699.

Since the calculated t-statistic (0) is within the range of the critical t-value (±1.699), we fail to reject the null hypothesis. Therefore, we can conclude that there is no significant effect of caffeine on reaction time at a 90% confidence level.
# In[ ]:




