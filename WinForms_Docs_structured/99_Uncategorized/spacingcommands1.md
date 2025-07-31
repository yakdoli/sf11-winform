---
title: spacingcommands1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\spacingcommands1.md
created_at: 2025-07-03
---








  









### Spacing Commands {#spacing-commands style="tab-stops: 0pt"}

Spacing commands enables you to place selected objects (nodes and connectors) on the page at equal intervals from each other. The objects are spaced within the bounds of the first and last objects in the selection object.

 

The following spacing commands are used to space objects.

[] 

Horizontal Spacing

The **SpaceAcross** command spaces selected objects with equal horizontal distance between them.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [DiagramCommandManager][.SpaceAcross.Execute(diagramView.Page, diagramView);]                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| **[]**                                                                                                                                         |
|                                                                                                                                                                                                  |
| [DiagramCommandManager][.SpaceAcross.Execute(diagramView.Page, diagramView)**[]**] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

The following screen shot illustrates horizontally spaced objects.

[] 

{border="0"}

Figure 160: SpaceAcross command applied to Diagram Objects[]

***[]*** 

***[]*** 

Vertical Spacing

The **SpaceDown** command spaces selected objects with equal vertical distance between them.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [DiagramCommandManager][.SpaceDown.Execute(diagramView.Page, diagramView);]                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                                |
| [DiagramCommandManager][.SpaceDown.Execute(diagramView.Page, diagramView)**[]**] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

The following screen shot illustrates vertically spaced objects.

[] 

{border="0"}

Figure 161: SpaceDown command applied to Diagram Objects[]

[] 


{border="0"}Note: The connector gets spaced only when the head node and the tail node of the connector is Null.


[]{#p89} 

[]{#related-topics}

