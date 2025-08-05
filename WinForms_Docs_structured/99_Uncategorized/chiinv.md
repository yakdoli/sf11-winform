---
title: chiinv.md
original_path: WinForms_Docs/99_Uncategorized/chiinv.md
created_at: 2025-08-05
---








  









### CHIINV {#chiinv style="tab-stops: 0pt"}

 

Returns the inverse of the one-tailed probability of the chi-squared ([χ][2]) distribution. If probability = CHIDIST(x,\...), then CHIINV(probability,\...) = x. Use this function to compare observed results with expected ones in order to decide whether your original hypothesis is valid.

 

**Syntax**

 

**CHIINV(probability, degrees_freedom)**

 

where:

**probability**[ ]is a probability associated with the chi-squared distribution.

**degrees_freedom**[ ]is the number of degrees of freedom.

 

**Remarks**

[] 

[·      ]Probability must be \>= 0 and \<= 1.

[·      ]degrees_freedom \>=1 and  = 10\^10.

[] 

Given a value for probability, CHIINV seeks the value x such that CHIDIST(x, degrees_freedom) = probability. Thus, precision of CHIINV depends on precision of CHIDIST. CHIINV uses an iterative search technique.

[]{#p89} 

[]{#related-topics}

