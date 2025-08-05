---
title: howtoviewthehiddenitemsinagroupviewprogrammatically.md
original_path: WinForms_Docs/99_Uncategorized/howtoviewthehiddenitemsinagroupviewprogrammatically.md
created_at: 2025-08-05
---






##### How to view the hidden Items in a GroupView programmatically {#how-to-view-the-hidden-items-in-a-groupview-programmatically style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

GroupView\'s **BringItemIntoView** method can be used to scroll down to a hidden item and bring that item into view.

 

The following code snippet illustrates this.

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                                 |
| []                                                                            |
|                                                                                                                                 |
| [this][.groupView1.SelectedItem = 20; ]    |
|                                                                                                                                 |
| [// This will scroll to Item 20. ]                                            |
|                                                                                                                                 |
| [this][.groupView1.BringItemIntoView(20);] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                           |
|                                                                                                                              |
| []                                                                         |
|                                                                                                                              |
| [Me][.groupView1.SelectedItem = 20]     |
|                                                                                                                              |
| [\' This will scroll to Item 20. ]                                         |
|                                                                                                                              |
| [Me][.groupView1.BringItemIntoView(20)] |
+------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p663} 

 

[]{#related-topics}

