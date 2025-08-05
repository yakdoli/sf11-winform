---
title: howtoaccessallthedisplayelementsoraparticulardisplayelementinthegridgroupingcontrol.md
original_path: WinForms_Docs/04_Controls/Grid/howtoaccessallthedisplayelementsoraparticulardisplayelementinthegridgroupingcontrol.md
created_at: 2025-08-05
---






#### How to access all the DisplayElements or a particular DisplayElement in the GridGrouping control {#how-to-access-all-the-displayelements-or-a-particular-displayelement-in-the-gridgrouping-control style="tab-stops: 0pt"}

[] 

You can access the DisplayElements by using the following code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// Accessing all the display elements]                                                                                                         |
|                                                                                                                                                                                                   |
| [foreach][ (Element el [in] gridGroupingControl1.Table.DisplayElements)]                |
|                                                                                                                                                                                                   |
| [{]                                                                                                                                                           |
|                                                                                                                                                                                                   |
| [    [Console].WriteLine(el.Info);]                                                                                                      |
|                                                                                                                                                                                                   |
| [}]                                                                                                                                                           |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// Accessing a particular display element]                                                                                                     |
|                                                                                                                                                                                                   |
| [Console][.WriteLine([this].gridGroupingControl1.Table.DisplayElements\[index\].Info);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\'Accessing all the display element]                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [ [For] [Each] el [As] Element [In] [Me].gridGroupingControl1.Table.DisplayElements] |
|                                                                                                                                                                                                                                   |
| [    Console.WriteLine(el.Info)]                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [ [Next] el]                                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\'Accessing a particular display element]                                                                                                                                      |
|                                                                                                                                                                                                                                   |
| [Console.WriteLine([Me].gridGroupingControl1.Table.DisplayElements(index).Info)]                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p674} 

 

[]{#related-topics}

