---
title: usingthegridstyleinfoclass.md
original_path: WinForms_Docs/04_Controls/Grid/usingthegridstyleinfoclass.md
created_at: 2025-08-05
---






##### Using the GridStyleInfo Class {#using-the-gridstyleinfo-class style="tab-stops: 0pt"}

[] 

By using the **GridRangeInfo** class and the properties of the **GridStyleInfo** class, you can write code illustrating how to enter values into a grid and how to affect the appearance of these displayed values. In the sections that follow, you will learn how to create a Grid object and place it on a form. Then you can set the style values by using the Grid classes discussed so far: GridStyleInfo, GridRangeInfo and GridControl.

[] 

 

[]{#p284} 

 

###### 4.1.4.7.3.1 Setting GridStyleInfo Properties {#setting-gridstyleinfo-properties style="tab-stops: 0pt"}

[] 

There are several ways of setting the **GridStyleInfo** properties. If you want to set them for a particular cell, you need to use the row and column values as indexers on the **GridControl** object to retrieve the **GridStyleInfo** object that is associated with a particular cell. But, to change a **BaseStyle**, a **ColumnStyle** or a **RowStyle**, you will have to use different accessory methods to retrieve the style which is under consideration. In the code samples that follow, we will show you several ways of changing particular styles.

[] 


{border="0"}Note: In this section, we are working with the cell-oriented Grid control which allows us to explicitly set individual cell and row properties. In the column-oriented Grid Data Bound Grid, explicitly setting individual cell and row properties is not supported. Instead, events are used to set these properties on demand. You can see samples in the Grid Data Bound Grid section.


[] 

It comprises the following sections:

[] 

 

[]{#p285} 

4.1.4.7.3.1.1      Through Code

[] 

Given below is the code to help you create **GridStyleInfo** properties.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [// Add some text to cell (2,3).]                                                                                                       |
|                                                                                                                                                                                           |
| [gridControl1\[2, 3\].CellValue = [\"Essential\"];]                                                                           |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [// Create a GridStyleInfo.]                                                                                                            |
|                                                                                                                                                                                           |
| [GridStyleInfo][ style = [new] [GridStyleInfo]();]   |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [// Set some properties.]                                                                                                               |
|                                                                                                                                                                                           |
| [style.BackColor = [Color].Aquamarine;]                                                                                       |
|                                                                                                                                                                                           |
| [style.CellValue = [\"Grid\"];]                                                                                               |
|                                                                                                                                                                                           |
| [style.Font.Facename = [\"Verdana\"];]                                                                                        |
|                                                                                                                                                                                           |
| [style.Font.Size = 8.2f;]                                                                                                                             |
|                                                                                                                                                                                           |
| [style.Font.Bold = [true];]                                                                                                      |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [// Apply this style to several cells.]                                                                                                 |
|                                                                                                                                                                                           |
| [this][.gridControl1.ChangeCells([GridRangeInfo].Cells(3, 3, 4, 4), style);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                           |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [\' Add some text to cell (2,3).]                                                                          |
|                                                                                                                                                              |
| [gridControl1(2, 3).CellValue = [\"Essential\"]]                                                 |
|                                                                                                                                                              |
| []                                                                                                       |
|                                                                                                                                                              |
| [\' Create a GridStyleInfo.]                                                                               |
|                                                                                                                                                              |
| [Dim][ style [As] GridStyleInfo]                   |
|                                                                                                                                                              |
| [style = [New] GridStyleInfo()]                                                                     |
|                                                                                                                                                              |
| []                                                                                                                       |
|                                                                                                                                                              |
| [\' Set some properties.]                                                                                  |
|                                                                                                                                                              |
| [style.BackColor = Color.Aquamarine]                                                                                     |
|                                                                                                                                                              |
| [style.CellValue = [\"Grid\"]]                                                                   |
|                                                                                                                                                              |
| [style.Font.Facename = [\"Verdana\"]]                                                            |
|                                                                                                                                                              |
| [style.Font.Size = 8.2!]                                                                                                 |
|                                                                                                                                                              |
| [style.Font.Bold = [True]]                                                                          |
|                                                                                                                                                              |
| []                                                                                                          |
|                                                                                                                                                              |
| [\' Apply this style to several cells.]                                                                    |
|                                                                                                                                                              |
| [Me][.gridControl1.ChangeCells(GridRangeInfo.Cells(3, 3, 4, 4), style)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][133][: Result of the ChangeCells Call in the Previous Code Sample]*

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| []                                                                                                                                       |
|                                                                                                                                                                                            |
| [// Change the back color of the grid by using TableStyle.]                                                                              |
|                                                                                                                                                                                            |
| [this][.gridControl1.TableStyle.BackColor = [Color].FromArgb(255, 192, 192);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                          |
|                                                                                                                                                                             |
| []                                                                                                                        |
|                                                                                                                                                                             |
| [\' Change the back color of the grid using TableStyle.]                                                                  |
|                                                                                                                                                                             |
| [Me][.gridControl1.TableStyle.BackColor = Color.FromArgb(255, 192, 192)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

[] 

*[Figure ][134][: Changing the TableStyle BackColor Property Adds a Rose Background for Cells Whose BackColor Was Not Explicitly Set]*

*[]* 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                                             |
| []                                                                                                                        |
|                                                                                                                                                                             |
| [// Change a row style and a column style.]                                                                               |
|                                                                                                                                                                             |
| [this][.gridControl1.RowStyles\[3\].TextColor = [Color].Blue;] |
|                                                                                                                                                                             |
| [this][.gridControl1.RowStyles\[3\].CellValue = [\"Blue\"];]   |
|                                                                                                                                                                             |
| [this][.gridControl1.ColStyles\[3\].TextColor = [Color].Red;]  |
|                                                                                                                                                                             |
| [this][.gridControl1.ColStyles\[3\].CellValue = [\"Red\"];]    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                   |
|                                                                                                                                                                      |
| []                                                                                                                 |
|                                                                                                                                                                      |
| [\' Change a row style and a column style.]                                                                        |
|                                                                                                                                                                      |
| [Me][.gridControl1.RowStyles(3).TextColor = Color.Blue]                         |
|                                                                                                                                                                      |
| [Me][.gridControl1.RowStyles(3).CellValue = [\"Blue\"]] |
|                                                                                                                                                                      |
| [Me][.gridControl1.ColStyles(3).TextColor = Color.Red]                          |
|                                                                                                                                                                      |
| [Me][.gridControl1.ColStyles(3).CellValue = [\"Red\"]]  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

[] 

*[Figure ][135][: Row 3 with Blue Text and Column 3 With Red Text. Note the Row Attribute Takes Precedence Over the Column Attribute in Cell 3,3 as the TGxt is Blue]*

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [// Change a base style, eg. Row Header.]                                                                                                 |
|                                                                                                                                                                                             |
| [gridControl1.BaseStylesMap\[[\"Row Header\"]\].StyleInfo.BackColor = [Color].FromArgb(228, 255, 255);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [\' Change a base style, eg. Row Header.]                                                                    |
|                                                                                                                                                                |
| [gridControl1.BaseStylesMap([\"Row Header\"]).StyleInfo.BackColor = Color.FromArgb(228, 255, 255)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

[] 

*[Figure ][136][: Row Headers No Longer Shaded Gray, Now Light Blue]*

 

[]{#p286} 

 

4.1.4.7.3.1.2      Through Designer

[] 

To edit cell styles from the designer you must select the grid on the design surface and then click the Toggle Interactive Mode verb shown at the bottom of the **PropertyGrid**. This will allow you to select the cells that are within the Grid control on the design surface. To change any of the style settings of the selected cells, you must first click the Cell Settings tool bar button at the top of the PropertyGrid. This will display the cell style settings that are within the PropertyGrid and will allow you to change them. The changes will affect the currently selected range or the current cell if no range is selected.

[] 

{border="0"}

[] 

*[Figure ][137][: Toggle Interactive Mode Verb and CellSettings Button]*

 

[]{#p287} 

 

###### 4.1.4.7.3.2 Creating a Grid Object {#creating-a-grid-object style="tab-stops: 0pt"}

[] 

To add a Grid control to a form, you must create an instance of the Grid control, set the row and column count, then position it on your form[.]

[] 

It comprises the following sections:

[] 

 

[]{#p288} 

 

4.1.4.7.3.2.1      Through Designer

[] 

With the designer, you can drag-and-drop the control, size it, and then set a couple of properties.

[] 

[·      ]Drag a Grid control object from your toolbox and drop it on the form.

[·      ]Size and position it.

[·      ]Change the **RowCount** and **ColCount** values in the **PropertyGrid** for this control.

 

[]{#p289} 

 

4.1.4.7.3.2.2      Through Code

[] 

Given below is the code to help you create a grid.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [using][ Syncfusion.Windows.Forms.Grid;]                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [                        \....]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [// Create the Essential Grid.]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [private][ GridControl gridControl1;]                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [                        \....]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [this][.gridControl1 = ][new][ GridControl();]                         |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [// Set the number of rows and columns.]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| [this][.gridControl1.ColCount = 10;]                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [this][.gridControl1.RowCount = 100;]                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [                        ]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [// Position it on the form.]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [this][.gridControl1.Location = ][new][ System.Drawing.Point(20, 20);] |
|                                                                                                                                                                                                                                                                              |
| [this][.gridControl1.Size = ][new][ System.Drawing.Size(344, 200);]    |
|                                                                                                                                                                                                                                                                              |
| [                        ]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [// Add it to the forms\' controls.]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [this][.Controls.Add(][this][.gridControl1);]                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [imports][ Syncfusion.Windows.Forms.Grid]                                                                                                                              |
|                                                                                                                                                                                                                                                                           |
| [                \....]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| [\' Create the Essential Grid.]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                           |
| [Private WithEvents][ gridControl1 ][As][ GridControl]              |
|                                                                                                                                                                                                                                                                           |
| [                \....]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| [Me][.gridControl1 = ][New][ GridControl()]                         |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [\' Set the number of rows and columns.]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [Me][.gridControl1.ColCount = 10]                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [Me][.gridControl1.RowCount = 100]                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [\' Position it on the form.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [Me][.gridControl1.Location = ][New][ System.Drawing.Point(20, 15)] |
|                                                                                                                                                                                                                                                                           |
| [Me][.gridControl1.Size = ][New][ System.Drawing.Size(344, 150)]    |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [\' Add it to the forms\' controls.]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [Me][.Controls.Add(][Me][.gridControl1)]                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p290} 

 

[]{#related-topics}

