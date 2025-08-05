---
title: negbinomdist.md
original_path: WinForms_Docs/99_Uncategorized/negbinomdist.md
created_at: 2025-08-05
---








  









### NEGBINOMDIST {#negbinomdist style="tab-stops: 0pt"}

 

Returns the negative binomial distribution. NEGBINOMDIST returns the probability that there will be number_f failures before the number_s-th success, when the constant probability of a success is probability_s.

 

**Syntax**

 

**NEGBINOMDIST(number_f, number_s, probability_s)**

 

where:

**number_f** is the number of failures.

**number_s** is the threshold number of successes.

**probability_s** is the probability of a success.

 

**Remarks**

 

[·      ]number_s  must be \>= 1.

[·      ]probability_s must be \>= 0 and \<= 1.

[·      ]number_f  must be \>= 0.

[·      ]The equation for the negative binomial distribution is:

[] 

{border="0"}

 

where:

**x** is number_f

**r** is number_s

**p** is probability_s

 

[]{#p156} 

[]{#related-topics}

