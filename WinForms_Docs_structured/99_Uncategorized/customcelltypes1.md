---
title: customcelltypes1.md
original_path: WinForms_Docs/99_Uncategorized/customcelltypes1.md
created_at: 2025-08-05
---








  









### Custom Cell Types {#custom-cell-types style="tab-stops: 0pt"}

[] 

Following are the custom cell types supported by the Grid Helper Library.

[] 

a.   ButtonEdit

b.   CalculatorTextBox

c.   Calendar

d.   DateTimePicker

e.   FNumericUpDown

f.    GridinCell

g.   LinkLabelCell

h.   PictureBox

[] 

ButtonEdit

 

You can implement a Button Edit control in grid cells by using the **ButtonEdit** cell type. ButtonEdit cell types can be used by initializing the **ButtonEditStyleProperties** class for the grid cells.

 

Following are the Button Edit cell types available in the Grid control.

[] 

[·      ]Browse

[·      ]Check

[·      ]Down

[·      ]Image

[·      ]Left

[·      ]Leftend

[·      ]None

[·      ]Redo

[·      ]Right

[·      ]Rightend

[·      ]Undo

[·      ]Up

 

The following code example illustrates how to set the grid cell type to ButtonEdit.

[] 

1.   Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| [// Register the Cell Type with Grid control.]                                                                                                                        |
|                                                                                                                                                                                                                         |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].ButtonEdit);]                         |
|                                                                                                                                                                                                                         |
| [Syncfusion.GridHelperClasses.[ButtonEditStyleProperties] sp;]                                                                                              |
|                                                                                                                                                                                                                         |
| [sp = [new] Syncfusion.GridHelperClasses.[ButtonEditStyleProperties]([this].gridControl1\[rowIndex, colIndex\]);] |
|                                                                                                                                                                                                                         |
| [sp.ButtonEditInfo.ButtonEditType = Syncfusion.GridHelperClasses.[ButtonType].Browse;]                                                                      |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                         |
| [this][.gridControl1\[2, 2\].CellType = [\"ButtonEdit\"];]                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [\' Register the Cell Type with Grid control.]                                                                                         |
|                                                                                                                                                                                          |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.ButtonEdit)]                                                                           |
|                                                                                                                                                                                          |
| [Dim][ sp [As] Syncfusion.GridHelperClasses.ButtonEditStyleProperties]         |
|                                                                                                                                                                                          |
| [sp = [New] Syncfusion.GridHelperClasses.ButtonEditStyleProperties([Me].gridControl1(rowIndex, colIndex))] |
|                                                                                                                                                                                          |
| [sp.ButtonEditInfo.ButtonEditType = Syncfusion.GridHelperClasses.ButtonType.Browse]                                                                  |
|                                                                                                                                                                                          |
| [gridControl1\[2, 2\].CellType = [\"ButtonEdit\"]]                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Following screen shots illustrate different Button Edit cell types.

[] 

{border="0"}

[                                                 ]

*[Figure ][448][: \"Browse\" Button Edit Cell Type]*

[] 

{border="0"}

[] 

*[Figure ][449][: \"Check\" Button Edit Cell Type]****[]***

[] 

{border="0"}

[] 

*[Figure ][450][: \"Down\" Button Edit Cell Type]*

*[]* 

{border="0"}

[] 

*[Figure ][451][: \"Image\" Button Edit Cell Type]*

[] 

{border="0"}

[] 

*[Figure ][452][: \"Left\" Button Edit Cell Type]*

[] 

{border="0"}

[] 

*[Figure ][453][: \"Leftend\" Button Edit Cell Type]*

*[]* 

{border="0"}

***[]*** 

*[Figure ][454][: \"None\" Button Edit Cell Type]*

[] 

{border="0"}

[] 

*[Figure ][455][: \"Redo\" Button Edit Cell Type]*

[] 

{border="0"}

[] 

*[Figure ][456][: \"Right\" Button Edit Cell Type]*

[] 

{border="0"}

[] 

*[Figure ][457][: \"Rightend\" Button Edit Cell Type]****[]***

[] 

[{border="0"}][]

[] 

*[Figure ][458][: \"Undo\" Button Edit Cell Type]*

[] 

[{border="0"}][]

[] 

*[Figure ][459][: \"Up\" Button Edit Cell Type]*

[] 

CalculatorTextBox

 

You can implement a Calculator control in grid cells by using the **CalculatorTextBox** cell type. This cell type is implemented as a drop-down container, embedded into the cell. The drop down contains the calculator which displays and stores the value in the cell.

 

The following code example illustrates how to set the grid cell type to CalculatorTextBox.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].CalculatorTextBox);] |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [CalculatorControl c1 = [new] CalculatorControl();]                                                                                                           |
|                                                                                                                                                                                                                                        |
| [c1.BorderStyle = [Border3DStyle].Flat;]                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [c1.ButtonStyle = Syncfusion.Windows.Forms.[ButtonAppearance].Office2007;]                                                                                 |
|                                                                                                                                                                                                                                        |
| [c1.UseVisualStyle = [true];]                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [GridStyleInfo][ style = gridControl1\[4, 2\];]                                                                |
|                                                                                                                                                                                                                                        |
| [style.CellType = [\"CalculatorTextBox\"];]                                                                                                                |
|                                                                                                                                                                                                                                        |
| [style.Control = c1;]                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                                          |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.CalculatorTextBox)]                                                                    |
|                                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                                          |
| [Dim][ c1 [As] [New] CalculatorControl()] |
|                                                                                                                                                                                                          |
| [c1.BorderStyle = Border3DStyle.Flat]                                                                                                                |
|                                                                                                                                                                                                          |
| [c1.ButtonStyle = Syncfusion.Windows.Forms.ButtonAppearance.Office2007]                                                                              |
|                                                                                                                                                                                                          |
| [c1.UseVisualStyle = [True]]                                                                                                    |
|                                                                                                                                                                                                          |
| []                                                                                                                                      |
|                                                                                                                                                                                                          |
| [Dim][ style [As] GridStyleInfo = gridControl1(4, 2)]          |
|                                                                                                                                                                                                          |
| [style.CellType = [\"CalculatorTextBox\"]]                                                                                   |
|                                                                                                                                                                                                          |
| [style.Control = c1]                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Following screen shot illustrates CalculatorTextBox cell type in the Grid control.

[] 

[{border="0"}][]

[] 

*[Figure ][460][: CalculatorTextBox cell type in Grid Control]*

*[]* 

Calendar

[] 

You can implement a MonthCalendar control in a grid cell by enabling the **Calendar** cell type for that particular cell.

 

The following code example illustrates how to set the grid cell type to Calendar.

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].Calendar);] |
|                                                                                                                                                                                               |
| [GridStyleInfo][ style;]                                                                              |
|                                                                                                                                                                                               |
| [style = gridControl1\[row, 2\];]                                                                                                                         |
|                                                                                                                                                                                               |
| [style.CellType = [\"Calendar\"];]                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [// Provide a Month Calendar control for drawing cell contents.]                                                                            |
|                                                                                                                                                                                               |
| [style.Control = [new] [MonthCalendar]();]                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                         |
|                                                                                                                                            |
| []                                                                                       |
|                                                                                                                                            |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.Calendar)]                               |
|                                                                                                                                            |
| [Dim][ style [As] GridStyleInfo] |
|                                                                                                                                            |
| [style = gridControl1(row, 2)]                                                                         |
|                                                                                                                                            |
| [style.CellType = [\"Calendar\"]]                                              |
|                                                                                                                                            |
| []                                                                                     |
|                                                                                                                                            |
| [\' Provide a Month Calendar control for drawing cell contents.]                         |
|                                                                                                                                            |
| [style.Control = [New] MonthCalendar()]                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Following screen shot illustrates Calendar cell type in Grid control.

[] 

{border="0"}

[] 

*[Figure ][461][: Calendar cell type in Grid Control]*

[] 

DateTimePicker

[] 

You can implement a Date Time Picker control in grid cells by using the **DateTimePicker** cell type. This cell type is implemented as a drop-down container, embedded into the cell, where the date and time picker is added. The drop down contains the calendar which displays and stores the date value in the cell. Various formats for the date and time can be specified by using the **Format** style property.

[] 

The following code example illustrates how to set the grid cell type to DateTimePicker.

[] 

1.   Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].DateTimePicker);]   |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [// Set up DateTimePicker Cells.]                                                                                                                   |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[4, 2\].CellType = [\"DateTimePicker\"];]                           |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[4, 2\].CellValueType = [typeof]([DateTime]);] |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[4, 2\].CellValue = [DateTime].Now;]                                |
|                                                                                                                                                                                                       |
| [this][.gridControl1\[4, 2\].Format = [\"MM/dd/yyyy hh:mm\"];]                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.DateTimePicker)]                                                      |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [\' Set up DateTimePicker Cells.]                                                                                     |
|                                                                                                                                                                         |
| [Me][.gridControl1(4, 2).CellType = [\"DateTimePicker\"]]  |
|                                                                                                                                                                         |
| [Me][.gridControl1(4, 2).CellValueType = [GetType](DateTime)] |
|                                                                                                                                                                         |
| [Me][.gridControl1(4, 2).CellValue = DateTime.Now]                                 |
|                                                                                                                                                                         |
| [Me][.gridControl1(4, 2).Format = [\"MM/dd/yyyy hh:mm\"]]  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Following screen shot illustrates DateTimePicker cell type in the Grid control.

[] 

{border="0"}

[] 

*[Figure ][462][: DateTimePicker cell type in Grid Control]*

[] 

FnumericUpDown

[] 

You can implement a Float Numeric Up Down control in grid cells by using the **FNumericUpDown** cell type. FNumericUpDown cell types can be used by initializing the **FloatNumericUpDownStyleProperties** class for the grid cells. This will allow you set the limitations of the numeric values and several other properties can also be added as follows.

 

The following code example illustrates how to set the grid cell type to FNumericUpDown.

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].FNumericUpDown);] |
|                                                                                                                                                                                                     |
| [GridStyleInfo][ style = [this].gridControl1\[2, 2\];]                                 |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [// Set up FNumericUpDown Cell. ]                                                                                                                 |
|                                                                                                                                                                                                     |
| [style.CellType = [\"FNumericUpDown\"];]                                                                                                |
|                                                                                                                                                                                                     |
| [style.Text = [\"0.5\"];]                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.FNumericUpDown)]                                                                        |
|                                                                                                                                                                                           |
| [Dim][ style [As] GridStyleInfo = [Me].gridControl1(2, 2)] |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [\' Set up FNumericUpDown Cell. ]                                                                                                       |
|                                                                                                                                                                                           |
| [style.CellType = [\"FNumericUpDown\"]]                                                                                       |
|                                                                                                                                                                                           |
| [style.Text = [\"0.5\"]]                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Following screen shot illustrates FNumericUpDown cell type in the Grid control.

[] 

{border="0"}

[] 

*[Figure ][463][: FNumericUpDown cell type in Grid Control]*

[] 

GridinCell

[] 

The **GridinCell** cell type provides a covered range of cells to embed the grid, which is added as a control to the cells. The registered cell model initializes the range by calculating the size of the grid control to be embedded, and adds styles such as borders and scroll bars to have the control within the range.

 

The following code example illustrates how to set the grid cell type to GridinCell.

[] 

1.   Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].GridinCell);] |
|                                                                                                                                                                                                 |
| [GridControl][ grid;]                                                                                   |
|                                                                                                                                                                                                 |
| [this][.gridControl1\[3, 2\].CellType = [\"GridinCell\"];]                         |
|                                                                                                                                                                                                 |
| [this][.gridControl1.CoveredRanges.Add([GridRangeInfo].Cells(3, 2, 7, 4));]        |
|                                                                                                                                                                                                 |
| [grid = [new] Syncfusion.GridHelperClasses.[CellEmbeddedGrid]([this].gridControl1);]      |
|                                                                                                                                                                                                 |
| [grid.BackColor = [Color].FromArgb(0xb4, 0xe7, 0xf2);]                                                                              |
|                                                                                                                                                                                                 |
| [grid.RowCount = 10;]                                                                                                                                       |
|                                                                                                                                                                                                 |
| [grid.ColCount = 4;]                                                                                                                                        |
|                                                                                                                                                                                                 |
| [grid\[1, 1\].Text = [\"this is a 10x4 grid\"];]                                                                                    |
|                                                                                                                                                                                                 |
| [grid.ThemesEnabled = [true];]                                                                                                         |
|                                                                                                                                                                                                 |
| [this][.gridControl1\[3, 2\].Control = grid;]                                                              |
|                                                                                                                                                                                                 |
| [this][.gridControl1.Controls.Add(grid);]                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.GridinCell)]                                                     |
|                                                                                                                                                                    |
| [Dim][ grid [As] GridControl]                            |
|                                                                                                                                                                    |
| [Me][.gridControl1(3, 2).CellType = [\"GridinCell\"]] |
|                                                                                                                                                                    |
| [Me][.gridControl1.CoveredRanges.Add(GridRangeInfo.Cells(3, 2, 7, 4))]        |
|                                                                                                                                                                    |
| [grid = [New] Syncfusion.GridHelperClasses.CellEmbeddedGrid([Me].gridControl1)]      |
|                                                                                                                                                                    |
| [grid.BackColor = Color.FromArgb(&HB4, &HE7, &HF2)]                                                                            |
|                                                                                                                                                                    |
| [grid.RowCount = 10]                                                                                                           |
|                                                                                                                                                                    |
| [grid.ColCount = 4]                                                                                                            |
|                                                                                                                                                                    |
| [grid(1, 1).Text = [\"this is a 10x4 grid\"]]                                                          |
|                                                                                                                                                                    |
| [grid.ThemesEnabled = [True]]                                                                             |
|                                                                                                                                                                    |
| [Me][.gridControl1(3, 2).Control = grid]                                      |
|                                                                                                                                                                    |
| [Me][.gridControl1.Controls.Add(grid)]                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Following screen shot illustrates GridinCell cell type in the Grid control.

[] 

{border="0"}

[] 

*[Figure ][464][: GridinCell cell type in Grid Control]*

[] 

LinkLabelCell

[] 

The **LinkLabelCell** cell type displays text which can be hyperlinked to a specific location. The path to be hyperlinked is specified by using the **Tag** property.

 

The following code example illustrates how to set the grid cell type to LinkLabelCell.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].LinkLabelCell);] |
|                                                                                                                                                                                                    |
| [int][ rowIndex = 5;]                                                                                         |
|                                                                                                                                                                                                    |
| [gridControl1\[rowIndex, 2\].CellType = [\"LinkLabelCell\"];]                                                                          |
|                                                                                                                                                                                                    |
| [gridControl1\[rowIndex, 2\].Text = [\"Syncfusion, Inc.\"];]                                                                           |
|                                                                                                                                                                                                    |
| [gridControl1\[rowIndex, 2\].Font.Bold = [true];]                                                                                         |
|                                                                                                                                                                                                    |
| [gridControl1\[rowIndex, 2\].Tag = [\"http://www.syncfusion.com\"];]                                                                   |
|                                                                                                                                                                                                    |
| [gridControl1\[rowIndex, 2\].HorizontalAlignment = [GridHorizontalAlignment].Center;]                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.LinkLabelCell)]                                                  |
|                                                                                                                                                                    |
| [Dim][ rowIndex [As] [Integer] = 5] |
|                                                                                                                                                                    |
| [gridControl1(rowIndex, 2).CellType = [\"LinkLabelCell\"]]                                             |
|                                                                                                                                                                    |
| [gridControl1(rowIndex, 2).Text = [\"Syncfusion, Inc.\"]]                                              |
|                                                                                                                                                                    |
| [gridControl1(rowIndex, 2).Font.Bold = [True]]                                                            |
|                                                                                                                                                                    |
| [gridControl1(rowIndex, 2).Tag = [\"http://www.syncfusion.com\"]]                                      |
|                                                                                                                                                                    |
| [gridControl1(rowIndex, 2).HorizontalAlignment = GridHorizontalAlignment.Center]                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Following screen shot illustrates LinkLabelCell cell type in the Grid control.

[                                        ]

{border="0"}

[] 

*[Figure ][465][: LinkLabelCell cell type in Grid Control]****[]***

[] 

PictureBox

 

The **PictureBox** cell type can be embedded into a cell by calculating the size of the picture and extending the width and height of the cell accordingly. The **PictureBoxStyleProperties** class is used to specify the style for the Picture Box control.

 

The following code example illustrates how to set the grid cell type to PictureBox.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                        |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].PictureBox);]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                        |
| [Syncfusion.GridHelperClasses.[PictureBoxStyleProperties] tsp = [new] Syncfusion.GridHelperClasses.[PictureBoxStyleProperties]([new] [GridStyleInfo](gridControl1.TableStyle));] |
|                                                                                                                                                                                                                                                                                                                                        |
| [tsp.SizeMode = [PictureBoxSizeMode].AutoSize;]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                        |
| [Syncfusion.GridHelperClasses.[PictureBoxStyleProperties] sp;]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                        |
| [GridStyleInfo][ style;]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                        |
| [gridControl1.ColWidths\[1\] = 20;]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                        |
| [style = gridControl1\[2, 2\];]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                        |
| [style.CellType = [\"PictureBox\"];]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                        |
| [sp = [new] Syncfusion.GridHelperClasses.[PictureBoxStyleProperties](style);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                        |
| [sp.Image = GetImage([\"one.jpg\"]);]                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.PictureBox)]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ tsp [As] [New] Syncfusion.GridHelperClasses.PictureBoxStyleProperties([New] GridStyleInfo(gridControl1.TableStyle))] |
|                                                                                                                                                                                                                                                                                 |
| [tsp.SizeMode = PictureBoxSizeMode.AutoSize]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ sp [As] Syncfusion.GridHelperClasses.PictureBoxStyleProperties]                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [Dim][ style [As] GridStyleInfo]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [gridControl1.ColWidths(1) = 20]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [style = gridControl1(2, 2)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| [style.CellType = [\"PictureBox\"]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [sp = [New] Syncfusion.GridHelperClasses.PictureBoxStyleProperties(style)]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [sp.Image = GetImage([\"one.jpg\"])]                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Following screen shot illustrates PictureBox cell type in the Grid control.

[] 

{border="0"}

[] 

*[Figure ][466][: PictureBox cell type in Grid Control]*

 

[]{#p535} 

 

[]{#related-topics}

