---
title: addinglocalizationtoanapplication4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addinglocalizationtoanapplication4.md
created_at: 2025-07-03
---








  









### Adding Localization to an Application {#adding-localization-to-an-application style="tab-stops: 0pt"}

Localization can be achieved by following the steps given below:

1.   OlapClient localization is fully based on the resource (.resx) file generation. Prepare the translated version the strings tabulated below and update it in the resource (.resx) files.

[] 

OlapClient:

 


  ------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------
  [Localization Key][]   [Strings to be localized][]
  Categorical                                                                                                  Categorical
  CategoricalPage                                                                                              Categorical Page
  Chart                                                                                                        Chart
  CubeDimensionBrowser                                                                                         Cube Dimension Browser
  CubeSelector                                                                                                 Cube Selector
  Dialog_AddNewReport                                                                                          Add New Report
  Dialog_Cancel                                                                                                Cancel
  Dialog_ColumnPageSize                                                                                        Column Page Size
  Dialog_ConnectOption                                                                                         Connect Option
  Dialog_CreateNewReport                                                                                       Create New Report
  Dialog_DatabaseName                                                                                          Database Name
  Dialog_ElementsEditor                                                                                        Elements Editor
  Dialog_LoadReport                                                                                            Load Report
  Dialog_MDXQuery                                                                                              MDX Query
  Dialog_OK                                                                                                    OK
  Dialog_PagerSettings                                                                                         Pager Settings
  Dialog_RenameReport                                                                                          Rename Report
  Dialog_ReportName                                                                                            Report Name
  Dialog_RowPageSize                                                                                           Row Page Size
  Dialog_ServerName                                                                                            Server Name
  Expanding                                                                                                    Expanding\...
  Grid                                                                                                         Grid
  Loading                                                                                                      Loading\...
  Measures                                                                                                     Measures
  Report                                                                                                       Report
  Series                                                                                                       Series
  SeriesPage                                                                                                   Series Page
  Slicer                                                                                                       Slicer
  ToolTip_AddNewReport                                                                                         Add a New Report
  ToolTip_AutoExecute                                                                                          AutoExecute
  ToolTip_CheckAll                                                                                             Check All
  ToolTip_ConnectOption                                                                                        Connect Option
  ToolTip_CreateNewReport                                                                                      Create New Report
  ToolTip_Enable3DView                                                                                         Enable 3D View
  ToolTip_EnableDisablePaging                                                                                  Enable / Disable Paging
  ToolTip_ExcelLikeLayout                                                                                      Excel-Like Layout
  ToolTip_ExportToExcel                                                                                        Export To Excel
  ToolTip_ExportToPDF                                                                                          Export To PDF
  ToolTip_ExportToWord                                                                                         Export To Word
  ToolTip_LegendTypes                                                                                          Legend Types
  ToolTip_LoadSavedReport                                                                                      Load Saved Report
  ToolTip_NormalLayout                                                                                         Normal
  ToolTip_NoSummariesLayout                                                                                    No Summaries
  ToolTip_PagerOptions                                                                                         Pager Options
  ToolTip_RemoveSelectedReport                                                                                 Remove the Selected Report
  ToolTip_RenameSelectedReport                                                                                 Rename the Selected Report
  ToolTip_ReportList                                                                                           ReportList
  ToolTip_SaveCurrentReport                                                                                    Save the Current Report
  ToolTip_SelectChartTypes                                                                                     Select Chart Types
  ToolTip_ShowHeaderCellTooltip                                                                                Show HeaderCell ToolTip
  ToolTip_ShowHyperlinkCells                                                                                   Show Hyperlink Cells
  ToolTip_ShowLegends                                                                                          Show Legends
  ToolTip_ShowMDX                                                                                              Show MDX
  ToolTip_UncheckAll                                                                                           Uncheck All
  ------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------


[] 

