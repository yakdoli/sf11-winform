---
title: styleproperties3.md
original_path: WinForms_Docs/02_Concepts/styleproperties3.md
created_at: 2025-08-05
---






##### Style Properties {#style-properties style="tab-stops: 0pt"}

Property settings for individual/groups of cells are stored in a GridStyleInfo property. The style allows you to set properties such as background, cell value, and cell type for a particular cell.

 

Essential Grid for WPF holds two different style caches that depend upon how the cell style is being used:

 

Volatile style-cache-Is maintained for styles populated through calls made to the QueryCellInfo (the virtual grid event that provides the cell values to the grid on demand) event. This volatile style-cache uses weak references to interact with the .NET Framework\'s Garbage collection to ensure optimal memory use. These styles remain cached as long as they are not garbage collected by the framework.

Render style-cache-Is maintained for styles needed to draw the grid and are disposed of as soon as the cell scrolls out of view.\
\

The combination of these two caches makes Essential Grid for WPF highly efficient. This section elaborates on important style properties.

 

Base Styles

Base Styles, otherwise named as Parent Styles, define the style information for individual cell groups such that all the cells belonging to a group will share the same Base style. On changing the common base style, the dependent cells styles also get updated automatically.

 

Following code snippet illustrates the effect of various Base styles.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                   |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [//Defines the base styles named PinkStyle and GreenStyle.]                                                                                |
|                                                                                                                                                                                              |
| [GridBaseStyle][ baseStyle1 = [new] [GridBaseStyle]();] |
|                                                                                                                                                                                              |
| [baseStyle1.Name = [\"PinkStyle\"];]                                                                                             |
|                                                                                                                                                                                              |
| [baseStyle1.StyleInfo.Background = [Brushes].LightPink;]                                                                         |
|                                                                                                                                                                                              |
| [baseStyle1.StyleInfo.Foreground = [Brushes].Maroon;]                                                                            |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [GridBaseStyle][ baseStyle2 = [new] [GridBaseStyle]();] |
|                                                                                                                                                                                              |
| [baseStyle2.Name = [\"GreenStyle\"];]                                                                                            |
|                                                                                                                                                                                              |
| [baseStyle2.StyleInfo.Background = [Brushes].PaleGreen;]                                                                         |
|                                                                                                                                                                                              |
| [baseStyle2.StyleInfo.Foreground = [Brushes].Olive;]                                                                             |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [//Add the above styles to the grid base styles collection.]                                                                               |
|                                                                                                                                                                                              |
| [grid.Model.BaseStylesMap.Add(baseStyle1);]                                                                                                              |
|                                                                                                                                                                                              |
| [grid.Model.BaseStylesMap.Add(baseStyle2);]                                                                                                              |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [//Applying base styles.]                                                                                                                  |
|                                                                                                                                                                                              |
| [for][ ([int] i = 1; i \<= grid.Model.RowCount; i++)]                              |
|                                                                                                                                                                                              |
| [{]                                                                                                                                                      |
|                                                                                                                                                                                              |
| [   [for] ([int] j = 1; j \<= grid.Model.ColumnCount; j++)]                                                    |
|                                                                                                                                                                                              |
| [   {]                                                                                                                                                   |
|                                                                                                                                                                                              |
| [        [if](j ==2)]                                                                                                               |
|                                                                                                                                                                                              |
| [           grid.Model\[i, j\].BaseStyle = [\"PinkStyle\"];]                                                                     |
|                                                                                                                                                                                              |
| [        [else]]                                                                                                                    |
|                                                                                                                                                                                              |
| [           grid.Model\[i,j\].BaseStyle = [\"GreenStyle\"];]                                                                     |
|                                                                                                                                                                                              |
| [   }]                                                                                                                                                   |
|                                                                                                                                                                                              |
| [}]                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The code above displays the following output:

 

{border="0"}

Figure 46: Base Style

 

Background

The Background property specifies a background brush for the grid cell. The cell's background can be painted with either a solid brush or a gradient brush.

**[]** 


{border="0"}Note:



***[·    ]***Gradient-A gradient brush uses two colors. These colors merge to create a transition or fading effect.

***[·    ]***Solid-A solid brush is equipped with only one color.


 

Setting Background Brush Type

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                              |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[2, 1\].Background = Brushes.Aquamarine;]                                                                       |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[2, 2\].Background = Brushes.Violet ;]                                                                          |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[2, 3\].Background = Brushes.LawnGreen;]                                                                        |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[2, 4\].Background = Brushes.LavenderBlush  ;]                                                                  |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[2, 5\].Background = Brushes.CadetBlue ;]                                                                       |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[2, 6\].Background = Brushes.LemonChiffon;]                                                                     |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[3, 1\].Background = GetLinerBrush();]                                                                          |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[3, 2\].Background = [new] LinearGradientBrush(Colors.Turquoise, Colors.White, 90.0);]     |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[3, 3\].Background = [new] LinearGradientBrush(Colors.Firebrick, Colors.Orange, 90.0);]    |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[3, 4\].Background = [new] LinearGradientBrush(Colors.CornflowerBlue, Colors.White, 0.0);] |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[3, 5\].Background = [new] LinearGradientBrush(Colors.Olive, Colors.PaleGreen, 0.0);]      |
|                                                                                                                                                                                                                         |
| [this][.grid.Model\[3, 6\].Background = [new] LinearGradientBrush(Colors.Gold, Colors.Yellow, 90.0);]         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The following output is generated using the code above.

 

