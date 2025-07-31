---
title: howtocreateamultiselectdropdowngridinacell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtocreateamultiselectdropdowngridinacell.md
created_at: 2025-07-03
---








  









### How to Create a Multi-Select DropDown Grid in a Cell {#how-to-create-a-multi-select-dropdown-grid-in-a-cell style="tab-stops: 0pt"}

[] 

Introduction

 

To have a cell that has a multi-selection dropdown grid, you must use a derived custom cell that is derived from the **GridDropDownGridCellModel** and the **GridDropDownGridCellRenderer**.

[] 

1.   In the derived renderer, the code embeds the **GridControl** whose **ListBoxSelectionMode** is set to MultiSimple. The renderer uses the **DropDownContainerCloseDropDown** override to move the text in the selected rows of the embedded grid, into a string that is set into the style. The **CellValue** of the cell in the parent grid which, hosts this custom **celltype** lists the selected options as a hyphen delimited string for every column, and the NewLine delimited string for every row.

[] 

Example

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [// Creates an instance of the DropDownGrid Model.]                                                                                                      |
|                                                                                                                                                                                                            |
| [DropDownGridCellModel aModel = ][new][ ]             |
|                                                                                                                                                                                                            |
| [DropDownGridCellModel(][this][.gridControl1.Model);] |
|                                                                                                                                                                                                            |
| [aModel.EmbeddedGrid = GridA;]                                                                                                                           |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [// To register the DropDownGridCellModel to GridModel.]                                                                                                 |
|                                                                                                                                                                                                            |
| [gridControl1.CellModels.Add(\"MultiSelectCombo\",aModel);]                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' Creates an instance of the DropDownGrid Model.]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ aModel ][As][ DropDownGridCellModel = ][New][ ] |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [DropDownGridCellModel(][Me][.gridControl1.Model)]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [aModel.EmbeddedGrid = GridA]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\' To register the DropDownGridCellModel to GridModel.]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [gridControl1.CellModels.Add(\"MultiSelectCombo\",aModel)]                                                                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Set the CellType property to \"MultiSelectCombo\".

[] 

Example

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [// Set the CellType to \'MultiSelectCombo\'.]                                                                 |
|                                                                                                                                                                  |
| [this][.gridControl1\[4,2\].CellType = \"MultiSelectCombo\";] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [\' Set the CellType to \'InPlaceRTB\'.]                                                                  |
|                                                                                                                                                             |
| [Me][.gridControl1(4,2).CellType = \"MultiSelectCombo\"] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p554} 

 

[]{#related-topics}

