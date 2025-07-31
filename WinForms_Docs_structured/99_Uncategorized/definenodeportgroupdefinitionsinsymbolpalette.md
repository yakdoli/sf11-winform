---
title: definenodeportgroupdefinitionsinsymbolpalette.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definenodeportgroupdefinitionsinsymbolpalette.md
created_at: 2025-07-03
---






#### Define Node, Port, Group definitions in SymbolPalette {#define-node-port-group-definitions-in-symbolpalette style="tab-stops: 0pt"}

The following steps demonstrate how to specify a Node or Node with Port in SymbolPaletteItem:

1.   To add more than one port, a node is created.

2.   Then several ports are added to it.

3.   Create a SymbolPaletteItem and add the node as content for the SymbolPaletteItem.

At runtime, Nodes that are added in the SymbolPalette can be dragged and dropped on the page. All the ports, and their properties will cloned and a new copy of the node will be created.

{border="0"}

Figure 154: Node with several Ports

To Create a new Node

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Node][ node = [new] [Node]();]             |
|                                                                                                                                                                                  |
| [            node.Width = 100;]                                                                                                              |
|                                                                                                                                                                                  |
| [            node.Height = 100;]                                                                                                             |
|                                                                                                                                                                                  |
| [            node.OffsetX = 200;]                                                                                                            |
|                                                                                                                                                                                  |
| [            node.OffsetY = 200;]                                                                                                            |
|                                                                                                                                                                                  |
| [            node.Background = [new] [SolidColorBrush]([Colors].Aqua);] |
|                                                                                                                                                                                  |
| [            AddMorePorts(node);]                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

To add more Ports

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [private][ [void] AddMorePorts([Node] node)] |
|                                                                                                                                                                                |
| [        {]                                                                                                                                |
|                                                                                                                                                                                |
| [            Left=10;]                                                                                                                     |
|                                                                                                                                                                                |
| [            Top=10;]                                                                                                                      |
|                                                                                                                                                                                |
| [            [for] ([int] i = 0; i \< 4; i++)]                                                   |
|                                                                                                                                                                                |
| [            {]                                                                                                                            |
|                                                                                                                                                                                |
| [                [ConnectionPort] port = [new] [ConnectionPort]();]   |
|                                                                                                                                                                                |
| [                port.Left = Left;]                                                                                                        |
|                                                                                                                                                                                |
| [                port.Top = Top;]                                                                                                          |
|                                                                                                                                                                                |
| [                port.Node = node;]                                                                                                        |
|                                                                                                                                                                                |
| [                node.Ports.Add(port);]                                                                                                    |
|                                                                                                                                                                                |
| [                Left += 10;]                                                                                                              |
|                                                                                                                                                                                |
| [                Top += 10;]                                                                                                               |
|                                                                                                                                                                                |
| [            }]                                                                                                                            |
|                                                                                                                                                                                |
| [        }]                                                                                                                                |
|                                                                                                                                                                                |
| []                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Creating Groups and SymbolPaletteItems

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [SymbolPaletteGroup][ group = ][new][ ][SymbolPaletteGroup][();]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [group.Label = ][\"Custom\"][;]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [SymbolPalette][.SetFilterIndexes(group, ][new][ ][List][\<][[int]]{.apple-style-span}[\>[(])[\[\] { 0, 6 }));]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [dc.SymbolPalette.SymbolGroups.Add(group);]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [[SymbolPaletteItem]]{.apple-style-span}[[ ]]{.apple-converted-space}[[item =]]{.apple-style-span}[[ ]]{.apple-converted-space}[[new]]{.apple-style-span}[[ ]]{.apple-converted-space}[[SymbolPaletteItem]]{.apple-style-span}[[();]]{.apple-style-span}[ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [[// Node added as SymbolPaletteItem\'s Content]]{.apple-style-span}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [item.Content =][ node[ ;]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [group.Items.Add(item);]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

More:





