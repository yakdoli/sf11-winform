---
title: settingvisualstylesfordocumentcontainer1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\settingvisualstylesfordocumentcontainer1.md
created_at: 2025-07-03
---






#### Setting Visual Styles for Document Container {#setting-visual-styles-for-document-container style="tab-stops: 0pt"}

Document Container comes with the support of visual styles, which gives a great look and feel for the Document Container and enhances the overall appearance of the end user\'s applications. The visual style for the Document Container is set by using the **VisualStyle** property.

 

+-----------------------------------+---------------------------------------------------------------------------------------+
| Property                          | Description                                                                           |
+-----------------------------------+---------------------------------------------------------------------------------------+
| VisualStyle                       | Sets the visual style for the DocumentContainer. The options provided are as follows. |
|                                   |                                                                                       |
|                                   | []  |
|                                   |                                                                                       |
|                                   | [·      ]Blend                                           |
|                                   |                                                                                       |
|                                   | [·      ]Office2003                                      |
|                                   |                                                                                       |
|                                   | [·      ]Office2007Blue                                  |
|                                   |                                                                                       |
|                                   | [·      ]Office2007Black                                 |
|                                   |                                                                                       |
|                                   | [·      ]Office2007Silver                                |
|                                   |                                                                                       |
|                                   | [·      ]ShinyBlue                                       |
|                                   |                                                                                       |
|                                   | [·      ]ShinyRed                                        |
|                                   |                                                                                       |
|                                   | [·      ]SyncOrange                                      |
|                                   |                                                                                       |
|                                   | [·      ]VS2010                                          |
|                                   |                                                                                       |
|                                   | [·      ]Metro                                           |
|                                   |                                                                                       |
|                                   |                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------+

 

Use the following code to set the skin for the Document Container.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<!\--][ Adding document container ][\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion:DocumentContainer][ ][Name][=][\"[DocContainer]\"[ ][syncfusion:SkinStorage.VisualStyle][=]\"[Office2007Blue]\"[ ][Mode][=]\"[MDI]\"[\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [  ...\....]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [  ...\....]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][syncfusion:DocumentContainer][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [ ][// Setting the visual style as Office2007Blue ] |
|                                                                                                                                                       |
| [SkinStorage.SetVisualStyle(DocContainer, [\"Office2007Blue\"]);  ]                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 405: Document Container with \"Office2007Blue\" Theme

 

***[]*** 

{border="0"}

Figure 406: Document Container with \"Blend\" Theme

***[]*** 

***[]*** 

{border="0"}

Figure 407: Document Container with \"Office2003\" Theme

 

[]{#p226}{border="0"}

Figure 408: Document Container with \"Metro\" Theme

 

[]{#related-topics}

