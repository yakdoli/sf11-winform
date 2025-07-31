---
title: howtocustomizetheborderpropertiesoftheolaparea.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocustomizetheborderpropertiesoftheolaparea.md
created_at: 2025-07-03
---






##### How to customize the border properties of the OlapArea? {#how-to-customize-the-border-properties-of-the-olaparea style="tab-stops: 0pt"}

[] 

OlapArea allows you to customize the border properties. The following code snippets explain how these properties can be customized:

[] 

###### 1.6.1.1.3.1 BorderBrush {#borderbrush style="tab-stops: 0pt"}

[] 

+----------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                     |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
| [this].olapchart1.Series\[0\].Area.BorderBrush = [Brushes].Black; |
|                                                                                                                |
|                                                                                                                |
+----------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                      |
|                                                                                                                 |
|                                                                                                                 |
|                                                                                                                 |
| [      Me].olapchart1.Series(0).Area.BorderBrush = [Brushes].Black |
|                                                                                                                 |
|                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------+

[] 

###### 1.6.1.1.3.2 BorderThickness {#borderthickness style="tab-stops: 0pt"}

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                          |
|                                                                                                                                                     |
|                                                                                                                                                     |
|                                                                                                                                                     |
| [       this].olapchart1.Series\[0\].Area.BorderThickness = [new] [Thickness](2); |
|                                                                                                                                                     |
|                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                    |
|                                                                                                                                               |
|                                                                                                                                               |
|                                                                                                                                               |
| [      Me].olapchart1.Series(0).Area.BorderThickness = [New] [Thickness](2) |
|                                                                                                                                               |
|                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

###### 1.6.1.1.3.3 CornerRadius {#cornerradius style="tab-stops: 0pt"}

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                          |
|                                                                                                                                                     |
|                                                                                                                                                     |
|                                                                                                                                                     |
| [       this].olapchart1.Series\[0\].Area.CornerRadius = [new] [CornerRadius](5); |
|                                                                                                                                                     |
|                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                    |
|                                                                                                                                               |
|                                                                                                                                               |
|                                                                                                                                               |
| [      Me].olapchart1.Series(0).Area.CornerRadius = [New] [CornerRadius](5) |
|                                                                                                                                               |
|                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 28: An OlapArea customized with border color, border thickness, and corner radius[]

[] 

[]{#related-topics}

