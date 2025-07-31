---
title: symbolfilters1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\symbolfilters1.md
created_at: 2025-07-03
---








  









### Symbol Filters {#symbol-filters style="tab-stops: 0pt"}

A SymbolPalette filter can be added to the SymbolPalette control, using the **SymbolFilters** property, so that only desired SymbolPalette groups get displayed. The **SetFilterIndexes** property is used to specify the index value of the filters for which the group is to be displayed. The filter names are specified integer values, with the first filter index starting from 0. Based on the filter indexes specified for that particular group, the visibility of the group is controlled. So the group gets displayed only when any of the specified filter names are selected.

 

The following lines of code can be used to specify the SymbolPalette filter of the SymbolPalette Group.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [SymbolPaletteFilter][ sfilter = [new] [SymbolPaletteFilter]();]                                                                        |
|                                                                                                                                                                                                                                                                              |
| [sfilter.Label = [\"Custom\"];]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [dc.SymbolPalette.SymbolFilters.Add(sfilter);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                              |
| [SymbolPaletteGroup][ group = [new] [SymbolPaletteGroup]();]                                                                            |
|                                                                                                                                                                                                                                                                              |
| [group.Label = [\"Custom\"];]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                              |
| [SymbolPalette][.SetFilterIndexes(group, [new] [Int32Collection]([new] [int]\[\] { 0, 6 }));] |
|                                                                                                                                                                                                                                                                              |
| [dc.SymbolPalette.SymbolGroups.Add(s);]                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [Dim][ sfilter [As] [New] [SymbolPaletteFilter]()] |
|                                                                                                                                                                                                           |
| [sfilter.Label = \"Custom\"]                                                                                                                                          |
|                                                                                                                                                                                                           |
| [dc.SymbolPalette.SymbolFilters.Add(sfilter)]                                                                                                                         |
|                                                                                                                                                                                                           |
| [Dim][ group [As] [New] [SymbolPaletteGroup]()]    |
|                                                                                                                                                                                                           |
| [group][.Label = \"Custom\"]                                                                                         |
|                                                                                                                                                                                                           |
| [SymbolPalette.SetFilterIndexes(group, [New] Int32Collection(New [Integer]() { 0, 6 }))]                                    |
|                                                                                                                                                                                                           |
| [dc.SymbolPalette.SymbolGroups.Add(s)][]                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

This adds a new empty group named \"Custom\" and creates a filter for it.

[] 

{border="0"}

Figure 181: SymbolPalette Filter[]

[] 

The **SetFilterIndexes** property specifies the index value for the group as 0,4 which implies that this group should be displayed when the filter index is 0 (\"All\") or 4 (\"Custom\").

[]{#p95} 

Remove SymbolPaletteFilters[]

Like SymbolPaletteGroups, the SymbolPaletteFilters are also indexed from 0. The index 0 refers to the filter All. The index 1 refers to the filter Shapes and so on. The following table lists the filters with their index numbers.

[] 

Table 81: File Extention


  ------------------- -------
  Filter name         Index
  All                 0
  Shapes              1
  Connectors          2
  Flowchart           3
  Custom Shapes       4
  Electrical Shapes   5
  ------------------- -------


[] 

a\) Removing filters and groups named Shapes, Custom Shapes and Electrical Shapes

**[]** 

Use the following code to remove the filters and groups named Shapes, Custom Shapes and Electrical Shapes:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [DiagramControl][ diagramControl = [new] [DiagramControl]();] |
|                                                                                                                                                                                                    |
| [diagramControl.SymbolPalette.SymbolGroups.Remove(diagramControl.SymbolPalette.SymbolGroups\[4\]);]                                                            |
|                                                                                                                                                                                                    |
| [diagramControl.SymbolPalette.SymbolGroups.Remove(diagramControl.SymbolPalette.SymbolGroups\[3\]);]                                                            |
|                                                                                                                                                                                                    |
| [diagramControl.SymbolPalette.SymbolGroups.Remove(diagramControl.SymbolPalette.SymbolGroups\[0\]);]                                                            |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [diagramControl.SymbolPalette.SymbolFilters.Remove(diagramControl.SymbolPalette.SymbolFilters\[5\]);]                                                          |
|                                                                                                                                                                                                    |
| [diagramControl.SymbolPalette.SymbolFilters.Remove(diagramControl.SymbolPalette.SymbolFilters\[4\]);]                                                          |
|                                                                                                                                                                                                    |
| [diagramControl.SymbolPalette.SymbolFilters.Remove(diagramControl.SymbolPalette.SymbolFilters\[1\]);]                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [Dim][ diagramControl [As] [New] [DiagramControl]()] |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolGroups.Remove(diagramControl.SymbolPalette.SymbolGroups(4))]                                                                        |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolGroups.Remove(diagramControl.SymbolPalette.SymbolGroups(3))]                                                                        |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolGroups.Remove(diagramControl.SymbolPalette.SymbolGroups(0))]                                                                        |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolFilters.Remove(diagramControl.SymbolPalette.SymbolFilters(5))]                                                                      |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolFilters.Remove(diagramControl.SymbolPalette.SymbolFilters(4))]                                                                      |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolFilters.Remove(diagramControl.SymbolPalette.SymbolFilters(1))][]                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the application. The following output is displayed and the groups and filters are removed.

[] 

{border="0"}

Figure 182: Palette with Groups and Filters removed[]

[] 

[]{#related-topics}

