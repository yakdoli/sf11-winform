---
title: percentile.md
original_path: WinForms_Docs/99_Uncategorized/percentile.md
created_at: 2025-08-05
---








  









### PERCENTILE {#percentile style="tab-stops: 0pt"}

 

Returns the k-th percentile of values in a range.

 

**Syntax**

**\
PERCENTILE(array, k)**

 

where:

**array** is the array or range of data that defines relative standing.

**k** is the percentile value in the range 0..1, inclusive.

 

**Remarks**

 

[·      ]k must be \>=10 and \<= 1.

[·      ]If k is not a multiple of 1/(n - 1), PERCENTILE interpolates to determine the value at the k-th percentile.

 

[]{#p166} 

[]{#related-topics}

