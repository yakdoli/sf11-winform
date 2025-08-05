---
title: rowstyles.md
original_path: WinForms_Docs/02_Concepts/rowstyles.md
created_at: 2025-08-05
---






##### Row Styles {#row-styles style="tab-stops: 0pt"}

There are two ways to format the grid rows. They are,

 

[·      ]Using properties

[·      ]By handling QueryCellInfo event

**[]** 

Using Properties

 

You can change the background of the grid rows by setting a color for the RowBackground property. To override the color of the alternative rows in the same grid use the AlternatingRowBackground property.

 

The following code illustrates the properties settings.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                           |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [grid.AlternatingRowBackground = [new] [SolidColorBrush]([Colors].Orchid);] |
|                                                                                                                                                                                      |
| [grid.RowBackground = [new] [SolidColorBrush]([Colors].Tan);]               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following image corresponds to the output of the above given code:

 

{border="0"}

Figure 202: Applying row and alternative row backgrounds for the Grid

 

The row styles of the GDC are customized using background properties.

 

Using QueryCellInfo Event

 

QueryCellInfo event is handled whenever a grid cell needs to be redrawn or repainted. In the GDC, you can use Model.QueryCellInfo event to format the rows by checking the row and column indices on the event arguments.

 

The following code illustrates this:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                      |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [grid.Model.QueryCellInfo += [new] [GridQueryCellInfoEventHandler](Model_QueryCellInfo);]                                      |
|                                                                                                                                                                                                                 |
| [void][ Model_QueryCellInfo([object] sender, [GridQueryCellInfoEventArgs] e)] |
|                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                 |
|                                                                                                                                                                                                                 |
| [            [if] (e.Cell.RowIndex \> 0)]                                                                                                              |
|                                                                                                                                                                                                                 |
| [            {]                                                                                                                                                             |
|                                                                                                                                                                                                                 |
| [                [if] (e.Cell.RowIndex % 2 == 0)]                                                                                                      |
|                                                                                                                                                                                                                 |
| [                    e.Style.Background = [Brushes].BlanchedAlmond;]                                                                                |
|                                                                                                                                                                                                                 |
| [                [else]]                                                                                                                               |
|                                                                                                                                                                                                                 |
| [                    e.Style.Background = [Brushes].LightCyan;]                                                                                     |
|                                                                                                                                                                                                                 |
| [            }]                                                                                                                                                             |
|                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following image corresponds to the output of the above given code:

 

{border="0"}

Figure 203: Applying row styles using QueryCellInfo Event

***[]*** 

The row styles of the GDC are customized by handling the QueryCellInfo event.

 

 

[]{#related-topics}

