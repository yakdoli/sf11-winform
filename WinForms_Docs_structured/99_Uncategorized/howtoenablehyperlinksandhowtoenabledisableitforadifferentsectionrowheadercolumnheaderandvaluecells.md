---
title: howtoenablehyperlinksandhowtoenabledisableitforadifferentsectionrowheadercolumnheaderandvaluecells.md
original_path: WinForms_Docs/99_Uncategorized/howtoenablehyperlinksandhowtoenabledisableitforadifferentsectionrowheadercolumnheaderandvaluecells.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## How to enable hyper-links and how to enable/disable it for a different section (row header, column header and value cells)? {#how-to-enable-hyper-links-and-how-to-enabledisable-it-for-a-different-section-row-header-column-header-and-value-cells style="tab-stops: 0pt"}

Hyperlinks can be enabled by the following property of OlapGrid:

+--------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                 |
|                                                                                                        |
|                                                                                                        |
|                                                                                                        |
| [// To Enable Hyperlink for Column Header] []               |
|                                                                                                        |
| [this].OlapGrid1.ColumnHeaderStyle.IsHyperlinkCell = [true]; |
|                                                                                                        |
| [// To Enable Hyperlink for Row Header]                                          |
|                                                                                                        |
| [this].OlapGrid1.RowHeaderStyle.IsHyperlinkCell = [true];    |
|                                                                                                        |
| [// To Enable Hyperlink for Value Cell]                                          |
|                                                                                                        |
| [this].OlapGrid1.ValueCellStyle.IsHyperlinkCell = [true];    |
|                                                                                                        |
|                                                                                                        |
+--------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------+
| \[VB\]                                                                                              |
|                                                                                                     |
|                                                                                                     |
|                                                                                                     |
| [\' To Enable Hyperlink for Column Header]                                    |
|                                                                                                     |
| [Me].OlapGrid1.ColumnHeaderStyle.IsHyperlinkCell = [True] |
|                                                                                                     |
| [\' To Enable Hyperlink for Row Header]                                       |
|                                                                                                     |
| [Me].OlapGrid1.RowHeaderStyle.IsHyperlinkCell = [True]    |
|                                                                                                     |
| [\' To Enable Hyperlink for Value Cell]                                       |
|                                                                                                     |
| [Me].OlapGrid1.ValueCellStyle.IsHyperlinkCell = [True]    |
|                                                                                                     |
|                                                                                                     |
+-----------------------------------------------------------------------------------------------------+

[] 

Hyperlink can be disabled by setting the following property of OlapGrid to false

+---------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                  |
|                                                                                                         |
|                                                                                                         |
|                                                                                                         |
| [// To Disable Hyperlink for Column Header] []               |
|                                                                                                         |
| [this].OlapGrid1.ColumnHeaderStyle.IsHyperlinkCell = [false]; |
|                                                                                                         |
| [// To Disable Hyperlink for Row Header]                                          |
|                                                                                                         |
| [this].OlapGrid1.RowHeaderStyle.IsHyperlinkCell = [false];    |
|                                                                                                         |
| [// To Disable Hyperlink for Value Cell]                                          |
|                                                                                                         |
| [this].OlapGrid1.ValueCellStyle.IsHyperlinkCell = [false];    |
|                                                                                                         |
|                                                                                                         |
+---------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------+
| \[VB\]                                                                                               |
|                                                                                                      |
|                                                                                                      |
|                                                                                                      |
| [\' To Disable Hyperlink for Column Header]                                    |
|                                                                                                      |
| [Me].OlapGrid1.ColumnHeaderStyle.IsHyperlinkCell = [False] |
|                                                                                                      |
| [\' To Disable Hyperlink for Row Header]                                       |
|                                                                                                      |
| [Me].OlapGrid1.RowHeaderStyle.IsHyperlinkCell = [False]    |
|                                                                                                      |
| [\' To Disable Hyperlink for Value Cell]                                       |
|                                                                                                      |
| [Me].OlapGrid1.ValueCellStyle.IsHyperlinkCell = [False]    |
|                                                                                                      |
|                                                                                                      |
+------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

