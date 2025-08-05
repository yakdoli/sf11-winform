---
title: ztest2.md
original_path: WinForms_Docs/99_Uncategorized/ztest2.md
created_at: 2025-08-05
---








  









### ZTEST {#ztest style="tab-stops: 0pt"}

 

Returns the one-tailed probability-value of a z-test.

 

**Syntax**

 

**ZTEST(array, u0, sigma)**

 

where:

**array** is the array or range of data against which, to test u0

**u0** is the value to test.

**sigma** is the population (known) standard deviation. If omitted, the sample standard deviation is used.

 

Remarks

 

[·      ]ZTEST is calculated as follows when sigma is not omitted:

[] 

{border="0"}

 

or when sigma is omitted:

 

{border="0"}

 

where:

**x** is the sample mean AVERAGE(array); s is the sample standard deviation STDEV(array).

**n** is the number of observations in the sample COUNT(array).

 

 

 

[]{#related-topics}

