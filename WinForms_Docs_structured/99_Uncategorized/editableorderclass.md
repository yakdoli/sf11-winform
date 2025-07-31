---
title: editableorderclass.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\editableorderclass.md
created_at: 2025-07-03
---








  









### EditableOrder Class {#editableorder-class style="tab-stops: 0pt"}

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [    ///][ ][\<summary\>][] |
|                                                                                                                                                                                                                     |
| [    [///][ EditableOrder Model.]]                                                                                                   |
|                                                                                                                                                                                                                     |
| [    [///][ ][\</summary\>]]                                                                                    |
|                                                                                                                                                                                                                     |
| [    [public] [class] [EditableOrder]]                                                                        |
|                                                                                                                                                                                                                     |
| [    {]                                                                                                                                                                         |
|                                                                                                                                                                                                                     |
| [        \[[Required](ErrorMessage = [\"Order ID is required.\"])\]]                                                            |
|                                                                                                                                                                                                                     |
| [        [public] [int] OrderID]                                                                                                      |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [        \[[StringLength](5, ErrorMessage = [\"Customer ID must be 5 characters.\"])\]]                                         |
|                                                                                                                                                                                                                     |
| [        [public] [string] CustomerID]                                                                                                |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [        \[[Range](1, 9, ErrorMessage = [\"EmployeeID must be between 0 and 9.\"])\]]                                           |
|                                                                                                                                                                                                                     |
| [        [public] [int]? EmployeeID]                                                                                                  |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [        [public] [DateTime]? OrderDate]                                                                                           |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [        [public] [string] ShipName]                                                                                                  |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [        \[[StringLength](15, ErrorMessage = [\"ShipCity must be 15 characters.\"])\]]                                          |
|                                                                                                                                                                                                                     |
| [        [public] [string] ShipCity]                                                                                                  |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [        [public] [string] ShipAddress]                                                                                               |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [        [public] [string] ShipRegion]                                                                                                |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [        [public] [string] ShipPostalCode]                                                                                            |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [        \[[StringLength](15, ErrorMessage = [\"ShipName must be 15 characters.\"])\]]                                          |
|                                                                                                                                                                                                                     |
| [        [public] [string] ShipCountry]                                                                                               |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [        \[[Range](1.00, 1000.00, ErrorMessage = [\"Freight must be between 1.00 & 1000\"])\]]                                  |
|                                                                                                                                                                                                                     |
| [        [public] [decimal]? Freight]                                                                                                 |
|                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [            [get];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [            [set];]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [    }][]                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

