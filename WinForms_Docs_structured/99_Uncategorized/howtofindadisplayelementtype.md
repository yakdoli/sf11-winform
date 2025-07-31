---
title: howtofindadisplayelementtype.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtofindadisplayelementtype.md
created_at: 2025-07-03
---






#### How to find a DisplayElement Type {#how-to-find-a-displayelement-type style="tab-stops: 0pt"}

[] 

You can find the type of a particular DisplayElement using the below code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                                   |
| []                                                                                            |
|                                                                                                                                                   |
| [// Accessing the type of display element]                                                      |
|                                                                                                                                                   |
| [Console.WriteLine([this].gridGroupingControl1.Table.DisplayElements\[rowindex\].Kind);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                               |
|                                                                                                                                              |
| []                                                                                       |
|                                                                                                                                              |
| [\' Accessing the type of display element]                                                 |
|                                                                                                                                              |
| [Console.WriteLine([Me].gridGroupingControl1.Table.DisplayElements(rowindex).Kind)] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p676} 

 

[]{#related-topics}

