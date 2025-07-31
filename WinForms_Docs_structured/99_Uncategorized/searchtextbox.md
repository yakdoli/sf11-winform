---
title: searchtextbox.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\searchtextbox.md
created_at: 2025-07-03
---








  









### Search TextBox {#search-textbox style="tab-stops: 0pt"}

[] 

The main advantage of the Search TextBox is to search for text in the data displayed in the grid. It is displayed on top of the GroupDrop area. This works like the \"Find\" in the text editor application. The user can effectively use this feature for finding the Search strings.

[] 

Through Designer

[] 

To activate the Search TextBox from the designer, set the **ShowSearchBox** property to **True** in the Properties window.

[] 

{border="0"}

Figure 82

[] 

Through Code

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][syncfusion][:][GridGroupingControl][ [ID][=\"GridGroupingControl2\"] [runat][=\"server\"] [BorderCollapse][=\"Separate\"] [ClientSideColumnResizing][=\"False\"] [DragSelectionBackColor][=\"Yellow\"] [DataSourceID][=\"AccessDataSource1\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][TopLevelGroupOptions][ [CacheValues][=\"False\"] [ShowFilterBarTextCell][=\"True\"] [/\>]]                                                                                                                                                                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [using][ Syncfusion.Web.UI.WebControls.Grid.Grouping;]                                                                                               |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [public][ [partial] [class] [\_Default] : System.Web.UI.[Page] ] |
|                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                           |
| [    [protected] [void] Page_Load([object] sender, [EventArgs] e)]                                                |
|                                                                                                                                                                                                                                           |
| [    {]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [      [GridGroupingControl] GridGroupingControl1 = [new] [GridGroupingControl]();]                                                    |
|                                                                                                                                                                                                                                           |
| [      GridGroupingControl1.ShowSearchBox = [true];]                                                                                                                             |
|                                                                                                                                                                                                                                           |
| [      GridGroupingControl1.DataSource = AccessDataSource1;]                                                                                                                                          |
|                                                                                                                                                                                                                                           |
| [      [this].Controls.Add(GridGroupingControl1);]                                                                                                                               |
|                                                                                                                                                                                                                                           |
| [    ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                           |
| [    }]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [Imports][ Syncfusion.Web.UI.WebControls.Grid.Grouping]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [Partial][ [Public] [Class] \_Default : [Inherits] System.Web.UI.Page]                                                                                 |
|                                                                                                                                                                                                                                                                                                            |
| [Protected][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]   |
|                                                                                                                                                                                                                                                                                                            |
| [Dim][ GridGroupingControl1 [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridGroupingControl = [New] Syncfusion.Web.UI.WebControls.Grid.Grouping.GridGroupingControl()] |
|                                                                                                                                                                                                                                                                                                            |
| [GridGroupingControl1.ShowSearchBox = [True]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [GridGroupingControl1.DataSource = AccessDataSource1]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                            |
| [Me][.Controls.Add(GridGroupingControl1)]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| [End][ [Class]]                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p70} 

[]{#related-topics}

