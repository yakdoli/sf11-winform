---
title: gridlistcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\gridlistcontrol.md
created_at: 2025-07-03
---






##### Grid List Control {#grid-list-control style="tab-stops: 0pt"}

[] 

The **GridListControl** cell type allows you to display a drop-down list that can contain multiple columns as an image. It uses **DataSource**, **DisplayMember** and **ValueMember** properties to control what is shown in the multiple columns. The DataSource member is generally stored in a parent style, and this member is then shared among grid cells which might use DisplayMember and ValueMember properties to customize their look if needed.

[] 


  ------------------------ -------------------------------------------------------------------------------------------------------------------------
  GridStyleInfo Property   Description
  DisplayMember            Any object that implements either IList or IListSource. These include DataTable, DataView, or ArrayList objects.
  ValueMember              Indicates the column from the data source that is to be used for the value of the cell.
  ExclusiveChoiceList      Determines whether the user is required to select an item in the drop-down list.
  MultiColumn              Determines whether all the columns in the data source are displayed or if the single DisplayMember column is displayed.
  ------------------------ -------------------------------------------------------------------------------------------------------------------------


[] 

Let us assume you have an ArrayList of US State objects. When you set the cell type to GridListControl, you will get the output as displayed in the screen shot.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                                      |
| []                                                                                                                 |
|                                                                                                                                                                      |
| [// Set up the data source.]                                                                                       |
|                                                                                                                                                                      |
| [// Here \"USStates\" is an arraylist of state objects, each of which have the properties LongName and ShortName.] |
|                                                                                                                                                                      |
| [gridControl1.TableStyle.DataSource = USStates;]                                                                                 |
|                                                                                                                                                                      |
| [gridControl1.TableStyle.DisplayMember = [\"LongName\"];]                                                |
|                                                                                                                                                                      |
| [gridControl1.TableStyle.ValueMember = [\"ShortName\"];]                                                 |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [gridControl1\[rowIndex, colIndex + 2\].CellType = [\"GridListControl\"];]                               |
|                                                                                                                                                                      |
| [gridControl1\[rowIndex, colIndex + 2\].Text = [\"Wisconsin\"];]                                         |
|                                                                                                                                                                      |
| [gridControl1\[rowIndex, colIndex + 2\].ExclusiveChoiceList = [true];]                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                   |
|                                                                                                                                                                      |
| []                                                                                                                 |
|                                                                                                                                                                      |
| [\' Set up the data source.]                                                                                       |
|                                                                                                                                                                      |
| [\' Here \"USStates\" is an arraylist of state objects each of which, have the properties LongName and ShortName.] |
|                                                                                                                                                                      |
| [gridControl1.TableStyle.DataSource = USStates]                                                                                  |
|                                                                                                                                                                      |
| [gridControl1.TableStyle.DisplayMember = [\"LongName\"]]                                                 |
|                                                                                                                                                                      |
| [gridControl1.TableStyle.ValueMember = [\"ShortName\"]]                                                  |
|                                                                                                                                                                      |
| []                                                                                                               |
|                                                                                                                                                                      |
| [gridControl1(rowIndex, colIndex + 2).CellType = [\"GridListControl\"]]                                  |
|                                                                                                                                                                      |
| [gridControl1(rowIndex, colIndex + 2).Text = [\"Wisconsin\"]]                                            |
|                                                                                                                                                                      |
| [gridControl1(rowIndex, colIndex + 2).ExclusiveChoiceList = [True]]                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 81: Grid List Control Cells

[] 

A sample which demonstrates Grid List Control cell type is available in the following sample installation path.

***[]*** 

***C:\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Grid List Control\\Grid List Control Demo***

 

[]{#p57} 

 

[]{#related-topics}

