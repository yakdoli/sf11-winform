---
title: throughcode1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode1.md
created_at: 2025-07-03
---








  









### Through Code {#through-code style="tab-stops: 0pt"}

[] 

The below code snippets illustrates the creation of GridGroupingControl programmatically.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [using][ Syncfusion.Web.UI.WebControls.Grid.Grouping;]                                                                                                    |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [public][ [partial] [class] [\_Default] : System.Web.UI.[Page]] |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [    [protected] [void] Page_Load([object] sender, [EventArgs] e)]                                                  |
|                                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                |
| [        [GridGroupingControl] GridGroupingControl1 = [new] [GridGroupingControl]();]                                                 |
|                                                                                                                                                                                                                                                |
| [        GridGroupingControl1.Autoformat= [\"Vista\"];]                                                                                                                            |
|                                                                                                                                                                                                                                                |
| [        [this].Controls.Add(GridGroupingControl1);]                                                                                                                                  |
|                                                                                                                                                                                                                                                |
| [        GridGroupingControl1.DataSource=AccessDataSource1;]                                                                                                                                               |
|                                                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| [Imports][ Syncfusion.Web.UI.WebControls.Grid.Grouping]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| [Partial][ [Public] [Class] \_Default : [Inherits] System.Web.UI.Page]                                                                                |
|                                                                                                                                                                                                                                                                                                           |
| [Protected][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]  |
|                                                                                                                                                                                                                                                                                                           |
| [Dim][ GridGroupingControl1 [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridGroupingControl = [New]Syncfusion.Web.UI.WebControls.Grid.Grouping.GridGroupingControl()] |
|                                                                                                                                                                                                                                                                                                           |
| [GridGroupingControl1.Autoformat = [\"Vista\"]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                           |
| [Me][.Controls.Add(GridGroupingControl1)]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| [GridGroupingControl1.DataSource = AccessDataSource1]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                           |
| [End][ [Class]]                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p18} 

 

[]{#related-topics}

