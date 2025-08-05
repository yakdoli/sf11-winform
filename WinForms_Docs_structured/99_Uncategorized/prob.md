---
title: prob.md
original_path: WinForms_Docs/99_Uncategorized/prob.md
created_at: 2025-08-05
---








  









### PROB {#prob style="tab-stops: 0pt"}

 

Returns the probability whose values are in a range that is between two limits. If upper_limit is not supplied, returns the probability that values in x_range are equal to lower_limit.

[] 

Syntax

[] 

PROB(x_range, prob_range, lower_limit, upper_limit)

 

where:

**x_range[ ]**is the range of numeric values of x with which, there are associated probabilities.

**prob_range** is a set of probabilities associated with values in x_range.

**lower_limit** is the lower bound on the value for which, you want a probability.

**upper_limit**[ ]is the optional upper bound on the value for which, you want a probability.

 

**Remarks**

 

[·      ]Any value in prob_range must be \> 0 and \< 1.

[·      ]If upper_limit is omitted, PROB returns the probability of being equal to lower_limit.

[]{#p173} 

 

[]{#related-topics}

