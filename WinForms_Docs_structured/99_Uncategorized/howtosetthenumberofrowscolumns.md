---
title: howtosetthenumberofrowscolumns.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetthenumberofrowscolumns.md
created_at: 2025-07-03
---








  









### How to Set the Number of Rows / Columns {#how-to-set-the-number-of-rows-columns style="tab-stops: 0pt"}

[] 

Introduction

[] 

Dynamically changing the **RowCount** or **ColCount** properties while a **GridControl** is being displayed is an efficient way to add or remove rows and / or columns from a GridControl. Using the designer, set the grids RowCount and ColCount properties. From code, set these properties after the call to InitializeComponent in the form\'s constructor (or anytime later in your code after the GridControl has been created).

[] 

Example

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [public ][Form1()]                                   |
|                                                                                                                                                         |
| [{]                                                                                                   |
|                                                                                                                                                         |
| [       ][ //]                                      |
|                                                                                                                                                         |
| [        // Required for Windows Form Designer support.]                                              |
|                                                                                                                                                         |
| [        //]                                                                                          |
|                                                                                                                                                         |
| [        InitializeComponent();]                                                                      |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [     ][   //]                                      |
|                                                                                                                                                         |
| [        // TODO: Add any constructor code after InitializeComponent call.]                           |
|                                                                                                                                                         |
| [        //]                                                                                          |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [        // Set the number of rows.    ][         ] |
|                                                                                                                                                         |
| [        gridControl1.RowCount = 20;]                                                                 |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [        ][// Set the number of columns.    ]       |
|                                                                                                                                                         |
| [        gridControl1.ColCount = 200;]                                                                |
|                                                                                                                                                         |
| [}]                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                              |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [ [ Public Sub New][()]]                                                                         |
|                                                                                                                                                                                 |
| [        ][MyBase][.New()] |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [        ][\' This call is required by the Windows Form Designer.]          |
|                                                                                                                                                                                 |
| [        InitializeComponent()]                                                                                               |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [       ][ \' Add any initialization after the InitializeComponent() call.] |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [        \' Set the number of rows.][             ]                         |
|                                                                                                                                                                                 |
| [        GridControl1.RowCount = 20 ]                                                                                         |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [        \' Set the number of columns.    ]                                                                                   |
|                                                                                                                                                                                 |
| [        GridControl1.ColCount = 200 ]                                                                                        |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [   ][ End Sub]                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p565}**[]** 

[]{#related-topics}

