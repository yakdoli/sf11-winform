---
title: sizingcommands1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\sizingcommands1.md
created_at: 2025-07-03
---








  









### Sizing Commands {#sizing-commands style="tab-stops: 0pt"}

Sizing commands enable you to resize selected objects (nodes and connectors) on the page. The selected objects get resized with respect to the first object in the selection list. 

 

The following sizing commands are used to resize objects.

[] 

Height Customization

The **SameHeight** command resizes selected objects to the height of the first object in the selection list.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [DiagramCommandManager][.SameHeight.Execute(diagramView.Page, diagramView);]                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [DiagramCommandManager][.SameHeight.Execute(diagramView.Page, diagramView)**[]**] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 162: SameHeight command applied to Diagram Objects*[ ]*

[] 


{border="0"}Note: The width of the selected object remains the same.


[] 

Width Customization

The **SameWidth** command resizes selected objects to the width of the first object in the selection list.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [DiagramCommandManager][.SameWidth.Execute(diagramView.Page, diagramView);]                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [DiagramCommandManager][.SameWidth.Execute(diagramView.Page, diagramView)**[]**] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 163: SameWidth command applied to Diagram Objects[]


 

{border="0"}Note: The height of the selected object remains the same.


[] 

Height and Width Customization

The **SameSize** command resizes selected objects to the height and width of the first object in the selection list.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [DiagramCommandManager][.SameSize.Execute(diagramView.Page, diagramView);]                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| **[]**                                                                                                                                      |
|                                                                                                                                                                                               |
| [DiagramCommandManager][.SameSize.Execute(diagramView.Page, diagramView)**[]**] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 164: SameSize command applied to Diagram Objects[]

[] 


{border="0"}Note: The connector gets spaced only when the head node and the tail node of the connector is Null.


[]{#p90} 

[]{#related-topics}

