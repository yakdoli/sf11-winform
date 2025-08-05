---
title: sorting6.md
original_path: WinForms_Docs/99_Uncategorized/sorting6.md
created_at: 2025-08-05
---






##### Sorting {#sorting style="tab-stops: 0pt"}

[] 

Grid Grouping control allows you to sort the table data against one or more columns. The number of columns by which the data can be sorted is unlimited. When sorting is applied, the grid will rearrange the data to match with the current sort criteria.

 

**SortedColumns Collection**

**[]** 

The **SortedColumns** collection defines the sort order for records within groups. Multiple entries can be added with the first entry having the highest precedence when sorting records. The properties and methods in this collection lets you manage the elements in the collection. The collection can be viewed as a set of SortColumnDescriptors one for every column against which the data is sorted. The SortColumnDescriptor of a field contains the details like the name of a field, sort direction and optionally a custom comparer and categorization object. The custom comparer and categorizer will allow you to customize the sorting.

[] 

**Sorting Methods**

**[]** 

There are multiple ways through which you can apply sorting on table data. A simple one is just clicking the desired column headers by which the grouping grid needs to be sorted. Once the sorting is applied, the grid will display a sort icon in the respective column headers showing the sort direction. The sorting can also be done against multiple columns by holding the Ctrl key and doing a click on the desired column headers.

 

**Through Designer**

**[]** 

At design time, the data can be sorted by accessing **SortedColumns** property under the TableDescriptor section in the property grid of the Grid Grouping control. This will open the SortColumnDescriptorCollection Editor. In that Editor, clicking the Add button will add the existing columns into the collection. The **Name** and **SortDirection** in the property window of the editor will let you specify your desired field name to sort and the sort order. The image given below illustrates this process.

[] 

{border="0"}

[] 

*[Figure ][284][: SortColumnDescriptor Collection Editor]*

[] 

Programmatically

[] 

