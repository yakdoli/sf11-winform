---
title: customizinglineconnectors1.md
original_path: WinForms_Docs/99_Uncategorized/customizinglineconnectors1.md
created_at: 2025-08-05
---








  









### Customizing Line Connectors {#customizing-line-connectors style="tab-stops: 0pt"}

[] 

This topic describes two properties namely:

[·      ]LineStyle

[·      ]DecoratorStyle

[] 

Line Style

**[]** 

A connector can be customized by specifying the values under the **LineStyle** property. The various properties under LineStyle are:

[] 

[·      ]**Fill -** Specifies the color used to fill the connector.

[·      ]**StrokeThickness -** Specifies the thickness value for the connector\'s border.

[·      ]**Stroke** - Specifies the color used for the border of the connector.

[·      ]**StrokeStartLineCap -** Specifies the shape to be used at the start of a line or segment.

[·      ]**StrokeEndLineCap** - Specifies the shape at the end of a line or segment.

[·      ]**StrokeLineJoin -** Specifies the shape that joins two lines or segments.

[·      ]**StrokeDashArray -** Specifies a collection of double values that indicate the pattern of dashes and gaps used to outline shapes.

[] 

As an example, the Stroke property can be applied as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [LineConnector][ l1 = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [l1.HeadNode = n1;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.TailNode = n2;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.ConnectorType = [ConnectorType].Bezier;]                                                                             |
|                                                                                                                                                                                      |
| [l1.LineStyle.Stroke = [Brushes].Red;]                                                                                   |
|                                                                                                                                                                                      |
| [diagramModel.Connections.Add(l1);]                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ l1 [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [l1.HeadNode = n1]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.TailNode = n2]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.ConnectorType = ConnectorType.Bezier]                                                                                                                  |
|                                                                                                                                                                                                |
| [l1.LineStyle.Stroke = Brushes.Red]                                                                                                                        |
|                                                                                                                                                                                                |
| [diagramModel.Connections.Add(l1)][]                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 66: LineStyle**[]**

**[]** 

DecoratorStyle

**[]** 

The decorator shapes used for the connector can be customized by specifying the property values under the **DecoratorStyle** property. To change the decorator style, the HeadDecoratorStyle and TailDecoratorStyle properties are used.

 

The various properties under the DecoratorStyle property are as follows:

[] 

[·      ]**Fill** - Specifies the color to be used to fill the decorator.

[·      ]**StrokeThickness** - Specifies the thickness value for the decorator\'s border.

[·      ]**Stroke -** Specifies the color to be used for the border of the decorator.

[·      ]**StrokeStartLineCap** - Specifies the shape used at the start of a line or segment.

[·      ]**StrokeEndLineCap -** Specifies the shape at the end of a line or segment.

[·      ]**StrokeLineJoin** - Specifies the shape that joins two lines or segments.

[·      ]**StrokeDashArray** - Specifies a collection of double values that indicate the pattern of dashes and gaps used to outline shapes.

[] 

An example of the **Stroke** property can be applied to the head decorator as folllows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [LineConnector][ l1 = [new] [LineConnector]();] |
|                                                                                                                                                                                      |
| [l1.HeadNode = n1;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.TailNode = n2;]                                                                                                                              |
|                                                                                                                                                                                      |
| [l1.ConnectorType = [ConnectorType].Bezier;]                                                                             |
|                                                                                                                                                                                      |
| [l1.HeadDecoratorStyle.Stroke = [Brushes].Red;]                                                                          |
|                                                                                                                                                                                      |
| [l1.TailDecoratorStyle.Stroke = [Brushes].Red;]                                                                          |
|                                                                                                                                                                                      |
| [diagramModel.Connections.Add(l1);]                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Dim][ l1 [As] [New] [LineConnector]()] |
|                                                                                                                                                                                                |
| [l1.HeadNode = n1]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.TailNode = n2]                                                                                                                                         |
|                                                                                                                                                                                                |
| [l1.ConnectorType = ConnectorType.Bezier]                                                                                                                  |
|                                                                                                                                                                                                |
| [l1.HeadDecoratorStyle.Stroke = Brushes.Red]                                                                                                               |
|                                                                                                                                                                                                |
| [l1.TailDecoratorStyle.Stroke = Brushes.Red]                                                                                                               |
|                                                                                                                                                                                                |
| [diagramModel.Connections.Add(l1)][]                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 67: Decorator Style

[]{#p44} 

[]{#related-topics}

