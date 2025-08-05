---
title: connectorsorlinks.md
original_path: WinForms_Docs/99_Uncategorized/connectorsorlinks.md
created_at: 2025-08-05
---






#### Connectors or Links[] {#connectors-or-links style="tab-stops: 0pt"}

[] 

Connectors and lines have the following types of decorators.

[] 

[·      ]Circle

[·      ]CircleCross

[·      ]CircleReverseArrow

[·      ]Cross45

[·      ]Cross90

[·      ]CrossReverseArrow

[·      ]Custom

[·      ]Diamond

[·      ]DimensionLine

[·      ]DoubleArrow

[·      ]DoubleCross

[·      ]Filled45Arrow

[·      ]Filled60Arrow

[·      ]FilledCircle

[·      ]FilledDiamond

[·      ]FilledFancyArrow

[·      ]FilledSquare

[·      ]None

[·      ]Open45Arrow

[·      ]Open60Arrow

[·      ]OpenFancyArrow

[·      ]ReverseArrow

[·      ]ReverseDoubleArrow

[·      ]Square

[] 

Connecting Two Nodes with a Line Connector

[] 

The following code example illustrates how to create a link between two nodes.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Syncfusion.Windows.Forms.Diagram.[Ellipse] ellipse = [new] Syncfusion.Windows.Forms.Diagram.[Ellipse](10, 10, 110, 70);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Syncfusion.Windows.Forms.Diagram.[Rectangle] rectangle = [new] Syncfusion.Windows.Forms.Diagram.[Rectangle](300, 50, 50, 80);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Syncfusion.Windows.Forms.Diagram.[LineConnector] lineconnector = [new] Syncfusion.Windows.Forms.Diagram.[LineConnector]([new] System.Drawing.[PointF](10, 200), [new] System.Drawing.[PointF](300, 250));] |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.DiagramWebControl1.Model.AppendChild(ellipse);]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.DiagramWebControl1.Model.AppendChild(rectangle);]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [ellipse.CentralPort.TryConnect(lineconnector.HeadEndPoint);]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [rectangle.CentralPort.TryConnect(lineconnector.TailEndPoint);]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.DiagramWebControl1.Model.AppendChild(lineconnector);]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 8: Diagram with Connector

[] 

Connector Property Settings

[] 

Connectors have separate properties which can be set dynamically through code. The following code example illustrates the Line properties of Connectors.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Syncfusion.Windows.Forms.Diagram.[Ellipse] ellipse = [new] Syncfusion.Windows.Forms.Diagram.[Ellipse](160, 60, 100, 60);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Syncfusion.Windows.Forms.Diagram.[Rectangle] rectangle = [new] Syncfusion.Windows.Forms.Diagram.[Rectangle](150, 250, 120, 100);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Syncfusion.Windows.Forms.Diagram.[LineConnector] lineconnector = [new] Syncfusion.Windows.Forms.Diagram.[LineConnector]([new] System.Drawing.[PointF](10, 200), [new] System.Drawing.[PointF](300, 250));] |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.DiagramWebControl1.Model.AppendChild(ellipse);]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.DiagramWebControl1.Model.AppendChild(rectangle);]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [ellipse.CentralPort.TryConnect(lineconnector.TailEndPoint);]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [rectangle.CentralPort.TryConnect(lineconnector.HeadEndPoint);]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.DiagramWebControl1.Model.AppendChild(lineconnector);]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [lineconnector.HeadDecorator.DecoratorShape = DecoratorShape.Filled45Arrow;]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [lineconnector.LineStyle.LineColor = Color.MidnightBlue;]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [lineconnector.HeadDecorator.FillStyle.Color = Color.MidnightBlue;]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [lineconnector.HeadDecorator.Size = [new] SizeF(10, 5);]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 9: Diagram with Connection Property Settings

[]{#related-topics}

