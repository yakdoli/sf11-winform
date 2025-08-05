---
title: hypegeomdist.md
original_path: WinForms_Docs/99_Uncategorized/hypegeomdist.md
created_at: 2025-08-05
---








  









### HYPEGEOMDIST {#hypegeomdist style="tab-stops: 0pt"}

 

Returns the hypergeometric distribution. HYPGEOMDIST returns the probability of a given number of sample successes, given the sample size, population successes and population size.

 

**Syntax**

 

**HYPGEOMDIST(sample_s, number_sample, population_s, number_population)**

 

where:

**sample_s** is the number of successes in the sample.

**number_sample** is the size of the sample.

**population_s** is the number of successes in the population.

**number_population** is the population size.

 

**Remarks**

 

[·      ]All arguments are truncated to integers.

[·      ]sample_s must be \>= 0 less than both  number_sample and population_s.

[·      ]number_sample must be \>= 0 and \<  number_population.

[·      ]population_s must be \>= 0 and \<  number_population.

[·      ]number_population must b \>= 0.

[·      ]The equation for the hypergeometric distribution is:

[] 

{border="0"}

 

where:

**x** = sample_s

**n** = number_sample

**M** = population_s

**N** = number_population

 

[]{#related-topics}

