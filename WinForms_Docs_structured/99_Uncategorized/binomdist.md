---
title: binomdist.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\binomdist.md
created_at: 2025-07-03
---








  









### BINOMDIST {#binomdist style="tab-stops: 0pt"}

 

Returns the individual term binomial distribution probability.

 

Syntax

 

**BINOMDIST(number_s, trials, probability_s, cumulative)**

 

where:

**number_s**[  ]is the number of successes in trials.

**trials**[ ]is the number of independent trials.

**probability_s  **is the probability of success on each trial.

**Cumulative**[ ]is a logical value that determines the form of the function. If cumulative is True, then**[ ]**BINOMDIST returns the cumulative distribution which, is the probability that there are at most number_s successes; if False, it returns the probability that there are exactly number_s successes.

 

Remarks

[] 

[·      ]Number_s and trials are truncated to integers.

[·      ]Number_s should be \>= 0 and \<= trials.

[·      ]Probability_s  should be \>=0 and \<= 1.

[·      ]The binomial probability mass function is:

[] 

{border="0"}

[] 

where:

{border="0"} is COMBIN(n,x).   

[] 

[·      ]The cumulative binomial distribution is:

[] 

[{border="0"}][]

[]{#p86} 

[]{#related-topics}

