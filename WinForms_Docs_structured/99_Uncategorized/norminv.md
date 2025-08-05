---
title: norminv.md
original_path: WinForms_Docs/99_Uncategorized/norminv.md
created_at: 2025-08-05
---








  









### NORMINV {#norminv style="tab-stops: 0pt"}

 

Returns the inverse of the normal cumulative distribution for the specified mean and standard deviation.

 

**Syntax**

 

**NORMINV(probability, mean, standard_dev)**

 

where:

**probability** is a probability corresponding to the normal distribution.

**mean** is the arithmetic mean of the distribution.

**standard_dev** is the standard deviation of the distribution.

 

**Remarks**

 

[·      ]Probability must be \>= 0 and \<= 1.

[·      ]standard_dev must be \> 0.

 

Given a value for probability, NORMINV seeks value x such that NORMDIST(x, mean, standard_dev, True) = probability. NORMINV uses an iterative search technique.

[]{#p158} 

[]{#related-topics}

