---
title: datavalidation2.md
original_path: WinForms_Docs/03_Data_Binding/datavalidation2.md
created_at: 2025-08-05
---








  









### Data Validation {#data-validation style="tab-stops: 0pt"}

The Data Validation enables you to dynamically validate the data entered in a cell. You can specify the validation rules in the Data Validation dialog box. Spreadsheet control supports the various validation types for each data type. This also enables you to show the error message for invalid.

 

{border="0"}

Figure 25: Data Validation Dialog

 

Data Validation in Spreadsheet control

 

Essential Spreadsheet control enables you to edit the existing data validation. You can also create new data validation. Spreadsheet control supports the following validation types:

[] 

[·      ]Text Length Validation

[·      ]Time Validation

[·      ]List Validation

[·      ]Number Validation

[·      ]Date Validation

 

Events

 

Table 1: EventTable


+------------------------+-----------------------------------------------------+-----------------------------------------------------------------------------+-------------+-----------------+
| Event                  | Description                                         | Arguments                                                                   | Type        | Reference links |
+------------------------+-----------------------------------------------------+-----------------------------------------------------------------------------+-------------+-----------------+
| CurrentCellValidating  | Will be triggered when the cell value is committed. | void CurrentCellValidating(object sender, CurrentCellValidatingEventArgs e) | Routed      | NA              |
|                        |                                                     |                                                                             |             |                 |
|                        | This can be cancelled.                              |                                                                             |             |                 |
|                        |                                                     |                                                                             |             |                 |
|                        | Error alert can be customized.                      |                                                                             |             |                 |
+========================+=====================================================+=============================================================================+=============+=================+


 

 

More:





