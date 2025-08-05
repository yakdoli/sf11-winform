---
title: addinglocalizationtoanapplication5.md
original_path: WinForms_Docs/99_Uncategorized/addinglocalizationtoanapplication5.md
created_at: 2025-08-05
---








  





### Adding Localization to an Application {#adding-localization-to-an-application style="tab-stops: 0pt"}

Localization can be achieved by following the steps given below:

[1.    ]OlapGrid localization is fully based on the resource (.resx) file generation. Prepare a translated version of the strings tabulated below and update it in the resource (.resx) file.

 


  ----------------------------------- -------------------------------
  **Localization Key**                **Strings to be Localized**
  Dialog_AddNew                       Add New
  Dialog_BackColor                    Back Color
  Dialog_Between                      Between
  Dialog_BorderColor                  Border Color
  Dialog_BorderStyle                  Border Style
  Dialog_BorderWidth                  Border Width
  Dialog_Cancel                       Cancel
  Dialog_Condition                    Condition
  Dialog_ConditionalFormatting        Conditional Formatting
  Dialog_ConditionType                Condition Type
  Dialog_EditCondition                Edit Condition
  Dialog_Equal                        Equal
  Dialog_Font                         Font
  Dialog_FontSize                     Font Size
  Dialog_Format                       Format
  Dialog_Greater                      Greater
  Dialog_Lesser                       Lesser
  Dialog_Measure                      Measure
  Dialog_NotBetween                   Not Between
  Dialog_NotEqual                     Not Equal
  Dialog_Ok                           OK
  Dialog_Operand                      Operand
  Dialog_Padding                      Padding
  Dialog_Remove                       Remove
  Dialog_Reset                        Reset
  Dialog_Style                        Style
  ToolTip_ApplyFormatting             Apply Formatting
  ToolTip_ClearFormatting             Clear Formatting
  ToolTip_Column                      Column
  ToolTip_ExcelLikeLayout             Excel Like Layout
  ToolTip_NormalLayout                Normal Layout
  ToolTip_NormalTopSummaryLayout      Normal Top Summary Layout
  ToolTip_NoSummariesLayout           No Summaries Layout
  ToolTip_Row                         Row
  ToolTip_ShowHideHeaderCellToolTip   Show/Hide Header Cell ToolTip
  ToolTip_ShowHideValueCellToolTip    Show/Hide Value Cell ToolTip
  ToolTip_Value                       Value
  ----------------------------------- -------------------------------


 

[2.    ]Name the resource file as **OlapGrid.*\<locale string representation\>*.resx**. For example, French culture can be written as **OlapGrid.fr-FR.resx** and place the resource file in the **App_GlobalResources** folder of the Web site.

[3.    ]Change the culture setting of the Web page through OlapDataManger by using the following code:

**** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                        |
| [var][ olapDataManager = [new] [OlapDataManager](connectionString);] |
|                                                                                                                                                                                                        |
| [olapDataManager.Culture = [new] System.Globalization.[CultureInfo]([\"fr-FR\"]);]            |
|                                                                                                                                                                                                        |
| [olapDataManager.OverrideDefaultFormatStrings = [true];]                                                                                      |
|                                                                                                                                                                                                        |
| [this][.OlapGrid1.OlapDataManager = olapDataManager;]                                                             |
|                                                                                                                                                                                                        |
| [this][.OlapGrid1.DataBind();][]                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                      |
|                                                                                                                                                                                                       |
| [Dim][ olapDataManager = [New ][OlapDataManager](connectionString)] |
|                                                                                                                                                                                                       |
| [olapDataManager.Culture = [New] System.Globalization.[CultureInfo]([\"fr-FR\"])]            |
|                                                                                                                                                                                                       |
| [olapDataManager.OverrideDefaultFormatStrings = [True]]                                                                                      |
|                                                                                                                                                                                                       |
| [Me.OlapGrid1.OlapDataManager = olapDataManager]                                                                                                                  |
|                                                                                                                                                                                                       |
| [Me][.OlapGrid1.DataBind()][]                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

