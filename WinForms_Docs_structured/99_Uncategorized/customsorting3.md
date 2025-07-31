---
title: customsorting3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customsorting3.md
created_at: 2025-07-03
---






##### Custom Sorting {#custom-sorting style="tab-stops: 0pt"}

Custom sorting helps you to sort the records of the selected field values depending on your needs.  It also allows you to sort the data against one or more columns in the GridDataControl.

 

The custom sorting sorts the values using custom sorting logic. To perform the custom sorting, you need to hook the *SortColumnChanging* or *SortColumnChangingCommand* event and pass the custom sorting logic to the *CustomComparer*.

 

To create a custom comparer to implement the custom sorting logic, you need to derive the logic from *IComparer\<object\>* and *ISortDirection*. The custom sorting is performed by comparing the values of particular columns. When grouping is applied, the custom sorting can be performed by comparing the Group keys.

 

Example Scenario

 

The following code examples illustrate how to perform the custom sorting for the names in the **Company Name** column according to the string length of the names.

 

To enable the custom sorting, hook the *SortColumnsChanging* event.

**[]** 

+----------------------------------------------------------------------------------+
|     [C#]                                                                         |
|                                                                                  |
|                                                                                  |
|                                                                                  |
|     this.dataGrid.Model.Table.SortColumnsChanging += new GridDataSortColumnsChan |
|                                                                                  |
|     gingEventHandler(Table_SortColumnsChanging);                                 |
|                                                                                  |
|                                                                                  |
+----------------------------------------------------------------------------------+

**[]** 

Set the comparer for the column on which the data needs to be sorted using the custom sorting logic. Here, the comparer is assigned to CompanyName.

**[]** 

+------------------------------------------------------------------------------------+
| **[\[C#\]]**                                   |
|                                                                                    |
| []                                |
|                                                                                    |
|     //This method will be hooked when clicking the header                          |
|                                                                                    |
|                                                                                    |
|       void Table_SortColumnsChanging(object sender, GridDataSortColumnsChangingEve |
|                                                                                    |
|     ntArgs args)                                                                   |
|                                                                                    |
|     {                                                                              |
|                                                                                    |
|         if (args != null)                                                          |
|                                                                                    |
|         {                                                                          |
|                                                                                    |
|             foreach (var item in args.AddedItems)                                  |
|                                                                                    |
|             {                                                                      |
|                                                                                    |
|                //Choosing the column to be sorted                                  |
|                                                                                    |
|                                                                                    |
|                if (item.ColumnName.Equals("CompanyName"))                          |
|                                                                                    |
|                {                                                                   |
|                                                                                    |
|                    //Passing the custom sort logic to CustomComparer               |
|                                                                                    |
|                                                                                    |
|                    item.CustomComparer = new CustomerInfo();                       |
|                                                                                    |
|                }                                                                   |
|                                                                                    |
|             }                                                                      |
|                                                                                    |
|         }                                                                          |
|                                                                                    |
|     }                                                                              |
+------------------------------------------------------------------------------------+

 

Check the direction of the sorting by using the *SortDirection* property of the *ListSortDirection* class. The *Compare* method of the *IComparer* interface uses two parameters to compare the length of the string.

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [public][ [class] [CustomerInfo] : [IComparer]\<[Object]\>, [ISortDirection]\ |
|     {\                                                                                                                                                                                                                                              |
|         [//Implementation of ICompare method]]                                                                                                                                            |
|                                                                                                                                                                                                                                                     |
| [\                                                                                                                                                                                                                                                  |
|         [public] [int] Compare([object] x, [object] y)\                                                                                                         |
|         {\                                                                                                                                                                                                                                          |
|             [int] namX;\                                                                                                                                                                                                       |
|             [int] namY;\                                                                                                                                                                                                       |
|             [//For Normal case]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [            [if] (x.GetType() == [typeof]([Customers]))\                                                                                                                         |
|             {\                                                                                                                                                                                                                                      |
|                 [//Calculating the length if the object is of Customers type]]                                                                                                            |
|                                                                                                                                                                                                                                                     |
| [\                                                                                                                                                                                                                                                  |
|                 namX = (([Customers])x).CompanyName.Length;\                                                                                                                                                                |
|                 namY = (([Customers])y).CompanyName.Length;\                                                                                                                                                                |
|             }]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                     |
| [            [//While Grouping]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [\                                                                                                                                                                                                                                                  |
|             [else] [if] (x.GetType() == [typeof]([Group]))\                                                                                                  |
|             {\                                                                                                                                                                                                                                      |
|                 [//Calculating the length if the object is of Group type]]                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [\                                                                                                                                                                                                                                                  |
|                 namX = (([Group])x).Key.ToString().Length;\                                                                                                                                                                 |
|                 namY = (([Group])y).Key.ToString().Length;\                                                                                                                                                                 |
|             }\                                                                                                                                                                                                                                      |
|             [else]\                                                                                                                                                                                                            |
|             {\                                                                                                                                                                                                                                      |
|                 namX = x.ToString().Length;\                                                                                                                                                                                                        |
|                 namY = y.ToString().Length;\                                                                                                                                                                                                        |
|             }\                                                                                                                                                                                                                                      |
|             [//Object is passed through the Compare method and gets the]]                                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [ SortDirection.]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [\                                                                                                                                                                                                                                                  |
|             [if] (namX.CompareTo(namY) \> 0)\                                                                                                                                                                                  |
|                 [return] SortDirection == [ListSortDirection].Ascending ? 1 : -1;\                                                                                                                     |
|             [else] [if] (namX.CompareTo(namY) == -1)\                                                                                                                                                     |
|                 [return] SortDirection == [ListSortDirection].Ascending ? -1 : 1;\                                                                                                                     |
|             [else]\                                                                                                                                                                                                            |
|                 [return] 0;\                                                                                                                                                                                                   |
|         }\                                                                                                                                                                                                                                          |
|  \                                                                                                                                                                                                                                                  |
|         [//gets or sets the SortDirection]]                                                                                                                                               |
|                                                                                                                                                                                                                                                     |
| [\                                                                                                                                                                                                                                                  |
|         [private] [ListSortDirection] \_SortDirection;\                                                                                                                                                |
|         [public] [ListSortDirection] SortDirection\                                                                                                                                                    |
|         {\                                                                                                                                                                                                                                          |
|             [get]\                                                                                                                                                                                                             |
|             {\                                                                                                                                                                                                                                      |
|                 [return] \_SortDirection;\                                                                                                                                                                                     |
|             }\                                                                                                                                                                                                                                      |
|             [set]\                                                                                                                                                                                                             |
|             {\                                                                                                                                                                                                                                      |
|                 \_SortDirection = [value];\                                                                                                                                                                                    |
|             }\                                                                                                                                                                                                                                      |
|         }\                                                                                                                                                                                                                                          |
|     }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screenshot displays the **Company Name** column with the sorted names according to their length.

 

{border="0"}

Figure 171. Custom Sorting by "Company Name" header according to the string length

 

[]{#related-topics}

