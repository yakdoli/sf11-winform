---
title: panning4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\panning4.md
created_at: 2025-07-03
---








  









### Panning {#panning style="tab-stops: 0pt"}

Essential Diagram WPF provides the ability to pan a page. Panning is used to move the contents of page both horizontally and vertically by holding down a mouse button and then moving the mouse.

 

Table 62: Property Table

+--------------+----------------------------------------------------------------+---------------------+---------------------+---------------------------------------------------+
| Property     | Description                                                    | Type Of  the        | Value it accepts    | Any other dependencies/ sub properties associated |
|              |                                                                |                     |                     |                                                   |
|              |                                                                | property            |                     |                                                   |
+--------------+----------------------------------------------------------------+---------------------+---------------------+---------------------------------------------------+
| IsPanEnabled | Gets or sets a value indicating whether pan is enabled or not. | Dependency property | Boolean(True/False) | No                                                |
|              |                                                                |                     |                     |                                                   |
|              |                                                                |                     |                     |                                                   |
|              |                                                                |                     |                     |                                                   |
|              | Default value is False.                                        |                     |                     |                                                   |
+--------------+----------------------------------------------------------------+---------------------+---------------------+---------------------------------------------------+

[] 

Steps for panning a page

**[]** 

1.   A page can be panned by setting the **IsPanEnabled** property to *True*.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                              |
|                                                                                                                                                                                           |
| [DiagramView][ diagramView = [new] [DiagramView]();] |
|                                                                                                                                                                                           |
| [diagramView.IsPanEnabled = [true];]                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                   |
|                                                                                                                                                                                                       |
| [Dim][ diagramView [As] [New] [DiagramView]()] |
|                                                                                                                                                                                                       |
| [diagramView.IsPanEnabled = [True]][]                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Click and drag the diagram page to the desired position. Note that the negative rulers get displayed while panning to the right.       

[] 


{border="0"}Note: No other operations can be performed on page elements while IsPanEnabled is set to True.


[] 

 

{border="0"}

Figure 137: Pan[]

[] 

[]{#related-topics}

