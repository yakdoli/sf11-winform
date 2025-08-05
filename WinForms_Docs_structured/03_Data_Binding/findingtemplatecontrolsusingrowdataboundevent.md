---
title: findingtemplatecontrolsusingrowdataboundevent.md
original_path: WinForms_Docs/03_Data_Binding/findingtemplatecontrolsusingrowdataboundevent.md
created_at: 2025-08-05
---








  









### Finding Template controls using RowDataBound Event {#finding-template-controls-using-rowdatabound-event style="tab-stops: 0pt"}

[] 

You can find the TemplateControls through **RowDataBound** event using **FindControl** method. Refer the below code snippet which illustrates this.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][sfwg][:][GridColumnDescriptor][ [MappingName][=\"Name\"\>]]                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\<][ItemTemplate][\>]]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        [\<][asp][:][TextBox] [ID][=\"TextBox1\"] [runat][=\"server\"\>\</][asp][:][TextBox][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\</][ItemTemplate][\>] ]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][sfwg][:][GridColumnDescriptor][\>]                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [void][ GridGroupingControl1_RowDataBound([object] sender, Syncfusion.Web.UI.WebControls.Grid.Grouping.RowDataBoundEventArgs e)] |
|                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [    [for] ([int] i = 0; i \< e.Row.Cells.Count; i++)]                                                                                                       |
|                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| [        [if] (((Syncfusion.Web.UI.WebControls.Grid.Grouping.GridCell)(e.Row.Cells\[i\])).ColumnDescriptor != [null])]                                       |
|                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| [            [if] (((Syncfusion.Web.UI.WebControls.Grid.Grouping.GridCell)(e.Row.Cells\[i\])).ColumnDescriptor.Name == [\"Name\"])]                        |
|                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                            |
| [                TextBox textbox = (TextBox)e.Row.Cells\[i\].FindControl([\"TextBox1\"]);]                                                                                      |
|                                                                                                                                                                                                                                            |
| [                [if] (textbox != [null])]                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [                {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [                }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [            }]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] GridGroupingControl1_RowDataBound([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Web.UI.WebControls.Grid.Grouping.RowDataBoundEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [    [For] i [As] [Integer] = 0 [To] e.Row.Cells.Count - 1]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [        [If] ([CType](e.Row.Cells(i), Syncfusion.Web.UI.WebControls.Grid.Grouping.GridCell)).ColumnDescriptor [IsNot] [Nothing] [Then]]                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [            [If] ([CType](e.Row.Cells(i), Syncfusion.Web.UI.WebControls.Grid.Grouping.GridCell)).ColumnDescriptor.Name = [\"Name\"] [Then]]                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [                [Dim] textbox [As] TextBox = [CType](e.Row.Cells(i).FindControl([\"TextBox1\"]), TextBox)]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [                [If] textbox [IsNot] [Nothing] [Then]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [                [End] [If]]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [            [End] [If]]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [        [End] [If]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [    [Next] i]                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p94} 

[]{#related-topics}

