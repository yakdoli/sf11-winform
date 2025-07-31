---
title: settingvisualstyle.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\settingvisualstyle.md
created_at: 2025-07-03
---






#### Setting Visual Style {#setting-visual-style style="tab-stops: 0pt"}

[] 

The appearance of the TreeViewAdv control is customized by using the **VisualStyle** property. It gets or sets the visual style for the TreeViewAdv control.

 

The various built-in visual styles are listed below.\
\

[·      ]Blend

[·      ]Office2003

[·      ]Office2007Blue

[·      ]Office2007Black

[·      ]Office2007Silver

[·      ]ShinyBlue

[·      ]ShinyRed

[·      ]SyncOrange

[·      ]VS2010

[·      ]Metro

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<!\--][ Adding TreeViewAdv with visual style ][\--\>]                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion:TreeViewAdv][ ][Name][=][\"[treeViewAdv]\"[ ][syncfusion:SkinStorage.VisualStyle][=]\"[Office2007Blue]\"[\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \<!\--][ Adding TreeViewItemAdv ][\--\>]                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Marital Status]\"[\>]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Single]\"[/\>]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Married]\"[/\>]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Married with Children]\"[/\>]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \</][syncfusion:TreeViewItemAdv][\>]                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Baby Vaccines]\"[\>]]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Hepatitis B]\"[/\>]]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Tetanus]\"[/\>]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Polio]\"[/\>]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Measles]\"[/\>]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \</][syncfusion:TreeViewItemAdv][\>]                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Country Information]\"[\>]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Canada]\"[/\>]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[France]\"[/\>]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[Germany]\"[/\>]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[UK]\"[/\>]]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [    \<][syncfusion:TreeViewItemAdv][ ][Header][=][\"[USA]\"[/\>]]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [  \</][syncfusion:TreeViewItemAdv][\>]                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\</][syncfusion:TreeViewAdv][\>]                                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                |
|                                                                                                                                               |
| []                                                                           |
|                                                                                                                                               |
| [//Setting the visaul style as Office2007Blue ]                             |
|                                                                                                                                               |
| [SkinStorage.SetVisualStyle(treeViewAdv, [\"Office2007Blue\"]); ] |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1133: TreeViewAdv with \"Office2007Blue\" Visual Style

***[]*** 

{border="0"}

***[]*** 

Figure 1134:TreeViewAdv with \"Office2007Black\" Visual Style

***[]*** 

{border="0"}

***[]*** 

Figure 1135:TreeViewAdv with \"Blend\" Visual Style

***[]*** 

{border="0"}

***[]*** 

Figure 1136:TreeViewAdv with \"Office2003\" Visual Style

 

[]{#p599}{border="0"}

Figure 1137:TreeViewAdv with \"Metro\" Visual Style

 

[]{#related-topics}

