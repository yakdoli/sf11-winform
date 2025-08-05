---
title: summaries1.md
original_path: WinForms_Docs/99_Uncategorized/summaries1.md
created_at: 2025-08-05
---








  









## Summaries {#summaries style="tab-stops: 0pt"}

 

The Grid control allows you to display summaries. Summaries let you derive additional information from your data like averages, maximums, summations, counts, and more.

For instance, you can get the number of records or maximum value and so on. They display the calculation results in separate display rows. The summary values are calculated using **Linq** expressions.

The Grid control provides the following built-in summary types.

[·      ]Int32Aggregate, DoubleAggregate (Average, Minimum, Maximum, Sum)

[·      ]BooleanAggregate (Count, FalseCount, TrueCount)

[·      ]Count

 

Summary Rows

 

The **GridPropertiesModel.SummaryRows** manages the collection of summary rows for the grid. It is the **GridSummaryRowDescriptorCollection** that manages the summaries for the given data source containing one entry for each summary. Each **GridSummaryRowDescriptor** in this collection has a name that identifies the **SummaryRowDescriptors** for which summaries are calculated for and a **SummaryType** property that defines the type of calculations to be performed. Possible options for **SummaryType** are: **Count**, **BooleanAggregate**, **Int32Aggregate**, **DoubleAggregate**.

 

Properties

 


+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| Property       | Description                                                                                                                     | Type of property                      | Value it accepts               | Any other dependencies/sub-properties associated |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| AllowSummaries | Used to enable or disable the summary feature.                                                                                  | bool                                  | True/False                     | NA                                               |
|                |                                                                                                                                 |                                       |                                |                                                  |
|                | Default value is False.                                                                                                         |                                       |                                |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| SummaryRows    | A collection from GridSummaryRwoDecriptor that declares summary rows each with a multiple GridSummaryColumnDescriptor elements. | GridSummaryRowDescriptorCollection    |                                | Dependent with AllowSummaries.                   |
|                |                                                                                                                                 |                                       |                                |                                                  |
|                |                                                                                                                                 |                                       |                                |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| Name           | Name used to identify in the Summary collection.                                                                                |                                       |                                |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| SummaryType    | Specify the build-in summary type for SummaryColumnDescriptor.                                                                  | Enum                                  | SummaryType .Int32Aggregate,   |                                                  |
|                |                                                                                                                                 |                                       |                                |                                                  |
|                |                                                                                                                                 |                                       | SummaryType .DoubleAggregate,  |                                                  |
|                |                                                                                                                                 |                                       |                                |                                                  |
|                |                                                                                                                                 |                                       | SummaryType .BooleanAggregate, |                                                  |
|                |                                                                                                                                 |                                       |                                |                                                  |
|                |                                                                                                                                 |                                       | SummaryType .Count             |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| DataMember     | Specifies summary column used to perform the summary calculation.                                                               | string                                |                                |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| Format         | Indicates the format for the text applied on the column.                                                                        | string                                |                                |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| Prefix         | Specifies the text displayed before the summary column value.                                                                   | string                                |                                |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| Suffix         | Indicates the text displayed after the summary column value.                                                                    | string                                |                                |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| DisplayColumn  | Gets or sets the target column at which to display the summary.                                                                 | string                                |                                |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| Title          | Specifies the text displayed on the summary row.                                                                                | string                                |                                |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+
| SummaryColumns | Used to add summary columns in the Summary row.                                                                                 | GridSummaryColumnDescriptorCollection |                                |                                                  |
|                |                                                                                                                                 |                                       |                                |                                                  |
|                |                                                                                                                                 |                                       |                                |                                                  |
+----------------+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------+--------------------------------+--------------------------------------------------+


 

Methods

 

 


