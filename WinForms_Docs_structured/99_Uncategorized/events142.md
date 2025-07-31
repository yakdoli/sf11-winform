---
title: events142.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\events142.md
created_at: 2025-07-03
---






#### Events {#events style="tab-stops: 0pt"}

The **Hyperlink Cell Click** event can be tagged in the following ways:

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                              |
| [// Tag Hyperlink Cell Click Event.]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [this][.OlapGrid1.HyperlinkCellClick += [new] [OlapGrid].[RaiseHyperlinkCellClick](OlapGrid1_HyperlinkCellClick);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                       |
| [\'Tag Hyperlink Cell Click Event.][]                                                                                           |
|                                                                                                                                                                                                                       |
| [Me][.OlapGrid1.HyperlinkCellClick += [New] OlapGrid.RaiseHyperlinkCellClick(OlapGrid1_HyperlinkCellClick)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The **HyperlinkCellClickArg**[ ]argument will return the clicked cell descriptor.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                     |
| [void][ OlapGrid1_HyperlinkCellClick([object] sender, [HyperlinkCellClickArg] e)] |
|                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| [   [string] uniqueName = e.PivotCellDescriptor.UniqueName;     ]                                                                                          |
|                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] OlapGrid1_HyperlinkCellClick([ByVal] sender [As] [Object], [ByVal] e [As] HyperlinkCellClickArg)] |
|                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ uniqueName [As] [String] = e.PivotCellDescriptor.UniqueName]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 17: OLAP Grid with Hyperlinked Column Header

[] 

{border="0"}

Figure 18: OLAP Grid with Hyperlinked Row Header

 

{border="0"}

Figure 19: OLAP Grid with Hyperlinked Value Cell

 

Table 8: Properties


  ----------------------------- ---------------------------------------------------------------- ------------- -----------
  Property                      Description                                                      Type          Data Type
  EnableHyperLinkColumnHeader   Gets or sets to enable or disable the Hyperlink Column Header.   Server side   boolean
  EnableHyperLinkRowHeader      Gets or sets to enable or disable the Hyperlink Row Header.      Server side   boolean
  EnableHyperLinkValueCell      Gets or sets to enable or disable the Hyperlink Value Cell.      Server side   boolean
  ----------------------------- ---------------------------------------------------------------- ------------- -----------


 

Table 9: HyperlinkCellClick Event


+--------------------+----------------------------------------------------------------+---------------------+-----------------------+
|                    |                                                                |                     |                       |
|                    |                                                                |                     |                       |
| Event              | Description                                                    | Arguments           |  Type                 |
|                    |                                                                |                     |                       |
|                    |                                                                |                     |                       |
+--------------------+----------------------------------------------------------------+---------------------+-----------------------+
| HyperlinkCellClick | Handles the Hyperlink Cell Click event of the OlapGrid control | PivotCellDescriptor | HyperlinkCellClickArg |
+--------------------+----------------------------------------------------------------+---------------------+-----------------------+


 

Sample Location

A sample demo is available in the following location:

**..\\Syncfusion\\EssentialStudio\\\<VersionNumber\>\\BI\\Web\\OlapGrid.Web\\Samples\\3.5\\Hyperlink Cells\\Hyperlink Cells Demo**

 

[]{#related-topics}

