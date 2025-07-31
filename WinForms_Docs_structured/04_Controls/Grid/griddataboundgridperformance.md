---
title: griddataboundgridperformance.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\griddataboundgridperformance.md
created_at: 2025-07-03
---






#### Grid Data Bound Grid Performance {#grid-data-bound-grid-performance style="tab-stops: 0pt"}

[] 

Essential Grid Data Bound Grid can handle large amount of data without a performance hit.

[] 

{border="0"}

[] 

*[Figure ][226][: Grid Data Bound Grid]*

[] 

For more details, refer the sample under the following path from our sample browser:

 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Data Bound\\Grid Performance Demo***

 

**Example**

 

The Grid can be loaded by specifying the number of record and using the options-Use OptimizedListChangeEvent, Use ResizeToFit on ColWidths and Use DataTableList.

 

In the Initialize Table group box

[] 

[·      ]**Use OptimizedListChangeEvent**--Selecting this option ensures that the grid data is updated using the IBindingList.ListChanged instead of the CurrencyManager change events.

[·      ]**Use ResizeToFit on ColWidths**--Selecting this option ensures column width is resized to fit the cell content after the data is loaded.

[·      ]**Use DataTableList**-Selecting this option ensures that the Syncfusion.Collections.DataTableWrapperList is used as the data source instead of the data table. The DataTableWrapperList is an IBindingList collection that wraps a data table and provides optimized access to the rows of the data table in turn improving the performance when inserting records into an existing table holding many records.

 

In the Manipulate Grid group box

 

[·      ]The Repeat Count and the Batch Size can be specified in order to check the performance in batch updates.

[·      ]Selecting the Use ScrollWindow check box invalidates only the inserted or removed rows instead of invalidating the whole Grid.

[·      ]The Insert Records, Remove Records and Change Records buttons let you check the performance when inserting, removing or changing the records in the underlying data table. Once the data is loaded after the batch update, you will be able to see the performance and the memory usage in a text box, as shown below.

[] 

{border="0"}

***[]*** 

*[Figure ][227][: Grid Performance Check]*

 

[]{#p386} 

 

[]{#related-topics}

