---
title: customdropdowncells.md
original_path: WinForms_Docs/99_Uncategorized/customdropdowncells.md
created_at: 2025-08-05
---






##### Custom Drop-down Cells {#custom-drop-down-cells style="tab-stops: 0pt"}

[]{#p194}This cell displays customized drop-downs in grid cells. To attach a drop-down to a grid cell, you need to derive from GridCellDropDownCellModel and GridCellDropDownCellRenderer classes.

 

Example

For example, let us create a custom drop-down which lists an image alongside text in each entry and sets the text of the current drop-down selection as the cell value. The cellmodel class just creates the cell type by calling the cellrenderer. The cellrenderer then loads the cell with ImageTextListBoxItem (a custom control having two properties, Image and Text) to show image alongside text. The renderer then overrides the ArrangeUIElement method in order to bind the drop down to the data source, which is a collection of ImageTextListBoxItem and sets its current selection based on current cell value. It triggers the ComboBoxSelectionChanged event to set the new cell value based on the current drop-down selection.

 

CellModel class

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [public][ [class] [CustomeDropDownCellModel] : GridCellDropDownCellModel\<CustomDropDownRenderer\>] |
|                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

CellRenderer Class

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [public][ [class] [CustomDropDownRenderer] : GridCellDropDownCellRenderer\<CustomeDropDown\>]                                      |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [    [private] CustomeDropDownCellModel CustomDropDownModel]                                                                                                                                                |
|                                                                                                                                                                                                                                                                      |
| [    {]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [        [get]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [            [return] [this].CellModel [as] CustomeDropDownCellModel;]                                                                                            |
|                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [    }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [    [public] [override] [void] OnInitializeContent(CustomeDropDown dropDownControl, GridRenderStyleInfo style)]                                                  |
|                                                                                                                                                                                                                                                                      |
| [    {]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [        [if] (dropDownControl.ListBoxPart != [null])]                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [            dropDownControl.ListBoxPart.SelectionChanged -= [this].OnComboBoxSelectionChanged;]                                                                                                            |
|                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [        [base].OnInitializeContent(dropDownControl, style);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [    }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [    [protected] [override] [void] ArrangeUIElement(Syncfusion.Windows.Controls.Cells.ArrangeCellArgs aca, CustomeDropDown uiElement, GridRenderStyleInfo style)] |
|                                                                                                                                                                                                                                                                      |
| [    {]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [        [base].ArrangeUIElement(aca, uiElement, style);]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [        [var] dropDownControl = uiElement;]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                      |
| [        [if] (style.ItemsSource != [null])]                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [            dropDownControl.ListBoxPart.ItemsSource = [this].CustomDropDownModel.GetDataSource(style);]                                                                                                    |
|                                                                                                                                                                                                                                                                      |
| [            dropDownControl.ListBoxPart.DisplayMemberPath = style.HasDisplayMember ? style.DisplayMember : [string].Empty;]                                                                                |
|                                                                                                                                                                                                                                                                      |
| [            dropDownControl.ListBoxPart.SelectedValue = [this].GetControlValue(style);]                                                                                                                    |
|                                                                                                                                                                                                                                                                      |
| [            [if] (style.HasValueMember)]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [            {]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [                dropDownControl.ListBoxPart.SelectedValuePath = style.ValueMember;]                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [            }]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [        uiElement.ListBoxPart.SelectionChanged += [this].OnComboBoxSelectionChanged;]                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [    }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [    [protected] [override] [void] SetSelectedIndex([int] index)]                                                                            |
|                                                                                                                                                                                                                                                                      |
| [    {]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [        [if] (index != [this].CurrentCellUIElement.ListBoxPart.SelectedIndex)]                                                                                                        |
|                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [            [this].CurrentCellUIElement.ListBoxPart.SelectedIndex = index;]                                                                                                                                |
|                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [    }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [    [private] [void] OnComboBoxSelectionChanged([object] sender, [SelectionChangedEventArgs] e)]                                         |
|                                                                                                                                                                                                                                                                      |
| [    {]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [        [if] (e.AddedItems.Count \> 0)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [            [var] item = e.AddedItems\[0\].ToString();]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                      |
| [            [this].CustomDropDownModel.ListModel.CurrentIndex = [this].CustomDropDownModel.FindValue([this].CurrentStyle, item);]                                |
|                                                                                                                                                                                                                                                                      |
| [            ]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [            [if] (\![this].AlreadyTextChanged)]                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [            {]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [                [this].CurrentCellUIElement.TextBoxPart.Text = item;]                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [            }]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [    }]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Custom Drop-down control

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                    |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [public][ [class] [CustomeDropDown] : GridCellDropDownControlBase]          |
|                                                                                                                                                                                                               |
| [{]                                                                                                                                                                       |
|                                                                                                                                                                                                               |
| [    [public] ImageTextListBox ListBoxPart]                                                                                                          |
|                                                                                                                                                                                                               |
| [    {]                                                                                                                                                                   |
|                                                                                                                                                                                                               |
| [        [get]]                                                                                                                                      |
|                                                                                                                                                                                                               |
| [        {]                                                                                                                                                               |
|                                                                                                                                                                                                               |
| [            [if] ([this].PopupContent != [null])]                                                         |
|                                                                                                                                                                                                               |
| [            {]                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [                [return] [this].PopupContent.Content [as] ImageTextListBox;]                              |
|                                                                                                                                                                                                               |
| [            }]                                                                                                                                                           |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [            [return] [null];]                                                                                                  |
|                                                                                                                                                                                                               |
| [        }]                                                                                                                                                               |
|                                                                                                                                                                                                               |
| [    }]                                                                                                                                                                   |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [    [public] [override] [void] OnApplyTemplate()]                                                         |
|                                                                                                                                                                                                               |
| [    {]                                                                                                                                                                   |
|                                                                                                                                                                                                               |
| [        [base].OnApplyTemplate();]                                                                                                                  |
|                                                                                                                                                                                                               |
| [    }]                                                                                                                                                                   |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [    [protected] [override] [void] OnContentLoaded([ContentControl] popupContent)] |
|                                                                                                                                                                                                               |
| [    {]                                                                                                                                                                   |
|                                                                                                                                                                                                               |
| [        ImageTextListBox l = [new] ImageTextListBox([this]);]                                                                  |
|                                                                                                                                                                                                               |
| [        l.Height = 200;]                                                                                                                                                 |
|                                                                                                                                                                                                               |
| [        popupContent.Content = l;]                                                                                                                                       |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [        [// this will wire the events in the base implementation]]                                                                                 |
|                                                                                                                                                                                                               |
| [        [base].OnContentLoaded(popupContent);]                                                                                                      |
|                                                                                                                                                                                                               |
| [    }]                                                                                                                                                                   |
|                                                                                                                                                                                                               |
| [}]                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Associate this Cell Type to the Grid

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                    |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [// Registering the cell model]                                                                                                                                             |
|                                                                                                                                                                                                                               |
| [this][.grid.Model.CellModels.Add([\"CustomDropDown\"], [new] CustomeDropDownCellModel());] |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [// Binding the celltype]                                                                                                                                                   |
|                                                                                                                                                                                                                               |
| [var dropdown1 = [this].grid.Model\[7, 2\];]                                                                                                                         |
|                                                                                                                                                                                                                               |
| [dropdown1.CellType = [\"CustomDropDown\"];]                                                                                                                      |
|                                                                                                                                                                                                                               |
| [dropdown1.ItemsSource = GenerateListBoxContent();]                                                                                                                                       |
|                                                                                                                                                                                                                               |
| [dropdown1.DisplayMember = [\"Text\"];]                                                                                                                           |
|                                                                                                                                                                                                                               |
| [dropdown1.DropDownStyle = GridDropDownStyle.Editable;]                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The following output is generated using the code above.

 

{border="0"}

Figure 40: Custom Drop-down

 


{border="0"}Note: For complete code, please refer to the following browser sample.


 

***\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\Cell Types\\Custom Drop Down Demo***

**** 

**** 

[]{#related-topics}

