---
title: chidist.md
original_path: WinForms_Docs/99_Uncategorized/chidist.md
created_at: 2025-08-05
---








  









### CHIDIST {#chidist style="tab-stops: 0pt"}

 

Returns the one-tailed probability of the chi-squared ( ) distribution. The  distribution is associated with a  test.

 

**Syntax**

 

**CHIDIST(x, degrees_freedom)**

 

where:

x is the value at which you want to evaluate the distribution.

**degrees_freedom** is the number of degrees of freedom.

 

**Remarks**

[] 

[·      ]Both arguments should be numeric.

[·      ]degrees_freedom  \>= 1 and \< 10\^10.

[·      ]CHIDIST is calculated as follows:

[] 

CHIDIST = P(X \> x)

 

where:

**X** is a [χ][2][ ]random variable.

 

[]{#p88} 

[]{#related-topics}

