---
title: howtogettheclickedcellinfohyperlinkfeature.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\howtogettheclickedcellinfohyperlinkfeature.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## How to get the clicked cell info (Hyperlink feature)? {#how-to-get-the-clicked-cell-info-hyperlink-feature style="tab-stops: 0pt"}

The Hyperlink Click event can be tagged by the following way:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                               |
|                                                                                                                                                                                      |
|                                                                                                                                                                                      |
|                                                                                                                                                                                      |
| [// Tag Hyperlink Cell Click Event]                                                                                                                            |
|                                                                                                                                                                                      |
| [this].OlapGrid1.LinkClick += [new] Syncfusion.Windows.Grid.Olap.[LinkLabelClickEventHander](OlapGrid1_LinkClick); |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[VB\]                                                                                                                                                                           |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
| [\' Tag Hyperlink Cell Click Event]                                                                                                                        |
|                                                                                                                                                                                  |
| [Me].OlapGrid1.LinkClick += [New] Syncfusion.Windows.Grid.Olap.[LinkLabelClickEventHander](OlapGrid1_LinkClick); |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The HyperlinkCellClickArg event will return the clicked Cell Descriptor.

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                            |
|                                                                                                                                                   |
|                                                                                                                                                   |
|                                                                                                                                                   |
| [void] OlapGrid1_HyperlinkCellClick([object] sender, [HyperlinkCellClickArg] e) |
|                                                                                                                                                   |
| {                                                                                                                                                 |
|                                                                                                                                                   |
|                                                                                                                                                   |
|                                                                                                                                                   |
| }                                                                                                                                                 |
|                                                                                                                                                   |
|                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[VB\]\                                                                                                                                                                                                                                                            |
| \                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                    |
| [Private] [Sub] OlapGrid1_HyperlinkCellClick([ByVal] sender [As][Object], [ByVal] e [As] HyperlinkCellClickArg) |
|                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                    |
| [End] [Sub]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

