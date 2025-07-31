---
title: trimmean.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\trimmean.md
created_at: 2025-07-03
---








  









### TRIMMEAN {#trimmean style="tab-stops: 0pt"}

 

Returns the mean of the interior of a data set. TRIMMEAN calculates the mean taken by excluding a percentage of data points from the top and bottom tails of a data set.

 

**Syntax**

**TRIMMEAN(array, percent)**

 

where:

**array** is the array or range of values to trim and average.

**percent** is the fractional number of data points to exclude from the calculation. For example, if percent = 0.2, 4 points are trimmed from a data set of 20 points (20 x 0.2): 2 from the top and 2 from the bottom of the set.

 

**Remarks**

 

[·      ]Percent must be \>= 0 and \<= 1.

[·      ]TRIMMEAN rounds off the number of excluded data points down to the nearest multiple of 2. If percent = 0.1, 10 percent of 30 data points equals 3 points. For symmetry, TRIMMEAN excludes a single value from the top and bottom of the data set.

 

[]{#related-topics}

