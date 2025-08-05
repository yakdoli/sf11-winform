---
title: orgchartlayout.md
original_path: WinForms_Docs/04_Controls/Chart/orgchartlayout.md
created_at: 2025-08-05
---






#### OrgChart Layout  [] {#orgchart-layout style="tab-stops: 0pt"}

[] 

Event arranges all the nodes in parent/child relationship with the new OrgLineConnector that connects the nodes to get the OrgLayout appearance. The OrgLineConnector is specially designed for connecting the nodes in OrgChartLayoutManager.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------+
| Property                          | Description                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| Model                             | Represents the model of the diagram, which is displayed as an OrgLayout.                  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| RotationDirection                 | Gets / sets the layout directions. There are four major directions, which are as follows: |
|                                   |                                                                                           |
|                                   | BottomToTop                                                                               |
|                                   |                                                                                           |
|                                   | LeftToRight                                                                               |
|                                   |                                                                                           |
|                                   | RightToLeft                                                                               |
|                                   |                                                                                           |
|                                   | TopToBottom                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| HorizontalSpacing                 | Holds the value for the horizontal offset between adjacent nodes (float value).           |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| VerticalSpacing                   | Holds the value for the vertical offset between adjacent nodes (float value).             |
+-----------------------------------+-------------------------------------------------------------------------------------------+


[] 

Programmatically, the organization layout manager instance should be created with the respective arguments, assigned to the Layout Manager and updated as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [OrgChartLayoutManager manager = [new] OrgChartLayoutManager([this].DiagramWebControl1.Model,RotateDirection.TopToBottom, 20, 50);] |
|                                                                                                                                                                                                                   |
| [this][.DiagramWebControl1.LayoutManager = manager;]                                                                         |
|                                                                                                                                                                                                                   |
| [this][.DiagramWebControl1.LayoutManager.UpdateLayout([null]);]                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| [Dim][ manager [As] [New] OrgChartLayoutManager([Me].DiagramWebControl1.Model, RotateDirection.TopToBottom, 20, 50)] |
|                                                                                                                                                                                                                                                                          |
| [Me][.DiagramWebControl1.LayoutManager = manager]                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [Me][.DiagramWebControl1.LayoutManager.UpdateLayout([Nothing])]                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Sample Diagram is as follows.

**[]** 

{border="0"}

[] 

Figure 29: Top-to-Bottom Direction Organizational Chart Layout

**[]** 

{border="0"}

[] 

Figure 30: Bottom-to-Top Direction Organizational Chart Layout

[] 

OrgChart Alignment

**[]** 

As this OrgChartLayout follows a Waterfall model, whenever there is only one child node, the layout will be widened. To overcome this, Essential diagram enables you to align the single child node parallel to the parent node, which will be reduce the layout structure.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [OrgChartLayoutManager][ manager = ][new][ ][OrgChartLayoutManager][(][this][.][DiagramWebControl1[.Model, ][RotateDirection][.TopToBottom, 20, 50, ][LayoutType][.Waterfall, 1, ][true][);]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Dim][ manager ][as New][ OrgChartLayoutManager(][Me][.][DiagramWebControl1[.Model,RotateDirection.TopToBottom, 20, 50,LayoutType.Waterfall, 1, ][True][)]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Table Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Directed Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Hierarchical Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Graph Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Subgraph Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Radial Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Symmetric Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Updating the Layout]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

