---
title: throughcode36.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode36.md
created_at: 2025-07-03
---






#### Through Code {#through-code style="tab-stops: 0pt"}

[] 

The Grid List control sample that ships with Essential Grid does not use the designer. It creates an ArrayList of objects that serves as a data source for the Grid List control. Each state object has a LongName, ShortName and **ImageIndex** properties that can be displayed in the list control. Here are some code samples that illustrate the assignments of the major properties.

[] 

For the complete implementation details, refer to the sample in the below installation path.

[] 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Grid List Control***

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                    |
|                                                                                                                   |
| []                                                              |
|                                                                                                                   |
| [// Set to arraylist of states.]                                |
|                                                                                                                   |
| [gridListBox1.DataSource = USStates;]                                         |
|                                                                                                                   |
| []                                                                            |
|                                                                                                                   |
| [// ImageList-the images displayed in the list.      ]          |
|                                                                                                                   |
| [gridListBox1.ImageList = imageList;]                                         |
|                                                                                                                   |
| []                                                                            |
|                                                                                                                   |
| [// Displays multiple columns.]                                 |
|                                                                                                                   |
| [gridListBox1.MultiColumn = [true];]                     |
|                                                                                                                   |
| [gridListBox1.ShowColumnHeader = [true];]                |
|                                                                                                                   |
| [gridListBox1.SelectionMode = [SelectionMode].One;]   |
|                                                                                                                   |
| []                                                                            |
|                                                                                                                   |
| [// Makes the last column wide enough to fill the client area.] |
|                                                                                                                   |
| [gridListBox1.FillLastColumn = [true]; ]                 |
+-------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [\' Set to arraylist of states.]                                                                                                                         |
|                                                                                                                                                                                                            |
| [gridListBox1.DataSource = USStates        ]                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [\' ImageList-the images displayed in the list.       ]                                                                                                  |
|                                                                                                                                                                                                            |
| [gridListBox1.ImageList = ImageList           ]                                                                                                          |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [\' Displays multiple columns.       ]                                                                                                                   |
|                                                                                                                                                                                                            |
| [gridListBox1.MultiColumn = ][True][                ] |
|                                                                                                                                                                                                            |
| [gridListBox1.ShowColumnHeader = ][True]                                                                |
|                                                                                                                                                                                                            |
| [gridListBox1.SelectionMode = SelectionMode.One]                                                                                                         |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [\' Makes last column.]                                                                                                                                  |
|                                                                                                                                                                                                            |
| [gridListBox1.FillLastColumn = ][True][             ] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p520} 

 

[]{#related-topics}

