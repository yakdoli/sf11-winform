---
title: stackedheaders2.md
original_path: WinForms_Docs/99_Uncategorized/stackedheaders2.md
created_at: 2025-08-05
---








  









## Stacked Headers {#stacked-headers style="tab-stops: 0pt"}

The stacked headers in Essential Grid for MVC help you see how data in columns can be categorized and grouped under a single header within the organization of a grid.

Stacked headers allow users to have additional header rows that span across grid columns. Users can group columns under such headers.

You can effectively group extensive data with the help of multilevel stacked headers as well.

The skins applied to the grid are applied to the headers as well by default. Essential Grid has 14 built-in skins, and supports customizable themes as well.

 

Use Case Scenario

Users will be able to clearly see which dimensions of data relate to the same topic, as this feature helps organize grid data better.\
Related columns in the same grid can be grouped under one single heading, so data in those columns will be seen as part of a whole.

Appearance and Structure

The following figures illustrate the appearance and structure of stacked headers in Essential Grid for MVC:

 

{border="0"}

Figure 273: Grid with "Product," "Category," and "Order Details" as Stacked Headers

 

{border="0"}

 

Figure 274: Grid with Multilevel  Stacked Headers

 

Properties

+-----------------------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+--------------+
| Property                                                  | Description                                            | Type of property                                                                                                                                                                 | Value it accepts       | Dependencies |
+-----------------------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+--------------+
| ShowStackedHeader                                         | Specifies whether the stacked header is enabled or not | bool                                                                                                                                                                             | True                   | NA           |
|                                                           |                                                        |                                                                                                                                                                                  |                        |              |
|                                                           |                                                        |                                                                                                                                                                                  | False                  |              |
|                                                           |                                                        |                                                                                                                                                                                  |                        |              |
|                                                           |                                                        |                                                                                                                                                                                  | Default value is False |              |
+-----------------------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+--------------+
| HeaderText                                                | Specifies the text to be displayed in the header       | string                                                                                                                                                                           | Any string             | NA           |
+-----------------------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+--------------+
| Name                                                      | Specifies the name of the stacked header               | string                                                                                                                                                                           | Any string             | NA           |
+-----------------------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+--------------+
| [StackedColumnsCollection] | Gets or sets the Stacked columns collection            | [List][\<[GridStackedColumns]\<T\>\>]  | GridStackedColumns     | NA           |
|                                                           |                                                        |                                                                                                                                                                                  |                        |              |
|                                                           |                                                        |                                                                                                                                                                                  |                        |              |
+-----------------------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+--------------+
| [NestedStackedColumns]     | Gets or sets the nested columns collections            | [IList][\<[GridStackedColumns]\<T\>\>] | GridStackedColumns     | NA           |
|                                                           |                                                        |                                                                                                                                                                                  |                        |              |
|                                                           |                                                        | []                                                                                                              |                        |              |
+-----------------------------------------------------------+--------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+--------------+

[] 

Methods

+----------------------+-----------------------------------------------------------------------------------------+------------------------------+--------------------+-------------------------------+
| Method               | Description                                                                             | Parameters                   | Type               | Return Type                   |
+----------------------+-----------------------------------------------------------------------------------------+------------------------------+--------------------+-------------------------------+
| StackedRows()        | Specifies the Stacked Header Rows and it is used for creating stacked header rows.      | Name,                        | StackedRows        | IGridStackedHeaderBuilder\<\> |
|                      |                                                                                         |                              |                    |                               |
|                      |                                                                                         | GridStackedRowBuilder\<\>    |                    |                               |
+----------------------+-----------------------------------------------------------------------------------------+------------------------------+--------------------+-------------------------------+
| GridStackedColumns() | Specifies the Stacked Header Columns and it is used for creating stacked header columns | Name,                        | StackedColumns     | IGridStackedRowsBuilder\<\>   |
|                      |                                                                                         |                              |                    |                               |
|                      |                                                                                         | GridStackedColumnBuilder\<\> |                    |                               |
+----------------------+-----------------------------------------------------------------------------------------+------------------------------+--------------------+-------------------------------+
| Add()                | Specifies columns to be added to the stacked header                                     | String or lamda expression   | GridStackedColumns | IGridStackedColumnsBuilder    |
+======================+=========================================================================================+==============================+====================+===============================+

[] 

Where do I find the installed samples?

Steps to launch sample:

1.   Open the sample browser and select **ASP.NET MVC** from the left-hand panel.

2.   Click **Run samples** to launch the ASP.NET MVC sample browser.

3.   Select **Grid** from the product icons in the bottom-left of the screen.

4.   Select **Rows and Columns\>StackedHeader** to launch the sample.

[] 

More:





