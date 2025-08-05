---
title: throughcode14.md
original_path: WinForms_Docs/99_Uncategorized/throughcode14.md
created_at: 2025-08-05
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

The tabstrip control can also be created programmatically.

 

{border="0"}

[] 

Figure 292: Programmatically created tabstrip

[] 

1.   Drag the control onto the webpage of the project.

104.   In the view, add the following code.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [private][ [void] Page_Load([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [  BuildTabs();]                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [private][ [void] BuildTabs()]                                                         |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [  TabStrip1=[new] Syncfusion.Web.UI.WebControls.Tools.TabStrip();]                                                                                     |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.TabLayout = TabLayout.Horizontal;]                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.CustomCSS = [\"css/Tab.css\"];]                                                                                                          |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.ControlRootCSSClass=[\"TopGroup\"];  ]                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItemLook RootLook=[new] TabStripItemLook();]                                                                                                 |
|                                                                                                                                                                                                                                  |
| [  RootLook.ID=[\"RootLook\"];]                                                                                                                       |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataDefault.ItemCSSClass = [\"Root_ItemCSS\"];]                                                                                      |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataDefault.LeftImageCSSClass = [\"empty\"];]                                                                                        |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataDefault.LeftImageURL = [\"../images/leftbl.gif\"];]                                                                              |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataDefault.TextContainerCSSClass = [\"DefRoot_TextCell\"];]                                                                         |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataDefault.RightImageCSSClass = [\"empty\"];]                                                                                       |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataDefault.RightImageURL = [\"../images/right.gif\"];]                                                                              |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataHover.ItemCSSClass = [\"DefaultTab\"];]                                                                                          |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataHover.TextContainerCSSClass = [\"DefRoot_TextCell\"];]                                                                           |
|                                                                                                                                                                                                                                  |
| [            ]                                                                                                                                                               |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataPushed.ItemCSSClass = [\"Root_ItemCSS\"];]                                                                                       |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataPushed.LeftImageCSSClass = [\"empty\"];]                                                                                         |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataPushed.LeftImageURL = [\"../images/nrm_left.gif\"];]                                                                             |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataPushed.TextContainerCSSClass = [\"SelRoot_TextCell\"];]                                                                          |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataPushed.RightImageCSSClass = [\"empty\"];]                                                                                        |
|                                                                                                                                                                                                                                  |
| [  RootLook.StateDataPushed.RightImageURL = [\"../images/nrm_right.gif\"];]                                                                           |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItemLook ChildLook=[new] TabStripItemLook();]                                                                                                |
|                                                                                                                                                                                                                                  |
| [  ChildLook.ID =[\"ChildLook\"];]                                                                                                                    |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  ChildLook.StateDataDefault.ItemCSSClass = [\"DefChild_ItemCSS\"];]                                                                                 |
|                                                                                                                                                                                                                                  |
| [  ChildLook.StateDataDefault.TextContainerCSSClass = [\"Child_TextCont\"];]                                                                          |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.Looks.Add(RootLook );]                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.Looks.Add(ChildLook );]                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItem Products=[new] TabStripItem();]                                                                                                         |
|                                                                                                                                                                                                                                  |
| [  Products.ID = [\"Products\"];]                                                                                                                     |
|                                                                                                                                                                                                                                  |
| [  Products.Text = [\"Products\"];]                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [  Products.Look = [\"RootLook\"];]                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [  Products.SubPanelCSSClass=[\"Level2Group\"];]                                                                                                      |
|                                                                                                                                                                                                                                  |
| [  Products.Selected = [true];]                                                                                                                         |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItem Services = [new] TabStripItem();]                                                                                                       |
|                                                                                                                                                                                                                                  |
| [  Services.ID = [\"Services\"];]                                                                                                                     |
|                                                                                                                                                                                                                                  |
| [  Services.Text = [\"Services\"];]                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [  Services.Look = [\"RootLook\"];]                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItem EssenTools=[new] TabStripItem ();]                                                                                                      |
|                                                                                                                                                                                                                                  |
| [  EssenTools.ID =[\"EssenTools\"];]                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [  EssenTools.Text =[\"Essential Tools\"];]                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  EssenTools.Look=[\"ChildLook\"];]                                                                                                                  |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItem EssenGrid=[new] TabStripItem ();]                                                                                                       |
|                                                                                                                                                                                                                                  |
| [  EssenGrid.ID =[\"EssenGrid\"];]                                                                                                                    |
|                                                                                                                                                                                                                                  |
| [  EssenGrid.Text =[\"Essential Grid\"];]                                                                                                             |
|                                                                                                                                                                                                                                  |
| [  EssenGrid.Look=[\"ChildLook\"];]                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItem EssenPdf=[new] TabStripItem ();]                                                                                                        |
|                                                                                                                                                                                                                                  |
| [  EssenPdf.ID =[\"EssenPdf\"];]                                                                                                                      |
|                                                                                                                                                                                                                                  |
| [  EssenPdf.Text =[\"Essential PDF\"];]                                                                                                               |
|                                                                                                                                                                                                                                  |
| [  EssenPdf.Look=[\"ChildLook\"];]                                                                                                                    |
|                                                                                                                                                                                                                                  |
| [            ]                                                                                                                                                               |
|                                                                                                                                                                                                                                  |
| [  Products.Items.Add(EssenTools);           ]                                                                                                                               |
|                                                                                                                                                                                                                                  |
| [  Products.Items.Add(EssenGrid);]                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  Products.Items.Add(EssenPdf);]                                                                                                                                            |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItem Support= [new] TabStripItem();]                                                                                                         |
|                                                                                                                                                                                                                                  |
| [  Support.ID = [\"Support\"];]                                                                                                                       |
|                                                                                                                                                                                                                                  |
| [  Support.Text = [\"Support\"];]                                                                                                                     |
|                                                                                                                                                                                                                                  |
| [  Support.Look = [\"RootLook\"];]                                                                                                                    |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItem Sales = [new] TabStripItem();]                                                                                                          |
|                                                                                                                                                                                                                                  |
| [  Sales.ID = [\"Sales\"];]                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  Sales.Text = [\"Sales\"];]                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [  Sales.Look = [\"RootLook\"];]                                                                                                                      |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItem Downloads = [new] TabStripItem();]                                                                                                      |
|                                                                                                                                                                                                                                  |
| [  Downloads.ID = [\"Downloads\"];]                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [  Downloads.Text = [\"Downloads\"];]                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [  Downloads.Look = [\"RootLook\"];]                                                                                                                  |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStripItem Corporate = [new] TabStripItem();]                                                                                                      |
|                                                                                                                                                                                                                                  |
| [  Corporate.ID = [\"Corporate\"];]                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [  Corporate.Text = [\"Corporate\"];]                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [  Corporate.Look = [\"RootLook\"];]                                                                                                                  |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.Items.Add (Products);]                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.Items.Add (Services);]                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.Items.Add (Support);]                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.Items.Add (Sales);]                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.Items.Add (Downloads);]                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [  TabStrip1.Items.Add (Corporate);]                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [  [this].Controls.Add(TabStrip1);   ]                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                               |
| [  BuildTabs()]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] BuildTabs()]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1 = [New] Syncfusion.Web.UI.WebControls.Tools.TabStrip()]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.TabLayout = TabLayout.Horizontal]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.CustomCSS = [\"css/Tab.css\"]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.ControlRootCSSClass = [\"TopGroup\"]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] RootLook [As] TabStripItemLook = [New] TabStripItemLook()]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.ID = [\"RootLook\"]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataDefault.ItemCSSClass = [\"Root_ItemCSS\"]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataDefault.LeftImageCSSClass = [\"empty\"]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataDefault.LeftImageURL = [\"../images/leftbl.gif\"]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataDefault.TextContainerCSSClass = [\"DefRoot_TextCell\"]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataDefault.RightImageCSSClass = [\"empty\"]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataDefault.RightImageURL = [\"../images/right.gif\"]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataHover.ItemCSSClass = [\"DefaultTab\"]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataHover.TextContainerCSSClass = [\"DefRoot_TextCell\"]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataPushed.ItemCSSClass = [\"Root_ItemCSS\"]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataPushed.LeftImageCSSClass = [\"empty\"]]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataPushed.LeftImageURL = [\"../images/nrm_left.gif\"]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataPushed.TextContainerCSSClass = [\"SelRoot_TextCell\"]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataPushed.RightImageCSSClass = [\"empty\"]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                               |
| [  RootLook.StateDataPushed.RightImageURL = [\"../images/nrm_right.gif\"]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] ChildLook [As] TabStripItemLook = [New] TabStripItemLook()]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [  ChildLook.ID = [\"ChildLook\"]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  ChildLook.StateDataDefault.ItemCSSClass = [\"DefChild_ItemCSS\"]]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| [  ChildLook.StateDataDefault.TextContainerCSSClass = [\"Child_TextCont\"]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.Looks.Add(RootLook)]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.Looks.Add(ChildLook)]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] Products [As] TabStripItem = [New] TabStripItem()]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Products.ID = [\"Products\"]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Products.Text = [\"Products\"]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Products.Look = [\"RootLook\"]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Products.SubPanelCSSClass = [\"Level2Group\"]]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Products.Selected = [True]]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] Services [As] TabStripItem = [New] TabStripItem()]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Services.ID = [\"Services\"]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Services.Text = [\"Services\"]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Services.Look = [\"RootLook\"]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] EssenTools [As] TabStripItem = [New] TabStripItem()]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                               |
| [  EssenTools.ID = [\"EssenTools\"]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| [  EssenTools.Text = [\"Essential Tools\"]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [  EssenTools.Look = [\"ChildLook\"]]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] EssenGrid [As] TabStripItem = [New] TabStripItem()]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| [  EssenGrid.ID = [\"EssenGrid\"]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [  EssenGrid.Text = [\"Essential Grid\"]]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [  EssenGrid.Look = [\"ChildLook\"]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] EssenPdf [As] TabStripItem = [New] TabStripItem()]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| [  EssenPdf.ID = [\"EssenPdf\"]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                               |
| [  EssenPdf.Text = [\"Essential PDF\"]]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| [  EssenPdf.Look = [\"ChildLook\"]]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Products.Items.Add(EssenTools)]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Products.Items.Add(EssenGrid)]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Products.Items.Add(EssenPdf)]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] Support [As] TabStripItem = [New] TabStripItem()]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Support.ID = [\"Support\"]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Support.Text = [\"Support\"]]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Support.Look = [\"RootLook\"]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] Sales [As] TabStripItem = [New] TabStripItem()]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Sales.ID = [\"Sales\"]]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Sales.Text = [\"Sales\"]]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Sales.Look = [\"RootLook\"]]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] Downloads [As] TabStripItem = [New] TabStripItem()]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Downloads.ID = [\"Downloads\"]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Downloads.Text = [\"Downloads\"]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Downloads.Look = [\"RootLook\"]]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Dim] Corporate [As] TabStripItem = [New] TabStripItem()]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Corporate.ID = [\"Corporate\"]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Corporate.Text = [\"Corporate\"]]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| [  Corporate.Look = [\"RootLook\"]]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.Items.Add(Products)]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.Items.Add(Services)]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.Items.Add(Support)]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.Items.Add(Sales)]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.Items.Add(Downloads)]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [  TabStrip1.Items.Add(Corporate)]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [  [Me].Controls.Add(TabStrip1)]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

105.   Add the following style sheet to the project\'s css folder.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| [.DefRoot_TextCell]                                                                    |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [background-image]:[url(../images/nrm_bg.png)]; ]         |
|                                                                                                                                                           |
| [  [color] :[Black] ;]                                       |
|                                                                                                                                                           |
| [  [font-size]:[11px];]                                      |
|                                                                                                                                                           |
| [  [font-family]:[Verdana] ;  ]                              |
|                                                                                                                                                           |
| [  [height]:[22px];]                                         |
|                                                                                                                                                           |
| [  [padding-top]:[4px]; ]                                    |
|                                                                                                                                                           |
| [  [padding-left]:[3px];]                                    |
|                                                                                                                                                           |
| [  [padding-right]:[3px];   ]                                |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.SelRoot_TextCell]                                                                    |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [background-image]:[url(../images/sel_bg.gif)];         ] |
|                                                                                                                                                           |
| [  [color] :[Black] ;]                                       |
|                                                                                                                                                           |
| [  [font-size]:[11px];]                                      |
|                                                                                                                                                           |
| [  [font-family]:[Verdana] ;  ]                              |
|                                                                                                                                                           |
| [  [padding-top]:[4px]; ]                                    |
|                                                                                                                                                           |
| [  [padding-left]:[3px];]                                    |
|                                                                                                                                                           |
| [  [padding-right]:[3px];  ]                                 |
|                                                                                                                                                           |
| [  [height]:[22px];]                                         |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.empty]                                                                               |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.DefChild_ItemCSS]                                                                    |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [padding-left]:[8px];]                                    |
|                                                                                                                                                           |
| [  [padding-top]:[2px];  ]                                   |
|                                                                                                                                                           |
| [  [padding-bottom]:[2px];]                                  |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.Child_TextCont]                                                                      |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [padding-left]:[8px];]                                    |
|                                                                                                                                                           |
| [  [padding-top]:[2px];  ]                                   |
|                                                                                                                                                           |
| [  [padding-bottom]:[2px];]                                  |
|                                                                                                                                                           |
| [  [color] :[black];]                                        |
|                                                                                                                                                           |
| [  [font-size]:[11px];]                                      |
|                                                                                                                                                           |
| [  [font-family]:[Verdana] ;  ]                              |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.Root_ItemCSS]                                                                        |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [border]:[0px]; ]                                         |
|                                                                                                                                                           |
| [  [padding-top]:[4px]; ]                                    |
|                                                                                                                                                           |
| [  [padding-left]:[3px];]                                    |
|                                                                                                                                                           |
| [  [padding-right]:[3px];  ]                                 |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.topgroup]                                                                            |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [width]:[1500px];]                                        |
|                                                                                                                                                           |
| [}]                                                                                                   |
|                                                                                                                                                           |
| [.Level2group]                                                                         |
|                                                                                                                                                           |
| [{]                                                                                                   |
|                                                                                                                                                           |
| [  [width]:[1500px]; ]                                       |
|                                                                                                                                                           |
| [  [background-image]:[url(../images/bglevel2.gif)]; ]       |
|                                                                                                                                                           |
| [  [background-repeat]:[repeat-x];  ]                        |
|                                                                                                                                                           |
| [}    ]                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

106.   Build and run the application.

 

[]{#related-topics}

