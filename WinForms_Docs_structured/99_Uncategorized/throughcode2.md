---
title: throughcode2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode2.md
created_at: 2025-07-03
---






##### [Through Code] {#through-code style="tab-stops: 0pt"}

[] 

This tutorial shows how to create RichTextEditor control programmatically.

To create RichTextEditor control through ASP.NET code, follow the below given steps.

[] 

1.   Open **ASP.NET** web application.

2.   In code view, add following subroutines to handle the page load event.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                  |
| [using][ System;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [// add **using** deractive to have quality the use type of Syncfusion RichTextEditor]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [using][ Syncfusion.Web.UI.WebControls.Tools;]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [public][ [partial] [class] [CreatingRichTextEditorThroughCode] : System.Web.UI.[Page]] |
|                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                  |
| [       [protected] [void] Page_Load([object] sender, [EventArgs] e)]                                                                                    |
|                                                                                                                                                                                                                                                                                                  |
| [       {]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| [              CreateRichTextEditor();]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                  |
| [       }]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [       [private] [void] CreateRichTextEditor()]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| [       {]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| [              [//Create new RichTextEditor control]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                  |
| [              [RichTextEditor] RTE1 = [new] [RichTextEditor]();]                                                                                                             |
|                                                                                                                                                                                                                                                                                                  |
| [              RTE1.ID=[\"richTextEditor1\"];]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [              [//Set some RichTextEditor\'s properties programatically]]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                  |
| [              RTE1.Text = [\"Some started text\"];         ]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [              [//add RichTextEditor control to Form]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                  |
| [              form1.Controls.Add( RTE1 );]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                  |
| [       }]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Run the application.

[] 

The result will be displayed as follows.

[] 

{border="0"}

Figure 78

 

[]{#related-topics}

