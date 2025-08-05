---
title: howtocustomizethebackgroundpropertiesoftheolaparea.md
original_path: WinForms_Docs/99_Uncategorized/howtocustomizethebackgroundpropertiesoftheolaparea.md
created_at: 2025-08-05
---






##### How to customize the background properties of the OlapArea? {#how-to-customize-the-background-properties-of-the-olaparea style="tab-stops: 0pt"}

[] 

OlapArea allows you to customize the background properties in an easy manner. The following code snippets explain how to customize the OlapArea with various background properties:

 

###### 1.6.1.1.4.1 Background {#background style="tab-stops: 0pt"}

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                             |
|                                                                                                                        |
|                                                                                                                        |
|                                                                                                                        |
| [       this].olapchart1.Series\[0\].Area.Background = [Brushes].SkyBlue; |
|                                                                                                                        |
|                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                               |
|                                                                                                                                          |
|                                                                                                                                          |
|                                                                                                                                          |
| [       ][Me].olapchart1.Series(0).Area.Background = [Brushes].SkyBlue |
|                                                                                                                                          |
|                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

###### 1.6.1.1.4.2 GridBackground {#gridbackground style="tab-stops: 0pt"}

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                   |
|                                                                                                                              |
|                                                                                                                              |
|                                                                                                                              |
| [       this].olapchart1.Series\[0\].Area.GridBackground = [Brushes].LightBlue; |
|                                                                                                                              |
|                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                     |
|                                                                                                                                                |
|                                                                                                                                                |
|                                                                                                                                                |
| [       ][Me].olapchart1.Series(0).Area.GridBackground = [Brushes].LightBlue |
|                                                                                                                                                |
|                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

 

Figure 29: An OlapArea of the OlapChart with customized Background and GridBackground

[] 

[]{#related-topics}

