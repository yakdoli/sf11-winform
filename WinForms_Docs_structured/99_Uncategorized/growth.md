---
title: growth.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\growth.md
created_at: 2025-07-03
---








  









### GROWTH {#growth style="tab-stops: 0pt"}

 

This feature enables you to calculate predicted exponential growth using existing data.  This calculates and returns an array of values used for the regression analysis. Growth enables you to perform a regression analysis.

     Table 2: Method Table


  Method     Description                                    Parameters                                                                                                    Type     Return Type   Reference links
  ---------- ---------------------------------------------- ------------------------------------------------------------------------------------------------------------- -------- ------------- -----------------
  Growth()   Calculates the Growth for an array of cells.   [Known y's, Known x's, new_x\'s]   Method   String        N/A


 

The following is the formula to calculate Growth for an array of cells in a column:

\[Syntax\]

 

[=GROWTH(known_y\'s, \[known_x\'s\], \[new_x\'s\], ]

[] 

**[Known_y\'s]**[: A set of y-values you already know in a relationship, where y = b\*m\^x.]

[] 

Known_x\'s: An optional set of x-values that you may already know in the relationship, where y = b\*m\^x.

 

**[New_x\'s:]**[ New x-values for which you want GROWTH to return corresponding y-values.]

[] 

[] 

\[Code\]

 

**=**Growth(B2:B7,A2:A7,C6:C7)

 

[]{#related-topics}

