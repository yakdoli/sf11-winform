---
title: gridproperties.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\gridproperties.md
created_at: 2025-07-03
---






##### Grid Properties {#grid-properties style="tab-stops: 0pt"}

[] 

Essential Grid provides support to customize the appearance and behavior of the grid cells. This section would provide you more insight on the properties affecting the Appearance, Print Styles, and Scroll Bar Settings available. It includes the following topics.

[] 

 

[]{#p319} 

 

###### 4.1.4.13.4.1        Appearance Properties {#appearance-properties style="tab-stops: 0pt"}

[   ]

The properties that majorly affect the appearance cells and data in cells of a grid can be named as Appearance properties.

[] 

{border="0"}

[] 

*[Figure ][153][: Grid Control]*

[] 

The following properties are used to customize the appearance of Grid.

[] 

[·      ]**TransparentBackground**-Specifies whether to display grid with background image. When this property is set to false, the background image will not be displayed even if it is set by using the BackgroundImage property.

[] 

The following code examples can be used to set this property:

 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [// Enable TransparentBackground property.]                                                                   |
|                                                                                                                                                                 |
| [this][.gridControl1.TransparentBackground = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [\' Enable TransparentBackground property.]                                                                |
|                                                                                                                                                              |
| [Me][.gridControl1.TransparentBackground = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the TransparentBackground property is set to true.

[] 

{border="0"}

[] 

*[Figure ][154][: Grid with TransparentBackground property set to True]****[]***

[] 

[·      ]**DisplayHorzLines**-Specifies whether horizontal grid lines marking the cells are to be displayed. Default value is set to *true*.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| []                                                                                                                   |
|                                                                                                                                                                        |
| [// Enable DisplayHorzLines property.]                                                                               |
|                                                                                                                                                                        |
| [this][.gridControl1.Properties.DisplayHorzLines = [false];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                  |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [\' Enable DisplayHorzLines property.]                                                                            |
|                                                                                                                                                                     |
| [Me][.gridControl1.Properties.DisplayHorzLines = [False]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the Properties.DisplayHorzLines property is set to false.

[] 

{border="0"}

[] 

*[Figure ][155][: Horizontal Lines hidden in Grid]*

[] 

[·      ]**DisplayVertLines**-Specifies whether vertical grid lines marking the cells are to be displayed. Default value is set to *true*.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| []                                                                                                                   |
|                                                                                                                                                                        |
| [// Enable DisplayVertLines property.]                                                                               |
|                                                                                                                                                                        |
| [this][.gridControl1.Properties.DisplayVertLines = [false];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                  |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [\' Enable DisplayVertLines property.]                                                                            |
|                                                                                                                                                                     |
| [Me][.gridControl1.Properties.DisplayVertLines = [False]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the Properties.DisplayVertLines property is set to false.

[] 

{border="0"}

***[]*** 

*[Figure ][156][: Vertical Lines hidden in Grid]*

[] 

[·      ]**ColHeaders**-Specifies whether column headers are to be displayed. Default value is set to *true*.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [// Hiding the column headers.]                                                                                |
|                                                                                                                                                                  |
| [this][.gridControl1.Properties.ColHeaders = [false];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [\' Hiding the column headers.]                                                                             |
|                                                                                                                                                               |
| [Me][.gridControl1.Properties.ColHeaders = [False]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the Properties.ColHeaders property is set to false.

[] 

{border="0"}

***[]*** 

*[Figure ][157][: Column Headers hidden in Grid]*

[] 

[·      ]**RowHeaders**-Specifies whether row headers are to be displayed. Default value is set to *true*.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [// Hiding the row headers.]                                                                                   |
|                                                                                                                                                                  |
| [this][.gridControl1.Properties.RowHeaders = [false];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [\' Hiding the row headers.]                                                                                |
|                                                                                                                                                               |
| [Me][.gridControl1.Properties.RowHeaders = [False]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the Properties.RowHeaders property is set to false.

[] 

{border="0"}

***[]*** 

Figure 158: Row Headers hidden in Grid

[] 

[·      ]**Buttons3D**-Specifies if the row and column headers should have a three dimensional look which in turn makes headers visually appealing. If this property is set to false, the row and column headers will appear flat. Default value is set to *true*.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [// Enable Buttons3D property.]                                                                               |
|                                                                                                                                                                 |
| [this][.gridControl1.Properties.Buttons3D = [false];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [\' Enable Buttons3D property.]                                                                            |
|                                                                                                                                                              |
| [Me][.gridControl1.Properties.Buttons3D = [False]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the Properties.Buttons3D property is set to false.

[] 

{border="0"}

***[]*** 

*[Figure ][159][: Buttons3D effect disabled for Rows and Columns Headers in Grid]*

[] 

[·      ]**GridLineColor**-Specifies the color for the grid lines (for example, active border). Default value is set to *GrayText*.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [// Specify the color for the grid lines.]                                                                                                    |
|                                                                                                                                                                                                 |
| [this][.gridControl1.Properties.GridLineColor = System.Drawing.[Color].IndianRed;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [\' Specify the color for the grid lines.]                                                                       |
|                                                                                                                                                                    |
| [Me][.gridControl1.Properties.GridLineColor = System.Drawing.Color.IndianRed] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the Properties.GridLineColor property is set to IndianRed.

[] 

{border="0"}

***[]*** 

*[Figure ][160][: Grid with Line Color set to Red]*

[] 

[·      ]**BackgroundImage**-Enables to insert a background image for the grid.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [// Specify the background image.]                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [this][.gridControl1.BackgroundImage = [Image].FromFile(FindImageFile([@\"..\\..\\..\\..pic.jpg\"]));] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                            |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [\' Specify the background image.]                                                                                                                          |
|                                                                                                                                                                                                               |
| [Me][.gridControl1.BackgroundImage = Image.FromFile(FindImageFile([\"..\\..\\..\\..pic.jpg\"]))] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the BackgroundImage property is set.

[] 

{border="0"}

***[]*** 

*[Figure ][161][: Background Image set for Grid]*

[] 

[·      ]**TextColor**-Specifies the color of the text in the grid.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [// Set grid text color.]                                                                                                     |
|                                                                                                                                                                                 |
| [this][.gridControl1.TableStyle.TextColor = [Color].MidnightBlue;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                 |
|                                                                                                                                                    |
| []                                                                                               |
|                                                                                                                                                    |
| [\' Set grid text color.]                                                                        |
|                                                                                                                                                    |
| [Me][.gridControl1.TableStyle.TextColor = Color.MidnightBlue] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the TableStyle.TextColor property is set to MidnightBlue.

[] 

{border="0"}

***[]*** 

*[Figure ][162][: Grid with Text Color set to MidnightBlue]*

[] 

[·      ]**BackColor**-Specifies the color of the grid line marker when the user resizes rows or columns by dragging the row or column headers. Default value is set to *Red*.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [// Set the grid background color.]                                                                         |
|                                                                                                                                                               |
| [this][.gridControl1.BackColor = [Color].Beige;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                               |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [\' Set the grid background color.]                                            |
|                                                                                                                                  |
| [Me][.gridControl1.BackColor = Color.Beige] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the BackColor property is set to Beige.

[] 

{border="0"}

***[]*** 

*[Figure ][163][: Grid with Background Color set to Beige]*

[] 

[·      ]**ResizingCellsLinesColor**-Specifies the color for the grid lines (for example, active border). Default value is set to *GrayText*.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [// Specify the color for the grid line marker while resizing rows and columns.]                                                             |
|                                                                                                                                                                                                |
| [this][.gridControl1.Properties.ResizingCellsLinesColor = [Color].PaleVioletRed;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [\' Specify the color for the grid line marker while resizing rows and columns.]                                |
|                                                                                                                                                                   |
| [Me][.gridControl1.Properties.ResizingCellsLinesColor = Color.PaleVioletRed] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**Borders**-Specifies settings for Top, Left, Bottom and Right borders.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                  |
| [// Set border settings for the grid.]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [this][.gridControl1.TableStyle.Borders.All = [new] [GridBorder]([GridBorderStyle].Solid, [Color].SteelBlue);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                              |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [\' Set border settings for the grid.]                                                                                                                        |
|                                                                                                                                                                                                                 |
| [Me][.gridControl1.TableStyle.Borders.All = [New] GridBorder(GridBorderStyle.Solid, Color.SteelBlue)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**FixedLinesColor**-Specifies the color of frozen grid lines (for example, row or column headers). Default value is set to *ActiveCaption*.

[] 

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [// Set the color of frozen grid lines.]                                                                                           |
|                                                                                                                                                                                      |
| [this][.gridControl1.Properties.FixedLinesColor = [Color].YellowGreen;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                      |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [\' Set the color of frozen grid lines.]                                                              |
|                                                                                                                                                         |
| [Me][.gridControl1.Properties.FixedLinesColor = Color.YellowGreen] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

***[]*** 

A sample demonstrating these properties is available under the following sample installation path.

[] 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Appearance\\Grid Properties Demo***

 

[]{#p320} 

 

###### 4.1.4.13.4.2        Print Properties {#print-properties style="tab-stops: 0pt"}

[   ]

The following properties are associated with printing in Grid. They are generally referred to as Print Styles.

[] 

[·      ]**BlackWhite**-Specifies if the grid should be printed only in black and white.

[] 

The following code examples illustrate how to set this property:

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [// Specify if the grid should print only in black and white.]                                                |
|                                                                                                                                                                 |
| [this][.gridControl1.Properties.BlackWhite = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [\' Specify if the grid should print only in black and white.]                                             |
|                                                                                                                                                              |
| [Me][.gridControl1.Properties.BlackWhite = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**Printing**-Prints the grid.

[] 

The following code examples illustrate how to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [// Prints the grid.]                                                                                       |
|                                                                                                                                                               |
| [this][.gridControl1.Properties.Printing = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                         |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [\' Prints the grid.]                                                                                    |
|                                                                                                                                                            |
| [Me][.gridControl1.Properties.Printing = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**PrintFrame**-Specifies the appearance of a frame around the grid while printing.

[] 

The following code examples illustrate how to set this property:

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                  |
|                                                                                                                                                                 |
| []                                                                                                            |
|                                                                                                                                                                 |
| [// Specify if a frame should be drawn around the grid while printing.]                                       |
|                                                                                                                                                                 |
| [this][.gridControl1.Properties.PrintFrame = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [\' Specify if a frame should be drawn around the grid while printing.]                                    |
|                                                                                                                                                              |
| [Me][.gridControl1.Properties.PrintFrame = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**PrintColHeader**-Specifies if column headers should be printed.

[] 

The following code examples illustrate how to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [// Specify if column headers should be printed.]                                                                 |
|                                                                                                                                                                     |
| [this][.gridControl1.Properties.PrintColHeader = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [\' Specify if column headers should be printed.]                                                              |
|                                                                                                                                                                  |
| [Me][.gridControl1.Properties.PrintColHeader = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**PrintRowHeader**-Specifies if row headers should be printed.

[] 

The following code examples illustrate how to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [// Specify if row headers should be printed.]                                                                    |
|                                                                                                                                                                     |
| [this][.gridControl1.Properties.PrintRowHeader = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [\' Specify if row headers should be printed.]                                                                 |
|                                                                                                                                                                  |
| [Me][.gridControl1.Properties.PrintRowHeader = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**CenterVertical**-Specifies if the grid should be centered vertically on printing.

[] 

The following code examples illustrate how to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [// Specify if the grid should be centered vertically on printing.]                                               |
|                                                                                                                                                                     |
| [this][.gridControl1.Properties.CenterVertical = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [\' Specify if the grid should be centered vertically on printing.]                                            |
|                                                                                                                                                                  |
| [Me][.gridControl1.Properties.CenterVertical = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**PrintHorzLines**-Specifies if horizontal lines of the grid should be printed.

[] 

The following code examples illustrate how to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [// Specify if horizontal lines of the grid should be printed.]                                                   |
|                                                                                                                                                                     |
| [this][.gridControl1.Properties.PrintHorzLines = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [\' Specify if horizontal lines of the grid should be printed.]                                                |
|                                                                                                                                                                  |
| [Me][.gridControl1.Properties.PrintHorzLines = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**PrintVertLines**-Specifies if vertical lines of the grid should be printed.

[] 

The following code examples illustrate how to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [// Specify if vertical lines of the grid should be printed.]                                                     |
|                                                                                                                                                                     |
| [this][.gridControl1.Properties.PrintVertLines = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [\' Specify if vertical lines of the grid should be printed.]                                                  |
|                                                                                                                                                                  |
| [Me][.gridControl1.Properties.PrintVertLines = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample demonstrating these properties is available under the following sample installation path.

 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Print***

 

[]{#p321} 

 

###### 4.1.4.13.4.3        Scroll Bar Properties {#scroll-bar-properties style="tab-stops: 0pt"}

[   ]

Essential Grid provides support to control the functionalities and appearance of the grid scroll bars.

[] 

{border="0"}

[] 

*[Figure ][164][: Grid with Horizontal and Vertical Scroll Bars ]*

[] 

The following properties are associated with scrolling in grid.

[] 

[] 

[·      ]**HscrollPixel**-Specifies whether to enable/disable horizontal pixel scrolling for the grid. Default value is set to *false*.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [// Enable horizontal pixel scrolling for the grid.]                                                 |
|                                                                                                                                                        |
| [this][.gridControl1.HScrollPixel = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [\' Enable horizontal pixel scrolling for the grid.]                                              |
|                                                                                                                                                     |
| [Me][.gridControl1.HScrollPixel = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**VscrollPixel**-Specifies whether to enable/disable vertical pixel scrolling for the grid. Default value is set to *false*.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [// Enable vertical pixel scrolling for the grid.]                                                   |
|                                                                                                                                                        |
| [this][.gridControl1.VScrollPixel = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [\' Enable vertical pixel scrolling for the grid.]                                                |
|                                                                                                                                                     |
| [Me][.gridControl1.VScrollPixel = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**HorizontalScrollTips**-Specifies if the control should display scroll tips while the user is dragging a horizontal scroll bar thumb. Default value is set to *false*.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [// Specify whether scroll tips should be displayed while dragging the horizontal scroll bar thumb.]         |
|                                                                                                                                                                |
| [this][.gridControl1.HorizontalScrollTips = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [\' Specify whether scroll tips should be displayed while dragging the horizontal scroll bar thumb.]      |
|                                                                                                                                                             |
| [Me][.gridControl1.HorizontalScrollTips = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   The following illustration shows how the Grid in \"Figure 1\" is transformed when the HorizontalScrollTips property is set to true.

[] 

{border="0"}

***[]*** 

Figure 165: HorizontalScrollTips = \"True\"

[] 

[] 

[] 

[·      ]**VerticalScrollTips**-Specifies if the control should display scroll tips while the user is dragging a vertical scroll bar thumb. Default value is set to *false*.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [// Specify whether scroll tips should be displayed while dragging the vertical scroll bar thumb.]         |
|                                                                                                                                                              |
| [this][.gridControl1.VerticalScrollTips = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [\' Specify whether scroll tips should be displayed while dragging the vertical scroll bar thumb.]      |
|                                                                                                                                                           |
| [Me][.gridControl1.VerticalScrollTips = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the VerticalScrollTips property is set to true.

[] 

{border="0"}

***[]*** 

*[Figure ][166][: VerticalScrollTips = \"True\"]*

[] 

[] 

[] 

[·      ]**HscrollBehavior**-Specifies the behavior of the horizontal scroll bar. GridScrollbarMode enumeration provides the following options to control the scroll bar behavior: Automatic, AutoScroll, DetectIfShared, DisableAutoScroll, Disabled, Enabled and Shared*.*

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [// Set the behavior of the horizontal scroll bar.]                                                                            |
|                                                                                                                                                                                  |
| [this][.gridControl1.HScrollBehavior = [GridScrollbarMode].Shared;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [\' Set the behavior of the horizontal scroll bar.]                                               |
|                                                                                                                                                     |
| [Me][.gridControl1.HScrollBehavior = GridScrollbarMode.Shared] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**VScrollBehavior**-Specifies the behavior of the vertical scroll bar. GridScrollbarMode enumeration provides the following options to control the scroll bar behavior: Automatic, AutoScroll, DetectIfShared, DisableAutoScroll, Disabled, Enabled and Shared*.*

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [// Set the behavior of the vertical scroll bar.]                                                                              |
|                                                                                                                                                                                  |
| [this][.gridControl1.VScrollBehavior = [GridScrollbarMode].Shared;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [\' Set the behavior of the vertical scroll bar.]                                                 |
|                                                                                                                                                     |
| [Me][.gridControl1.VScrollBehavior = GridScrollbarMode.Shared] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**HorizontalThumbTrack**-Specifies whether the control should scroll while the user is dragging the horizontal scroll bar thumb. Default value is set to *false*.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [// Specify whether the control should scroll while dragging the horizontal scroll bar thumb.]               |
|                                                                                                                                                                |
| [this][.gridControl1.HorizontalThumbTrack = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [\' Specify whether the control should scroll while dragging the horizontal scroll bar thumb.]            |
|                                                                                                                                                             |
| [Me][.gridControl1.HorizontalThumbTrack = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the HorizontalThumbTrack property is set to true.

[] 

{border="0"}

***[]*** 

*[Figure ][167][: HorizontalThumbTrack = \"True\"]****[]***

[] 

[] 

[] 

[·      ]**VerticalThumbTrack**-Specifies whether the control should scroll while the user is dragging vertical scroll bar thumb. Default value is set to *false*.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [// Specify whether the control should scroll while dragging the vertical scroll bar thumb.]               |
|                                                                                                                                                              |
| [this][.gridControl1.VerticalThumbTrack = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [\' Specify whether the control should scroll while dragging the vertical scroll bar thumb.]            |
|                                                                                                                                                           |
| [Me][.gridControl1.VerticalThumbTrack = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following illustration shows how the Grid in \"Figure 1\" is transformed when the VerticalThumbTrack property is set to true.

[] 

{border="0"}

***[]*** 

*[Figure ][168][: VerticalThumbTrack = \"True\"]*

[] 

[] 

[] 

[·      ]**Office2007ScrollBars**-Toggles between standard and Office 2007 scroll bars. Default value is set to *false*.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [// Toggle to Office 2007 scroll bar.]                                                                       |
|                                                                                                                                                                |
| [this][.gridControl1.Office2007ScrollBars = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [\' Toggle to Office 2007 scroll bar.]                                                                    |
|                                                                                                                                                             |
| [Me][.gridControl1.Office2007ScrollBars = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**Office2007ScrollBarsColorScheme**-Specifies the style for Office 2007 scroll bars. Default value is set to *Blue*.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [// Set the style for Office 2007 scroll bar.]                                                                                                   |
|                                                                                                                                                                                                    |
| [this][.gridControl1.Office2007ScrollBarsColorScheme = [Office2007ColorScheme].Blue;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                    |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [\' Set the style for Office 2007 scroll bar.]                                                                      |
|                                                                                                                                                                       |
| [Me][.gridControl1.Office2007ScrollBarsColorScheme = Office2007ColorScheme.Blue] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**ScrollFrozen**-Defines scroll behavior when user moves current cell with arrow keys into frozen cells area. Default value is set to *true*.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [// Define scroll behavior in frozen cells.]                                                         |
|                                                                                                                                                        |
| [this][.gridControl1.ScrollFrozen = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [\' Define scroll behavior in frozen cells.]                                                      |
|                                                                                                                                                     |
| [Me][.gridControl1.ScrollFrozen = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**ScrollTipFormat**-Specifies the text to be displayed in the ScrollTip window with a place holder for scroll position.

The following code examples can be used to set this property:

 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                           |
|                                                                                                                                                                          |
| []                                                                                                                     |
|                                                                                                                                                                          |
| [// Set the text to be displayed in the ScrollTip window with a place holder for scroll position.]                     |
|                                                                                                                                                                          |
| [this][.gridControl1.ScrollTipFormat = [\"Position {0}\"];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                    |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [\' Set the text to be displayed in the ScrollTip window with a place holder for scroll position.]                  |
|                                                                                                                                                                       |
| [Me][.gridControl1.ScrollTipFormat = [\"Position {0}\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**AutoScrolling**-Specifies whether to enable/disable automatic scrolling.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [// Enable AutoScrolling.]                                                                            |
|                                                                                                                                                         |
| [this][.gridControl1.AutoScrolling = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                   |
|                                                                                                                                                      |
| []                                                                                                 |
|                                                                                                                                                      |
| [\' Enable AutoScrolling.]                                                                         |
|                                                                                                                                                      |
| [Me][.gridControl1.AutoScrolling = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**Hscroll**-Specifies whether to enable/disable horizontal scroll bar.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                                   |
| []                                                                                              |
|                                                                                                                                                   |
| [// Enable horizontal scroll bar.]                                                              |
|                                                                                                                                                   |
| [this][.gridControl1.HScroll = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                             |
|                                                                                                                                                |
| []                                                                                           |
|                                                                                                                                                |
| [\' Enable horizontal scroll bar.]                                                           |
|                                                                                                                                                |
| [Me][.gridControl1.HScroll = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

[·      ]**VScroll**-Specifies whether to enable/disable vertical scroll bar.

The following code examples can be used to set this property:

[] 

1.   Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                    |
|                                                                                                                                                   |
| []                                                                                              |
|                                                                                                                                                   |
| [// Enable vertical scroll bar.]                                                                |
|                                                                                                                                                   |
| [this][.gridControl1.VScroll = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                             |
|                                                                                                                                                |
| []                                                                                           |
|                                                                                                                                                |
| [\' Enable vertical scroll bar.]                                                             |
|                                                                                                                                                |
| [Me][.gridControl1.VScroll = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample demonstrating these properties is available under the following sample installation path.

 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Zoom and Scrolling\\Scroll Bar Demo***

 

[]{#p322} 

 

[]{#related-topics}