{border="0"}

Figure 47: Cell Background

***[]*** 

Visual properties

The visual aspects of the cell text can be controlled by the following properties.

 


  --------------- -------------------------------------------------------
  Property Name   Description
  Text            Holds the text to be displayed in the cell
  Foreground      Specifies text color
  Font            Controls the font properties for the text in the cell
  Orientation     Determines the angle of rotation of the text
  --------------- -------------------------------------------------------


**[]** 

1.   Setting Text, Foreground and Font Properties

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                         |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [//Setting text, foreground and fonts]                                                                                                           |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[6, 1\].Font.FontSize = 10;]                                                               |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[6, 1\].Text = [\"The quick brown fox jumps over the lazy dog\"];] |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[6, 1\].Foreground = Brushes.Gray;]                                                        |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[7, 1\].Font.FontSize = 12;]                                                               |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[7, 1\].Text = [\"The quick brown fox jumps over the lazy dog\"];] |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[7, 1\].Foreground = Brushes.Red;]                                                         |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[8, 1\].Font.FontSize = 14;]                                                               |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[8, 1\].Text = [\"The quick brown fox jumps over the lazy dog\"];] |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[8, 1\].Foreground = Brushes.Blue;]                                                        |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[9, 1\].Font.FontSize = 16;]                                                               |
|                                                                                                                                                                                                    |
| [this][.grid.RowHeights\[9\] = 30d;]                                                                          |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[9, 1\].Text = [\"The quick brown fox jumps over the lazy dog\"];] |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[9, 1\].Foreground = Brushes.Green;]                                                       |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [//Setting font weights]                                                                                                                         |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[6, 5\].Font.FontWeight = FontWeights.Bold;]                                               |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[6, 5\].HorizontalAlignment = HorizontalAlignment.Center;]                                 |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[6, 5\].CellValue = [\"Font weight is Bold\"];]                    |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[7, 5\].Font.FontStyle  = FontStyles.Italic;]                                              |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[7, 5\].HorizontalAlignment = HorizontalAlignment.Center;]                                 |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[7, 5\].CellValue = [\"Font style is Itlaic\"];]                   |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[8, 5\].Font.FontStyle = FontStyles.Normal;]                                               |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[8, 5\].HorizontalAlignment = HorizontalAlignment.Center;]                                 |
|                                                                                                                                                                                                    |
| [this][.grid.Model\[8, 5\].CellValue = [\"Font style is Normal\"];]                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The following output is generated using the code above.

 

{border="0"}

Figure 48: Font, Foreground and Text Properties

[] 

2.   Setting Cell Orientation

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                             |
|                                                                                                                                                                        |
| []                                                                                                                                 |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 1\].Font.Orientation = 45;]                               |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 1\].CellValue = [\"Angle 45\"];]  |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 1\].HorizontalAlignment = HorizontalAlignment.Center;]    |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 1\].VerticalAlignment = VerticalAlignment.Center;]        |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 2\].Font.Orientation = 90;]                               |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 2\].CellValue = [\"Angle 90\"];]  |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 2\].HorizontalAlignment = HorizontalAlignment.Center;]    |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 2\].VerticalAlignment = VerticalAlignment.Center;]        |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 3\].Font.Orientation = 180;]                              |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 3\].CellValue = [\"Angle 180\"];] |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 3\].HorizontalAlignment = HorizontalAlignment.Center;]    |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 3\].VerticalAlignment = VerticalAlignment.Center;]        |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 4\].Font.Orientation = 270;]                              |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 4\].CellValue = [\"Angle 270\"];] |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 4\].HorizontalAlignment = HorizontalAlignment.Center;]    |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 4\].VerticalAlignment = VerticalAlignment.Center;]        |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 5\].Font.Orientation = 320;]                              |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 5\].CellValue = [\"Angle 320\"];] |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 5\].HorizontalAlignment = HorizontalAlignment.Center;]    |
|                                                                                                                                                                        |
| [this][.grid.Model\[12, 5\].VerticalAlignment = VerticalAlignment.Center;]        |
|                                                                                                                                                                        |
| [this][.grid.Model.RowHeights\[12\] = 50;]                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The following output is generated using the code above.

 

{border="0"}

Figure 49: Cell Orientation

 

Borders

Cell borders can be customized to have different color, thickness and style. It is possible to have different border styles for top, bottom, left and right borders for the same cell.

 

Setting Borders

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                  |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 1\].Borders.Bottom = [new] Pen(Brushes.Blue, 1);]         |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 1\].Borders.Top = [new] Pen(Brushes.Red, 1);]             |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 1\].Borders.Right = [new] Pen(Brushes.Purple,3);]         |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 1\].Borders.Left = [new] Pen(Brushes.RoyalBlue,1);]       |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 2\].Borders.Bottom = [new] Pen(Brushes.Turquoise, 1);]    |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 2\].Borders.Bottom.Thickness = 5;]                                             |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 2\].Borders.Top = [new] Pen(Brushes.LawnGreen, 1);]       |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 2\].Borders.Top.DashCap = PenLineCap.Round;]                                   |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 2\].Borders.Top.Thickness = 5;]                                                |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 2\].Borders.Right = [new] Pen(Brushes.SteelBlue, 3);]     |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 2\].Borders.Right.Thickness = 5;]                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 3\].Borders.Bottom = [new] Pen(Brushes.IndianRed, 2);]    |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 3\].Borders.Bottom.DashStyle = DashStyles.DashDot;]                            |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 3\].Borders.Top = [new] Pen(Brushes.Indigo, 2);]          |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 3\].Borders.Top.DashStyle = DashStyles.DashDot;]                               |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 3\].Borders.Right = [new] Pen(Brushes.Gray, 3);]          |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 3\].Borders.Right.DashStyle = DashStyles.DashDot;]                             |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 4\].Borders.Bottom = [new] Pen(Brushes.HotPink, 2);]      |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 4\].Borders.Top = [new] Pen(Brushes.DeepSkyBlue, 2);]     |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 4\].Borders.Right = [new] Pen(Brushes.Magenta, 3);]       |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 4\].Borders.Bottom.DashStyle = DashStyles.Dash;]                               |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 4\].Borders.Top.DashStyle = DashStyles.Dash;]                                  |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 4\].Borders.Right.DashStyle = DashStyles.Dash;]                                |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 5\].Borders.Bottom = [new] Pen(Brushes.Maroon, 2);]       |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 5\].Borders.Top = [new] Pen(Brushes.Olive, 2);]           |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 5\].Borders.Right = [new] Pen(Brushes.CadetBlue, 2);]     |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 5\].Borders.Bottom.DashStyle = DashStyles.Dot;]                                |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 5\].Borders.Top.DashStyle = DashStyles.Dot;]                                   |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 5\].Borders.Right.DashStyle = DashStyles.Dot;]                                 |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 6\].Borders.Bottom = [new] Pen(Brushes.Chocolate, 4);]    |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 6\].Borders.Top = [new] Pen(Brushes.Crimson, 4);]         |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 6\].Borders.Right = [new] Pen(Brushes.DarkGoldenrod, 4);] |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 6\].Borders.Bottom.DashStyle = DashStyles.DashDotDot;]                         |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 6\].Borders.Top.DashStyle = DashStyles.DashDotDot;]                            |
|                                                                                                                                                                                             |
| [this][.grid.Model\[15, 6\].Borders.Right.DashStyle = DashStyles.DashDotDot;]                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The following output is generated using the code above.

 

