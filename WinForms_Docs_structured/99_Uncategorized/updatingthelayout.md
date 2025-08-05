---
title: updatingthelayout.md
original_path: WinForms_Docs/99_Uncategorized/updatingthelayout.md
created_at: 2025-08-05
---








  









### Updating the Layout {#updating-the-layout style="tab-stops: 0pt"}

[] 

After creating the layout, you need to update it. This is done by using the following code example.

[] 

Example

[] 

1.   Drag the DiagramWebControl along with five Button controls onto the web page.

2.   Include the following code in the aspx.cs file of your application.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [using][ System;]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Collections;]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Configuration;]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Data;]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Linq;]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Web;]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Web.Security;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Web.UI;]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Web.UI.HtmlControls;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Web.UI.WebControls;]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Web.UI.WebControls.WebParts;]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Xml.Linq;]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [using][ Syncfusion.Windows.Forms.Diagram;]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                      |
| [using][ System.Drawing;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [namespace][ SamplesDoc]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [public][ [partial] [class] [\_Default] : System.Web.UI.[Page]]                                       |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)]                                                                |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [if][ (\![this].IsPostBack)]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.Model.SizeToContent = [true];]                                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| [PopulateNodes();]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [private][ [void] PopulateNodes()]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [//First level node]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [Ellipse e1 = [new] Ellipse(0, 0, 90, 90);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                      |
| [e1.FillStyle.Color = Color.OrangeRed;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                      |
| [e1.FillStyle.Type = FillStyleType.LinearGradient;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.Model.AppendChild(e1);]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [GenerateInnerLevelNodes(e1, 10, Color.Sienna, Color.SandyBrown,0);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [private][ [void] GenerateInnerLevelNodes(Node parentNode, [int] maxSubNodes, Color LevelColor, Color connectionColor, [int] n)] |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [if][ (n == 3)]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                      |
| [return][;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                      |
| [for][ ([int] i = 0; i \< maxSubNodes; i++)]                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [Ellipse e = [new] Ellipse(0, 0, 45, 45);]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| [e.FillStyle.Color = LevelColor;]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                      |
| [e.FillStyle.Type = FillStyleType.LinearGradient;]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.Model.AppendChild(e);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [ConnectNodes(parentNode, e, connectionColor);]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| [GenerateInnerLevelNodes(e, [new] [Random]().Next(i), Color.Plum, Color.Purple, n++);]                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [private][ [void] ConnectNodes(Node parentNode, Node childNode, Color connectionColor)]                                                                                    |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [if][ (parentNode != [null] && childNode != [null])]                                                                                                  |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [LineConnector lConnector = [new] LineConnector(PointF.Empty, [new] PointF(0, 1));]                                                                                                                    |
|                                                                                                                                                                                                                                                                                      |
| [lConnector.HeadDecorator.DecoratorShape =                                                             DecoratorShape.Filled45Arrow;]                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| [lConnector.LineStyle.LineColor = connectionColor;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [parentNode.CentralPort.TryConnect(lConnector.TailEndPoint);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                      |
| [childNode.CentralPort.TryConnect(lConnector.HeadEndPoint);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.Model.AppendChild(lConnector);]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.Model.SendToBack(lConnector);]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [protected][ [void] Button1_Click([object] sender, [EventArgs] e)]                                                            |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.LayoutManager = [new] TableLayoutManager([this].DiagramWebControl1.Model, 8,8);]                                           |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.LayoutManager.UpdateLayout([null]);]                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [protected][ [void] Button2_Click([object] sender, [EventArgs] e)]                                                            |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.LayoutManager = [new] DirectedTreeLayoutManager([this].DiagramWebControl1.Model, 0, 20, 20);]                              |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.LayoutManager.UpdateLayout([null]);]                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [protected][ [void] Button3_Click([object] sender, [EventArgs] e)]                                                            |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.LayoutManager = [new] HierarchicLayoutManager([this].DiagramWebControl1.Model, 0, 20, 20);]                                |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.LayoutManager.UpdateLayout([null]);]                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [protected][ [void] Button4_Click([object] sender, [EventArgs] e)]                                                            |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.LayoutManager = [new] RadialTreeLayoutManager([this].DiagramWebControl1.Model, 0, 20, 20);]                                |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.LayoutManager.UpdateLayout([null]);]                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| [protected][ [void] Button5_Click([object] sender, [EventArgs] e)]                                                            |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.LayoutManager = [new] SymmetricLayoutManager([this].DiagramWebControl1.Model, 200);]                                       |
|                                                                                                                                                                                                                                                                                      |
| [this][.DiagramWebControl1.LayoutManager.UpdateLayout([null]);]                                                                                                            |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 31: Layout Manager Sample

**[]** 

See Also

[] 

[Table Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Directed Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Hierarchical Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Graph Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Subgraph Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Radial Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Symmetric Layout]{.UGHyperlink}[, ]{.UGHyperlink}[OrgChart Layout]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

