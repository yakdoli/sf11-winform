---
title: stdev.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\stdev.md
created_at: 2025-07-03
---








  









### STDEV {#stdev style="tab-stops: 0pt"}

 

Estimates the standard deviation based on a sample. The standard deviation is a measure of how widely values are dispersed from the average value (the mean).

 

**Syntax**

 

**STDEV(number1, number2, \...)**

 

where:

**number1, number2, \...** are number arguments corresponding to a sample of a population.

 

**Remarks**

 

[·      ]STDEV assumes that its arguments are a sample of the population. If your data represents the entire population, then compute the standard deviation using STDEVP.

[·      ]STDEV uses the following formula:

[] 

{border="0"}

 

where:

**x-bar** is the sample mean AVERAGE(number1,number2,...).

**n** is the sample size.

 

[]{#related-topics}

