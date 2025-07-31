---
title: fdist.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\fdist.md
created_at: 2025-07-03
---








  









### FDIST {#fdist style="tab-stops: 0pt"}

 

Returns the**[ ]**F probability distribution.

 

**Syntax**

\
**FDIST(x, degrees_freedom1, degrees_freedom2)**

 

where:

**x** is the value at which to evaluate the function.

**degrees_freedom1** is the numerator degrees of freedom.

**degrees_freedom2**[ ]is the denominator degrees of freedom.

 

**Remarks**

 

[·      ]All arguments must be numeric.

[·      ]X must be \>= 0.

[·      ]Both degrees_freedom1 and degrees_freedom2 must be \>= 1 and \< 10\^10.

[·      ]FDIST is calculated as follows:

[] 

FDIST=P( F\>x )

 

where:

**F** is a random variable that has an F distribution with degrees_freedom1 and degrees_freedom2 degrees of freedom.

[]{#p115} 

[]{#related-topics}

