---
title: howtotogglethevisibilityoftheprimaryaxislabelpanel.md
original_path: WinForms_Docs/99_Uncategorized/howtotogglethevisibilityoftheprimaryaxislabelpanel.md
created_at: 2025-08-05
---






##### How to toggle the visibility of the PrimaryAxis LabelPanel {#how-to-toggle-the-visibility-of-the-primaryaxis-labelpanel style="tab-stops: 0pt"}

[] 

The PrimaryAxisLabelPanel visibility can be toggled by setting the *PrimaryAxisLabelVisibility* property.

The following code snippet is used to collapse the PrimaryAxis label:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][OlapChart][ Name][=\"olapchart1\"][ PrimaryAxisLabelVisibility][=\"Collapsed\" /\>] |
|                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                         |
|                                                                                                                                    |
|                                                                                                                                    |
|                                                                                                                                    |
| [this].olapchart1.PrimaryAxisLabelVisibility = System.Windows.[Visibility].Collapsed; |
|                                                                                                                                    |
|                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                      |
|                                                                                                                                 |
|                                                                                                                                 |
|                                                                                                                                 |
| [Me].olapchart1.PrimaryAxisLabelVisibility = System.Windows.[Visibility].Collapsed |
|                                                                                                                                 |
|                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------+

 

The following illustration shows how the OlapChart will look after collapsing the PrimaryAxis label.

 

{border="0"}

Figure 37: Before and After collapsing primary axis label

[] 

[]{#related-topics}

