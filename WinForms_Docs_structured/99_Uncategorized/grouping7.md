---
title: grouping7.md
original_path: WinForms_Docs/99_Uncategorized/grouping7.md
created_at: 2025-08-05
---






##### Grouping {#grouping style="tab-stops: 0pt"}

[] 

A Group represents a collection of records that belong to a category. The Grid Grouping control allows the user to group the data by one or more columns. When grouping is applied, the data will be organized into a hierarchical structure based on the matching field values. The records having identical values in the grouped column will be combined to form a group. Each group is identified by its GroupCaptionSection that can be expanded to bring the underlying records into view. The GroupCaptionSection carries the information about a particular group like the group name, number of items(records) in the group, etc. It also contains plus / minus buttons that allows the user to expand / collapse the groups individually. By default, a grid table has one group.

 

**GroupedColumns Collection**

 

The **GroupedColumns** collection defines the fields to group by and the sort order. The collection can have multiple entries resulting in nested groups. The GroupedColumns collection of grouping grid can be accessed via its TableDescriptor. The collection consists of various properties, methods and events that allows the user to manage the elements in it.

[] 

**Adding Data Groups**

 

**[Simple Grouping]**

**[]** 

The data can be grouped by adding the column name to the **TableDesriptor.GroupedColumns** property.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.Add([\"Title\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [Me][.gridGroupingControl1.TableDescriptor.GroupedColumns.Add([\"Title\"])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The below grid displays the data columns from the **Employees** Table grouped by the values of **Title** field.

[] 

{border="0"}

[] 

*[Figure ][268][: ListSortDirection]*

**[]** 

By default, the grouping of a column sorts the records in the ascending order of their GroupedColumn values. It is possible to specify the sort order while grouping. The code below arrange the data in the descending order of their Title field values.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.Add([\"Title\"], [ListSortDirection].Descending);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [Me][.gridGroupingControl1.TableDescriptor.GroupedColumns.Add([\"Title\"], ListSortDirection.Descending)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The below screenshot reflects this process.

[] 

{border="0"}

[] 

*[Figure ][269][: Nested Tables Grouping]*

**[]** 

When multiple tables are used in nested manner, a child table can also be grouped by getting access to the GroupedColumns property of the desired ChildTableDescriptor. The code below shows this process.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                |
| [this][.gridGroupingControl1.TableDescriptor.Relations\[0\].ChildTableDescriptor.GroupedColumns.Add([\"CategoryName\"], [ListSortDirection].Descending);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [Me][.gridGroupingControl1.TableDescriptor.Relations(0).ChildTableDescriptor.GroupedColumns.Add([\"CategoryName\"], ListSortDirection.Descending)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: For more details, refer the following browser sample:

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Grouping\\Grouping Demo


[] 

[] 

Multi Column Grouping

**[]** 

Grid Grouping control provides inbuilt support to group the data by more than one column. It is as simple as adding the column names to the GroupedColumns collection. With multicolumn grouping, the grouping grid organizes the data in a hierarchical structure showing groups in different levels. In the below image, you see the Employees data grouped by Title and Country columns.

[] 

{border="0"}

[] 

*[Figure ][270][: Multi Column Grouping]*

**[]** 


[{border="0"}]Note: For more details, refer the following browser sample:

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Grouping\\Multi Column Grouping Demo


[] 

Grouping Through Designer

[] 

[The Grouping can also be done at design time. After binding the dataset to the grouping grid, open the TableDescriptor node in the property grid of the Grid Grouping control. In that, accessing the GroupedColumns property will open the SortColumnDescriptorCollection Editor. Clicking the Add button will add an existing column from the dataset. By using the drop down Name, you can change the column by which you want to group the table data. You can also specify the sort order for that column using the SortDirection property.]

[] 

[The below image depicts this process.]

[] 

{border="0"}

**[]** 

*[Figure ][271][: Design Time Grouping]*

[] 

Using GroupDropArea

 

The table data can also be grouped simply by dragging the desired column header and dropping it into the GroupDropArea. Removing the column header from the drop area will ungroup the data. You can also be able to change the grouping order by a simple drag and drop action on the column headers.

 

For more information on GroupDropArea, refer [GroupDropArea]{.UGHyperlink}.

[] 

Preventing a Column from Grouping

**[]** 

To disallow a column being grouped by, the **AllowGroupByColumn** property should be set to False for that column. This property determines whether the grid can be grouped by a column when the user drags the column to the GroupDropArea.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [this][.gridGroupingControl1.TableDescriptor.Columns\[0\].AllowGroupByColumn = [false];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [Me][.gridGroupingControl1.TableDescriptor.Columns(0).AllowGroupByColumn = [False]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Clearing Groups

[] 

The GroupedColumns.Clear() method will remove all the elements from the GroupedColumns Collection and hence the data will get ungrouped.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear();] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                      |
|                                                                                                                                                         |
| []                                                                                                  |
|                                                                                                                                                         |
| [Me][.gridGroupingControl1.TableDescriptor.GroupedColumns.Clear()] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Removing a given Group

[] 

The GroupedColumns property provide two methods to remove a specific group from the collection. Remove() method deletes the column with a given name from the GroupedColumns collection. As a result, the table data is ungrouped by that column. The RemoveAt() method deletes the element at the specified index from the collection.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [// Removes the first element.]                                                                                                              |
|                                                                                                                                                                                                |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.RemoveAt(0);]                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [// Removes the Title element from the columns collection.]                                                                                  |
|                                                                                                                                                                                                |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.Remove([\"Title\"]);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                                             |
| [\' Removes the first element.]                                                                                                           |
|                                                                                                                                                                                             |
| [Me][.gridGroupingControl1.TableDescriptor.GroupedColumns.RemoveAt(0)]                                 |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [\' Removes the Title element from the columns collection.]                                                                               |
|                                                                                                                                                                                             |
| [Me][.gridGroupingControl1.TableDescriptor.GroupedColumns.Remove([\"Title\"])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p416} 

 

###### 4.3.4.3.1.1 GroupDropArea {#groupdroparea style="tab-stops: 0pt"}

[] 

**GroupDropArea** provides a drop panel onto which the user can drag and drop the column headers to group the table data by those columns. Its visibility can be controlled by the **ShowGroupDropArea** property. Once it is set to true, a Drop Panel will be added at the top of the grouping grid.

 

Following code example illustrates how to enable the Group Drop Area.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                              |
|                                                                                                                                                                     |
| [this][.gridGroupingControl1.ShowGroupDropArea = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                           |
|                                                                                                                                                                  |
| [Me][.gridGroupingControl1.ShowGroupDropArea = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Here are the runtime screens showing the effect of setting the ShowGroupDropArea property.

[] 

{border="0"}

**[]** 

*[Figure ][272][: Startup Grid without GroupDropArea]*

**[]** 

{border="0"}

**[]** 

*[Figure ][273][: Grid with GroupDropArea]*

**[]** 

{border="0"}

**[]** 

*[Figure ][274][: Drag & Drop Title column header to the Drop Area]*

**[]** 

{border="0"}

**[]** 

*[Figure ][275][: Grouped Grid by Title Column]*

**[]** 

{border="0"}

**[]** 

*[Figure ][276][: GroupDropArea with Multiple Column Headers]****[]***

**[]** 

See Also

[] 

[]{#p417}[]{#_Adding_GroupDropArea}4.3.4.3.1.1.1      Adding GroupDropArea

[] 

ShowGroupDropArea property will enable the GroupDropArea only for the table at the top level. When nested tables are used, the drop areas for the child tables need to be added at run time. It is achieved by calling the **AddGroupDropArea** method, by specifying the respective child table name in its parameter.

 

In this example, the grid is bound to a hierarchical dataset containing three tables Categories, Products and OrderDetails. The following code examples illustrate how to add the group drop area for the child tables Products and OrderDetails.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                                           |
| []                                                                                                                      |
|                                                                                                                                                                           |
| [// ShowGroupDropArea adds Group Drop Area for the parent Categories table.]                                            |
|                                                                                                                                                                           |
| [this][.gridGroupingControl1.ShowGroupDropArea = [true];]       |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [// Adding Group Drop Areas for nested tables.]                                                                         |
|                                                                                                                                                                           |
| [this][.groupingGrid1.AddGroupDropArea([\"Products\"]);]     |
|                                                                                                                                                                           |
| [this][.groupingGrid1.AddGroupDropArea([\"OrderDetails\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                            |
|                                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                                               |
| [\' ShowGroupDropArea adds Group Drop Area for the parent Categories table.]                                                |
|                                                                                                                                                                               |
| [Me][.gridGroupingControl1.ShowGroupDropArea = [True]]              |
|                                                                                                                                                                               |
| []                                                                                                                           |
|                                                                                                                                                                               |
| [\' Adding Group Drop Areas for nested tables.]                                                                             |
|                                                                                                                                                                               |
| [Me][.gridGroupingControl1.AddGroupDropArea([\"Products\"])]     |
|                                                                                                                                                                               |
| [Me][.gridGroupingControl1.AddGroupDropArea([\"OrderDetails\"])] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Given below is a sample screenshot.

[] 

{border="0"}

[] 

*[Figure ][277][: Adding Group Drop Areas to the Child Tables (Product and OrderDetails)]*

 

[]{#p418} 

 

4.3.4.3.1.1.2      Customizing GroupDropArea

[] 

Grid Group Drop Area is made up of a collection of Grid controls packed in a panel named GroupDropPanel. A Splitter provides the insulation between the Group Drop Panel and the Grid Table Panel by using which the size of the Drop Panel can be adjusted at run time. While formatting the Group Drop Area, the user should take care of these controls too.

[] 

Properties affecting GroupDropArea

**[]** 

The table given below lists the properties that allow you to customize the look and feel of the Grid Group Drop Area.

[] 


  ---------------------------------------- -----------------------------------------------------------
  Property                                 Description
  gridGroupingControl1.GridGroupDropArea   Lists the properties & events to customize the drop area.
  gridGroupingControl1.GroupDropPanel      Lets the user to control the drop panel behavior.
  gridGroupingControl1.Splitter            Provides the splitter related properties.
  ---------------------------------------- -----------------------------------------------------------


[] 

Example

[] 

[In this example, the grouping grid is built with hierarchical dataset created at runtime. The formatting of the Group Drop Area can be controlled by handling the PrepareViewStyleInfo event for each of the grids in the Group Drop Panel.]

[] 

1.   Formatting of the Splitter and GroupDropPanel.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                                            |
| [// Splitter Color.]                                                                                                                     |
|                                                                                                                                                                                            |
| [this][.gridGroupingControl1.Splitter.BackColor = [Color].Red;]               |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [// Panel Color.               ]                                                                                                         |
|                                                                                                                                                                                            |
| [this][.gridGroupingControl1.GroupDropPanel.BackColor = [Color].YellowGreen;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                           |
|                                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                                              |
| [\' Splitter Color.]                                                                                                                       |
|                                                                                                                                                                                              |
| [Private][ [Me].gridGroupingControl1.Splitter.BackColor = Color.Red]               |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [\' Panel Color.          ]                                                                                                                |
|                                                                                                                                                                                              |
| [Private][ [Me].gridGroupingControl1.GroupDropPanel.BackColor = Color.YellowGreen] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   The PrepareViewStyleInfo event for each of the grids can be hooked by looping through the controls in the panel.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [foreach][ ([Control] ctl [in] [this].gridGroupingControl1.GroupDropPanel.Controls)] |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [    [GridGroupDropArea] groupDropArea = ctl [as] [GridGroupDropArea];]                                                            |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [    [switch] (groupDropArea.Model.Table.TableDescriptor.Name)]                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [    {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [        [case] [\"ParentTable\"]:]                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [        groupDropArea.Model.ColCount = 80;]                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [        groupDropArea.PrepareViewStyleInfo += [new] [GridPrepareViewStyleInfoEventHandler](ParentTable_PrepareViewStyleInfo);]                            |
|                                                                                                                                                                                                                                             |
| [        [break];]                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [        [case] [\"ChildTable\"]:]                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [        groupDropArea.Model.ColCount = 80;]                                                                                                                                                            |
|                                                                                                                                                                                                                                             |
| [        groupDropArea.PrepareViewStyleInfo += [new] [GridPrepareViewStyleInfoEventHandler](ChildTable_PrepareViewStyleInfo);]                             |
|                                                                                                                                                                                                                                             |
| [        [break];]                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [    }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [Dim][ ctl [As] Control]                                                                                            |
|                                                                                                                                                                                                                               |
| [For][ [Each] ctl [In] [Me].gridGroupingControl1.GroupDropPanel.Controls] |
|                                                                                                                                                                                                                               |
| [Dim][ groupDropArea [As] GridGroupDropArea = ctl]                                                                  |
|                                                                                                                                                                                                                               |
| [Select][ [Case] groupDropArea.Model.Table.TableDescriptor.Name]                                                    |
|                                                                                                                                                                                                                               |
| [Case][ [\"ParentTable\"]]                                                                                       |
|                                                                                                                                                                                                                               |
| [groupDropArea.Model.ColCount = 80]                                                                                                                                                       |
|                                                                                                                                                                                                                               |
| [AddHandler][ groupDropArea.PrepareViewStyleInfo, [AddressOf] ParentTable_PrepareViewStyleInfo]                     |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [Case][ [\"ChildTable\"]]                                                                                        |
|                                                                                                                                                                                                                               |
| [groupDropArea.Model.ColCount = 80]                                                                                                                                                       |
|                                                                                                                                                                                                                               |
| [AddHandler][ groupDropArea.PrepareViewStyleInfo, [AddressOf] ChildTable_PrepareViewStyleInfo]                      |
|                                                                                                                                                                                                                               |
| [End][ [Select]]                                                                                                    |
|                                                                                                                                                                                                                               |
| [Next][ ctl]                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Setting the style properties in the PrepareViewStyleInfo event.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [private][ [void] ParentTable_PrepareViewStyleInfo([object] sender, [GridPrepareViewStyleInfoEventArgs] e)] |
|                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [    [// Setting color to the text displaying the table name.]]                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| [    [if] (e.ColIndex == 2 && e.RowIndex == 2)]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.Text = [\"ParentTable\"];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.Font.Bold = [true];]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.BackColor = [Color].YellowGreen;]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.TextColor = [Color].Blue;               ]                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.CellType = [\"Static\"];]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.HorizontalAlignment = [GridHorizontalAlignment].Left;                       ]                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.Enabled = [false];]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [    [// Setting color to the drop area.]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [    [else] [if] (e.Style.Text.StartsWith([\"Drag a\"]))]                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.Text = [\"Drag and Drop Parent Table Column headers\"];]                                                                                                                              |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.BackColor = [Color].White;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [    }       ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                    |
| [    [// Setting color to the dropped columns.]]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [    [else] [if] (e.Style.Text.StartsWith([\"Par\"]))]                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.BackColor = [Color].Tomato;                   ]                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.Themed = [false];]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [    [// Setting color to the remaining part.]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| [    [else]]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                    |
| [    e.Style.BackColor = [Color].YellowGreen;                  ]                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [private][ [void] ChildTable_PrepareViewStyleInfo([object] sender, [GridPrepareViewStyleInfoEventArgs] e)]  |
|                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [    [// Setting color to the text displaying the table name.]]                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| [    [if] (e.ColIndex == 2 && e.RowIndex == 2)]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.Text = [\"ChildTable \"];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.Font.Bold = [true];]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.BackColor = [Color].YellowGreen;]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.TextColor = [Color].Yellow; ]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.CellType = [\"Static\"];]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.HorizontalAlignment = [GridHorizontalAlignment].Left;                       ]                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.Enabled = [false];]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [    [// Setting color to the drop area.]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                    |
| [    [else] [if] (e.Style.Text.StartsWith([\"Drag a\"]))]                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.Text = [\"Drag and Drop Parent Table Column headers\"];]                                                                                                                              |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.BackColor = [Color].Orange;]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.TextColor = [Color].White;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [    [// Setting color to the dropped columns.]]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                    |
| [    [else] [if] (e.Style.Text.StartsWith([\"Child\"]))]                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.BackColor = [Color].Orange;]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.TextColor = [Color].White;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [        e.Style.Themed = [false];]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                    |
| [    [// Setting color to the remaining part.]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                    |
| [    [else]]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                    |
| [    e.Style.BackColor = [Color].YellowGreen;                  ]                                                                                                                                       |
|                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] ParentTable_PrepareViewStyleInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridPrepareViewStyleInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\' Setting color to the text displaying the table name.]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                       |
| [If][ e.ColIndex = 2 [AndAlso] e.RowIndex = 2 [Then]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.Text = [\"ParentTable\"]]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.Font.Bold = [True]]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.BackColor = Color.YellowGreen]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.TextColor = Color.Blue]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.CellType = [\"Static\"]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.HorizontalAlignment = GridHorizontalAlignment.Left]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.Enabled = [False]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\' Setting color to the drop area.]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [ElseIf][ e.Style.Text.StartsWith([\"Drag a\"]) [Then]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.Text = [\"Drag and Drop Parent Table Column headers\"]]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.BackColor = Color.White]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\' Setting color to the dropped columns.]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                       |
| [ElseIf][ e.Style.Text.StartsWith([\"Par\"]) [Then]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.BackColor = Color.Tomato]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.Themed = [False]]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\' Setting color to the remaining part.]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                       |
| [Else]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.BackColor = Color.YellowGreen]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [If]]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] ChildTable_PrepareViewStyleInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridPrepareViewStyleInfoEventArgs)]  |
|                                                                                                                                                                                                                                                                                                                                                       |
| [            ]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\' Setting color to the text displaying the table name.]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                       |
| [If][ e.ColIndex = 2 [AndAlso] e.RowIndex = 2 [Then]]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.Text = [\"ChildTable \"]]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.Font.Bold = [True]]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.BackColor = Color.YellowGreen]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.TextColor = Color.Yellow]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.CellType = [\"Static\"]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.HorizontalAlignment = GridHorizontalAlignment.Left]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.Enabled = [False]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\' Setting color to the drop area.]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [ElseIf][ e.Style.Text.StartsWith([\"Drag a\"]) [Then]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.Text = [\"Drag and Drop Parent Table Column headers\"]]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.BackColor = Color.Orange]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.TextColor = Color.White]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\' Setting color to the dropped columns.]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                       |
| [ElseIf][ e.Style.Text.StartsWith([\"Child\"]) [Then]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.BackColor = Color.Orange]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.TextColor = Color.White]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.Themed = [False]]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                       |
| [\' Setting color to the remaining part.]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                       |
| [Else]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Style.BackColor = Color.YellowGreen]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [If]]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Here is a sample output.

[] 

{border="0"}

[] 

*[Figure ][278][: Formatting the Group Drop Area by using the PreviewViewStyleInfo Event]*

 

[]{#p419} 

 

###### 4.3.4.3.1.2 GroupByOptions {#groupbyoptions style="tab-stops: 0pt"}

[] 

Grid Grouping control provides a number of options that allows you to control the look and behavior of the groups. You can control the caption text, where and if AddNew row will be displayed and whether captions, headers, footers, preview rows and summaries will be displayed.

 

**The GridGroupOptionsStyleInfo class**

 

The **GridGroupOptionsStyleInfo** class, derives **StyleInfoBase**, defines the properties to control the look and feel of the groups. A grouping grid distinguishes between three different kinds of group options which are listed below.

[] 


  ------------------------- ---------------------------------------------------------------------------
  Group Option              Description
  TopLevelGroupOptions      Lets you control the look & behavior of top level group.
  ChildGroupOptions         Lets you control the look & behavior of child groups.
  NestedTableGroupOptions   Lets you control the look & behavior of groups in nested child relations.
  ------------------------- ---------------------------------------------------------------------------


**[]** 

Properties for the Group Options

 

[The table below describes the properties defined in the GridGroupOptionsStyleInfo class. These properties are available for all kinds of Group Options.]

[] 


  ------------------------------- --------------------------------------------------------------------------------------------------------------
  Group Option                    Description
  CaptionText                     Lets you control the caption text that is displayed.
  ShowCaption                     Indicates whether a caption row is visible.
  ShowCaptionPlusMinus            Indicates whether a plus/minus cell is to be displayed next to the caption.
  ShowAddNewBeforeDetails         When true, AddNew record is shown at the top of a group.
  ShowAddNewAfterDetails          When true, AddNew record is shown at the bottom of a group.
  ShowColumnHeaders               Indicates whether the column headers are visible.
  ShowEmptyGroups                 Indicates whether a preview is visible when the group is collapsed.
  ShowGroupHeader                 Indicates whether a header is visible.
  ShowGroupFooter                 Indicates whether a footer is visible.
  ShowGroupPreview                Indicates whether a preview is visible when the group is collapsed.
  ShowSummaries                   Indicates whether summaries are visible.
  ShowGroupSummaryWhenCollapsed   Indicates whether summary items are visible when the group is collapsed.
  ShowFilterBar                   Indicates whether a filter bar is visible.
  ShowStackedHeaders              Indicates whether the stacked headers are visible.
  ShowGroupIndentAsCoveredRange   Indicates whether to treat all the indent cells for a group as a single covered cell.
  ShowCaptionSummaryCells         Indicates whether a group caption should display summaries in columns instead of only one large caption bar.
  ------------------------------- --------------------------------------------------------------------------------------------------------------


[] 

[Next chapter]{.UGHyperlink}[ ]in this section discuss these properties in detail with a suitable example.

 

[]{#p420} 

 

[]{#_Working_with_Group}4.3.4.3.1.2.1      Working with Group Elements

[] 

This section explores the various properties that can be used to manipulate the different group elements.

[] 

**Group Headers and Footers**

**[]** 

The headers and footers of a group can be used to display any information that is common to all the elements of that group. You can toggle the display of these headers and footers, by using the below given boolean properties.

[] 

[·      ]\<GroupOptions\>.ShowGroupHeader

[·      ]\<GroupOptions\>.ShowGroupFooter

[] 

where the **\<GroupOptions\>** can be any one of the following: **TopLevelGroupOptions** to affect only the top most group, **ChildGroupOptions** to affect the child groups or **NestedTableGroupOptions** to affect the groups in nested tables.

 

You can also able to set the header / footer attributes such as HeaderSectionHeight and FooterSectionHeight, by using the below given properties.

[] 

[·      ]TableOptions.GroupHeaderSectionHeight

[·      ]TableOptions.GroupFooterSectionHeight

[] 

Group headers and footers can be populated by handling the **QueryCellStyleInfo** event wherein you can check for the Header / Footer cell type and provide the data.

[] 

{border="0"}

[] 

*[Figure ][279][: Group Header and Footer]*

[] 

GroupPreviewRows

[] 

[GroupPreviewSection is the suitable place when you want to display memo fields or add custom notes for a given group. It can be enabled by setting the][ ][\<GroupOptions\>.ShowGroupPreview property to True. You can adjust the size of the preview row through the TableOptions.GroupPreviewSectionHeight property. The QueryCellStyleInfo event can be used to populate the preview rows.]

[] 

{border="0"}

***[]*** 

*[Figure ][280][: Group Preview Section]*

[] 

AddNew Records

[] 

[Each group can optionally have an AddNew row where you can provide the values for a new record. Once a new record is entered, the record will be sorted into the existing record set and will be assigned a group\'s category automatically. The visibility of the AddNewRecord can be controlled through the following two boolean properties.]

[] 

[·      ]\<GroupOptions\>.ShowAddNewRecordBeforeDetails - adds the AddNew row at the top of a group.

[·      ]\<GroupOptions\>.ShowAddNewRecordAfterDetails - adds the AddNew row at the bottom of a group.

[] 

{border="0"}

***[]*** 

*[Figure ][281][: AddNew Rows ]*

[] 

GroupCaptionSection

[] 

[This is the first section within a group that provides a caption bar above the column headers. The GroupCaptionRows are unbound rows that are created only to combine the records into a group. By default, they display the group category and the number of items in that group. The following properties can be used to control the CaptionSection display.]

[] 

[·      ]**\<GroupOptions\>.ShowCaption** - enables the display of caption section; True by default.

[·      ]**\<GroupOptions\>.CaptionText** - used to get / set the caption text.

[] 

{border="0"}

***[]*** 

*[Figure ][282][: Group Caption Section ]*

 

**CaptionText Tokens**

 

The following table lists the available token formats for **\<GroupOptions\>.CaptionText**.

**[]** 


  ------------------- -------------------------------------------------------------------------------------
  Token               Description
  {TableName}         Displays the CaptionSection.ParentTableDescriptor.Name.
  {CategoryName}      Displays the CaptionSection.ParentGroup.Name.
  {CategoryCaption}   Displays the Header Text of the column that this group belongs to.
  {Category}          Displays the CaptionSection.ParentGroup.Category.
  {RecordCount}       Displays the CaptionSection.ParentGroup.GetFilteredRecordCount().
  Summary Tokens      Allows you to display any item you enter as a Summary Column. See discussion below.
  ------------------- -------------------------------------------------------------------------------------


**[]** 

Custom Summary Tokens

[Any summary item you add can be included in the CaptionText. You have the option of hiding summaries, so it is possible to add summaries only for the purpose of displaying values in the CaptionText. If you have added a summary row named Row1, and a Summary columns named Column1, then you can also use the value of this summary item in the caption with the token {Row1.Column1}. ]

[] 

Example

[] 

[Here is a sample implementation that illustrates the usage of the above properties.]

[] 

5.   Set up a Grid Grouping control and bind a data source into it.

 

6.   Setup the necessary Group Options as required.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// Group Options Settings.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.ShowGroupDropArea = [true];]                                                                               |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TopLevelGroupOptions.ShowGroupHeader = [true];]                                                            |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TopLevelGroupOptions.ShowGroupFooter = [true];]                                                            |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TopLevelGroupOptions.ShowCaption = [true];]                                                                |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TopLevelGroupOptions.ShowGroupPreview = [true];]                                                           |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.ChildGroupOptions.ShowGroupPreview = [true];]                                                              |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TableOptions.GroupFooterSectionHeight = 30;]                                                                                    |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TableOptions.GroupHeaderSectionHeight = 30;]                                                                                    |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TableOptions.GroupPreviewSectionHeight = 25;]                                                                                   |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TopLevelGroupOptions.ShowAddNewRecordBeforeDetails = [true];]                                              |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.TopLevelGroupOptions.ShowAddNewRecordAfterDetails = [true];]                                               |
|                                                                                                                                                                                                                                                   |
| [this][.gridGroupingControl1.ChildGroupOptions.CaptionText = [\"There are {RecordCount} items under {CategoryName} : {Category}\"];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [\' Group Options Settings.]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.ShowGroupDropArea = [True]]                                                                               |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.TopLevelGroupOptions.ShowGroupHeader = [True]]                                                            |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.TopLevelGroupOptions.ShowGroupFooter = [True]]                                                            |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.TopLevelGroupOptions.ShowCaption = [True]]                                                                |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.TopLevelGroupOptions.ShowGroupPreview = [True]]                                                           |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.ChildGroupOptions.ShowGroupPreview = [True]]                                                              |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.TableOptions.GroupFooterSectionHeight = 30]                                                                                    |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.TableOptions.GroupHeaderSectionHeight = 30]                                                                                    |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.TableOptions.GroupPreviewSectionHeight = 25]                                                                                   |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.TopLevelGroupOptions.ShowAddNewRecordBeforeDetails = [True]]                                              |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.TopLevelGroupOptions.ShowAddNewRecordAfterDetails = [True]]                                               |
|                                                                                                                                                                                                                                                |
| [Me][.gridGroupingControl1.ChildGroupOptions.CaptionText = [\"There are {RecordCount} items under {CategoryName} : {Category}\"]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   Handle the QueryCellStyleInfo event to manipulate the group elements.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| [this][.gridGroupingControl1.QueryCellStyleInfo += [new] [GridTableCellStyleInfoEventHandler](gridGroupingControl1_QueryCellStyleInfo);]                 |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [void][ gridGroupingControl1_QueryCellStyleInfo([object] sender, [GridTableCellStyleInfoEventArgs] e)]                                                   |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [    [if] (e.TableCellIdentity.TableCellType == [GridTableCellType].GroupFooterSectionCell \|\| e.TableCellIdentity.TableCellType == [GridTableCellType].GroupHeaderSectionCell)] |
|                                                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [        e.Style.Enabled = [false];]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                            |
| [        [if] (e.TableCellIdentity.TableCellType == [GridTableCellType].GroupFooterSectionCell)]                                                                                                          |
|                                                                                                                                                                                                                                                                                            |
| [        e.Style.Text = [\"The details in the footer can be placed by enabling ShowGroupFooter and handling QueryCellStyleInfo\"];]                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [        [if] (e.TableCellIdentity.TableCellType == [GridTableCellType].GroupHeaderSectionCell)]                                                                                                          |
|                                                                                                                                                                                                                                                                                            |
| [        e.Style.Text = [\"The details in the header can be placed by enabling ShowGroupHeader and handling QueryCellStyleInfo\"];]                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [    [if] (e.TableCellIdentity.TableCellType == [GridTableCellType].GroupPreviewCell)]                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [    {]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [        [Element] el = e.TableCellIdentity.DisplayElement;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                            |
| [        e.Style.CellValue = [\"Preview notes for Group (\"] + el.ParentGroup.Name + [\": \"] + el.ParentGroup.Category.ToString() + [\")\"];]                                 |
|                                                                                                                                                                                                                                                                                            |
| [    }]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] gridGroupingControl1_QueryCellStyleInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridTableCellStyleInfoEventArgs) [Handles] gridGroupingControl1.QueryCellStyleInfo] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [If][ e.TableCellIdentity.TableCellType = GridTableCellType.GroupFooterSectionCell [OrElse] e.TableCellIdentity.TableCellType = GridTableCellType.GroupHeaderSectionCell [Then]]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.Style.Enabled = [False]]                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [If][ e.TableCellIdentity.TableCellType = GridTableCellType.GroupFooterSectionCell [Then]]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.Style.Text = [\"The details in the footer can be placed by enabling ShowGroupFooter and handling QueryCellStyleInfo\"]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [If][ e.TableCellIdentity.TableCellType = GridTableCellType.GroupHeaderSectionCell [Then]]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.Style.Text = [\"The details in the header can be placed by enabling ShowGroupHeader and handling QueryCellStyleInfo\"]]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [If][ e.TableCellIdentity.TableCellType = GridTableCellType.GroupPreviewCell [Then]]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ el [As] Element = e.TableCellIdentity.DisplayElement]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.Style.CellValue = [\"Preview notes for Group (\"] & el.ParentGroup.Name & [\": \"] & el.ParentGroup.Category.ToString() & [\")\"]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

8.   You can control the appearance of different group elements by using the **Appearance** property.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Appearance.AddNewRecordFieldCell.Interior = [new] BrushInfo([Color].FromArgb(255, 255, 192));] |
|                                                                                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Appearance.GroupCaptionCell.Interior = [new] BrushInfo([SystemColors].Control);]               |
|                                                                                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Appearance.GroupCaptionCell.TextColor = [Color].FromArgb(192, 64, 0);]                                              |
|                                                                                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Appearance.GroupFooterSectionCell.Interior = [new] BrushInfo([Color].Pink);]                   |
|                                                                                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Appearance.GroupHeaderSectionCell.Interior = [new] BrushInfo([Color].Pink);]                   |
|                                                                                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Appearance.GroupIndentCell.Interior = [new] BrushInfo([Color].FromArgb(192, 192, 255));]       |
|                                                                                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Appearance.GroupPreviewCell.Interior = [new] BrushInfo([Color].FromArgb(192, 255, 192));]      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                               |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.Appearance.AddNewRecordFieldCell.Interior = [New] BrushInfo(Color.FromArgb(255, 255, 192))] |
|                                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.Appearance.GroupCaptionCell.Interior = [New] BrushInfo(SystemColors.Control)]               |
|                                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.Appearance.GroupCaptionCell.TextColor = Color.FromArgb(192, 64, 0)]                                              |
|                                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.Appearance.GroupFooterSectionCell.Interior = [New] BrushInfo(Color.Pink)]                   |
|                                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.Appearance.GroupHeaderSectionCell.Interior = [New] BrushInfo(Color.Pink)]                   |
|                                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.Appearance.GroupIndentCell.Interior = [New] BrushInfo(Color.FromArgb(192, 192, 255))]       |
|                                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.Appearance.GroupPreviewCell.Interior = [New] BrushInfo(Color.FromArgb(192, 255, 192))]      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

9.   Run the sample and group the table against any data column. Here is a sample screen shot that shows the grouped grid against \'Sport\' column.

[] 

{border="0"}

***[]*** 

*[Figure ][283][: Manipulation and Customization of Group Elements]*

[] 


{border="0"}Note: For more details, refer the following browser samples:



***[·    ]***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Grouping Grid Options\\Top-Level-Group Options Demo

***[·    ]***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Grouping Grid Options\\Child-Group Options Demo

***[·    ]***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Window\\Grid.Grouping.Windows\\Samples\\2.0\\Grouping Grid Options\\Nested-Table Group Options Demo


 

[]{#p421} 

 

4.3.4.3.1.2.2      Working with Groups

[] 

This section best demonstrates how to work with the group rows and also shows how the groups are organized into a grouping grid. The Grouping Grid architecture can be viewed as a binary where the different grid elements like group rows, summary rows, filter rows, etc. form the nodes of the tree having the data records at the bottom as leaf nodes. A group can be a final node with records or it can be a node with nested groups rooting a sub tree.

 

This lesson will guide you the ways to access the individual groups in a collection, to retrieve all the groups, to expand/collapse groups and will discuss some of the properties and events used to process the groups.

 

**Expanding/Collapsing Groups**

 

All the groups can be expanded as well as collapsed at once by calling the respective methods, **Table.ExpandAllGroups** and **Table.CollapseAllGroups**. To expand or collapse a specific group, set **Group.IsExpanded** property to true or false respectively. Following code example illustrates this.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [// Expands all groups.]                                                                                                                    |
|                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Table.ExpandAllGroups();]                                                   |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [// Collapse all groups.]                                                                                                                   |
|                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Table.CollapseAllGroups();]                                                 |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [// Expand the group with index 3.]                                                                                                         |
|                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Table.TopLevelGroup.Groups\[3\].IsExpanded = [true];]  |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [// Collapse the group with index 4.]                                                                                                       |
|                                                                                                                                                                                               |
| [this][.gridGroupingControl1.Table.TopLevelGroup.Groups\[4\].IsExpanded = [false];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [\' Expands all groups.]                                                                                                               |
|                                                                                                                                                                                          |
| [Me][.gridGroupingControl1.Table.ExpandAllGroups()]                                                 |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [\' Collapse all groups.]                                                                                                              |
|                                                                                                                                                                                          |
| [Me][.gridGroupingControl1.Table.CollapseAllGroups()]                                               |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [\' Expand the group with index 3.]                                                                                                    |
|                                                                                                                                                                                          |
| [Me][.gridGroupingControl1.Table.TopLevelGroup.Groups(3).IsExpanded = [True]]  |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [\' Collapse the group with index 4.]                                                                                                  |
|                                                                                                                                                                                          |
| [Me][.gridGroupingControl1.Table.TopLevelGroup.Groups(4).IsExpanded = [False]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Accessing a Given Group

 

The Table.TopLevelGroup.Groups collection maintains the details of the individual groups in this collection which can be used to retrieve the details of any group.

[] 

Below code lets you access the details of a group with the category Sport. It also defines a method named IterateGroup that is used to iterate through the records and also the nested groups in a given group. It provides you with the group details such as the level of the group, number of items in that group, its category, and so on.

[] 

Accessing all the groups

 

Table.TopLevelGroup is the main topmost group in a grouping grid. It forms the root node of the group hierarchy where its categorized records and the nested groups form the child nodes. To access all the groups, you can make use of the same IterateThrough method by passing the TopLevelGroup as the method parameter. Then this method will loop through the categorized records and nested groups of the top level group and will print the details of all the groups.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [// Call IterateThrough method for a given group.]                                                                                                                      |
|                                                                                                                                                                                                                           |
| [Group][ g = [this].gridGroupingControl1.Table.TopLevelGroup.Groups\[[\"Sport\"]\];] |
|                                                                                                                                                                                                                           |
| [IterateGroup(g);]                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [// Call IterateThrough method for all the groups in a grid table.]                                                                                                     |
|                                                                                                                                                                                                                           |
| [IterateGroup([this].gridGroupingControl1.Table.TopLevelGroup);]                                                                                                 |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [// IterateThrough method iterates through the records and the nested groups.]                                                                                          |
|                                                                                                                                                                                                                           |
| [public][ [void] IterateThrough([Group] g)]                                             |
|                                                                                                                                                                                                                           |
| [{]                                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [    System.Diagnostics.[Trace].WriteLine([\"GroupLevel = \"]+g.GroupLevel);]                                                         |
|                                                                                                                                                                                                                           |
| [    System.Diagnostics.[Trace].WriteLine(g.Info);]                                                                                                           |
|                                                                                                                                                                                                                           |
| [    [foreach]([Record] r [in] g.Records)]                                                                          |
|                                                                                                                                                                                                                           |
| [    {]                                                                                                                                                                               |
|                                                                                                                                                                                                                           |
| [        System.Diagnostics.[Trace].WriteLine(r.Info);]                                                                                                       |
|                                                                                                                                                                                                                           |
| [    }]                                                                                                                                                                               |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [    [foreach]([Group] gr [in] g.Groups)]                                                                           |
|                                                                                                                                                                                                                           |
| [    {]                                                                                                                                                                               |
|                                                                                                                                                                                                                           |
| [        IterateGroup(gr);]                                                                                                                                                           |
|                                                                                                                                                                                                                           |
| [    }]                                                                                                                                                                               |
|                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                        |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [\' Call IterateThrough method for a given group.]                                                                                                      |
|                                                                                                                                                                                                           |
| [Dim ][g[ As ]Group]                                                                            |
|                                                                                                                                                                                                           |
| [g =[ Me].gridGroupingControl1.Table.TopLevelGroup.Groups([\"Sport\"])]                                                  |
|                                                                                                                                                                                                           |
| [IterateThrough(g)]                                                                                                                                                   |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [\' Call IterateThrough method for all the groups in a grid table.]                                                                                     |
|                                                                                                                                                                                                           |
| [IterateThrough([Me].gridGroupingControl1.Table.TopLevelGroup)]                                                                                  |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [\'IterateThrough method iterates through the records and the nested groups.]                                                                           |
|                                                                                                                                                                                                           |
| [Public][ [Sub] IterateThrough([ByVal] g [As] Group)] |
|                                                                                                                                                                                                           |
| [System.Diagnostics.Trace.WriteLine([\"GroupLevel = \"]+ g.GroupLevel.ToString())]                                                            |
|                                                                                                                                                                                                           |
| [System.Diagnostics.Trace.WriteLine(g.Info)]                                                                                                                          |
|                                                                                                                                                                                                           |
| [For][ [Each] r [As] Record [In] g.Records]           |
|                                                                                                                                                                                                           |
| [System.Diagnostics.Trace.WriteLine(r.Info)]                                                                                                                          |
|                                                                                                                                                                                                           |
| [Next][ r]                                                                                                           |
|                                                                                                                                                                                                           |
| [For][ [Each] gr [As] Group [In] g.Groups]            |
|                                                                                                                                                                                                           |
| [IterateThrough(gr)]                                                                                                                                                  |
|                                                                                                                                                                                                           |
| [Next][ gr]                                                                                                          |
|                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Accessing the group for a given record

 

It is the grid.Table object that provides access to the records and the grouped elements. The Table.Records collection returns a read only collection of the data records. The following code can be used to get access to the group for a particular record. Record.ParentGroup property is used to obtain the group that a record belongs to.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [System.Diagnostics.[Trace].WriteLine([this].gridGroupingControl1.Table.Records\[3\].ParentGroup.Info);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                         |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [System.Diagnostics.Trace.WriteLine([Me].gridGroupingControl1.Table.Records(3).ParentGroup.Info)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p422} 

 

4.3.4.3.1.2.3      Events

[] 

This section discusses some of the important events that could be handled to catch the grouping actions. Below is a list of such events.

**[]** 


  ------------------------- --------------------------------------------------------
  Event                     Description
  GroupedColumns_Changing   Occurs before a property in the collection is changed.
  GroupedColumns_Changed    Occurs after a property in the collection was changed.
  GroupExpanding            Occurs before a group is expanded.
  GroupExpanded             Occurs after a group was expanded.
  GroupCollapsing           Occurs before a group is collapsed.
  GroupCollapsed            Occurs after a group was collapsed.
  SortingItemsInGroup       Occurs before the records for a group are sorted.
  SortedItemsInGroup        Occurs after the records for a group were sorted.
  ------------------------- --------------------------------------------------------


**[]** 

Example

[] 

The GroupedColumns Changing/Changed events get fired when the list is modified i.e. when any item is added, removed or modified. It accepts an argument of type ListPropertyChangedEventArgs that lets you check the reason for a list change. The reason could be of ItemAdded, ItemInserted, ItemRemoved, ItemModified, ItemMoved, ItemPropertyChanged or the whole collection is modified.

 

The following code examples show you how to capture the events.\
\
[]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [// Subscribe to the events.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.Changing += [new] ListPropertyChangedEventHandler(GroupedColumns_Changing);] |
|                                                                                                                                                                                                                                                    |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.Changed += [new] ListPropertyChangedEventHandler(GroupedColumns_Changed);]   |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [// Event Handlers.]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                    |
| [// GroupedColumns_Changing event.]                                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [void][ GroupedColumns_Changing([object] sender, ListPropertyChangedEventArgs e)]                                                        |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [SortColumnDescriptor][ scd = e.Item [as] [SortColumnDescriptor];]                                            |
|                                                                                                                                                                                                                                                    |
| [if][ (e.Action == Syncfusion.Collections.[ListPropertyChangedType].Insert)]                                                          |
|                                                                                                                                                                                                                                                    |
| [Console][.WriteLine([\"Column Added - {0}\"], scd.Name);]                                                                         |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [// GroupedColumns_Changed event.]                                                                                                                                                               |
|                                                                                                                                                                                                                                                    |
| [void][ GroupedColumns_Changed([object] sender, ListPropertyChangedEventArgs e)]                                                         |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [SortColumnDescriptor][ scd = e.Item [as] [SortColumnDescriptor];]                                            |
|                                                                                                                                                                                                                                                    |
| [if][ (e.Action == Syncfusion.Collections.[ListPropertyChangedType].Remove)]                                                          |
|                                                                                                                                                                                                                                                    |
| [Console][.WriteLine([\"Column Removed - {0}\"], scd.Name);]                                                                       |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [\' Subscribe to the events.]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                         |
| [AddHandler][ gridGroupingControl1.TableDescriptor.GroupedColumns.Changing, [AddressOf] GroupedColumns_Changing]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| [\' Event Handlers.]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [\' GroupedColumns_Changing event.]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] GroupedColumns_Changed([ByVal] sender [As] [Object], [ByVal] e [As] ListPropertyChangedEventArgs)]  |
|                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ scd [As] SortColumnDescriptor = [CType](e.Item, SortColumnDescriptor)]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [If][ e.Action = ListPropertyChangedType.Insert [Then]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\"Column Added - {0}\"] + scd.Name)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [If]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                         |
| [\' GroupedColumns_Changed event.]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] GroupedColumns_Changing([ByVal] sender [As] [Object], [ByVal] e [As] ListPropertyChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                         |
| [Dim][ scd [As] SortColumnDescriptor = [CType](e.Item, SortColumnDescriptor)]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                         |
| [If][ e.Action = ListPropertyChangedType.Remove [Then]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                         |
| [Console.WriteLine([\"Column Removed - {0}\"] + scd.Name)]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [If]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The[ ][GroupExpanding]{.UGHyperlink}/[GroupExpanded]{.UGHyperlink} and [GroupCollapsing]{.UGHyperlink}/[GroupCollapsed]{.UGHyperlink} event handlers are best to use when you want to do some actions as a result of the group operations, GroupExpand and GroupCollapse.

 

The[ ]{.UGHyperlink}[SortingItemsInGroup]{.UGHyperlink} and [SortedItemsInGroup]{.UGHyperlink} events are raised when the records for a group are sorted. The grid should have at least one group for these events to occur. It does have no relationship with normal sorting. It occurs only when a grouped column is sorted.

 

**Tracking the changes in Nested Table**

[] 

It is possible to get notified of the changes in other table descriptor other than the default table. This can be achieved by listening to the **Engine.PropertyChanging** event and using the **GetNestedChildTableDescriptorEvent** method. This method lets you get the information about a change in the table descriptor of the nested child table. For example, when a column was changed in a nested table, the above method allows you to get the details such as the table descriptor of the affected table and the original EventArgs which was raised in response to the column changes(eg. ColumnsChanged event). Once you have the event data, you can then check for whether just the width of the column has changed or if other settings were changed.

 

Following code example illustrates the usage of this method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [protected][ [override] [void] Engine_PropertyChanging([object] sender, [DescriptorPropertyChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [if][ (e.PropertyName == [\"TableDescriptor\"])]                                                                                                                                |
|                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [TableDescriptor][ tableDescriptor = (([Engine]) sender).TableDescriptor;]                                                                                                   |
|                                                                                                                                                                                                                                                                                              |
| [e = ([DescriptorPropertyChangedEventArgs]) e.Inner;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [if][ (e.PropertyName == [\"Relations\"])]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [e = e.GetNestedChildTableDescriptorEvent([ref] tableDescriptor);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [if][ (e.PropertyName == [\"Columns\"])]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [ListPropertyChangedEventArgs le = (ListPropertyChangedEventArgs) e.Inner;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                              |
| [if][ (le.Action == ListPropertyChangedType.ItemPropertyChanged)]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [if][ (le.Property == [\"Appearance\"] \|\| le.Property == [\"Width\"]]                                                                                 |
|                                                                                                                                                                                                                                                                                              |
| [\|\| le.Property == [\"ReadOnly\"] \|\| le.Property == [\"HeaderText\"]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                              |
| [\|\| le.Action == ListPropertyChangedType.Remove]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [\|\| le.Action == ListPropertyChangedType.Move]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [\|\| le.Property == [\"AllowFilter\"])]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [return][;]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [else][ [if] (e.PropertyName == [\"Appearance\"])]                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [// Base class will end edit mode, which is not necessary.]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                              |
| [return][;]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [base][.Engine_PropertyChanging (sender, e);]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Protected][ [Overrides] [Sub] Engine_PropertyChanging([ByVal] sender [As] [Object], [ByVal] e [As] DescriptorPropertyChangedEventArgs)]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [If][ e.PropertyName = [\"TableDescriptor\"] [Then]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ tableDescriptor [As] TableDescriptor = ([CType](sender, Engine)).TableDescriptor]                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [e = [CType](e.Inner, DescriptorPropertyChangedEventArgs)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [If][ e.PropertyName = [\"Relations\"] [Then]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [e = e.GetNestedChildTableDescriptorEvent(tableDescriptor)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [If][ e.PropertyName = [\"Columns\"] [Then]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Dim][ le [As] ListPropertyChangedEventArgs = [CType](e.Inner, ListPropertyChangedEventArgs)]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [If][ le.Action = ListPropertyChangedType.ItemPropertyChanged [Then]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [If][ le.Property = [\"Appearance\"] [OrElse] le.Property = [\"Width\"] [OrElse] le.Property = [\"ReadOnly\"] [OrElse] le.Property = [\"HeaderText\"] [OrElse] le.Action = ListPropertyChangedType.Remove [OrElse] le.Action = ListPropertyChangedType.Move [OrElse] le.Property = [\"AllowFilter\"] [Then]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Return]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ElseIf][ e.PropertyName = [\"Appearance\"] [Then]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\' Base class will end edit mode, which is not necessary.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Return]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [If]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [MyBase][.Engine_PropertyChanging(sender, e)]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p423} 

 

[]{#related-topics}

