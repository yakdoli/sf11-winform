---
title: usewhereclauseforslicing.md
original_path: WinForms_Docs/99_Uncategorized/usewhereclauseforslicing.md
created_at: 2025-08-05
---








  









### UseWhereClauseForSlicing {#usewhereclauseforslicing style="tab-stops: 0pt"}

The UseWhereClauseForSlicing property facilitates the user to decide whether the MDX query parser engine should consider 'Where' or 'Select' clause for slicing data.

Use Case Scenarios

While slicing dimensions with a specific range of measures using 'Select' clause in MDX query, an exception is thrown. This can be resolved by using the 'Where' clause for slicing.

**Example:**[ ]Slicing the Date dimension from months of 2002 to months of 2003 will throw an exception when 'Select' clause is used.[ ]

Properties

Table 6: Property Table

+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------+-----------------------------+
| Property                                           | Description                                                                                                                                                   | Type                                   | Data Type                         | Reference links             |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------+-----------------------------+
| UseWhereClauseForSlicing[] | Enables the user to decide whether the MDX Query Parser Engine should consider the 'Where' or 'Select' clause for slicing operation[] | Server side[ ] | Boolean[] | []  |
|                                                    |                                                                                                                                                               |                                        |                                   |                             |
|                                                    |                                                                                                                                                               |                                        |                                   | \-\-\--                     |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------+-----------------------------------+-----------------------------+

 

Adding UseWhereClauseForSlicing property to an Application:



[]{#related-topics}

