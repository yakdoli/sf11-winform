---
title: howtochangetheselectionmodeoftheselecttool.md
original_path: WinForms_Docs/99_Uncategorized/howtochangetheselectionmodeoftheselecttool.md
created_at: 2025-08-05
---








  









## How to Change the Selection Mode of the SelectTool {#how-to-change-the-selection-mode-of-the-selecttool style="tab-stops: 0pt"}

The Diagram SelectTool provides an enum property called *SelectMode*, to change the selection mode. The following are the supported selection modes:

[·      ]**Containing** - Specific objects that are fully enveloped by the tracking rectangle will be selected by the tool.

[·      ]**Intersecting** - Specific objects that are intersecting the tracking rectangle will be selected by the tool.

 

Containing is the default selection mode.

The following code snippet illustrates how to change the selection mode at runtime:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                             |
| [(([DiagramViewerEventSink])diagram1.EventSink).ToolActivated += [new] [ToolEventHandler](Diagram_ToolActivated);] |
|                                                                                                                                                                                                                             |
| [private][ [void] Diagram_ToolActivated([ToolEventArgs] evtArgs)]                         |
|                                                                                                                                                                                                                             |
| [        {]                                                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [            [if] (evtArgs.Tool [is] [SelectTool])]                                                                   |
|                                                                                                                                                                                                                             |
| [            {]                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [                [//change the SelectionMode as \"Intersecting\" which Specifies that objects intersecting the tracking rectangle will be selected by the tool.]] |
|                                                                                                                                                                                                                             |
| [                (([SelectTool])evtArgs.Tool).SelectMode = [SelectMode].Intersecting;]                                                  |
|                                                                                                                                                                                                                             |
| [            }]                                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [        }]                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                |
| [AddHandler][ ([CType](Diagram1.EventSink, DiagramViewerEventSink)).ToolActivated, [AddressOf] Diagram_ToolActivated]**[]** |
|                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] Diagram_ToolActivated([ByVal] evtArgs [As] ToolEventArgs)]                                                                |
|                                                                                                                                                                                                                                                                                                |
| [        [If] [TypeOf] evtArgs.Tool [Is] SelectTool [Then]]                                                                                                            |
|                                                                                                                                                                                                                                                                                                |
| [            [\'change the SelectionMode as \"Intersecting\" which Specifies that objects intersecting the tracking rectangle will be selected by the tool. ]]                                                                       |
|                                                                                                                                                                                                                                                                                                |
| [            [CType](evtArgs.Tool, SelectTool).SelectMode = SelectMode.Intersecting]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| [        [End] [If]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                |
| [    [End] [Sub]]**[]**                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

 

[]{#related-topics}

