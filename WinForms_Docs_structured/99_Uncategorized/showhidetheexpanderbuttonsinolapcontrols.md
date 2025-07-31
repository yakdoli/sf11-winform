---
title: showhidetheexpanderbuttonsinolapcontrols.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\showhidetheexpanderbuttonsinolapcontrols.md
created_at: 2025-07-03
---








  









## Show/hide the Expander buttons in OLAP controls {#showhide-the-expander-buttons-in-olap-controls style="tab-stops: 0pt"}

There is a property in **OlapReport** called **ShowExpanders,** which is used to show/hide the expander buttons in the OLAP controls. By using this property, we can disable or enable the drill down/up behavior of the OLAP control.

To show the Expanders:

+-----------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                              |
|                                                                                               |
| []                                                        |
|                                                                                               |
| [ [//// Displaying the Expander button in Controls]\                    |
|  olapReport.ShowExpanders = [true];] |
|                                                                                               |
| []                                                        |
+-----------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                           |
|                                                                                                                                            |
| []                                                                                                     |
|                                                                                                                                            |
| [\'\'\'Displaying the Expander button in Controls][] |
|                                                                                                                                            |
| [olapReport.ShowExpanders = [True][ ]]                      |
|                                                                                                                                            |
| []                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 

To hide the Expanders:

+------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                               |
|                                                                                                |
| []                                                         |
|                                                                                                |
| [ [//// Displaying the Expander button in Controls]\                     |
|  olapReport.ShowExpanders = [false];] |
|                                                                                                |
| []                                                         |
+------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                           |
|                                                                                                                                            |
| []                                                                                                     |
|                                                                                                                                            |
| [\'\'\'Displaying the Expander button in Controls][] |
|                                                                                                                                            |
| [olapReport.ShowExpanders = [false][ ]]                     |
|                                                                                                                                            |
| []                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