+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Method                                                             | Parameters                            | Class                                 | Return type | Description                                                                                                                |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Add(GridSummaryColumnDescriptor value)                             | GridSummaryColumnDescriptor           | GridSummaryColumnDescriptorCollection | Int         | Adds GridSummaryColumnDescriptor to the end of the collection.                                                             |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| AddRange(GridSummaryColumnDescriptor\[\] summaryColumnDescriptors) | Array of GridSummaryColumnDescriptors | GridSummaryColumnDescriptorCollection | Void        | Adds multiple GridSummaryColumnDescriptor at the end of the collection.                                                    |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Clear()                                                            | No parameter                          | GridSummaryColumnDescriptorCollection | Void        | Removes all GridSummaryColumnDescriptor from the collection.                                                               |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Contains(GridSummaryColumnDescriptor value)                        | GridSummaryColumnDescriptor           | GridSummaryColumnDescriptorCollection | bool        | Determines if the GridSummaryColumnDescriptor belongs to this Collection.                                                  |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Contains(string name)                                              | Name of the SummaryColumnDescriptor   |                                       | bool        | Determines if the GridSummaryColumnDescriptor with the specified name belongs to this Collection.                          |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       | GridSummaryColumnDescriptorCollection |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| IndexOf(GridSummaryColumnDescriptor value)                         | GridSummaryColumnDescriptor           | GridSummaryColumnDescriptorCollection | int         | Returns the zero-based index of the occurrence of the GridSummaryColumnDescriptor in the collection                        |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| IndexOf(string name)                                               | Name of the SummaryColumnDescriptor   | GridSummaryColumnDescriptorCollection | int         | Returns the zero-based index of the occurrence of the GridSummaryColumnDescriptor that matches the name in the collection. |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Insert(int index, GridSummaryColumnDescriptor value)               | Index, GridSummaryColumnDescriptor    | GridSummaryColumnDescriptorCollection | void        | Inserts a descriptor element into the collection at the specified index.                                                   |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Remove(GridSummaryColumnDescriptor value)                          | GridSummaryColumnDescriptor           | GridSummaryColumnDescriptorCollection | void        | Removes the specified GridSummaryColumnDescriptor from the collection.                                                     |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| RemoveAt(int index)                                                | Index                                 | GridSummaryColumnDescriptorCollection | void        | Removes the GridSummaryColumnDescriptor that matches the specified name from the collection.                               |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Add(GridSummaryRowDescriptor value)                                | GridSummaryRowDescriptor              | GridSummaryRowDescriptorCollection    | int         | Adds GridSummaryRowDescriptor to the end of the collection.                                                                |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Clear()                                                            | No Parameter                          | GridSummaryRowDescriptorCollection    | void        | Removes all GridSummaryRowDescriptor from the collection.                                                                  |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Contains(GridSummaryRowDescriptor value)                           | GridSummaryRowDescriptor              | GridSummaryRowDescriptorCollection    | bool        | Determines if the GridSummaryRowDescriptor belongs to this Collection.                                                     |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Contains(string name)                                              | Name of the SummaryRowDescriptor      | GridSummaryRowDescriptorCollection    | bool        | Determines if the GridSummaryRowDescriptor with the specified name belongs to this Collection.                             |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| IndexOf(GridSummaryRowDescriptor value)                            | GridSummaryRowDescriptor              | GridSummaryRowDescriptorCollection    | int         | Returns the zero-based index of the occurrence of the GridSummaryRowDescriptor in the collection.                          |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| IndexOf(string name)                                               | Name of the SummaryRowDescriptor      | GridSummaryRowDescriptorCollection    | int         | Returns the zero-based index of the occurrence of the GridSummaryRowDescriptor that matches the name in the collection.    |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Insert(int index, GridSummaryRowDescriptor value)                  | Index, GridSummaryRowDescriptor       | GridSummaryRowDescriptorCollection    | void        | Inserts a descriptor GridSummaryRowDescriptor into the collection at the specified index.                                  |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Remove(GridSummaryRowDescriptor value)                             | GridSummaryRowDescriptor              | GridSummaryRowDescriptorCollection    | void        | Removes the specified GridSummaryRowDescriptor from the collection.                                                        |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| Remove(string name)                                                | Name of the GridSummaryRowDescriptor  | GridSummaryRowDescriptorCollection    | void        | Removes the specified GridSummaryRowDescriptor from the collection that matches the name.                                  |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+
| RemoveAt(int index)                                                | Index                                 | GridSummaryRowDescriptorCollection    | void        | Removes the GridSummaryRowDescriptor that matches the specified name from the collection.                                  |
|                                                                    |                                       |                                       |             |                                                                                                                            |
|                                                                    |                                       |                                       |             |                                                                                                                            |
+--------------------------------------------------------------------+---------------------------------------+---------------------------------------+-------------+----------------------------------------------------------------------------------------------------------------------------+


 

More:







