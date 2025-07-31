---
title: textbox3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textbox3.md
created_at: 2025-07-03
---






#### Text Box {#text-box style="tab-stops: 0pt"}

**[]** 

Essential XlsIO can now read and write text boxes. The **ITextBoxShape** interface lets you add a new text box inside a worksheet. The **IFill** interface is used to customize the inner appearance of the textbox. **IShapeLineFormat** interface is used to modify the border. Various other properties like Horizontal and Vertical Alignment, Alternative Text, Text Rotation, and so on, are also supported.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                             |
| **[]**                                                                                                                  |
|                                                                                                                                                             |
| [// Creates a new Text Box.]                                                                              |
|                                                                                                                                                             |
| [ITextBoxShape][ textbox = sheet.TextBoxes.AddTextBox(3, 7, 25, 100);] |
|                                                                                                                                                             |
| [textbox.Text = [\"Essential XlsIO\"];]                                                          |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [// Reads a Text Box.]                                                                                    |
|                                                                                                                                                             |
| [ITextBoxShape][ shape1 = sheet.TextBoxes\[0\];]                       |
|                                                                                                                                                             |
| [shape1.Name = [\"First TextBox\"];]                                                             |
|                                                                                                                                                             |
| [shape1.Fill.ForeColor = [Color].Gold;]                                                            |
|                                                                                                                                                             |
| [shape1.Fill.BackColor = [Color].Black;]                                                           |
|                                                                                                                                                             |
| [shape1.Fill.Pattern = [ExcelGradientPattern].Pat_90_Percent;]                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                     |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                               |
|                                                                                                                                                                                          |
| [\' Creates a new Text Box.]                                                                                                           |
|                                                                                                                                                                                          |
| [Dim][ textbox [As] ITextBoxShape = sheet.TextBoxes.AddTextBox(3, 7, 25, 100)] |
|                                                                                                                                                                                          |
| [textbox.Text = [\"Essential XlsIO\"]]                                                                                        |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [\' Reads a Text Box.]                                                                                                                 |
|                                                                                                                                                                                          |
| [ITextBoxShape shape1 = sheet.TextBoxes(0)]                                                                                                          |
|                                                                                                                                                                                          |
| [shape1.Name = [\"First TextBox\"]]                                                                                           |
|                                                                                                                                                                                          |
| [shape1.Fill.ForeColor = Color.Gold]                                                                                                                 |
|                                                                                                                                                                                          |
| [shape1.Fill.BackColor = Color.Black]                                                                                                                |
|                                                                                                                                                                                          |
| [shape1.Fill.Pattern = ExcelGradientPattern.Pat_90_Percent]                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

Figure 96: TextBox created using XlsIO**[]**

[] 

 

[]{#related-topics}

