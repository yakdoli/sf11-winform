---
title: businessobjects.md
original_path: WinForms_Docs/99_Uncategorized/businessobjects.md
created_at: 2025-08-05
---






#### Business Objects {#business-objects style="tab-stops: 0pt"}

[] 

The grid can be bound to user-defined collections that let you store arbitrary objects in a structured fashion.  The data binding is based on a set of interfaces that differ in the context of accessing and navigating through data and of course manipulating the data. These interfaces set up a two-way communication between the bound grid and the objects collection used by the same grid. Such object collections are called as *custom business collections*.

 

The data binding interfaces will allow you to create collection of custom objects where you want to present those collection of objects together, through the grid. You can also navigate through the objects to view them through the same grid and interact with them. Some of these interfaces are IList, IBindingList, and so on. For ease of use, .NET provides built-in, ready-to-use collection classes that internally implements these collection interfaces.

 

Some of the collection classes are as follows:

[] 

[·      ]List that implements IList

[·      ]BindingList that implements IBindingList

[·      ]ObservableCollection.

[] 

Of the above classes, the **ObservableCollection** is widely preferred as it is more user-friendly to use in a WPF application, and can be easily created using XAML. 

 

Let us see an example usage of this collection class with our Grid Data control.

 

Example

**[]** 

Defining Observable Collection

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [public][ [class] Customer : ObservableCollection\<Customers\>]                                                                                         |
|                                                                                                                                                                                                                                                                   |
| [{        ]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [Northwind northWind;        ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| [public][ Customer()        ]                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| [{            ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [string][ connectionString = [string].Format([@\"Data Source = {0}\"], [Northwind.sdf\"]);            ] |
|                                                                                                                                                                                                                                                                   |
| [northWind = [new] Northwind(connectionString);            ]                                                                                                                                             |
|                                                                                                                                                                                                                                                                   |
| [var customer = northWind.Customers.Skip(0).Take(100).ToList();            ]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| [foreach][ (var o [in] customer)            ]                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [{                ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                   |
| [this][.Add(o);            ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                   |
| [}        ]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [}    ]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Binding the Above Collection to GDC

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][Window.Resources][\>][        ]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][ObjectDataProvider][ [x:Key][=\"customer\"] [ObjectType][=\"{x:Type local:Customer}\"] [/\>]]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][Window.Resources][\>]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][syncfusion:GridDataControl][ [x:Name][=\"grid\"]  [AutoPopulateColumns][=\"True\"]    [AutoPopulateRelations][=\"False\"] [ItemsSource][=\"{StaticResource customer}\"\>]            ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][syncfusion:GridDataControl][\>]                                                                                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image shows a Grid bound with an Observable collection.

[] 

{border="0"}

***[]*** 

Figure 98: GDC bound to the ObservableCollection

***[]*** 

The GDC is bound with a data source provided by Observable Collection.

[] 

Collection View Source

**[]** 

The CollectionViewSource\[CVS\] serves as a wrapper for the custom collections. It acts as a filter between the source collection (ObservableCollection or List or BindingList) and the grid. Once your grid is bound to CollectionViewSource-driven source list, the CVS will manage all the data related operations such as grouping, sorting, filtering and so on. This relieves you of writing custom code for these operations. CVS does this by internally implementing the **ICollectionView** interface that understands the source type and manages the data operations. It also implements INotifyCollectionChanged interface. This means that if CVS is linked to a source collection (ObservableCollection), then all the updates to the source list will be transmitted to the grid.

[] 

Example

[] 

Let us see an example usage of this Collection View Source with our GDC.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][Window.Resources][\>][        ]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][ObjectDataProvider][ [x:Key][=\"customer\"] [ObjectType][=\"{x:Type local:Customer}\"] [/\>]        ]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][CollectionViewSource][ [x:Key][=\"customerSource\"] [Source][=\"{StaticResource customer}\"] [\>]        ]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][CollectionViewSource][\>][    ]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][Window.Resources][\>]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion:GridDataControl][ [x:Name][=\"grid\"]  [AutoPopulateColumns][=\"True\"]    [AutoPopulateRelations][=\"False\"] [ItemsSource][=\"{StaticResource customerSource}\"\>]            ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][syncfusion:GridDataControl][\>]                                                                                                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Defining the Source Collection

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [public][ [class] Customer : ObservableCollection\<Customers\>    ]                                                                                       |
|                                                                                                                                                                                                                                                                     |
| [{        ]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
| [Northwind northWind;        ]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| [public][ Customer()        ]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| [{            ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [string][ connectionString = [string].Format([@\"Data Source = {0}\"], [\"Northwind.sdf\"]);            ] |
|                                                                                                                                                                                                                                                                     |
| [northWind = [new] Northwind(connectionString);            ]                                                                                                                                               |
|                                                                                                                                                                                                                                                                     |
| [var customer = northWind.Customers.Skip(0).Take(100).ToList();            ]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| [foreach][ (var o [in] customer)            ]                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [{                ]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [this][.Add(o);            ]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                     |
| [}        ]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
| [}    ]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image shows the output of the above given code:

[] 

{border="0"}

[] 

Figure 99: Collection View Source with GDC

***[]*** 

The GDC is bound with a data source provided by Collection View Source.

[] 

Entity Collection

[] 

GridDataControl confirms that it is an EntityFramework-aware control by providing support to EF-driven data sources. The EF model offers several architectural benefits that can be experienced in the networking applications.

 

To bind your grid to an EF-driven data source, use the below code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [string][ connectionString = [string].Format([@\"Data Source = {0}\"], [LayoutControl].FindFile([\"NorthwindGrid.sdf\"]));            ] |
|                                                                                                                                                                                                                                                                                                                        |
| [EntityConnectionStringBuilder entityBuilder = [new] EntityConnectionStringBuilder();            ]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                        |
| [entityBuilder.Metadata = [\"res://\*/NorthWind.csdl\|res://\*/NorthWind.ssdl\|res://\*/NorthWind.msl\"];            ]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                        |
| [entityBuilder.Provider = [\"System.Data.SqlServerCe.3.5\"];            ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                        |
| [entityBuilder.ProviderConnectionString = connectionString;]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                        |
| [NorthWind][ northwind = [new] [NorthWind](entityBuilder.ToString());            ]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.gridDataControl1.ItemsSource = northwind.Orders;]                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 100: Grid Control bound to an EntityFramework-driven Data Source

[]{#p232} 

 

[]{#related-topics}

