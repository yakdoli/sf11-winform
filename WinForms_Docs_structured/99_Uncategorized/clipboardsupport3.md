---
title: clipboardsupport3.md
original_path: WinForms_Docs/99_Uncategorized/clipboardsupport3.md
created_at: 2025-08-05
---






#### Clipboard Support {#clipboard-support style="tab-stops: 0pt"}

Essential Grid provides complete support for clipboard operations. End users can copy/cut & paste any data inside the grid and to or from other OLE \[Object Linking and Embedding\]-enabled applications such as Notepad. The built-in source allows us to copy the text data along with the style information and also provides hooks that let us customize the clipboard operation of pasting the custom formatted data.

 

Copy Paste Options

 

CopyPasteOption property defines the list of clipboard operations supported by the grid. It exposes the following options:

 

[·      ]CopyText--Copies only the text from the grid selection to clipboard

[·      ]CopyCellData--Copies both text and style information from grid cells to clipboard

[·      ]PasteText--Pastes only the text from clipboard

[·      ]PasteCell--Pastes the cell text along with its style information from the clipboard

[·      ]CutText--Moves only the text from grid to clipboard

[·      ]CutCell--Moves the text and the style information from grid to clipboard

[·      ]ExcludeCurrentCell--Skips current cell while doing clipboard operations

[·      ]XmlCopyPaste -- Copy the cell value along with basic styles in  Xml format and supported to paste in Microsoft Excel. This also supports to copy the Formula value from the Grid Control and Paste in Microsoft Excel

 

Example

 

Here are the sample code snippets that define certain copy paste behaviors. 

 

+---------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                            |
|                                                                                                                                       |
| **[]**                                                                              |
|                                                                                                                                       |
| [//Copy cell data with style]                                                       |
|                                                                                                                                       |
| [gridControl.Model.Options.CopyPasteOption \|= [CopyPaste].CopyCellData;] |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [//Cut cell data with style]                                                        |
|                                                                                                                                       |
| [gridControl.Model.Options.CopyPasteOption \|= [CopyPaste].CutCell;]      |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [//Paste cell data with style]                                                      |
|                                                                                                                                       |
| [gridControl.Model.Options.CopyPasteOption \|= [CopyPaste].PasteCell;]    |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [//Code to cut copy paste cell text (excluding style)]                              |
|                                                                                                                                       |
| [gridControl.Model.Options.CopyPasteOption = ([CopyPaste])(0);]           |
|                                                                                                                                       |
| [gridControl.Model.Options.CopyPasteOption \|= [CopyPaste].CopyText;]     |
|                                                                                                                                       |
| [gridControl.Model.Options.CopyPasteOption \|= [CopyPaste].CutText;]      |
|                                                                                                                                       |
| [gridControl.Model.Options.CopyPasteOption \|= [CopyPaste].PasteText;]    |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 69: Pasting the grid data in Notepad

***[]*** 

Text Data Exchange

 

GridModel.TextDataExchange helps you in customizing the clipboard operations. It is used as an interface that exposes the following property and methods. 

 

[·      ]Property-TabDelimiter

[·      ]Method-CopyTextToBuffer(), PasteTextFromBuffer()

 

The above attributes are discussed below in detail:

 

1.   TabDelimiter Property

 

This property specifies a delimiter for the text to be pasted. It can be used when you want to paste the cell data in CSV (Comma-Separated Values) format.

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                               |
|                                                                                                                          |
| **[]**                                                                 |
|                                                                                                                          |
| [gridControl.Model.TextDataExchange.TabDelimiter = [\",\"];] |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 70: Pasting the grid data in CSV format

***[]*** 

2.   CopyTextToBuffer() Method

 

This method lets you place the cell data into an intermediate buffer, which can be customized. The method performs clipboard cut or copy operation depending on the third parameter given to it. This method accepts the following parameters:

 

[·      ]String buffer

[·      ]Selected range of cells

[·      ]Boolean value-This should be set to true for cut operation and should be set to false for copy operation.

 

The following code illustrates the CopyTextToBuffer method:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [gridControl.Model.TextDataExchange.CopyTextToBuffer([out] buffer, gridControl.Model.SelectedRanges, [out] row, [out] col, [false]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Result of this Method Call

 

It returns the following values:

 

[·      ]Cell text

[·      ]No. of rows affected

[·      ]No. of columns affected

**[]** 

3.   PasteTextFromBuffer() Method

 

The values returned by the CopyTextToBuffer method is passed as parameter to the PasteTextFromBuffer method using the below code:

 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                              |
|                                                                                                                                         |
|                                                                                                                                         |
|                                                                                                                                         |
| [gridControl.Model.TextDataExchange.PasteTextFromBuffer(buffer, gridControl.Model.SelectedRanges);] |
+-----------------------------------------------------------------------------------------------------------------------------------------+

 

Result of this Method Call

 

It pastes the text from the given buffer into specified range of grid cells.

 

Events

 

Grid provides the following events which are available for the end user to customize the clipboard data.

 

[·      ]ClipboardCanCopy

[·      ]ClipboardCanCut

[·      ]ClipboardCanPaste

[·      ]ClipboardCopy

[·      ]ClipboardCut

[·      ]ClipboardPaste

**[]** 

IGridCopyPaste

 

Essential Grid defines an interface called IGridCopyPaste that exposes some methods, namely Copy(), Cut() and Paste(). Here the users can write custom code to perform cut copy or paste operations with any kind of user-defined data. Thereby, it extends its clipboard support behavior to perform clipboard operations in various forms.

 

For instance, let us consider performing the copy and paste operations in HTML format. The respective implementation of IGridCopyPaste is as follows:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                     |
|                                                                                                                                                                                                                |
| **[]**                                                                                                                                                       |
|                                                                                                                                                                                                                |
| [class][ [HtmlCopy] : IGridCopyPaste]                                                             |
|                                                                                                                                                                                                                |
| [{]                                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [    [public] [void] Copy(GridCellData gridData, GridRangeInfoList rangeList)]                                                   |
|                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                    |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [        [IDataObject] iData = [null];]                                                                                       |
|                                                                                                                                                                                                                |
| [        iData = [Clipboard].GetDataObject();]                                                                                                     |
|                                                                                                                                                                                                                |
| [        [string] buffer = iData.GetData([DataFormats].UnicodeText) [as] [string];] |
|                                                                                                                                                                                                                |
| [        [int] top = rangeList\[0\].Top;]                                                                                                             |
|                                                                                                                                                                                                                |
| [        [int] left = rangeList\[0\].Left;]                                                                                                           |
|                                                                                                                                                                                                                |
| [        [int] right = rangeList\[0\].Right;]                                                                                                         |
|                                                                                                                                                                                                                |
| [        [int] bottom = rangeList\[0\].Bottom;]                                                                                                       |
|                                                                                                                                                                                                                |
| [        [string] stylesheet = [string].Empty;]                                                                                  |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [        [StringBuilder] sb = [new] [StringBuilder]();]                                               |
|                                                                                                                                                                                                                |
| [        GridStyleInfoStore gsis;]                                                                                                                                         |
|                                                                                                                                                                                                                |
| [        GridStyleInfo style;]                                                                                                                                             |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [        sb.Append([\"\<html\>\<body\>\<table border=1\>\"]);]                                                                                     |
|                                                                                                                                                                                                                |
| [        [for] ([int] row = top; row \<= bottom; row++)]                                                                         |
|                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                |
|                                                                                                                                                                                                                |
| [            sb.Append([\"\<tr\>\"]);]                                                                                                             |
|                                                                                                                                                                                                                |
| [            [for] ([int] col = left; col \<= right; col++)]                                                                     |
|                                                                                                                                                                                                                |
| [            {]                                                                                                                                                            |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                gsis = gridData\[row - top, col - left\];]                                                                                                                |
|                                                                                                                                                                                                                |
| [                style = [new] GridStyleInfo(gsis);]                                                                                                  |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                stylesheet = [\"\\\"\"];]                                                                                                         |
|                                                                                                                                                                                                                |
| [                [if] (style.HasBackground)]                                                                                                          |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    [string] backgroundColor = style.Background.ToString();]                                                                         |
|                                                                                                                                                                                                                |
| [                    backgroundColor = backgroundColor.Substring(3, backgroundColor.Length - 3);]                                                                          |
|                                                                                                                                                                                                                |
| [                    stylesheet = [\"\\\"background-color:\"] + backgroundColor;]                                                                  |
|                                                                                                                                                                                                                |
| [                }]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                [if] (style.HasForeground)]                                                                                                          |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    [string] foregroundColor = style.Foreground.ToString();]                                                                         |
|                                                                                                                                                                                                                |
| [                    foregroundColor = foregroundColor.Substring(3, foregroundColor.Length - 3);]                                                                          |
|                                                                                                                                                                                                                |
| [                    stylesheet = stylesheet + [\";color:\"] + foregroundColor;]                                                                   |
|                                                                                                                                                                                                                |
| [                }]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                [if] (style.HasHorizontalAlignment)]                                                                                                 |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    stylesheet = stylesheet + [\";text-align:\"] + style.HorizontalAlignment;]                                                    |
|                                                                                                                                                                                                                |
| [                }]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                [if] (style.HasVerticalAlignment)]                                                                                                   |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    stylesheet = stylesheet + [\";vertical-align:\"] + style.VerticalAlignment;]                                                  |
|                                                                                                                                                                                                                |
| [                }]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                [if] (style.HasBorders)]                                                                                                             |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    [string] borderBrush;]                                                                                                           |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                    borderBrush = style.Borders.Left.Brush.ToString();]                                                                                                   |
|                                                                                                                                                                                                                |
| [                    borderBrush = borderBrush.Substring(3, borderBrush.Length - 3);]                                                                                      |
|                                                                                                                                                                                                                |
| [                    stylesheet = stylesheet + [\";border-left:solid  #\"] + borderBrush;]                                                         |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                    borderBrush = style.Borders.Right.Brush.ToString();]                                                                                                  |
|                                                                                                                                                                                                                |
| [                    borderBrush = borderBrush.Substring(3, borderBrush.Length - 3);]                                                                                      |
|                                                                                                                                                                                                                |
| [                    stylesheet = stylesheet + [\";border-right:solid  #\"] + borderBrush;]                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                    borderBrush = style.Borders.Bottom.Brush.ToString();]                                                                                                 |
|                                                                                                                                                                                                                |
| [                    borderBrush = borderBrush.Substring(3, borderBrush.Length - 3);]                                                                                      |
|                                                                                                                                                                                                                |
| [                    stylesheet = stylesheet + [\";border-bottom:solid  #\"] + borderBrush;]                                                       |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                    borderBrush = style.Borders.Top.Brush.ToString();]                                                                                                    |
|                                                                                                                                                                                                                |
| [                    borderBrush = borderBrush.Substring(3, borderBrush.Length - 3);]                                                                                      |
|                                                                                                                                                                                                                |
| [                    stylesheet = stylesheet + [\";border-top:solid  #\"] + borderBrush;]                                                          |
|                                                                                                                                                                                                                |
| [                }]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                stylesheet = stylesheet + [\"\\\"\"];]                                                                                            |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                [if] (!stylesheet.Equals([\"\\\"\\\"\"]))]                                                                   |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    sb.Append([@\"\<td style=\"] + stylesheet + [\"\>\"]);]                                               |
|                                                                                                                                                                                                                |
| [                }]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                [else]]                                                                                                                              |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    sb.Append([@\"\<td\>\"]);]                                                                                                    |
|                                                                                                                                                                                                                |
| [                }]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                [if] (!style.CellValue.ToString().Equals([\"\"]))]                                                           |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    sb.Append(style.CellValue.ToString());]                                                                                                               |
|                                                                                                                                                                                                                |
| [                }]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                [else]]                                                                                                                              |
|                                                                                                                                                                                                                |
| [                {]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [                    sb.Append([\"\<pre\>       \</pre\>\"]);]                                                                                     |
|                                                                                                                                                                                                                |
| [                }]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [                sb.Append([\"\</td\>\"]);]                                                                                                        |
|                                                                                                                                                                                                                |
| [                stylesheet = [string].Empty;]                                                                                                        |
|                                                                                                                                                                                                                |
| [            }]                                                                                                                                                            |
|                                                                                                                                                                                                                |
| [            sb.Append([\"\</tr\>\"]);]                                                                                                            |
|                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                |
|                                                                                                                                                                                                                |
| [        sb.Append([\"\</table\>\</body\>\</html\>\"]);]                                                                                           |
|                                                                                                                                                                                                                |
| [        [DataObject] dataObject = [new] [DataObject]();]                                             |
|                                                                                                                                                                                                                |
| [        dataObject.SetData([DataFormats].UnicodeText, sb.ToString());]                                                                            |
|                                                                                                                                                                                                                |
| [        [Clipboard].SetDataObject(dataObject);]                                                                                                   |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                    |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [    [public] [void] Cut(GridCellData grodCellData, GridRangeInfoList rangeList)]                                                |
|                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                    |
|                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                    |
|                                                                                                                                                                                                                |
| [    [public] [DataObject] Paste(GridRangeInfoList rangeList)]                                                                |
|                                                                                                                                                                                                                |
| [    {]                                                                                                                                                                    |
|                                                                                                                                                                                                                |
| [        [return] [new] [DataObject]();]                                                                 |
|                                                                                                                                                                                                                |
| [    }]                                                                                                                                                                    |
|                                                                                                                                                                                                                |
| [}]                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The next step is to attach the above custom copy and paste operations to the grid control.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                       |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [HtmlCopy][ htmlCopy = [new] [HtmlCopy]();] |
|                                                                                                                                                                                  |
| [gridControl.Model.GridCopyPaste = htmlCopy;]                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 71: Pasting the grid data in HTML format

 

See Also

 

[ ]{.UGHyperlink}

[]{.UGHyperlink}

[]{.UGHyperlink}

[]{.UGHyperlink}

[]{.UGHyperlink}

[]{.UGHyperlink}

 

 

 

[]{#related-topics}

