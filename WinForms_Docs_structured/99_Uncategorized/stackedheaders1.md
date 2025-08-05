---
title: stackedheaders1.md
original_path: WinForms_Docs/99_Uncategorized/stackedheaders1.md
created_at: 2025-08-05
---






#### Stacked Headers[]{#p289} {#stacked-headers style="tab-stops: 0pt"}

Essential Grid allows you to have additional unbound header rows, called Stacked Header Rows that span across visible grid columns. You can group one or more columns under each stacked header.

 

The StackedHeaderRows Collection

 

Stacked Header rows for a given grid are gathered under Grid.StackedHeaderRow collection. This collection contains the property definitions that control the behavior and appearance of the Stacked Headers. A StackedHeaderRow collection can be viewed as a set of stacked header rows in which each header row contains a collection of stacked headers, which span across multiple columns.

 

Every stacked header row is defined by a GridDataStackedHeaderRow. This class contains a property named Columns, which is a collection of GridDataStackedHeaderColumn objects and this collection contains an entry for each stacked header.

 

Below are the properties of the GridDataStackedHeaderColumn:

 


  ---------------- -------------------------------------------------------------------------------
  Property         Description
  ColumnSpan       Specifies the number of columns that a particular stacked header should span.
  ColumnStyle      Specifies the style for the stacked header column.
  HeaderText       Specifies the header text for the stacked header.
  VisibleColumns   Specifies the collection of visible columns under the stacked header.
  ---------------- -------------------------------------------------------------------------------


 

Example

 

The following sample code illustrates the creation of two stacked headers:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][GridDataControl][ x][:][Name][=\"dataGrid2\"][ [AutoPopulateColumns][=\"True\"] [AutoPopulateRelations][=\"False\"] ]                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [                                   [ ItemsSource][=\"{][StaticResource][ ordersSource][}\"\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            ][\<][syncfusion][:][GridDataControl.StackedHeaderRows][\>]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [               ][\<][syncfusion][:][GridDataStackedHeaderRow][ Name][=\"Row1\"\>]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [                  ][\<][syncfusion][:][GridDataStackedHeaderRow.Columns][\>]                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [                      ][\<][syncfusion][:][GridDataStackedHeaderColumn][ HeaderText][=\"Header 1\"][ Name][=\"Header1\"][ ColumnSpan][=\"3\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [                      ][\<][syncfusion][:][GridDataStackedHeaderColumn][ HeaderText][=\"Header 2\"][ Name][=\"Header2\"][ ColumnSpan][=\"2\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [                   ][\</][syncfusion][:][GridDataStackedHeaderRow.Columns][\>]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [               ][\</][syncfusion][:][GridDataStackedHeaderRow][\>]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            ][\</][syncfusion][:][GridDataControl.StackedHeaderRows][ \>]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][syncfusion][:][GridDataControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output of the above given code is the following image:

 

{border="0"}

Figure 191: Two stacked headers spanning three and two columns respectively

***[]*** 

The preceding screen shot shows a GridData control with stacked headers.

 

 

[]{#related-topics}

