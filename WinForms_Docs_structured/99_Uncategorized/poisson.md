---
title: poisson.md
original_path: WinForms_Docs/99_Uncategorized/poisson.md
created_at: 2025-08-05
---








  









### POISSON {#poisson style="tab-stops: 0pt"}

 

Returns the Poisson distribution.

 

**Syntax**

 

**POISSON(x, mean, cumulative)**

 

where:

**x** is the number of events.

**mean** is the expected numeric value.

**cumulative** is a logical value that determines the form of the probability distribution returned. If cumulative is True, POISSON returns the cumulative Poisson probability that the number of random events occurring will be between zero and x inclusive; if False, it returns the Poisson probability mass function that the number of events occurring will be exactly x.

 

**Remarks**

 

[·      ]X must be \>= 0.

[·      ]Mean must be \> 0.

[·      ]POISSON is calculated as follows:

 

For cumulative = False:

 

{border="0"}

[] 

For cumulative = True:

[] 

{border="0"}

 

[]{#related-topics}

