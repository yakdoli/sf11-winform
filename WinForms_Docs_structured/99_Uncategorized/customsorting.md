---
title: customsorting.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customsorting.md
created_at: 2025-07-03
---








  









### Custom Sorting {#custom-sorting style="tab-stops: 0pt"}

[] 

Custom Sorting

**[]** 

Custom sorting enables you to implement custom sorting logic if the standard sorting techniques don\'t meet your requirements.

 

You can add a custom IComparer to the GridSortColumnDescriptor for this column. You do this by setting the Comparer property on the GridSortColumnDescriptor. In your custom IComparer object, you can sort based on any criteria you choose including any color criteria on the record value.

 

The Comparer object allows you to control how the sorting is done on your column. Once the column is sorted, the custom Categorizer is used to determine which adjacent records in the sorted column belong to the same group. To create custom Comparer and Categorizer objects, you define classes that implement IComparer.

[] 

Example Scenario

[] 

The following code snippet sorts the column Name.

[] 

[·      ]First include the required namespace for implementing the custom Comparer.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                                             |
| []                                                                                        |
|                                                                                                                                             |
| [using][ System.Collections;]                          |
|                                                                                                                                             |
| [using][ Syncfusion.Web.UI.WebControls.Grid.Grouping;] |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                            |
|                                                                                                                                               |
| []                                                                                           |
|                                                                                                                                               |
| [Imports][ System.Collections]                           |
|                                                                                                                                               |
| [Imports][ Syncfusion.Web.UI.WebControls.Grid.Grouping;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Set up the following data source to the GridGroupingControl.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][asp][:][AccessDataSource][ [ID][=\"AccessDataSource1\"] [runat][=\"server\"] [SelectCommand][=\"SELECT \[EmployeeID\],\[FirstName\]+ \' \' + \[LastName\] as Name, \[BirthDate\], \[Address\], \[PostalCode\], \[Country\], \[City\] FROM \[Employees\]\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [ [\</][asp][:][AccessDataSource][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)]                           |
|                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [    [this].AccessDataSource1.DataFile = ResolveApplicationDataPath([\"NWIND.MDB\"]);]                                                                         |
|                                                                                                                                                                                                                                                 |
| [    [this].GridGroupingControl1.DataSource = AccessDataSource1;]                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [  [if](RadioButtonList1.SelectedItem.Value==[\"2\"])]                                                                                                         |
|                                                                                                                                                                                                                                                 |
| [    [this].GridGroupingControl1.TableDescriptor.SortedColumns.Changed += [new] Syncfusion.Collections.ListPropertyChangedEventHandler(SortedColumns_Changed);]   |
|                                                                                                                                                                                                                                                 |
| [  [else]]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [      [this].GridGroupingControl1.TableDescriptor.SortedColumns.Changed -= [new] Syncfusion.Collections.ListPropertyChangedEventHandler(SortedColumns_Changed);] |
|                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Use **GridGroupingControl.TableDescriptor.SortedColumns.Changing** event to hook into the sorting to use custom comparer.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [this][.GridGroupingControl1.TableDescriptor.SortedColumns.Changing+=[new] Syncfusion.Collections.ListPropertyChangedEventHandler(SortedColumns_Changed);] |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [void][ SortedColumns_Changed([object] sender, Syncfusion.Collections.ListPropertyChangedEventArgs e)]                                                     |
|                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [if][ (e.Action == Syncfusion.Collections.ListPropertyChangedType.Add \|\| e.Action == Syncfusion.Collections.ListPropertyChangedType.Insert)]                                  |
|                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [            ]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [            SortColumnDescriptor sd = e.Item [as] SortColumnDescriptor;]                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [            ]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [            [if] (sd.Name == [\"Name\"])]                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [            {]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [                sd.Comparer = [new] NameComparer();]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [            }]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [        [else] [if] (!IsAlreadySorted)]                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [            [if] (e.Action == Syncfusion.Collections.ListPropertyChangedType.ItemPropertyChanged)]                                                                                                         |
|                                                                                                                                                                                                                                                                      |
| [            {]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [                SortColumnDescriptor sd = e.Item [as] SortColumnDescriptor;]                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [                [if] (sd.Name == [\"Name\"])]                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [                {]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [                    IsAlreadySorted = [true];]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [                    sd.Comparer = [new] NameComparer();]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| [                }]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                      |
| [            }]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Me][.GridGroupingControl1.TableDescriptor.SortedColumns.Changing+= [New] Syncfusion.Collections.ListPropertyChangedEventHandler(SortedColumns_Changed)]                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] SortedColumns_Changed([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Collections.ListPropertyChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [If] e.Action = Syncfusion.Collections.ListPropertyChangedType.Add [OrElse] e.Action = Syncfusion.Collections.ListPropertyChangedType.Insert [Then]]                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [Dim] sd [As] SortColumnDescriptor = [TryCast](e.Item, SortColumnDescriptor)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [If] sd.Name = [\"Name\"] [Then]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            sd.Comparer = [New] NameComparer()]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [End] [If]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [ElseIf] ([Not] IsAlreadySorted) [Then]]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [If] e.Action = Syncfusion.Collections.ListPropertyChangedType.ItemPropertyChanged [Then]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            [Dim] sd [As] SortColumnDescriptor = [TryCast](e.Item, SortColumnDescriptor)]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            [If] sd.Name = [\"Name\"] [Then]]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| [                IsAlreadySorted = [True]]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| [                sd.Comparer = [New] NameComparer()]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                              |
| [            [End] [If]]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                              |
| [        [End] [If]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| [    [End] [If]]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Set up the custom Comparer object.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                       |
|                                                                                                                                                                                                           |
| [public][ [class] [NameComparer] : [IComparer]] |
|                                                                                                                                                                                                           |
| [{]                                                                                                                                                                   |
|                                                                                                                                                                                                           |
| [    [public] NameComparer()]                                                                                                                    |
|                                                                                                                                                                                                           |
| [    {]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [    }]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [    #region][ IComparer Members]                                                                                    |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [    [public] [int] Compare([object] x, [object] y)]                              |
|                                                                                                                                                                                                           |
| [    {]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| [        [string] p1 = ([string])x;]                                                                                        |
|                                                                                                                                                                                                           |
| [        [string] p2 = ([string])y;]                                                                                        |
|                                                                                                                                                                                                           |
| [        [string]\[\] p1names = p1.Split([new] [char]\[\] { [\' \'] });]       |
|                                                                                                                                                                                                           |
| [        [string]\[\] p2names = p2.Split([new] [char]\[\] { [\' \'] });]       |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [        [return] p1names\[1\].CompareTo(p2names\[1\]);]                                                                                         |
|                                                                                                                                                                                                           |
| [    }]                                                                                                                                                               |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [    #endregion]                                                                                                                                         |
|                                                                                                                                                                                                           |
| [}]                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Public][ [Class] NameComparer : [Implements] IComparer]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [Public] [Sub] [New]()]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [End] [Sub]]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\#[Region] [\"IComparer Members\"]]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [Public] [Function] Compare([ByVal] x [As] [Object], [ByVal] y [As] [Object]) [As] [Integer] [Implements] IComparer.Compare] |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        [Dim] p1 [As] [String] = [CStr](x)]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        [Dim] p2 [As] [String] = [CStr](y)]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        [Dim] p1names [As] [String]() = p1.Split([New] [Char]() {\" \"c})]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        [Dim] p2names [As] [String]() = p2.Split([New] [Char]() {\" \"c})]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [        [Return] p1names(1).CompareTo(p2names(1))]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    [End] [Function]]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\#[End] [Region]]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Class]]                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

Figure 75[]

[] 

[]{#related-topics}