Sorting can be applied to the grid data by specifying the desired field name to the TableDescriptor.SortedColumns.Add() method.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                                  |
| [this][.gridGroupingControl1.TableDescriptor.SortedColumns.Add([\"ProductName\"]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                                               |
| [Me][.gridGroupingControl1.TableDescriptor.SortedColumns.Add([\"ProductName\"])] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**Multicolumn Sorting** can be achieved by adding the field names into the **SortedColumns** property and optionally specifying the sort direction. The following code example sorts the data by the ProductName and UnitPrice in ascending Order and by the column Quantity in descending Order.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [this][.gridGroupingControl1.TableDescriptor.SortedColumns.Add([\"ProductName\"], [ListSortDirection].Ascending);]      |
|                                                                                                                                                                                                                                                              |
| [this][.gridGroupingControl1.TableDescriptor.SortedColumns.Add([\"QuantityPerUnit\"], [ListSortDirection].Descending);] |
|                                                                                                                                                                                                                                                              |
| [this][.gridGroupingControl1.TableDescriptor.SortedColumns.Add([\"UnitPrice\"], [ListSortDirection].Ascending);]        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [Me][.gridGroupingControl1.TableDescriptor.SortedColumns.Add([\"ProductName\"], ListSortDirection.Ascending)]      |
|                                                                                                                                                                                                                                 |
| [Me][.gridGroupingControl1.TableDescriptor.SortedColumns.Add([\"QuantityPerUnit\"], ListSortDirection.Descending)] |
|                                                                                                                                                                                                                                 |
| [Me][.gridGroupingControl1.TableDescriptor.SortedColumns.Add([\"UnitPrice\"], ListSortDirection.Ascending)]        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Here is a sample output. To indicate the sort direction, a sort icon will be displayed in the column headers. When multicolumn sorting is applied, an index number will be displayed in the column headers along with the sort icon that facilitates the sort order. In the below example, the order of the sorting would be **ProductName(0)**, **Quantity(1)** and then **UnitPrice(2)**.

[] 

{border="0"}

***[]*** 

*[Figure ][285][: Multi Column Sorting]*

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Sort\\Multi Column Sort Demo


[] 

Sorting By Display Member

[] 

Grid Grouping control sorts the grid based on the Value member of the grid data, by default. The user can also sort the grid data by Display members of the foreign-key combo boxes by setting up a foriegn-key reference relation between the related tables.

[] 


{border="0"}Note: A foreign-key reference relation allows the user to look up values in a related table using an id column in the main table.


[] 

The following code example illustrates the usage of foreign key relation:

[] 

1.   Save the location of the mainTable.Customer column, so that it can be swapped after the foreign table reference has been set.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [GridTableDescriptor][ td = [this].gridGroupingControl1.TableDescriptor; td.VisibleColumns.LoadDefault();] |
|                                                                                                                                                                                                                         |
| [int][ lookUpIndex = td.VisibleColumns.IndexOf([\"Customer\"]);]                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [Dim][ td [As] GridTableDescriptor = [Me].gridGroupingControl1.TableDescriptor]                        |
|                                                                                                                                                                                                                                       |
| [td.VisibleColumns.LoadDefault()]                                                                                                                                                                 |
|                                                                                                                                                                                                                                       |
| [Dim][ lookUpIndex [As] [Integer] = td.VisibleColumns.IndexOf([\"Customer\"])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Add the foreign table to the Engine\'s source list.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [this][.gridGroupingControl1.Engine.SourceListSet.Add(ForeignTableName, ForeignTable.DefaultView);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                    |
|                                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                                       |
| [Me][.gridGroupingControl1.Engine.SourceListSet.Add(ForeignTableName, ForeignTable.DefaultView)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Create and setup a RelationKind.ForeignKeyReference relation.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [GridRelationDescriptor][ rd = [new] [GridRelationDescriptor]();] |
|                                                                                                                                                                                                        |
| [rd.Name = [\"CustomerColDisplay\"];]                                                                                                      |
|                                                                                                                                                                                                        |
| [rd.RelationKind = [RelationKind].ForeignKeyReference;]                                                                                    |
|                                                                                                                                                                                                        |
| [rd.ChildTableName = ForeignTableName;]                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                     |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [Dim][ rd [As] GridRelationDescriptor = [New] GridRelationDescriptor()] |
|                                                                                                                                                                                                        |
| [rd.Name = [\"CustomerColDisplay\"]]                                                                                                       |
|                                                                                                                                                                                                        |
| [rd.RelationKind = RelationKind.ForeignKeyReference]                                                                                                               |
|                                                                                                                                                                                                        |
| [rd.ChildTableName = ForeignTableName]                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Set any optional properties on the relation.

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [// Display column.     ]                                                   |
|                                                                                                                               |
| [rd.ChildTableDescriptor.VisibleColumns.Add([\"CustomerName\"]);] |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [// Sort it for dropdown display.]                                          |
|                                                                                                                               |
| [rd.ChildTableDescriptor.SortedColumns.Add([\"CustomerName\"]);]  |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                           |
|                                                                                                                              |
| []                                                                                       |
|                                                                                                                              |
| [\' Display column.    ]                                                   |
|                                                                                                                              |
| [rd.ChildTableDescriptor.VisibleColumns.Add([\"CustomerName\"])] |
|                                                                                                                              |
| []                                                                                       |
|                                                                                                                              |
| [\' Sort it for dropdown display. ]                                        |
|                                                                                                                              |
| [rd.ChildTableDescriptor.SortedColumns.Add([\"CustomerName\"])]  |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Add relation descriptor to MainTableDescriptor.

[] 

+-----------------------------------------------------------------------+
| **[\[C#\]]**        |
|                                                                       |
| []                  |
|                                                                       |
| [td.Relations.Add(rd); ]          |
+-----------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------+
| **[\[VB.NET\]]**    |
|                                                                       |
| []                                |
|                                                                       |
| [td.Relations.Add(rd)]            |
+-----------------------------------------------------------------------+

[] 

6.   Replace mainTable.Customer with foreignTable.CustomerName.   

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [string][ foreignCustomerColInMainTable = rd.Name + [\"\_\"] + [\"CustomerName\"]; ] |
|                                                                                                                                                                                                                           |
| [td.VisibleColumns.Insert(CustomerColIndex, foreignCustomerColInMainTable);]                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [Dim][ foreignCustomerColInMainTable [As] [String] = rd.Name & [\"\_\"] & [\"CustomerName\"]] |
|                                                                                                                                                                                                                                                                              |
| [td.VisibleColumns.Insert(CustomerColIndex, foreignCustomerColInMainTable)]                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the application. The following output is generated.

[] 

{border="0"}

[] 

*[Figure ][286][: Foreign-Key Relation]*

[] 

In the figure above, the CustomerName column is displayed in the Foreign Table where as a column named Customer is located in the Main Table. Customer column holds key values that match the values in a column named CustomerID in the Foreign Table.

 

Refer following sample in our sample browser:

[] 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Sort\\Sort By Display Member Demo***

 

[]{#p424} 

 

###### 4.3.4.3.2.1 Enable or Disable Sorting {#enable-or-disable-sorting style="tab-stops: 0pt"}

 

By default, the Grouping Grid supports automatic sorting. When you want to disable this automatic sorting, you can use the following methods to prevent sorting on specific columns.

 

**Properties used to control Sorting**

**[]** 

Sorting on the grid data can be controlled by two boolean properties under TableOptions: **AllowSortColumns** and **AllowMultiColumnSort**. These properties are used to enable and disable the sorting action. They are set to True by default. To prevent sorting against multiple columns, you should set AllowMultiColumnSort to False whereas the AllowSortColumns property should be set to True to allow single column sorting. The screenshot given below highlights these properties in the property window.

[] 

{border="0"}

[] 

*[Figure ][287][: Sorting Properties]*

[] 

Event used to Prevent Sorting

[] 

Sorting on specified columns can also be controlled by handling the TableControlQueryAllowSortColumn event. The event accepts an instance of GridQueryAllowSortColumnEventArgs as a parameter that contains the details of the column being affected. Using this instance, you can check for a particular column and cancel the sorting behavior.

 

The following code example prevents sorting on the CompanyName field.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [this][.gridGroupingControl1.TableControlQueryAllowSortColumn+=[new] [GridQueryAllowSortColumnEventHandler](gridGroupingControl1_TableControlQueryAllowSortColumn);] |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [private][ [void] gridGroupingControl1_TableControlQueryAllowSortColumn([object] sender, [GridQueryAllowSortColumnEventArgs] e)]                |
|                                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [    [if](e.Column.GetName() == [\"CompanyName\"])]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                        |
| [        e.AllowSort=[false];]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                        |
| [    }]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [AddHandler][ gridGroupingControl1.TableControlQueryAllowSortColumn, [AddressOf] gridGroupingControl1_TableControlQueryAllowSortColumn]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] gridGroupingControl1_TableControlQueryAllowSortColumn([ByVal] sender [As] [Object], [ByVal] e [As] GridQueryAllowSortColumnEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [If][ e.Column.GetName() = [\"CompanyName\"] [Then]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [e.AllowSort=[False]]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [If]]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: For more details, refer the following browser sample:

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Sort\\Sort Method Demo


 

[]{#p425} 

 

[]{#related-topics}

