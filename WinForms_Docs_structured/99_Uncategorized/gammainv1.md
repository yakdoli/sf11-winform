---
title: gammainv1.md
original_path: WinForms_Docs/99_Uncategorized/gammainv1.md
created_at: 2025-08-05
---






#### GAMMAINV {#gammainv style="tab-stops: 0pt"}

 

Returns the inverse of the gamma cumulative distribution. If p = GAMMADIST(x,\...), then GAMMAINV(p,\...) = x.

 

**Syntax**

 

**GAMMAINV(probability, alpha, beta)**

 

where:

**probability** is the probability associated with the gamma distribution.

**alpha** is a parameter to the distribution.

**beta** is a parameter to the distribution.

 

**Remarks**

[] 

[·      ]Probability must be \>= 0 and \<= 1.

[·      ]Alpha and beta must be positive.

 

Given a value for probability, GAMMAINV seeks value x such that GAMMADIST(x, alpha, beta, True) = probability. Thus, precision of GAMMAINV depends on the precision of GAMMADIST. GAMMAINV uses an iterative search technique.

 

[]{#p122} 

[]{#related-topics}

