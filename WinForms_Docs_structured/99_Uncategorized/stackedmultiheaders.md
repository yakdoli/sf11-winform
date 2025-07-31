---
title: stackedmultiheaders.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\stackedmultiheaders.md
created_at: 2025-07-03
---






##### Stacked MultiHeaders {#stacked-multiheaders style="tab-stops: 0pt"}

[] 

Essential Grouping Grid Control offers in built support for Stacked MultiHeaders. This feature allows you to create additional unbound header rows called **StackedHeaderRows** that span across visible grid columns. You can group some columns under each header row. It also supports Drag / Drop of these header rows. Grouped columns will also be rearranged along with the header.

 

**The StackedHeaderRows Collection**

 

Stacked Header rows for a given Grid Table are gathered under **TableDescriptor.StackedHeaderRows** collection. This contains the property definitions that controls the behavior and appearance of the Stacked Headers. A StackedHeaderRow collection can be viewed as a set of stacked header rows in which each header row contains a collection of stacked headers that span across multiple columns.

 

Every header in a Stacked Header Row is defined by a **GridStackedHeaderDescriptor**. All the headers for a given stacked header row is managed by **GridStackedHeaderRowDescriptor**. **GridStackedHeaderRowDescriptorCollection,** which is returned by TableDescriptor.StackedHeaderRows property, manages the collection of GridStackedHeaderRowDescriptors for a given table. It is the **GridStackedHeaderVisibleColumnDescriptor** that binds a Column or ColumnSet to the StackedHeaderCell.

 

The order in which the StackedHeaders will appear is determined by the VisibleColumns collection.When the layout of the GridStackedHeaderRow is calculated the grid will loop through the VisibleColumns collection and find the StackedHeader Descriptor that references the VisibleColumn. If the same StackedHeader references multiple neighboring VisibleColumns then the header for these columns will be drawn as one cell. If there are no visible columns specified for a StackedHeader, then it will span across all the visible columns similar to a Caption.

 

You could be able to rearrange the columns by dragging the stacked headers. While doing so, it is the Visible Columns collection that is being affected. Since the order of stacked headers is dependent on Visible Columns, the GridStackedHeaderCollections itself does not need to be modified.

 

It is possible to add Stacked Headers for nested tables and groups too. You can enable the display of the StackedHeaders by setting the **ShowStackedHeaders** property to true.\
\

[·      ]**TopLevelGroupOptions.ShowStackedHeaders -** Toggles the display of StackedHeaders for top most group.

[·      ]**ChildGroupOptions.ShowStackedHeaders -** Toggles the display of StackedHeaders for child groups.

[·      ]**NestedTableGroupOptions.ShowStackedHeaders -** Toggles the display of StackedHeaders for child table and its groups.

**[]** 

Through Designer

 

Creating Stacked Headers is a two-step process.

[] 

1.   As a first step, you must define the Stacked Header Rows by accessing the TableDescriptor.StackedHeaderRows property. This will open the GridStackedHeaderRowDescriptor Collection Editor wherein you can add as many header rows as you want, by specifying the different attributes like HeaderText, VisibleColumns, Appearance, and so on, for each header in the header row.

[] 

{border="0"}

[] 

*[Figure ][340][: Adding Stacked Headers by using the StackedHeaderRows Property]*

[] 

Property Definitions

[] 


  ---------------- -----------------------------------------------------------------------------
  Property Name    Description
  Name             Specifies the name of the descriptor.
  HeaderText       Specifies the text to be displayed in the StackedHeaderCell.
  VisibleColumns   The collection of columns that should be combined under the Stacked Header.
  Appearance       Controls the appearance of the StackedHeaderCell.
  ---------------- -----------------------------------------------------------------------------


[] 

2.   The second step is to enable the display of StackedHeaders for the given table and group by setting the ShowStackedHeaders property to true.

[] 

{border="0"}

***[]*** 

*[Figure ][341][: Setting ShowStackedHeaders property to True]*

**[]** 

Output

[] 

Here are the screen shots showing the Grouping Grid with two Stacked Header Rows. It illustrates the effect of doing Drag / Drop on StackedHeaders. You could notice that the order of the Visible columns gets affected automatically while rearranging the StackedHeaders.

[] 

{border="0"}

**[]** 

*[Figure ][342][: Grouping Grid with StackedHeaders]*

