---
title: datatemplatecells.md
original_path: WinForms_Docs/03_Data_Binding/datatemplatecells.md
created_at: 2025-08-05
---






##### Data Template Cells {#data-template-cells style="tab-stops: 0pt"}

This cell builds a custom data template that can be used to set enriched styles for associated cells. The DataTemplateCellModel creates the cell type with a Content Control (a WPF control) by calling the renderer.

 


{border="0"}Note: To create a cell type that hosts a WPF control, you should derive it from GridVirtualizingCellRenderer. The most important method to override is the OnInitializeContent method. It will be called for every UI element created for cells displaying this renderer. You can get access to the cell style from this method.


 

The DataTemplateCellRenderer is derived from GridVirtualizingCellRenderer and overrides OnInitializeContent and sets the Content Control template to Style.CellTemplate value.

 

Example

 

CellModel Class

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                               |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                          |
| [public][ [class] [DataTemplateCellModel] : GridCellModel\<DataTemplateCellRenderer\>] |
|                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

CellRenderer Class

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [public][ [class] [DataTemplateCellRenderer] : GridVirtualizingCellRenderer\<[ContentControl]\>] |
|                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [    [public] DataTemplateCellRenderer()]                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [        IsFocusable = [true];]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [        AllowRecycle = [true];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [    [public] [override] [void] OnInitializeContent([ContentControl] uiElement, GridRenderStyleInfo style)]                     |
|                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [        [base].OnInitializeContent(uiElement, style);]                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [        [bool] found = [false];]                                                                                                                                            |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [        [if] (style.CellTemplateKey != [null])]                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                            |
| [            [DataTemplate] dt = ([DataTemplate])style.GridControl.TryFindResource(style.CellTemplateKey);]                                                            |
|                                                                                                                                                                                                                                                            |
| [            found = dt != [null];]                                                                                                                                                               |
|                                                                                                                                                                                                                                                            |
| [            [if] (found)]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [                uiElement.ContentTemplate = dt;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                            |
| [        }]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [        [if] (!found)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                            |
| [            uiElement.ContentTemplate = style.CellTemplate;]                                                                                                                                                          |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [        uiElement.Content = style.CellValue;]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [    [protected] [override] [string] GetControlTextFromEditorCore([ContentControl] uiElement)]                                  |
|                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [        [return] uiElement.Content.ToString();]                                                                                                                                                  |
|                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Data Template Definition

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][DataTemplate][ x][:][Key][=\"editableEmployee\"\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\<][StackPanel][ Margin][=\"8,0\"][ [ Orientation][=\"Horizontal\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\<][TextBlock][ FontWeight][=\"Bold\"][ syncfusion][:][VisualContainer.WantsMouseInput][=\"False\"][ Text][=\"{][Binding][ Path][=Name}\"][ Width][=\"70\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\<][TextBox][ Text][=\"{][Binding][ Path][=Title}\"][ BorderThickness][=\"0\"][ [ Padding][=\"0\"][ Margin][=\"0\"][ Width][=\"130\"][ x][:][Name][=\"tb\"/\>]]                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\</][StackPanel][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\</][DataTemplate][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Setting up the Data Template Cell and assigning the Cell Template

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                             |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [grid.Model.CellModels.Add([\"DataTemplate\"], [new] DataTemplateCellModel());]                                                       |
|                                                                                                                                                                                                                        |
| [grid.Model.QueryCellInfo += [new] Syncfusion.Windows.Controls.Grid.GridQueryCellInfoEventHandler(Model_QueryCellInfo);]                                      |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [void][ Model_QueryCellInfo([object] sender, Syncfusion.Windows.Controls.Grid.GridQueryCellInfoEventArgs e)] |
|                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [    [if] (e.Cell.RowIndex \> 1 && e.Cell.ColumnIndex == 2)]                                                                                                  |
|                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                            |
|                                                                                                                                                                                                                        |
| [        e.Style.CellType = [\"DataTemplate\"];]                                                                                                           |
|                                                                                                                                                                                                                        |
| [        e.Style.CellTemplateKey = [\"editableEmployee\"];]                                                                                                |
|                                                                                                                                                                                                                        |
| [        e.Style.CellValue = employeesSource.Employees\[e.Cell.RowIndex % employeesSource.Employees.Count\];]                                                                      |
|                                                                                                                                                                                                                        |
| [        e.Style.Background = Brushes.Linen;]                                                                                                                                      |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                            |
|                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Output

[] 

The following output is generated using the code above.

[] 

{border="0"}

Figure 41: Data Template with Cell Template Assigned

***[]*** 


{border="0"}Note: For complete code, please refer to the following browser sample.


 

***\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\Cell Types\\Data Template Cell Demo***

**** 

**** 

[]{#related-topics}

