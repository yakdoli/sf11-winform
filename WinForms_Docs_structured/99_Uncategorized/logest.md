---
title: logest.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\logest.md
created_at: 2025-07-03
---








  









### LOGEST {#logest style="tab-stops: 0pt"}

 

This feature enables you to calculate predicted exponential growth using existing data.  This calculates and returns an array of values used for the regression analysis. Logest calculates and returns an array of values that is used in regression analysis.

 

Table 13: Method Table


+-----------+------------------------------------------+--------------------------------+------------+-------------+-----------------+
| Method    | Description                              | Parameters                     | Type       | Return Type | Reference links |
+-----------+------------------------------------------+--------------------------------+------------+-------------+-----------------+
| Logest()  | Calculates Logest for an array of cells. | known_y\'s, known_x\'s, const, | **Method** | String      | N/A             |
|           |                                          |                                |            |             |                 |
|           |                                          | stats                          |            |             |                 |
+===========+==========================================+================================+============+=============+=================+


[] 

The following is the formula to calculate Logest for an array of cells in a column:

\[Syntax\]

 

=LOGEST(known_y\'s, \[known_x\'s\], \[const\], \[stats\])

 

Known_y\'s : A set of y-values you already know in a relationship, where y = b\*m\^x.

 

Known_x\'s : An optional set of x-values that you may already know in a relationship, where y = b\*m\^x.

 

Const  :  A logical value specifying whether to force the constant b to equal 1.

 

Stats  : A logical value specifying whether to return additional regression statistics.

 

\[Code\]

 

**=** Logest(B2:B7,A2:A7,TRUE,FALSE)

 

[]{#related-topics}

