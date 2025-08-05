---
title: gammadist.md
original_path: WinForms_Docs/99_Uncategorized/gammadist.md
created_at: 2025-08-05
---








  









### GAMMADIST {#gammadist style="tab-stops: 0pt"}

 

Returns the**[ ]**gamma distribution.

 

**Syntax**

 

**GAMMADIST(x, alpha,beta, cumulative)**

 

where:

**x**[ ]is the value at which, you want to evaluate the distribution.

**alpha**[ ]is a parameter to the distribution.

**beta**[ ]is a parameter to the distribution. If beta = 1, GAMMADIST returns the standard gamma distribution.

**cumulative**[ ]is a logical value that determines the form of the function. If cumulative is True, GAMMADIST returns the cumulative distribution function; if False, it returns the probability density function.

 

**Remarks**

[] 

[·      ]X must be \>=  0.

[·      ]Alpha and beta must be \> 0.

[·      ]The equation for the gamma probability density function is:

{border="0"}

[] 

[·      ]The standard gamma probability density function is:

{border="0"}

[] 

[·      ]When alpha = 1, GAMMADIST returns the exponential distribution with:

[] 

{border="0"}[]{#p120}

 

[]{#related-topics}

