---
title: previewforsymbolpaletteitem1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\previewforsymbolpaletteitem1.md
created_at: 2025-07-03
---








  









### Preview for Symbol Palette Item {#preview-for-symbol-palette-item style="LINE-HEIGHT: 115%; TEXT-INDENT: -21.6pt; MARGIN: 24pt 0pt 0pt 21.6pt; tab-stops: 21.6pt"}

Essential Diagram for Windows Forms provides preview support for [[Symbol Palette. When you drag an item from Symbol Palette to Diagram View, Preview of the dragged item will be displayed. You can enable or disable the preview support. ]]{.apple-style-span}

 

Use Case Scenario

[[This feature displays a preview of the item you drag from Symbol Palette, thus enables you to identify the item you are dragging from the symbol palette to Diagram view.]]{.apple-style-span}

 

Properties

 

Table 5: Property Table


+--------------------+-------------------------------------------------------------+-------------+-------------+-----------------+
| Property           | Description                                                 | Type        | Data Type   | Reference links |
+--------------------+-------------------------------------------------------------+-------------+-------------+-----------------+
| ShowDragNodeCue    | Gets or sets a value indicating whether preview is visible. | NA          | Boolean     | NA              |
|                    |                                                             |             |             |                 |
|                    | The default value is true.                                  |             |             |                 |
+--------------------+-------------------------------------------------------------+-------------+-------------+-----------------+
| DragNodeCueEnabled | Gets or sets a value indicating whether preview is enabled. | NA          | Boolean     | NA              |
|                    |                                                             |             |             |                 |
|                    | The default value is true.                                  |             |             |                 |
+--------------------+-------------------------------------------------------------+-------------+-------------+-----------------+


 

Enabling Preview Support

To enable preview for the dragged item from Symbol Palette, set the *DragNodeCueEnabled* property of *PalatteGroupBar/PaletteGroupView* to true. To disable preview set this to false. By default this is set to true. 

Following code example illustrates how to enable preview support: 


+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                           |
| [      ][//enable dragged node cue] |
|                                                                                                                                           |
| [            paletteGroupBar1.DragNodeCueEnabled = [true];]                      |
|                                                                                                                                           |
| [            ]                                                                                        |
|                                                                                                                                           |
| [            paletteGroupView1.DragNodeCueEnabled = [true];]                     |
|                                                                                                                                           |
| []                                                                                    |
|                                                                                                                                           |
| [      ][//show dragged node cue]   |
|                                                                                                                                           |
| [            paletteGroupBar1.ShowDragNodeCue = [true];]                         |
|                                                                                                                                           |
| [            ]                                                                                        |
|                                                                                                                                           |
| [            paletteGroupView1.ShowDragNodeCue = [true];]                        |
+-------------------------------------------------------------------------------------------------------------------------------------------+


 


+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                   |
|                                                                                                                                                    |
| [  ][//enable dragged node cue] |
|                                                                                                                                                    |
| [            paletteGroupBar1.DragNodeCueEnabled = [True];           ]                    |
|                                                                                                                                                    |
| [            paletteGroupView1.DragNodeCueEnabled = [True]]                               |
|                                                                                                                                                    |
| []                                                                                |
|                                                                                                                                                    |
| [  ][//show dragged node cue]   |
|                                                                                                                                                    |
| [            paletteGroupBar1.ShowDragNodeCue = [True];        ]                          |
|                                                                                                                                                    |
| [            paletteGroupView1.ShowDragNodeCue = [True];]                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------+


 

{border="0"}

Figure 120: Preview of Dragged Item

 

The following code illustrates how to disable preview support:


+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                         |
| [      ][//hide dragged node cue] |
|                                                                                                                                         |
| [            paletteGroupBar1.ShowDragNodeCue = [false];]                      |
|                                                                                                                                         |
| [            paletteGroupView1.ShowDragNodeCue = [false];]                     |
+-----------------------------------------------------------------------------------------------------------------------------------------+


 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                       |
|                                                                                                                                                                        |
| [  ][            [//hide dragged node cue]] |
|                                                                                                                                                                        |
| [            paletteGroupBar1.ShowDragNodeCue = [False];]                                                     |
|                                                                                                                                                                        |
| [      paletteGroupView1.ShowDragNodeCue = [False];]                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

Sample Link

To view a sample:

1.   Open the Syncfusion Dashboard.

2.   Click the **Windows Forms** drop-down list and select **Run Locally Installed Samples.**

3.   Navigate to **Diagram[ ]Samples \> Product Showcase \> Diagram Builder.**

 

[]{#related-topics}

