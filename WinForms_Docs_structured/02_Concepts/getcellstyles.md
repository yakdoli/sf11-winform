---
title: getcellstyles.md
original_path: WinForms_Docs/02_Concepts/getcellstyles.md
created_at: 2025-08-05
---






##### Get Cell Styles {#get-cell-styles style="tab-stops: 0pt"}

[] 

This topic elaborates the way of retrieving the style information of grid cells. On a mouse hit, when you want to retrieve the content of underlying cells and also its style information, it is good to use the **PointToTableCellStyle** method on the instances of the Grid Table control.

 

**PointToTableCellStyleInfo Method**

[] 

For any given point on the grid, this method will return the style information of the underlying cell that is displayed under that point. If the underlying cell belongs to a nested table, then style information is returned for the cell inside the nested table. The details of this method are given below.

[] 


  ----------------------- ----------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------
  Method Name             Parameter                                                                                                   Return Value
  PointToTableCellStyle   ptClient: A type of System.Drawing Point object that represents the mouse position in client coordinates.   A GridTableCellStyleInfo object that stores the stye information of the underlying grid cell.
  ----------------------- ----------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------


[] 

[] 

Implementation

 

The implementation of this method is a two-step process.

[] 

1.   As a first step, it gets the corresponding nested display element that is displayed at the given mouse position. This can be performed easily by employing the **PointToNestedDisplayElement** method. This method is explained later in this chapter.

2.  

3.   Once the display element is retrieved, the style information of the corresponding cell can be got by using the **Table.GetTableCellStyleInfo** method which will return a cell style information given its row and column indices.

[] 

PointToNestedDisplayElement Method

[] 

This method returns the nested display element that is displayed at the given mouse position. The details are given below.

[] 


  ----------------------------- ----------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------
  Method Name                   Parameter                                                                                                   Return Value
  PointToNestedDisplayElement   ptClient: A type of System.Drawing Point object that represents the mouse position in client coordinates.   An Element object that represents the underlying display element.
  ----------------------------- ----------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------


[] 

Example

[] 

Below is an example that demonstrates how to use PointToTableCellStyle method to retrieve the cell style information. This example handles a MouseMove handler of the Grid Table Control, retrieves the cell content using the above given method and then writes the content to a listbox control.

[] 

1.   Setup a Grouping Grid and bind it to a dataset. Handle TableControl.MouseMove event to let the user get the cell style information printed while hovering the mouse over the grid cells. Once you have the style, you can check Style.TableCellIdentity for information about the cell such as its column, underlying record, parent table, and so on.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| [private][ [void] TableControl_MouseMove([object] sender, [MouseEventArgs] e)]                                                                     |
|                                                                                                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                           |
| [    [Point] ptClient = [new] [Point](e.X, e.Y);]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                           |
| [    [GridTableControl] tableControl = [this].groupingGrid1.TableControl;]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| [    [GridTableCellStyleInfo] style = tableControl.PointToTableCellStyle(ptClient);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [    [Element] displayElement = style.TableCellIdentity.DisplayElement;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                           |
| [    [string] info = [\"\"];]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| [    [if] (style != [null])]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                           |
| [    {]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                           |
| [        [if] (style.TableCellIdentity.Column != [null])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                           |
| [            info = [\"Field Name - \"]+style.TableCellIdentity.Column.Name + [\", Field Value - \\\"\"] + style.CellValue.ToString() + [\"\\\", Field Type - \"]+style.CellType.ToString();] |
|                                                                                                                                                                                                                                                                                                           |
| [        [else]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                           |
| [            info = style.TableCellIdentity.ToString();]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| [    }]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| [    listBox1.Items.Clear();]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                           |
| [    listBox1.Items.Add([\"MousePosition: \"] + ptClient.ToString());]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| [    listBox1.Items.Add([\"Category Keys: \"] + displayElement.ParentChildTable.CategoriesToString());]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [    listBox1.Items.Add([\"Display Element Type: \"] + displayElement.GetType().Name);]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [    listBox1.Items.Add([\"Cell Information: \"] + info);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                          |
| [Private][ [Sub] TableControl_MouseMove([ByVal] sender [As] [Object], [ByVal] e [As] MouseEventArgs)] |
|                                                                                                                                                                                                                                                                                                                          |
| [Dim][ ptClient [As] [New] Point(e.X, e.Y)]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                          |
| [Dim][ tableControl [As] GridTableControl = [Me].groupingGrid1.TableControl]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [Dim][ style [As] GridTableCellStyleInfo = tableControl.PointToTableCellStyle(ptClient)]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                          |
| [Dim][ displayElement [As] Element = style.TableCellIdentity.DisplayElement]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [Dim][ info [As] [String] = [\"\"]]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [If][ [Not] (style [Is] [Nothing]) [Then]]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                          |
| [If][ [Not] (style.TableCellIdentity.Column [Is] [Nothing]) [Then]]                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
| [info = [\"Field Name - \"] & style.TableCellIdentity.Column.Name & [\", Field Value - \"\"\"] & style.CellValue.ToString() & [\"\"\", Field Type - \"] & style.CellType.ToString()]                         |
|                                                                                                                                                                                                                                                                                                                          |
| [Else]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                          |
| [info = style.TableCellIdentity.ToString()]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                          |
| [End][ [If]]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [End][ [If]]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [listBox1.Items.Clear()]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
| [listBox1.Items.Add([\"MousePosition: \"] & ptClient.ToString())]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                          |
| [listBox1.Items.Add([\"Category Keys: \"] & displayElement.ParentChildTable.CategoriesToString())]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| [listBox1.Items.Add([\"Display Element Type: \"] & displayElement.GetType().Name)]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| [listBox1.Items.Add([\"Cell Information: \"] & info)]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Here is a sample output.

[] 

{border="0"}

[] 

*[Figure ][330][: Retrieving Cell Style Information by using the PointToTableCellStyle Method]*

 

[]{#p455} 

 

[]{#related-topics}