OlapGrid


  --------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Localization Key][]   [Strings to be localized][]
  Dialog_AddNew                                                                                                                                                         Add New
  Dialog_BackColor                                                                                                                                                      Back Color
  Dialog_Between                                                                                                                                                        Between
  Dialog_BorderColor                                                                                                                                                    Border Color
  Dialog_BorderStyle                                                                                                                                                    Border Style
  Dialog_BorderWidth                                                                                                                                                    Border Width
  Dialog_Cancel                                                                                                                                                         Cancel
  Dialog_Condition                                                                                                                                                      Condition
  Dialog_ConditionalFormatting                                                                                                                                          Conditional Formatting
  Dialog_ConditionType                                                                                                                                                  Condition Type
  Dialog_EditCondition                                                                                                                                                  Edit Condition
  Dialog_Equal                                                                                                                                                          Equal
  Dialog_Font                                                                                                                                                           Font
  Dialog_FontSize                                                                                                                                                       Font Size
  Dialog_Format                                                                                                                                                         Format
  Dialog_Greater                                                                                                                                                        Greater
  Dialog_Lesser                                                                                                                                                         Lesser
  Dialog_Measure                                                                                                                                                        Measure
  Dialog_NotBetween                                                                                                                                                     Not Between
  Dialog_NotEqual                                                                                                                                                       Not Equal
  Dialog_Ok                                                                                                                                                             OK
  Dialog_Operand                                                                                                                                                        Operand
  Dialog_Padding                                                                                                                                                        Padding
  Dialog_Remove                                                                                                                                                         Remove
  Dialog_Reset                                                                                                                                                          Reset
  Dialog_Style                                                                                                                                                          Style
  ToolTip_ApplyFormatting                                                                                                                                               Apply Formatting
  ToolTip_ClearFormatting                                                                                                                                               Clear Formatting
  ToolTip_Column                                                                                                                                                        Column
  ToolTip_ExcelLikeLayout                                                                                                                                               Excel Like Layout
  ToolTip_NormalLayout                                                                                                                                                  Normal Layout
  ToolTip_NormalTopSummaryLayout                                                                                                                                        Normal Top Summary Layout
  ToolTip_NoSummariesLayout                                                                                                                                             No Summaries Layout
  ToolTip_Row                                                                                                                                                           Row
  ToolTip_ShowHideHeaderCellToolTip                                                                                                                                     Show/Hide Header Cell ToolTip
  ToolTip_ShowHideValueCellToolTip                                                                                                                                      Show/Hide Value Cell ToolTip
  ToolTip_Value                                                                                                                                                         Value
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 

2.   Name the resource files as "**OlapClient.*\<locale string representation\>*.resx**" and "**OlapGrid.*\<locale string representation\>*.resx**". For example, French culture can be written as *"OlapClient.fr-FR.resx" and* *"OlapGrid.fr-FR.resx"* and place the resource files in the "App_GlobalResources" folder of the web site.

3.   Change the culture setting of the web page through OlapDataManger by using the following code:

**** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[CS\]]**[]                                                                                                    |
|                                                                                                                                                                                                        |
| [var][ olapDataManager = [new] [OlapDataManager](connectionString);] |
|                                                                                                                                                                                                        |
| [olapDataManager.Culture = [new] System.Globalization.[CultureInfo]([\"fr-FR\"]);]            |
|                                                                                                                                                                                                        |
| [olapDataManager.OverrideDefaultFormatStrings = [true];]                                                                                      |
|                                                                                                                                                                                                        |
| [this][.OlapClient1.OlapDataManager = olapDataManager;]                                                           |
|                                                                                                                                                                                                        |
| [this][.OlapClient1.DataBind();][]                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                   |
|                                                                                                                                                                                                       |
| [Dim][ olapDataManager = [New ][OlapDataManager](connectionString)] |
|                                                                                                                                                                                                       |
| [olapDataManager.Culture = [New] System.Globalization.[CultureInfo]([\"fr-FR\"])]            |
|                                                                                                                                                                                                       |
| [olapDataManager.OverrideDefaultFormatStrings = [True]]                                                                                      |
|                                                                                                                                                                                                       |
| [Me.OlapClient1.OlapDataManager = olapDataManager]                                                                                                                |
|                                                                                                                                                                                                       |
| [Me][.OlapClient1.DataBind()][]                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