{border="0"}

Figure 50: Setting Borders

 

Data Formats

Essential Grid allows the user to specify the format string for Text and DateTime cell values. The following table lists the various format strings supported.

**[]** 


  -------------- -----------------------------------
  Text Formats   Example with Cell Value = Math.PI
  0.00           3.14
  C              \$3.14
  0.00;(0.00)    3.14
  ###0.##%       314.16%
  #0.#E+00       3L4E-01
  10:##,##0.#    10.00,003.1
  -------------- -----------------------------------


[] 


  ---------- ----------------------------------------
  DateTime   Example with Cell Value = DateTime.Now
  d          8/10/2009
  D          Monday, August 10, 2009
  f          Monday, August 10, 2009 7.00 AM
  dddd       Monday, 10 August 2009
  t          7.00 AM
  s          2009-08-10T07:00:15
  ---------- ----------------------------------------


[] 

1.   Setting text format

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [//Setting Text formats            ]                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [int][ rowIndex = 3;]                                                                                                                     |
|                                                                                                                                                                                                                                |
| [int][ colIndex = 1;]                                                                                                                     |
|                                                                                                                                                                                                                                |
| [GridModel model =  [this].grid.Model; ]                                                                                                                              |
|                                                                                                                                                                                                                                |
| [foreach][ ([string] format [in] [new] [string]\[\] ] |
|                                                                                                                                                                                                                                |
| [      {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [            [\"0.00\"],]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [\"C\"],]                                                                                                                                             |
|                                                                                                                                                                                                                                |
| [            [\"0.00;(0.00)\"],]                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [            [\"###0.##%\"],]                                                                                                                                      |
|                                                                                                                                                                                                                                |
| [            [\"#0.#E+00\"],]                                                                                                                                      |
|                                                                                                                                                                                                                                |
| [            [\"10:##,##0.#\"]]                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [      })]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [    model\[rowIndex - 1, colIndex\].Text = format;]                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [    model\[rowIndex  , colIndex\].Format = format;]                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [    model\[rowIndex , colIndex\].CellValue = Math.PI;]                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [    model\[rowIndex , colIndex\].CellValueType = [typeof]([double]);]                                                                           |
|                                                                                                                                                                                                                                |
| [    rowIndex += 3;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Setting DateTime format

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [//Setting DateTime formats            ]                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [rowIndex = 2;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [colIndex = 3;]                                                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [           ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                |
| [foreach][ ([string] format [in] [new] [string]\[\] ] |
|                                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [\"d\"],]                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [        [\"D\"],]                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [        [\"f\"],]                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [        [\"dddd, dd MMMM yyyy\"],]                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [\"t\"],]                                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [        [\"s\"]]                                                                                                                                                  |
|                                                                                                                                                                                                                                |
| [    })]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [    model\[rowIndex - 1, colIndex\].Text = format;]                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [    grid.Model.ColumnWidths\[colIndex\] = 150d;]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [    model\[rowIndex, colIndex\].Format = format;]                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [    model\[rowIndex, colIndex\].CellValue = DateTime.Now;]                                                                                                                                |
|                                                                                                                                                                                                                                |
| [    model\[rowIndex, colIndex\].CellValueType = [typeof](DateTime);]                                                                                                 |
|                                                                                                                                                                                                                                |
| [    rowIndex += 3;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Output

 

The following output is generated using the code above.

 

{border="0"}

Figure 51: Date Format

 

 

[]{#related-topics}

