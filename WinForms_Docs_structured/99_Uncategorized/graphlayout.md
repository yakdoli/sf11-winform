---
title: graphlayout.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\graphlayout.md
created_at: 2025-07-03
---






#### Graph Layout {#graph-layout style="tab-stops: 0pt"}

 

The **GraphLayoutManager** is an abstract base class that can be used for implementing layout managers for diagrams composed primarily of nodes forming connected graphs. The GraphLayoutManager implements the infrastructure for initializing, validating and creating the diagram graph by enumerating the diagram model\'s child nodes. It also enables positioning diagram nodes using the layout strategies provided by specialized directed tree layout managers that derive from it.

 

The event of the Graph Layout Manager class is:

[] 


  ----------------------- ---------------------------------------------------------------------------------
  Event                   Description
  PreferredLayout Event   Event provides the application a chance to customize the layout of the diagram.
  ----------------------- ---------------------------------------------------------------------------------


[] 

Programmatically, it is implemented as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [RadialTreeLayoutManager dtlm = [new] RadialTreeLayoutManager([this].diagram1.Model, 0, 20, 20);]                                           |
|                                                                                                                                                                                                                           |
| [dtlm.PreferredLayout += [new] PreferredLayoutEventHandler(dtlm_PreferredLayout);]                                                                               |
|                                                                                                                                                                                                                           |
| [this][.diagram1.LayoutManager = dtlm;]                                                                                              |
|                                                                                                                                                                                                                           |
| [this][.diagram1.LayoutManager.UpdateLayout([null]);]                                                           |
|                                                                                                                                                                                                                           |
| [this][.diagram1.UpdateView();]                                                                                                      |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [private][ [void] dtlm_PreferredLayout([object] sender, PreferredLayoutEventArgs evtArgs)] |
|                                                                                                                                                                                                                           |
| [ {]                                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [       [if] (evtArgs.IsGraphUnderLayout)]                                                                                                                       |
|                                                                                                                                                                                                                           |
| [       {]                                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| [            evtArgs.ResizeGraphNodes = [false];]                                                                                                                |
|                                                                                                                                                                                                                           |
| [            evtArgs.Location = [new] [PointF](150,150);]                                                                                   |
|                                                                                                                                                                                                                           |
| [            evtArgs.Size = [new] [SizeF](100, 100);]                                                                                       |
|                                                                                                                                                                                                                           |
| [       }]                                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| [ }]                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                        |
| [Dim][ dtlm [As] [New] RadialTreeLayoutManager([Me].diagram1.Model, 0, 20, 20)]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                        |
| [AddHandler][ dtlm.PreferredLayout, [AddressOf] dtlm_PreferredLayout]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                        |
| [Me][.diagram1.LayoutManager = dtlm]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                        |
| [Me][.diagram1.LayoutManager.UpdateLayout([Nothing])]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                        |
| [Me][.diagram1.UpdateView()]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] dtlm_PreferredLayout([ByVal] sender [As] [Object], [ByVal] evtArgs [As] PreferredLayoutEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                        |
| [    [If] evtArgs.IsGraphUnderLayout [Then]]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                        |
| [        evtArgs.ResizeGraphNodes = [False]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                        |
| [        evtArgs.Location = [New] PointF(150, 150)]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                        |
| [        evtArgs.Size = [New] SizeF(100, 100)]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                        |
| [    [End] [If]]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

*[]* 

*[]* 

Figure 23: Graph Layout Manager

***[]*** 

**[See Also]**

[] 

[Table Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Directed Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Hierarchical Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Subgraph Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Radial Tree Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Symmetric Layout]{.UGHyperlink}[, ]{.UGHyperlink}[OrgChart Layout]{.UGHyperlink}[, ]{.UGHyperlink}[Updating the Layout]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

