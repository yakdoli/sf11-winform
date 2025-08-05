---
title: navigationsupport.md
original_path: WinForms_Docs/99_Uncategorized/navigationsupport.md
created_at: 2025-08-05
---






##### Navigation Support {#navigation-support style="tab-stops: 0pt"}

[] 

Navigation to the required url on clicking a particular node is possible by setting the **NavigateUrl** property in the TreeView Designer dialog. By setting the **Target** property, you can monopolize to open the page either in the same window, the same frame or open the page in a new window.

 

For this to be processed the **AutoPostBackOnSelect** property must be set to **True**.

**[]** 


+-----------------------------------+-------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------------+
| NavigateUrl                       | Specifies the url to navigate to.                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------+
| Target                            | Specifies where the target of the url has to be displayed. The options included are as follows: |
|                                   |                                                                                                 |
|                                   | [·      ]self                                                      |
|                                   |                                                                                                 |
|                                   | [·      ]blank                                                     |
|                                   |                                                                                                 |
|                                   | [·      ]FrameName                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------------+


[] 

{border="0"}

**[]** 

Figure 172: NavigateUrl set to Syncfusion\'s homepage and Target set to \'blank\' to open it in a new window

[] 

Programmatically this can be set as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                            |
| []                                                        |
|                                                                                                                            |
| [Tree.AutopostbackOnSelect = [\"True\"];]       |
|                                                                                                                            |
| [NodeP.NavigateUrl = [\"www.syncfusion.com\"];] |
|                                                                                                                            |
| [Tree.Target = [\"\_blank\"];]                  |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                     |
|                                                                                                                                                                                                      |
| []                                                                                                                                  |
|                                                                                                                                                                                                      |
| [Private ][Tree.AutopostbackOnSelect = [\"True\"]]       |
|                                                                                                                                                                                                      |
| [Private][ NodeP.NavigateUrl = [\"www.syncfusion.com\"]] |
|                                                                                                                                                                                                      |
| [Private][ Tree.Target = [\"\_blank\"]]                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

