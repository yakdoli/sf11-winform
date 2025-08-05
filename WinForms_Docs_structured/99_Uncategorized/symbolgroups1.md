---
title: symbolgroups1.md
original_path: WinForms_Docs/99_Uncategorized/symbolgroups1.md
created_at: 2025-08-05
---








  









### Symbol Groups {#symbol-groups style="tab-stops: 0pt"}

A SymbolPalette group is a collection of SymbolPalette items. It is used to group the items in the SymbolPalette control based on classifications provided. The SymbolPalette group can be added to the SymbolPalette using the **SymbolGroups** property.  The filter index for the new groups should always start from 6 as the first five indices are predefined for the existing groups.

 

Use the following code to add a group to SymbolPalette:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[ ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [SymbolPaletteGroup][ s = [new] [SymbolPaletteGroup]();]                                                                            |
|                                                                                                                                                                                                                                                                          |
| [s.Label = [\"Custom\"];]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                          |
| [SymbolPalette][.SetFilterIndexes(s, [new] [Int32Collection]([new] [int]\[\] { 0, 6 }));] |
|                                                                                                                                                                                                                                                                          |
| [diagramControl.SymbolPalette.SymbolGroups.Add(s);]                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[ ]                                                                                              |
|                                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                                    |
| [Dim][ s [As] [New] [SymbolPaletteGroup]()] |
|                                                                                                                                                                                                    |
| [s.Label = \"Custom\"]                                                                                                                                         |
|                                                                                                                                                                                                    |
| [SymbolPalette.SetFilterIndexes(s, [New] Int32Collection(New [Integer]() { 0, 6 }))]                                 |
|                                                                                                                                                                                                    |
| [diagramControl.SymbolPalette.SymbolGroups.Add(s)][]                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the application. A new empty group named Custom is added to the SymbolPalette.

 

[]{#p96} 

Remove SymbolPaletteGroups[]

The SymbolPaletteGroups are indexed from 0. Therefore, the group with name Shapes is indexed as 0, the group with name Connectors is indexed as 1 and so on. The groups can be removed using their corresponding index values. The following table lists the groups with their index numbers.

[] 

Table 82: Symbol Palette Groups index value


  ------------------- -------
  Group Name          Index
  Shapes              0
  Connectors          1
  Flowchart           2
  Custom Shapes       3
  Electrical Shapes   4
  ------------------- -------


[] 

a\) Removing filter and group named Electrical Shapes and refreshing the Filters.

**[]** 

Use the following code to remove the filter and group named Electrical Shapes:

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [DiagramControl][ diagramControl = [new] [DiagramControl]();]                        |
|                                                                                                                                                                                                                           |
| [diagramControl.SymbolPalette.SymbolGroups.Remove(diagramControl.SymbolPalette.SymbolGroups\[4\]);]                                                                                   |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [diagramControl.SymbolPalette.SymbolFilters.Remove(diagramControl.SymbolPalette.SymbolFilters\[5\]);]                                                                                 |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [//Refreshing the filters][]                                                                                                        |
|                                                                                                                                                                                                                           |
| [foreach][ ([SymbolPaletteGroup] group [in] diagramControl.SymbolPalette.SymbolGroups)] |
|                                                                                                                                                                                                                           |
| [            {]                                                                                                                                                                       |
|                                                                                                                                                                                                                           |
| [                [Int32Collection] indices = [SymbolPalette].GetFilterIndexes(group);]                                                |
|                                                                                                                                                                                                                           |
| [                [if] (indices.Contains(5))]                                                                                                                     |
|                                                                                                                                                                                                                           |
| [                {]                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [                    indices.Remove(5);]                                                                                                                                              |
|                                                                                                                                                                                                                           |
| [                    [SymbolPalette].SetFilterIndexes(group, indices);]                                                                                       |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [                }]                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [                [if] (indices.Contains(6))]                                                                                                                     |
|                                                                                                                                                                                                                           |
| [                {]                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [                    indices.Remove(6);]                                                                                                                                              |
|                                                                                                                                                                                                                           |
| [                    indices.Add(5);]                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [                    [SymbolPalette].SetFilterIndexes(group, indices);]                                                                                       |
|                                                                                                                                                                                                                           |
| [                }]                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [            }]                                                                                                                                                                       |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [Dim][ diagramControl [As] [New] [DiagramControl]()]                                                            |
|                                                                                                                                                                                                                                                                        |
| [diagramControl.SymbolPalette.SymbolGroups.Remove(diagramControl.SymbolPalette.SymbolGroups(4))]                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [diagramControl.SymbolPalette.SymbolFilters.Remove(diagramControl.SymbolPalette.SymbolFilters(5))]                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [\'Refreshing the filters][]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| [For][ [Each] [group] [As] SymbolPaletteGroup [In] diagramControl.SymbolPalette.SymbolGroups] |
|                                                                                                                                                                                                                                                                        |
| [        [Dim] indices [As] [Int32Collection] = [SymbolPalette].GetFilterIndexes(Group)]                                                 |
|                                                                                                                                                                                                                                                                        |
| [                  [If] indices.Contains(5) [Then]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                        |
| [                        indices.Remove(5)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [                        SymbolPalette.SetFilterIndexes(group, indices)]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [                  [End] [If]]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [                  [If] indices.Contains(6) [Then]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                        |
| [                        indices.Remove(6)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                        |
| [                        indices.Add(5)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [                        SymbolPalette.SetFilterIndexes(group, indices)]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [                  [End] [If]]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [Next][ [group]][]                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the application. The following output is displayed and the groups and filters are removed.

[] 

{border="0"}

Figure 183: Palette with Groups and Filters removed[]

***[]*** 

***[]*** 


{border="0"}Note: Whenever a filter is removed the group containing the next filter index must be decremented by one to get the proper output as mentioned in the above code snippet.


 

b\) Removing all the groups from the palette

**[]** 

To remove all the groups from the palette, the Clear method can be used. The following code illustrates the usage of Clear method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [DiagramControl][ diagramControl = [new] [DiagramControl]();] |
|                                                                                                                                                                                                    |
| [diagramControl.SymbolPalette.SymbolGroups.Clear();]                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [Dim][ diagramControl [As] [New] [DiagramControl]()] |
|                                                                                                                                                                                                             |
| [diagramControl.SymbolPalette.SymbolGroups.Clear()][]                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Run the application. All the groups are removed from the SymbolPalette.

 

[]{#related-topics}

