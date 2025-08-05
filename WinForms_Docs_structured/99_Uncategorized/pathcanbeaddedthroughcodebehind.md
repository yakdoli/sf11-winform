---
title: pathcanbeaddedthroughcodebehind.md
original_path: WinForms_Docs/99_Uncategorized/pathcanbeaddedthroughcodebehind.md
created_at: 2025-08-05
---






#### Path can be added through Code Behind {#path-can-be-added-through-code-behind style="tab-stops: 0pt"}

Run the Application, the Path will be displayed.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [           ]                                                                                                                                              |
|                                                                                                                                                                                                |
| [    \[C#\]]                                                                                                                                               |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [                [MapPath] path = [new] [MapPath]();]                                 |
|                                                                                                                                                                                                |
| [                path.PathPoints.Add(([new] [Point] { X = -68, Y = -24 }));]                                  |
|                                                                                                                                                                                                |
| [                path.PathPoints.Add(([new] [Point] { X = 98, Y = 40 }));]                                    |
|                                                                                                                                                                                                |
| [                path.PathPoints.Add(([new] [Point] { X = 34, Y = 62 }));]                                    |
|                                                                                                                                                                                                |
| [                path.PathPoints.Add(([new] [Point] { X = -101, Y = 59 }));]                                  |
|                                                                                                                                                                                                |
| [                path.LabelPoint = [new] [Point] { X = 98, Y = 40 };]                                         |
|                                                                                                                                                                                                |
| [                path.PathLabel = [\"MapPAth\"];]                                                                                  |
|                                                                                                                                                                                                |
| [                path.PathLabelPosition = [PathLabelPosition].OnMiddlePoint;]                                                      |
|                                                                                                                                                                                                |
| [                path.PathColor = [new] [SolidColorBrush]([Colors].Black);]           |
|                                                                                                                                                                                                |
| [                path.PathLabelForeground = [new] [SolidColorBrush]([Colors].Black);] |
|                                                                                                                                                                                                |
| [                shapeControl.MapPathCollection.Add(path);              ]                                                                                  |
|                                                                                                                                                                                                |
| [            ]                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

