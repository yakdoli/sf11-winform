---
title: virtualcells.md
original_path: WinForms_Docs/99_Uncategorized/virtualcells.md
created_at: 2025-08-05
---






#### Virtual Cells {#virtual-cells style="tab-stops: 0pt"}

The Grid control supports virtual cell architecture where the cell contents are drawn statically until a live cell is required. For example, when you move the mouse over the grid, the cells under the mouse pointer needs to handle mouse inputs. Dynamically, the static cells are turned into live cells that can handle those mouse interactions, as required. These live cells stay in scope until they are no longer needed (which is usually when they are scrolled off the screen). Using static drawing for cells, and thus minimizing the need for large numbers of live cells, provides an optimal way to display large data sources very quickly.

 

Example

 

The given cell model and the renderer hosts a virtual cell editor inside the grid cell and this cell type is used or activated only when you move your mouse over any grid cell. By default, a grid cell displays a text that is set in OnRender overridden method. When you move the mouse over this cell, it will become a live UIElement editor and not render the cell anymore. This cell is now a virtual cell that will display the cell value stored in the internal cell structure, say, "Edit Me".

 

But, when you scroll the cell outside the view port, it will switch back to a normal renderer cell. When you move the mouse over this cell again, it will display "Edit Me".

 

Placing a UIElement as soon as a cell becomes visible is a time consuming process, while static rendering of a text is faster. The UI element which is required to edit the cell will be placed only on demand (that is when you hover or click a cell for editing). Hence, this approach will greatly improve the scrolling speed.

This mechanism will be enabled only if you set SupportsRenderOptimization property to true in the constructor.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [public][ [class] [VirtualizedCellModel] : GridCellModel\<[VirtualizedCellRenderer]\>]   |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [public][ [class] [VirtualizedCellRenderer] : GridVirtualizingCellRenderer\<[TextBox]\>] |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [    [public] VirtualizedCellRenderer()]                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        SupportsRenderOptimization = [true];]                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [        AllowRecycle = [true];]                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [        IsControlTextShown = [true];]                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [        IsFocusable = [true];]                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [    [protected] [override] [void] OnRender([DrawingContext] dc, RenderCellArgs rca, GridRenderStyleInfo cellInfo)]     |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        [if] (rca.CellUIElements != [null])]                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [            [return];]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [        [// Only if SupportsRenderOptimization is true, otherwise rca.CellVisuals is never null.]]                                                                                      |
|                                                                                                                                                                                                                                                    |
| [        [string] s = [String].Format([\"Render{0}/{1}\"], rca.RowIndex, rca.ColumnIndex);]                                               |
|                                                                                                                                                                                                                                                    |
| [        GridTextBoxPaint.DrawText(dc, rca.CellRect, s, cellInfo);]                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [    [public] [override] [void] OnInitializeContent([TextBox] textBox, GridRenderStyleInfo style)]                      |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        [base].OnInitializeContent(textBox, style);]                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [        [Thickness] margins = style.TextMargins.ToThickness();]                                                                                                                       |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [        [// TextBoxView always has a minimum margin of 2 for left and right.]]                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [        [// Margin is hard coded below so that text box behavior is properly emulated.]]                                                                                                |
|                                                                                                                                                                                                                                                    |
| [        margins.Left = [Math].Max(0, margins.Left - 2);]                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [        margins.Right = [Math].Max(0, margins.Right - 2);]                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [        textBox.Padding = margins;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [        textBox.BorderThickness = [new] [Thickness](0);]                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [        VirtualizingCellsControl.SetWantsMouseInput(textBox, [true]);]                                                                                                                   |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [        textBox.Text = GetControlText(style);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [    [protected] [override] [string] GetControlTextFromEditorCore([TextBox] uiElement)]                                 |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        [return] uiElement.Text;]                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [    [protected] [override] [void] OnInitialize()]                                                                                              |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        [base].OnInitialize();]                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [        ControlText = GetControlText(CurrentStyle);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [    [protected] [override] [void] OnWireUIElement([TextBox] textBox)]                                                  |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        [base].OnWireUIElement(textBox);]                                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [        textBox.TextChanged += [new] [TextChangedEventHandler](textBox_TextChanged);]                                                                            |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [    [protected] [override] [void] OnUnwireUIElement([TextBox] textBox)]                                                |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        [base].OnUnwireUIElement(textBox);]                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [        textBox.TextChanged -= [new] [TextChangedEventHandler](textBox_TextChanged);]                                                                            |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [    [void] textBox_TextChanged([object] sender, [TextChangedEventArgs] e)]                                                                  |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        [TextBox] textBox = ([TextBox])sender;]                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [        [if] (\![this].IsInArrange && IsCurrentCell(textBox))]                                                                                                      |
|                                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [            TraceUtil.TraceCurrentMethodInfo(textBox.Text);]                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [            [if] (!SetControlText(textBox.Text))]                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [                RefreshContent(); [// reverses change.]]                                                                                                                                |
|                                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [    [protected] [override] [void] OnGridPreviewTextInput([TextCompositionEventArgs] e)]                                |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        CurrentCell.ScrollInView();]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [        CurrentCell.BeginEdit([true]);]                                                                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [    [protected] [override] [bool] ShouldGridTryToHandlePreviewKeyDown([KeyEventArgs] e)]                               |
|                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| [        [if] (CurrentCellUIElement.IsFocused && e.Key != [Key].Escape)]                                                                                          |
|                                                                                                                                                                                                                                                    |
| [            [return] [false];]                                                                                                                                      |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [        [return] [true];]                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Here is the code to bind the above virtual cell to the grid:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                   |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [grid.Model.CellModels.Add([\"VirtualizedCell\"], [new] [VirtualizedCellModel]());] |
|                                                                                                                                                                                              |
| [grid.Model.TableStyle.CellType = [\"VirtualizedCell\"];]                                                                        |
|                                                                                                                                                                                              |
| [grid.Model.TableStyle.CellValue = [\"Edit Me!\"];]                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 87: Virtual cells

 

 

[]{#related-topics}

