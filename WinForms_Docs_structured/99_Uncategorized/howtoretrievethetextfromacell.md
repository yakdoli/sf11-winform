---
title: howtoretrievethetextfromacell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoretrievethetextfromacell.md
created_at: 2025-07-03
---








  









### How to Retrieve the Text From a Cell {#how-to-retrieve-the-text-from-a-cell style="tab-stops: 0pt"}

[] 

Introduction

[] 

To retrieve text from a cell, simply use the[ ]{.UGHyperlink}[Text]{.UGHyperlink} property of the cells style object which, is obtained through an indexer in the **GridControl**.

[] 

Example

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [// Access the cell\'s Text property to retrieve the text from the cell.]                         |
|                                                                                                                                                     |
| [string][ cellText = gridControl1\[2, 3\].Text;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' Access the cell\'s Text property to retrieve the text from the cell.]                                                                                                                                   |
|                                                                                                                                                                                                                                                               |
| [Dim][ cellText ][As String][ = gridControl1(2,3).Text] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note:

 

Depending upon exactly what object is stored in the [CellValue]{.UGHyperlink} property, you may have to do additional work to retrieve a usable value from the style. There is also a FormattedText property that may give you a different value. One example would be if the cell is a combobox cell type that is using the DisplayMember and ValueMember properties to show different values from the ones being stored in the GridControl (as in foreign key look tables). In this case, the Text property is the ValueMember value and the FormattedText property is the[ ]DisplayMember property.


 

[]{#p562} 

 

[]{#related-topics}

