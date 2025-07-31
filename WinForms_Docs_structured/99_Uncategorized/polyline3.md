---
title: polyline3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\polyline3.md
created_at: 2025-07-03
---








  









### Polyline {#polyline style="tab-stops: 0pt"}

Line connector can be used to draw polylines using **IntermediatePoints** property. Polylines are drawn using intermediate points for straight lines and orthogonal line connectors. For orthogonal lines, intermediate points are updated so that the adjacent line segments are always perpendicular to each other. These intermediate points are visually represented as vertex.

[] 

Table 31: Property Table[]

  -------------------- --------------------------------------- ---------------------- ------------------ ---------------------------------------------------
  Property             Description                             Type of the property   Value it accepts   Any other dependencies/ sub properties associated
  IntermediatePoints   Gets or sets the intermediate points.   Dependency property    List\<Point\>      No
  -------------------- --------------------------------------- ---------------------- ------------------ ---------------------------------------------------

[] 

Polylines

[] 

Straight line connectors can be used as poly line by using **IntermediatePoints** property. This can be achieved at run time by holding Ctrl + Shift and Click on the line, or by simply changing the **IntermediatePoints** collection. This will reflect in the line connector.

[] 

{border="0"}

Figure 61: Polyline

[] 

Poly Orthogonal Lines

**[]** 

Orthogonal lines can have more than two intermediate points. All these Intermediate points are can be dragged. Unlike straight lines, orthogonal lines maintain their perpendicularity even after the intermediate points are dragged.

[] 

{border="0"}

Figure 62: Poly Orthogonal Lines

[] 

More:













