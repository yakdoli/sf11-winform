---
title: propertiestableforpivotgrid1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\propertiestableforpivotgrid1.md
created_at: 2025-07-03
---








  









## Properties Table for PivotGrid {#properties-table-for-pivotgrid style="tab-stops: 0pt"}

**[]** 

Table 4: Properties Table


  ----------------------------------------------------- ----------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Property Name                                         Type                                      Description
  DeferLayoutUpdate****                                 bool****                                  Gets or sets a value to specify whether the layout should be updated immediately after updating the pivoting info, or if it should wait for a *Refresh()* call.[]
  FreezeHeaders[]               bool[]            Gets or sets a value to specify whether headers of a grid has to be frozen or not.[]
  DataSource[]                  object[]          Gets or sets the source of data for a pivot table. This object should be an IEnumerable or IQueryable list.[]
  PivotCalculations[]           Hashtable[]       Gets the collection of Pivot Calculations.[]
  PivotColumns[]                Hashtable[]       Gets the collection of pivot columns.[]
  PivotEngine[]                 PivotEngine[]     Gets or sets the pivot engine for a grid.[]
  PivotRows[]                   Hashtable[]       Gets the collection of pivot rows.[]
  ShowCalculationsAsColumns[]   bool[]            Gets or sets a value to specify whether calculations should appear as rows or columns. The default behavior is for calculations to appear as columns.[]
  ShowGrandTotals[]             bool[]            Gets or sets a value to specify whether grand total calculations should be computed by the engine.[]
  PivotCellInfo[]               PivotCellInfo[]   Gets or sets the PivotCellInfo in order to check the cell type.[]
  ----------------------------------------------------- ----------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[]{#related-topics}

