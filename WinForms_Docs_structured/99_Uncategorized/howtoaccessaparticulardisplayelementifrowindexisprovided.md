---
title: howtoaccessaparticulardisplayelementifrowindexisprovided.md
original_path: WinForms_Docs/99_Uncategorized/howtoaccessaparticulardisplayelementifrowindexisprovided.md
created_at: 2025-08-05
---






#### How to access a particular DisplayElement if RowIndex is provided {#how-to-access-a-particular-displayelement-if-rowindex-is-provided style="tab-stops: 0pt"}

[] 

You can access the DisplayElements with the rowindex, by using the following code.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                     |
|                                                                                                                                                    |
| []                                                                                             |
|                                                                                                                                                    |
| [// Accessing a particular display element]                                                      |
|                                                                                                                                                    |
| [Element el=[this].gridGroupingControl1.Table.DisplayElements\[rowindex\].ParentElement;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [\' Accessing a particular display element]                                                                                                                                    |
|                                                                                                                                                                                                                                  |
| [Dim][ el [As] Element = [Me].gridGroupingControl1.Table.DisplayElements(rowindex).ParentElement] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p675} 

 

[]{#related-topics}

