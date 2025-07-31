---
title: dataerrorvalidation.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\dataerrorvalidation.md
created_at: 2025-07-03
---






#### Data Error Validation {#data-error-validation style="tab-stops: 0pt"}

Essential Grid now provides support to validate the grid data and display error information. This is achieved by subscribing to the IDataErrorInfo, an interface that provides the functionality to display custom error information in any control.

 

To validate data errors, follow the steps below:

 

1.   Ensure that your data source implements the IDataErrorInfo interface, in which two of the properties, Error (which we can be left empty optionally) and Indexer (where the validation code is placed) must be defined.

 

2.   Then display the error information by setting the ShowErrorToolTips property of the GridData control to *true*.

[] 

+-------------------------------------------------------------------------------------------------+
| [\[C#\]]                                      |
|                                                                                                 |
| []                                            |
|                                                                                                 |
| [dataGrid.ShowErrorTooltips = [true];] |
+-------------------------------------------------------------------------------------------------+

 

The following code example illustrates how the GridData control throws an error message when the Freight value becomes lesser than 10.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                            |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [partial][ [class] [Orders] : IDataErrorInfo]                       |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [public][ [string] Error]                                                                   |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [get]                                                                                                                                                |
|                                                                                                                                                                                                       |
| [{ ]                                                                                                                                                              |
|                                                                                                                                                                                                       |
| [throw][ [new] [NotImplementedException]();]                        |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [public][ [string] [this]\[[string] columnName\]] |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [get]                                                                                                                                                |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [var][ result = [string].Empty;]                                                            |
|                                                                                                                                                                                                       |
| [if][ (columnName == [\"Freight\"])]                                                     |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [if][ ([this].Freight.Value \< 10)]                                                         |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [result = [\"Freight is very low\"];]                                                                                                     |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [return][ result;]                                                                                               |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screen shot illustrates Data Error Validation in the GridData control.

 

{border="0"}

Figure 151: Data Errors generated in the GridData control

 

[]{#p265} 

 

[]{#related-topics}

