---
title: databinding30.md
original_path: WinForms_Docs/03_Data_Binding/databinding30.md
created_at: 2025-08-05
---








  









### [][]{#p257}Data Binding {#data-binding style="tab-stops: 0pt"}

Data binding is the master feature of the GridData control. Grid must be bound to an external data source to display the data. GDC supports the following data sources such as, Data Tables, Data Sets or Custom collections of type List, Binding List, Observable Collection or Collection View Source. These data source can have multiple nested tables, which will be displayed hierarchically by the grouping grid.

 

Data Binding mechanisms

 

Following are the data binding mechanisms:

 

[·      ]Using Data Providers-Object Data Provider,  XML Data Provider and usage of Data Context

[·      ]Using ADO.NET Data-Data Table,  Data Set  and Data Row

[·      ]Using Business Objects-List, Binding List, Observable Collection, Collection View Source

[·      ]XAML Binding-Elaborates on data binding using XAML code

[·      ]Notify Property Changes-Elaborates on notifying the underlying data source changes to the grid

[·      ]Data Error Validation-Discusses on the support to validate the grid data and display error information

[·      ]Synchronize Current Selection-Discusses about synchronization of changes in the current with another control

[·      ]Unbound Columns-Discusses on the addition of unbound columns to the grid

**[]** 

Important Data Binding Properties

 

The following table contains some data binding properties and their corresponding descriptions:

 


  ----------------------- ------------------------------------------------------------------------------------------------------
  Property                Description
  DataContext             Gets or sets the data context for binding. It simplifies the data binding.
  ItemsSource             Binds the grid to a collection object.
  AutoPopulateColumns     When set to true, it extracts the column from the data set and populates the Grid automatically.
  AutoPopulateRelations   When set to true, it extracts the  relation from the data set and populates  the Grid automatically.
  ----------------------- ------------------------------------------------------------------------------------------------------


 

 

More:























