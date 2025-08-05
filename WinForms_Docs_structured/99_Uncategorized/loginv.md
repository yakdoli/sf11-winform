---
title: loginv.md
original_path: WinForms_Docs/99_Uncategorized/loginv.md
created_at: 2025-08-05
---








  









### LOGINV {#loginv style="tab-stops: 0pt"}

 

Returns the inverse of the lognormal cumulative distribution function of x, where ln(x) is normally distributed with parameters mean and standard_dev. If p = LOGNORMDIST(x,\...), then LOGINV(p,\...) = x.

 

**Syntax**

 

**LOGINV(probability, mean, standard_dev)**

 

where:

**probability**[ ]is the probability associated with the lognormal distribution.

**mean **is the mean of ln(x).

**standard_dev**[ ]is the standard deviation of ln(x).

 

**Remarks**

 

[·      ]Probability must be \>= 0 and \< 1.

[·      ]Standard_dev must be positive.

[·      ]The inverse of the lognormal distribution function is:

[] 

{border="0"}

[]{#p143} 

[]{#related-topics}

