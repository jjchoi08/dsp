[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

## acutal distribution
>> d_ex1 = resp['numkdhh'] <br>
pmf_ex1 = thinkstats2.Pmf(d_ex1, label='actual') <br>
pmf_ex1 <br>
Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})

## biased distribution
>> biased_pmf_ex1 = BiasPmf(pmf_ex1, label='observed')
>> biased_pmf_ex1
Pmf({0: 0.0, 1: 0.20899335717935616, 2: 0.38323965252938175, 3: 0.25523760858456823, 4: 0.10015329586101177, 5: 0.052376085845682166})

## Plot
>> thinkplot.PrePlot(2)
>> thinkplot.Pmfs([pmf_ex1, biased_pmf_ex1])
>> thinkplot.Show(xlabel='class size', ylabel='PMF')

## Mean
>> print('mean of actual:', pmf_ex1.Mean(), ' mean of biased:', biased_pmf_ex1.Mean())
mean of actual: 1.02420515504  mean of biased: 2.40367910066
