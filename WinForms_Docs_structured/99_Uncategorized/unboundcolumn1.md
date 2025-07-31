---
title: unboundcolumn1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\unboundcolumn1.md
created_at: 2025-07-03
---








  









### Unbound Column {#unbound-column style="tab-stops: 0pt"}

The data you display in the Grid control will normally come from a data source of some kind, but you might want to display a column of data that does not come from the data source. This kind of column is called an unbound column.

Unbound columns are used to display custom content in the grid. For example, if you want to display some new columns like buttons or links to other parts of the grid, this feature will be useful.

Essential Grid supports adding unbound column through **IRootGridColumnBuilder** in the view. While using unbound columns you will be unable to perform sorting, grouping, and filtering functionalities.

 

Methods

 


  ----------- -------------------------------------------- -------------- -------------------------
  Method      Descriptions                                 Parameters     Return type
  Add()       Used to add unbound column to grid control   string         IRootColumnBuilder\<T\>
  UnBound()   Used to convert the bound to Unbound         No parameter   IColumnBuilder\<T\>
  ----------- -------------------------------------------- -------------- -------------------------


 

More:







