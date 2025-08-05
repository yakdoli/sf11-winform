---
title: previewforsymbolpaletteitem2.md
original_path: WinForms_Docs/99_Uncategorized/previewforsymbolpaletteitem2.md
created_at: 2025-08-05
---








  









### Preview for Symbol Palette Item {#preview-for-symbol-palette-item style="tab-stops: 0pt"}

Essential Diagram for WPF provides preview support for Symbol Palette. When you drag an item from Symbol Palette to Diagram View, Preview of the dragged item will be displayed. You can enable or disable the preview support. You can also customize the preview. 

 

Use Case Scenario

This feature displays a preview of the item you drag from Symbol Palette, thus enables you to identify the item you are dragging from the symbol palette to Diagram view.

 

Properties

Table 80: Property Table

+--------------+-------------------------------------------------------------+---------------------+-------------+-----------------+
| Property     | Description                                                 | Type                | Data Type   | Reference links |
+--------------+-------------------------------------------------------------+---------------------+-------------+-----------------+
| ShowPreview  | Gets or sets a value indicating whether preview is enabled. | Dependency property | Boolean     | NA              |
|              |                                                             |                     |             |                 |
|              | The default value is true.                                  |                     |             |                 |
+--------------+-------------------------------------------------------------+---------------------+-------------+-----------------+
|              |                                                             |                     |             |                 |
|              |                                                             |                     |             |                 |
| PreviewBrush | Gets or sets a value for preview content.                   | Dependency property | Brush       | NA              |
+--------------+-------------------------------------------------------------+---------------------+-------------+-----------------+

[] 

Enabling Preview Support

To enable preview for the dragged item from Symbol Palette, set the *ShowPreview* property of *SymbolPalette* to true. To disable preview set this to false. By default this is set to true. 

Following code example illustrates how to enable preview support: 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                           |
| [      DiagramControl][ diagramControl1 = [new] [DiagramControl]();] |
|                                                                                                                                                                                                           |
| [diagramControl1.SymbolPalette.ShowPreview = [true];]                                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [       ][Dim][ diagramControl1 [As] [New] DiagramControl()] |
|                                                                                                                                                                                                                                                              |
| [      diagramControl1.SymbolPalette.ShowPreview = [true]]                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[ ]{border="0"}

Figure 179: Preview of Dragged Item

[] 

Change the preview content using PreviewBrush

You can customize the preview content using the *PreviewBrush* property of *SymbolPaletteItem*. Following code example illustrates how to customize preview content:

 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [       ][DiagramControl][ diagramControl1 = [new] [DiagramControl]();] |
|                                                                                                                                                                                                                                                                               |
| [      (diagramControl1.SymbolPalette.SymbolGroups\[0\].Items\[0\] [as    ][SymbolPaletteItem]).PreviewBrush = [Brushes].CornflowerBlue;]                            |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [       ][Dim][ diagramControl1 [As] [New] DiagramControl()] |
|                                                                                                                                                                                                                                                              |
| [      TryCast(diagramControl1.SymbolPalette.SymbolGroups(0).Items(0),  SymbolPaletteItem).PreviewBrush = Brushes.CornflowerBlue][]                                     |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

[ ]{border="0"}

Figure 180: Customized Preview Content[]

[] 

[] 

[]{#related-topics}

