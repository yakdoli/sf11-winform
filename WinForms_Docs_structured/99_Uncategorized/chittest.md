---
title: chittest.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\chittest.md
created_at: 2025-07-03
---








  









### CHITTEST {#chittest style="tab-stops: 0pt"}

 

Returns the test for independence. CHITEST returns the value from the chi-squared (c2) distribution for the statistic and the appropriate degrees of freedom.

 

**Syntax**

 

CHITEST(actual_range, expected_range)

 

where:

**actual_range** is the range of data that contains observations to test against expected values.

**expected_range** is the range of data that contains the ratio of the product of row totals and column totals to the grand total.

 

**Remarks**

[] 

[·      ]The[ ][χ][2][ ]test first calculates a[ ][χ][2] statistic using the formula:

[] 

{border="0"}

[] 

where:

Aij = actual frequency in the i-th row, j-th column

Eij = expected frequency in the i-th row, j-th column

r = number of rows

c = number of columns

 

A low value of [χ][2] is an indicator of independence. The use of CHITEST is most appropriate when Eij\'s are not too small. Some statisticians suggest that each Eij should be greater than or equal to 5.

 

[]{#p90} 

[]{#related-topics}