**[]** 

{border="0"}

**[]** 

*[Figure ][343][: Rearranging StackedHeaders by dragging and dropping Header2]*

**[]** 

**[]** 

{border="0"}

**[]** 

*[Figure ][344][: VisibleColumns rearranged as a result of the above Drag / Drop]*

**[]** 

StackedHeaders for NestedGroups

 

Stacked Headers can be enabled for Child Group by setting ChildGroupOptions.ShowStackedHeaders to true. The grouping grid in the below image displays the stacked headers for the nested groups.

**[]** 

{border="0"}

***[]*** 

*[Figure ][345][: Stacked Headers for Nested Groups]*

**[]** 

Appearance

 

A couple of ways are there to control the appearance of the StackedHeaders. By one way you can access Appearance.StackedHeaderCell property to enter the appearance definitions. Appearance set this way will be applied to all the stacked header cells. An alternate way is to specify the appearance settings through the GridStackedHeaderRow Descriptor. In this way, you can have different settings for individual stacked headers in each StackedHeaderRow.

 

Here is the property window with GridStackedHeaderRowDescriptor Collection Editor showing the appearance settings of Stacked Headers defined.

[] 

{border="0"}

***[]*** 

*[Figure ][346][: Appearance Settings for Stacked Headers]*

[] 

Output

 

Here is the effect of the above settings.

[] 

{border="0"}

***[]*** 

*[Figure ][347][: Stacked Headers created for the Grid Grouping Control]*

[] 

Programmatically

 

You can add the Stacked Header Rows at run time too. To achieve this, first you must define a required number of GridStackedHeaderDescriptors by specifying the VisibleColumns for each. Next, create a StackedHeaderRow by instantiating GridStackedHeaderRowDescriptor and add the above defined stacked headers into it. Finally, add this header row into the TableDescriptor.StackedHeaderRows collection. The following code example illustrates this process.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [GridStackedHeaderDescriptor][ shd = [new] [GridStackedHeaderDescriptor]([\"header1\"], [\"StackedHeader1\"]);] |
|                                                                                                                                                                                                                                                                                                      |
| [shd.VisibleColumns.Add([new] [GridStackedHeaderVisibleColumnDescriptor]([\"CustomerName\"]));]                                                                                             |
|                                                                                                                                                                                                                                                                                                      |
| [shd.VisibleColumns.Add([new] [GridStackedHeaderVisibleColumnDescriptor]([\"CompanyName\"]));]                                                                                              |
|                                                                                                                                                                                                                                                                                                      |
| [GridStackedHeaderRowDescriptor][ shrd = [new] [GridStackedHeaderRowDescriptor]([\"Row1\"],]                                            |
|                                                                                                                                                                                                                                                                                                      |
| [new][ [GridStackedHeaderDescriptor]\[\] { shd });]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                      |
| [this][.gridGroupingControl1.TableDescriptor.StackedHeaderRows.Add(shrd);]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [// Customize the Appearance.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                      |
| [this][.gridGroupingControl1.Appearance.StackedHeaderCell.BackColor = [Color].Teal;]                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                      |
| [Dim][ shd [As] GridStackedHeaderDescriptor = [New] GridStackedHeaderDescriptor([\"header1\"], [\"StackedHeader1\"])] |
|                                                                                                                                                                                                                                                                                                      |
| [shd.VisibleColumns.Add([New] GridStackedHeaderVisibleColumnDescriptor([\"CustomerName\"]))]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                      |
| [shd.VisibleColumns.Add([New] GridStackedHeaderVisibleColumnDescriptor([\"CompanyName\"]))]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| [Dim][ shrd [As] GridStackedHeaderRowDescriptor = [New] GridStackedHeaderRowDescriptor([\"Row1\"], ]                                          |
|                                                                                                                                                                                                                                                                                                      |
| [New][ GridStackedHeaderDescriptor() { shd })]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                      |
| [Me][.gridGroupingControl1.TableDescriptor.StackedHeaderRows.Add(shrd)]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                      |
| [\' Customize the Appearance.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                      |
| [Me][.gridGroupingControl1.Appearance.StackedHeaderCell.BackColor = Color.Teal]                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Grouping Grid Layout\\Stacked Multi Headers Demo


 

[]{#p459} 

 

[]{#related-topics}

