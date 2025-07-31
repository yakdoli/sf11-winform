---
title: numericvalue.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\numericvalue.md
created_at: 2025-07-03
---






#### Numeric Value {#numeric-value style="tab-stops: 0pt"}

 

Rolling Gauge can be restricted to display only the numeric values.

 

 


+-------------+----------------------------------------------------------------------------------------+-------------------------------+-------------------------------+------------------------------------------------------+
| Property    | Description                                                                            | Type of Property              | Value It Accepts              | Any other dependencies/Sub properties associated     |
+-------------+----------------------------------------------------------------------------------------+-------------------------------+-------------------------------+------------------------------------------------------+
| IsNumeric   | Sets to accept only the numeric values.                                                | [bool]   | [True]   | NA                                                   |
|             |                                                                                        |                               |                               |                                                      |
|             |                                                                                        |                               | []       |                                                      |
|             |                                                                                        |                               |                               |                                                      |
|             |                                                                                        |                               | [false]  |                                                      |
+-------------+----------------------------------------------------------------------------------------+-------------------------------+-------------------------------+------------------------------------------------------+
| MaxValue    | If IsNumeric is set to true then the MaxValue Property acts as MaximunRange for Value. | [double] | [double] | Dependency Property(dependent on IsNumeric property) |
+-------------+----------------------------------------------------------------------------------------+-------------------------------+-------------------------------+------------------------------------------------------+
| MinValue    | If IsNumeric is set to true then the MinValue Property acts as MinimumRange for Value. | [double] | [double] | Dependency Property(dependent on IsNumeric property) |
+-------------+----------------------------------------------------------------------------------------+-------------------------------+-------------------------------+------------------------------------------------------+


[] 

More:







