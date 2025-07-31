---
title: addingapathassymbolpaletteitem.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingapathassymbolpaletteitem.md
created_at: 2025-07-03
---






#### Adding a path as SymbolPaletteItem {#adding-a-path-as-symbolpaletteitem style="tab-stops: 0pt"}

[] 

To give a path as **SymbolPaletteItem** you can either create a **PathGeometry** in code behind or set the Data property of the path to **PathData** property.

[] 

a)   The following code illustrates the adding of the path as **SymbolPaletteItem** using mini language geometry.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [// Adding Group in SymbolPalette]                                                                                                              |
|                                                                                                                                                                                                   |
| [SymbolPaletteGroup][ group = [new] [SymbolPaletteGroup]();] |
|                                                                                                                                                                                                   |
| [            group.HeaderName = [\"Shapes\"];            diagramControl.SymbolPalette.SymbolGroups.Add(group);]                       |
|                                                                                                                                                                                                   |
| [//Adding a SymbolPaletteItem]                                                                                                                  |
|                                                                                                                                                                                                   |
| [SymbolPaletteItem][ item1 = [new] [SymbolPaletteItem]();]   |
|                                                                                                                                                                                                   |
| [            item1.Width = 50;]                                                                                                                               |
|                                                                                                                                                                                                   |
| [            item1.Height = 50;]                                                                                                                              |
|                                                                                                                                                                                                   |
| [            item1.Name = [\"item1\"];]                                                                                               |
|                                                                                                                                                                                                   |
| [//Initialising Path]                                                                                                                           |
|                                                                                                                                                                                                   |
| [            [Path] path1 = [new] [Path]();]                                             |
|                                                                                                                                                                                                   |
| [            path1.Height = 40;]                                                                                                                              |
|                                                                                                                                                                                                   |
| [            path1.Width = 40;]                                                                                                                               |
|                                                                                                                                                                                                   |
| [            path1.Fill = [new] [SolidColorBrush]([Colors].Blue);]                       |
|                                                                                                                                                                                                   |
| [            path1.Stretch = [Stretch].Fill;]                                                                                         |
|                                                                                                                                                                                                   |
| [            path1.Stroke = [new] [SolidColorBrush]([Colors].Red);]                      |
|                                                                                                                                                                                                   |
| [            path1.StrokeThickness = 1;]                                                                                                                      |
|                                                                                                                                                                                                   |
| [            path1.Margin = [new] [Thickness](3);]                                                               |
|                                                                                                                                                                                                   |
| [//setting the path geometry to PathData]                                                                                                       |
|                                                                                                                                                                                                   |
| [            item1.PathData = [\"M200,239L200,200 240,239 280,202 320,238 281,279 240,244 198,279z\"];]                               |
|                                                                                                                                                                                                   |
| [//setting path as content of SymbolPaletteItem]                                                                                                |
|                                                                                                                                                                                                   |
| [            item1.Content = path1;]                                                                                                                          |
|                                                                                                                                                                                                   |
| [            group.Items.Add(item1);]                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [\'Adding Group in SymbolPalette][]                                                     |
|                                                                                                                                                                               |
| [ [Dim] group [As] [New] [SymbolPaletteGroup]()]   |
|                                                                                                                                                                               |
| [                  [group].HeaderName = \"Shapes\"]                                                                  |
|                                                                                                                                                                               |
| [                  diagramControl.SymbolPalette.SymbolGroups.Add(group)]                                                                  |
|                                                                                                                                                                               |
| [    [\'Adding a SymbolPaletteItem]]                                                                                |
|                                                                                                                                                                               |
| [    [Dim] item1 [As] [New] [SymbolPaletteItem]()] |
|                                                                                                                                                                               |
| [                  item1.Width = 50]                                                                                                      |
|                                                                                                                                                                               |
| [                  item1.Height = 50]                                                                                                     |
|                                                                                                                                                                               |
| [                  item1.Name = \"item1\"]                                                                                                |
|                                                                                                                                                                               |
| [    [\'Initialising Path]]                                                                                         |
|                                                                                                                                                                               |
| [    [Dim] path1 [As] [New] [Path]()]              |
|                                                                                                                                                                               |
| [                  path1.Height = 40]                                                                                                     |
|                                                                                                                                                                               |
| [                  path1.Width = 40]                                                                                                      |
|                                                                                                                                                                               |
| [                  path1.Fill = [New] SolidColorBrush(Colors.Blue)]                                                  |
|                                                                                                                                                                               |
| [                  path1.Stretch = Stretch.Fill]                                                                                          |
|                                                                                                                                                                               |
| [                  path1.Stroke = [New] SolidColorBrush(Colors.Red)]                                                 |
|                                                                                                                                                                               |
| [                  path1.StrokeThickness = 1]                                                                                             |
|                                                                                                                                                                               |
| [                  path1.Margin = [New] Thickness(3)]                                                                |
|                                                                                                                                                                               |
| [    [\'setting the path geometry to PathData]]                                                                     |
|                                                                                                                                                                               |
| [                  item1.PathData = \"M200,239L200,200 240,239 280,202 320,238 281,279 240,244 198,279z\"]                                |
|                                                                                                                                                                               |
| [    [\'setting path as content of SymbolPaletteItem]]                                                              |
|                                                                                                                                                                               |
| [                  item1.Content = path1]                                                                                                 |
|                                                                                                                                                                               |
| [                  [group].Items.Add(item1)][]                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

b)   The following code illustrates the adding of path using Path Geometry.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [// Adding Group in SymbolPalette]                                                                                                              |
|                                                                                                                                                                                                   |
| [SymbolPaletteGroup][ group = [new] [SymbolPaletteGroup]();] |
|                                                                                                                                                                                                   |
| [            group.HeaderName = [\"Shapes\"];]                                                                                        |
|                                                                                                                                                                                                   |
| [            diagramControl.SymbolPalette.SymbolGroups.Add(group);]                                                                                           |
|                                                                                                                                                                                                   |
| [//Adding a SymbolPaletteItem]                                                                                                                  |
|                                                                                                                                                                                                   |
| [            [SymbolPaletteItem] item = [new] [SymbolPaletteItem]();]                    |
|                                                                                                                                                                                                   |
| [            item.Width = 50;]                                                                                                                                |
|                                                                                                                                                                                                   |
| [            item.Height = 50;]                                                                                                                               |
|                                                                                                                                                                                                   |
| [            item.Name = [\"item\"];]                                                                                                 |
|                                                                                                                                                                                                   |
| [//Initialising a Path]                                                                                                                         |
|                                                                                                                                                                                                   |
| [            [Path] path = [new] [Path]();]                                              |
|                                                                                                                                                                                                   |
| [//Initialising a PathGeometry]                                                                                                                 |
|                                                                                                                                                                                                   |
| [            [PathGeometry] geo = [new] [PathGeometry]();]                               |
|                                                                                                                                                                                                   |
| [            [PathFigure] pathfig = [new] [PathFigure]();]                               |
|                                                                                                                                                                                                   |
| [            pathfig.StartPoint = [new] [Point](0, 0);]                                                          |
|                                                                                                                                                                                                   |
| [//Adding line segments to path figure]                                                                                                         |
|                                                                                                                                                                                                   |
| [            [LineSegment] line = [new] [LineSegment]();]                                |
|                                                                                                                                                                                                   |
| [            line.Point = [new] [Point](-3, -7);]                                                                |
|                                                                                                                                                                                                   |
| [            pathfig.Segments.Add(line);]                                                                                                                     |
|                                                                                                                                                                                                   |
| [            line = [new] [LineSegment]();]                                                                      |
|                                                                                                                                                                                                   |
| [            line.Point = [new] [Point](-3, -15);]                                                               |
|                                                                                                                                                                                                   |
| [            pathfig.Segments.Add(line);]                                                                                                                     |
|                                                                                                                                                                                                   |
| [            line = [new] [LineSegment]();]                                                                      |
|                                                                                                                                                                                                   |
| [            line.Point = [new] [Point](3, -15);]                                                                |
|                                                                                                                                                                                                   |
| [            pathfig.Segments.Add(line);]                                                                                                                     |
|                                                                                                                                                                                                   |
| [            line = [new] [LineSegment]();]                                                                      |
|                                                                                                                                                                                                   |
| [            line.Point = [new] [Point](3, -7);]                                                                 |
|                                                                                                                                                                                                   |
| [            pathfig.Segments.Add(line);]                                                                                                                     |
|                                                                                                                                                                                                   |
| [            pathfig.IsClosed = [true];]                                                                                                 |
|                                                                                                                                                                                                   |
| [            geo.Figures.Add(pathfig);]                                                                                                                       |
|                                                                                                                                                                                                   |
| [            path.Data = geo;]                                                                                                                                |
|                                                                                                                                                                                                   |
| [            path.Height = 40;]                                                                                                                               |
|                                                                                                                                                                                                   |
| [            path.Width = 40;]                                                                                                                                |
|                                                                                                                                                                                                   |
| [            path.Fill = [new] [SolidColorBrush]([Colors].Red);]                         |
|                                                                                                                                                                                                   |
| [            path.Stretch = [Stretch].Fill;]                                                                                          |
|                                                                                                                                                                                                   |
| [            path.Stroke = [new] [SolidColorBrush]([Colors].Blue);]                      |
|                                                                                                                                                                                                   |
| [            path.StrokeThickness = 1;]                                                                                                                       |
|                                                                                                                                                                                                   |
| [            path.Margin = [new] [Thickness](3);]                                                                |
|                                                                                                                                                                                                   |
| [//setting path as the content of SymbolPaletteItem]                                                                                            |
|                                                                                                                                                                                                   |
| [            item.Content = path;]                                                                                                                            |
|                                                                                                                                                                                                   |
| [            group.Items.Add(item);]                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [   \'Adding Group in SymbolPalette][]                                                   |
|                                                                                                                                                                                |
| [    [Dim] group [As] [New] [SymbolPaletteGroup]()] |
|                                                                                                                                                                                |
| [                  [group].HeaderName = \"Shapes\"]                                                                   |
|                                                                                                                                                                                |
| [                  diagramControl.SymbolPalette.SymbolGroups.Add(group)]                                                                   |
|                                                                                                                                                                                |
| [    [\'Adding a SymbolPaletteItem]]                                                                                 |
|                                                                                                                                                                                |
| [    [Dim] item [As] [New] [SymbolPaletteItem]()]   |
|                                                                                                                                                                                |
| [                  item.Width = 50]                                                                                                        |
|                                                                                                                                                                                |
| [                  item.Height = 50]                                                                                                       |
|                                                                                                                                                                                |
| [                  item.Name = \"item\"]                                                                                                   |
|                                                                                                                                                                                |
| [    [\'Initialising a Path]]                                                                                        |
|                                                                                                                                                                                |
| [    [Dim] path [As] [New] [Path]()]                |
|                                                                                                                                                                                |
| [    [\'Initialising a PathGeometry]]                                                                                |
|                                                                                                                                                                                |
| [    [Dim] geo [As] [New] [PathGeometry]()]         |
|                                                                                                                                                                                |
| [    [Dim] pathfig [As] [New] [PathFigure]()]       |
|                                                                                                                                                                                |
| [                  pathfig.StartPoint = [New] Point(0, 0)]                                                            |
|                                                                                                                                                                                |
| [    [\'Adding line segments to path figure]]                                                                        |
|                                                                                                                                                                                |
| [    [Dim] line [As] [New] [LineSegment]()]         |
|                                                                                                                                                                                |
| [                  line.Point = [New] Point(-3, -7)]                                                                  |
|                                                                                                                                                                                |
| [                  pathfig.Segments.Add(line)]                                                                                             |
|                                                                                                                                                                                |
| [                  line = [New] LineSegment()]                                                                        |
|                                                                                                                                                                                |
| [                  line.Point = [New] Point(-3, -15)]                                                                 |
|                                                                                                                                                                                |
| [                  pathfig.Segments.Add(line)]                                                                                             |
|                                                                                                                                                                                |
| [                  line = [New] LineSegment()]                                                                        |
|                                                                                                                                                                                |
| [                  line.Point = [New] Point(3, -15)]                                                                  |
|                                                                                                                                                                                |
| [                  pathfig.Segments.Add(line)]                                                                                             |
|                                                                                                                                                                                |
| [                  line = [New] LineSegment()]                                                                        |
|                                                                                                                                                                                |
| [                  line.Point = [New] Point(3, -7)]                                                                   |
|                                                                                                                                                                                |
| [                  pathfig.Segments.Add(line)]                                                                                             |
|                                                                                                                                                                                |
| [                  pathfig.IsClosed = [True]]                                                                         |
|                                                                                                                                                                                |
| [                  geo.Figures.Add(pathfig)]                                                                                               |
|                                                                                                                                                                                |
| [                  path.Data = geo]                                                                                                        |
|                                                                                                                                                                                |
| [                  path.Height = 40]                                                                                                       |
|                                                                                                                                                                                |
| [                  path.Width = 40]                                                                                                        |
|                                                                                                                                                                                |
| [                  path.Fill = [New] SolidColorBrush(Colors.Red)]                                                     |
|                                                                                                                                                                                |
| [                  path.Stretch = Stretch.Fill]                                                                                            |
|                                                                                                                                                                                |
| [                  path.Stroke = [New] SolidColorBrush(Colors.Blue)]                                                  |
|                                                                                                                                                                                |
| [                  path.StrokeThickness = 1]                                                                                               |
|                                                                                                                                                                                |
| [                  path.Margin = [New] Thickness(3)]                                                                  |
|                                                                                                                                                                                |
| [    [\'setting path as the content of SymbolPaletteItem]]                                                           |
|                                                                                                                                                                                |
| [                  item.Content = path]                                                                                                    |
|                                                                                                                                                                                |
| [                  [group].Items.Add(item)][]                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[]{#p97} 

[]{#related-topics}

