---
title: ttests1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\ttests1.md
created_at: 2025-07-03
---






#### T-Tests {#t-tests style="tab-stops: 0pt"}

 

TTest is a statistical formula that is used to measure the equality between the means of two series. In other words, the T test compares the actual difference between two means in relation to the variation in data that can be measured by calculating the standard deviation of the difference between the means.

 

It is a statistical test used to test the null hypothesis that the means of two normally distributed populations are equal. This test can be performed on two given samples(series), each characterized by its mean, standard deviation and number of data points, to determine whether the means are distinct based on the assumption that the underlying distributions are normal.

 

Different T-Tests

 

There are different versions of T tests depending on whether the samples are:

 

[·      ]**independent** of each other, (where the series are random with no relationship between each other)

***OR***

[·      ]**paired**, (where every data point in one series will have a relationship with a particular point of another series).

 

If the calculated t-statistic exceeds the chosen threshold value (usually 0.05), then the decision is to reject the null hypothesis, which states that the two sample means are equal, in favor of an alternate hypothesis, which typically specifies that the two samples differ.

 

Below are the different formulae to calculate the t-statistic:

 

[[·      ]]{.UGHyperlink}[[T-Test with Equal Variances]]{.UGHyperlink}

This formula performs a T test for two groups of data and assumes equal variances between the two groups (i.e. series).

[[]]{.UGHyperlink} 

[[·      ]]{.UGHyperlink}[T-Test Paired]{.UGHyperlink}[]{.UGHyperlink}

This formula performs a paired two-sample student\'s t-test to determine whether a sample\'s means are distinct. This form of the t-test does not assume that the variances of both the populations are equal.

Use a paired test when there is a natural pairing of observations in the samples, such as a sample group that is tested twice. (e.g. before and after an experiment)

 

[[·      ]]{.UGHyperlink}[T-Test with UnEqual Variances]{.UGHyperlink}[]{.UGHyperlink}

This formula performs a T-test for two groups of data and assumes unequal variances between the two groups. (i.e. series)

This analysis tool is referred to as a heteroscedastic t-test and can be used when the groups that are under study are distinct. Use a paired test when there is one group before and after a treatment.

 


Note: For programming example, refer to the following Browser Sample:


 

[\[Installed drive\]:\\Documents and Settings\\\[User name\]\\My Documents\\Syncfusion\\EssentialStudio\\\[Installed version\]\\Windows\\Chart.Windows\\Samples\\2.0\\Statistical Analysis\\Chart Statistical Formulas]{.UGHyperlink}

 

[]{#p225} 

More:









