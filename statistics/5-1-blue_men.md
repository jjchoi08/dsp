[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Exercise: In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.

In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.


>> bman1 = dist.cdf(177.8) <br>
bman2 = dist.cdf(185.4)<br>
bman1, bman2

(0.48963902786483265, 0.83173371081078573)

>>bman2-bman1

0.34209468294595308<br>
34% of the U.S. male population is in this range
