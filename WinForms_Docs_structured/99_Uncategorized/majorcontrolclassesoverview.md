---
title: majorcontrolclassesoverview.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\majorcontrolclassesoverview.md
created_at: 2025-07-03
---








  









### Major Control Classes Overview {#major-control-classes-overview style="tab-stops: 0pt"}

[] 

GridGroupingControl Class

[] 

The GridGroupingControl class is derived from the **Control** class and implements several interfaces that add Grouping support to this class. Provides support for displaying ADO.NET data and other data sources in a grid. Data will be loaded from the given datasource and changes will be written back to the datasource.

 

It is the proper choice if you need grouping support, multi-column sort support or true nested-table hierarchical support in a grid. It can be bound to any IList datasource. You can easily add expression columns, filter columns and summary rows to this grid. It is fully designable using Visual Studio and is customizable from code.

 

The **GridTableControl** is the main element in the Grid Grouping control. The Grid Table control displays the rows from the **Syncfusion.Grouping.Table.DisplayElements** collection of the Grid Grouping control.Table using schema information stored in the TableDescriptor.

[] 

The **TableDescriptor** gives access to the table schema information of the root table in the datasource. The TableDescriptor object is instantiated by the **GridEngine** class and initialized with default schema information from the list assigned to the DataSource.

[] 

There is only one GridEngine object for a Grid Grouping control. The GridTableDescriptor and GridTable objects on the other side can be more than one when hierarchies are displayed. For each hierarchy level, a GridTableDescriptor and GridTable are initialized. For example, if you have an ADO.NET DataSet with three tables: \"Products\", \"Orders\", and \"OrderDetails\", there will be three GridTableDescriptors and GridTables.

[  ]

**Relations** between tables are defined with a GridTableDescriptor.Relations collection of a TableDescriptor. Each TableDescriptor can have one or multiple **RelationDescriptor** objects. A RelationDescriptor defines the foreign key columns in the parent table, a child with information about the related child table and the primary key columns in the child table.

[] 

The **GridTable** object is instantiated by the **GridEngine** class. The Table object manages the records from the engine\'s DataSource and provides access to records and grouped elements through several collection classes.

 

The most important collection used by the Grid Table control is the **DisplayElements** collection. This collection provides the Grid Table control with information on which element to display at a row. It returns elements such as CaptionSection, RecordRow, SummaryRow, and others. Based on the elements returned by this collection, the Grid Table control will display a record, a summary or a group caption bar. There are several collections returned such as Records which contains all records in the table. FilterRecords contains all visible records.

[] 

Another related collection is the **NestedDisplayElements** collection. Similar to DisplayElements, this collection also returns all records, groups and sections that are expanded and meet filter criteria. The only difference between these two collections is that the NestedDisplayElements collection steps into nested tables too where the DisplayElements collection will not.

[] 

The Grouping Engine

 

**Engine** is the main object of the grid grouping control. It contains the **TableDescriptor** with schema information such as fields, relations and the **Table** with runtime representation of the data source with groups, records, data and display elements. The engine lets you set the main datasource for the whole engine. The TableDescriptor will pick up the ItemProperties (schema information) from the datasource and the table will be initialized at runtime with records from the list.

 

The **GridEngineBase** class adds design-time support for the engine class. It can be dropped as a component into the component tray of the designer. It can be initialized with a BindingContext so that the CurrencyManager can be kept synchronized.

 

The **GridEngine** class adds the plumbing for displaying the data in a Grid Grouping control. You can specify the datasource using the DataSource and DataMember properties through the designer. It is instantiated with the virtual GridGroupingControl.CreateEngine method. If you want to customize the engine object, you should subclass this class and should override the CreateEngine method.

 

The GridEngine object is the main grouping engine object. It is derived from the Syncfusion.Grouping.Engine base class and adds Windows Forms specific functionality such as support for a Forms BindingContext and CurrencyManager. GridEngine also has special overrides of the virtual **Engine.CreateTableDescriptor** and **Engine.CreateTable** methods so that the grid-specific derived GridTable class and GridTableDescriptor class are instantiated.

 

[]{#p396} 

 

[]{#related-topics}

