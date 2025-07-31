---
title: percentrank.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\percentrank.md
created_at: 2025-07-03
---








  









### PERCENTRANK {#percentrank style="tab-stops: 0pt"}

 

Returns the rank of a value in a data set as a percentage of the data set.

 

**Syntax**

 

**PERCENTRANK(array, x, significance)**

 

where:

**array** is the range of data with numeric values that defines relative standing.

**x** is the value for which, you want to know the rank.

**significance** is an optional value that identifies the number of significant digits for the returned percentage value. If omitted, PERCENTRANK uses three digits (0.xxx).

 

**Remarks**

[] 

[·      ]Significance must be \>= 1.

[·      ]If x does not match one of the values in the array, PERCENTRANK interpolates to return the correct percentage rank.

[]{#p167} 

 

[]{#related-topics}

