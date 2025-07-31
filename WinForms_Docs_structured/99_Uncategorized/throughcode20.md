---
title: throughcode20.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\throughcode20.md
created_at: 2025-07-03
---






##### Through Code {#through-code style="tab-stops: 0pt"}

[] 

You can configure the contents of the Syncfusion Splitter programmatically. To do that you need to create SplitPanes and SplitterBars object and add them to the Items collection of their parent Splitter. **Items** property is not persisted in the ViewState and if you create the Splitter in the code-behind you need to recreate them on every postback / callback.

 

The following code example demonstrates how to create single Splitter control with three SplitPanes programmatically.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [      [//create Splitter control]]                                                                                                                      |
|                                                                                                                                                                                                                    |
| [      [Splitter] splitter = [new] [Splitter]();]                                                               |
|                                                                                                                                                                                                                    |
| [      splitter.Height = [Unit].Pixel( 150 );]                                                                                                            |
|                                                                                                                                                                                                                    |
| [      splitter.Width = [Unit].Pixel( 300 );]                                                                                                             |
|                                                                                                                                                                                                                    |
| [      splitter.ResizeMode = [SplitterResizeMode].Proportional;]                                                                                          |
|                                                                                                                                                                                                                    |
| [      form1.Controls.Add( splitter );]                                                                                                                                        |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create Left SplitPane]]                                                                                                                        |
|                                                                                                                                                                                                                    |
| [      [SplitPane] SplitPane_Left = [new] [SplitPane]();]                                                       |
|                                                                                                                                                                                                                    |
| [      SplitPane_Left.ID = [\"SplitPane_Left\"];]                                                                                                       |
|                                                                                                                                                                                                                    |
| [      SplitPane_Left.Controls.Add( [new] [LiteralControl]( [\"Left SplitPane\"] ) );]                        |
|                                                                                                                                                                                                                    |
| [      splitter.Items.Add( SplitPane_Left );]                                                                                                                                  |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create SplitterBar]]                                                                                                                           |
|                                                                                                                                                                                                                    |
| [      [SplitterBar] splitterbar1 = [new] [SplitterBar]();]                                                     |
|                                                                                                                                                                                                                    |
| [      splitterbar1.ID = [\"SplitterBar1\"];]                                                                                                           |
|                                                                                                                                                                                                                    |
| [      splitterbar1.CollapseMode = [SplitterBarCollapseMode].Both;]                                                                                       |
|                                                                                                                                                                                                                    |
| [      splitter.Items.Add( splitterbar1 );]                                                                                                                                    |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create Center SplitPane]]                                                                                                                      |
|                                                                                                                                                                                                                    |
| [      [SplitPane] SplitPane_Center = [new] [SplitPane]();]                                                     |
|                                                                                                                                                                                                                    |
| [      SplitPane_Center.ID = [\"SplitPane_Center\"];       ]                                                                                            |
|                                                                                                                                                                                                                    |
| [      SplitPane_Center.Controls.Add( [new] [LiteralControl]( [\"Center SplitPane\"] ) );]                    |
|                                                                                                                                                                                                                    |
| [      splitter.Items.Add( SplitPane_Center );]                                                                                                                                |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create SplitterBar]]                                                                                                                           |
|                                                                                                                                                                                                                    |
| [      [SplitterBar] splitterbar2 = [new] [SplitterBar]();]                                                     |
|                                                                                                                                                                                                                    |
| [      splitterbar2.ID = [\"SplitterBar2\"];]                                                                                                           |
|                                                                                                                                                                                                                    |
| [      splitterbar2.CollapseMode = [SplitterBarCollapseMode].Both;]                                                                                       |
|                                                                                                                                                                                                                    |
| [      splitter.Items.Add( splitterbar2 );]                                                                                                                                    |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create Right SplitPane]]                                                                                                                       |
|                                                                                                                                                                                                                    |
| [      [SplitPane] SplitPane_Right = [new] [SplitPane]();]                                                      |
|                                                                                                                                                                                                                    |
| [      SplitPane_Right.ID = [\"SplitPane_Right\"];         ]                                                                                            |
|                                                                                                                                                                                                                    |
| [      SplitPane_Right.Controls.Add( [new] [LiteralControl]( [\"Right SplitPane\"] ) );]                      |
|                                                                                                                                                                                                                    |
| [      splitter.Items.Add( SplitPane_Right );]                                                                                                                                 |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The result will look like this.

[] 

{border="0"}

Figure 393: Splitter control through code

[] 

Also you can create SlidingZones programmatically and add them to the Controls collection of existing SplitPane controls as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [protected][ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                    |
| [      [//create Splitter control]]                                                                                                                      |
|                                                                                                                                                                                                                    |
| [      [Splitter] splitter = [new] [Splitter]();]                                                               |
|                                                                                                                                                                                                                    |
| [      splitter.Layout = [SplitterLayout].Horizontal;]                                                                                                    |
|                                                                                                                                                                                                                    |
| [      splitter.Height = [Unit].Pixel( 300 );]                                                                                                            |
|                                                                                                                                                                                                                    |
| [      splitter.Width = [Unit].Pixel( 300 );]                                                                                                             |
|                                                                                                                                                                                                                    |
| [      form1.Controls.Add( splitter );]                                                                                                                                        |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create Left SplitPane for Left SlidingZone]]                                                                                                   |
|                                                                                                                                                                                                                    |
| [      [SplitPane] SplitPane_Left = [new] [SplitPane]();]                                                       |
|                                                                                                                                                                                                                    |
| [      SplitPane_Left.ID = [\"SplitPane_Left\"];]                                                                                                       |
|                                                                                                                                                                                                                    |
| [      splitter.Items.Add( SplitPane_Left );]                                                                                                                                  |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create Left SlidingZone]]                                                                                                                      |
|                                                                                                                                                                                                                    |
| [      [SlidingZone] SlidingZone_Left = [new] [SlidingZone]();]                                                 |
|                                                                                                                                                                                                                    |
| [      SlidingZone_Left.ID = [\"LeftSlidingZone\"];]                                                                                                    |
|                                                                                                                                                                                                                    |
| [      SlidingZone_Left.SlideDirection= [SplitterSlideDirection].Right;]                                                                                  |
|                                                                                                                                                                                                                    |
| [      SplitPane_Left.Controls.Add( SlidingZone_Left );]                                                                                                                       |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [for]( [int] i = 1; i \<= 3; i++ )]                                                                                           |
|                                                                                                                                                                                                                    |
| [      {]                                                                                                                                                                      |
|                                                                                                                                                                                                                    |
| [            [SlidingPane] slidingpane = [new] [SlidingPane]();]                                                |
|                                                                                                                                                                                                                    |
| [            slidingpane.ID = [\"LeftPane\"] + i;]                                                                                                      |
|                                                                                                                                                                                                                    |
| [            slidingpane.Title = [\"LeftPane\"] + i;]                                                                                                   |
|                                                                                                                                                                                                                    |
| [            slidingpane.Width = [Unit].Pixel( 120 );]                                                                                                    |
|                                                                                                                                                                                                                    |
| [            SlidingZone_Left.Items.Add( slidingpane );]                                                                                                                       |
|                                                                                                                                                                                                                    |
| [      }]                                                                                                                                                                      |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create SplitterBar]]                                                                                                                           |
|                                                                                                                                                                                                                    |
| [      [SplitterBar] splitterbar1 = [new] [SplitterBar]();]                                                     |
|                                                                                                                                                                                                                    |
| [      splitterbar1.ID = [\"SplitterBar1\"];]                                                                                                           |
|                                                                                                                                                                                                                    |
| [      splitterbar1.CollapseMode = [SplitterBarCollapseMode].Both;]                                                                                       |
|                                                                                                                                                                                                                    |
| [      splitter.Items.Add( splitterbar1 );]                                                                                                                                    |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create Center SplitPane]]                                                                                                                      |
|                                                                                                                                                                                                                    |
| [      [SplitPane] SplitPane_Center = [new] [SplitPane]();]                                                     |
|                                                                                                                                                                                                                    |
| [      SplitPane_Center.ID = [\"SplitPane_Center\"];       ]                                                                                            |
|                                                                                                                                                                                                                    |
| [      SplitPane_Center.Controls.Add( [new] [LiteralControl]( [\"Center SplitPane\"] ) );]                    |
|                                                                                                                                                                                                                    |
| [      splitter.Items.Add( SplitPane_Center );]                                                                                                                                |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create SplitterBar]]                                                                                                                           |
|                                                                                                                                                                                                                    |
| [      [SplitterBar] splitterbar2 = [new] [SplitterBar]();]                                                     |
|                                                                                                                                                                                                                    |
| [      splitterbar2.ID = [\"SplitterBar2\"];]                                                                                                           |
|                                                                                                                                                                                                                    |
| [      splitterbar2.CollapseMode = [SplitterBarCollapseMode].Both;]                                                                                       |
|                                                                                                                                                                                                                    |
| [      splitter.Items.Add( splitterbar2 );]                                                                                                                                    |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create Right SplitPane for Left SlidingZone]]                                                                                                  |
|                                                                                                                                                                                                                    |
| [      [SplitPane] SplitPane_Right = [new] [SplitPane]();]                                                      |
|                                                                                                                                                                                                                    |
| [      SplitPane_Right.ID = [\"SplitPane_Right\"];]                                                                                                     |
|                                                                                                                                                                                                                    |
| [      splitter.Items.Add( SplitPane_Right );]                                                                                                                                 |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [//create Right SlidingZone]]                                                                                                                     |
|                                                                                                                                                                                                                    |
| [      [SlidingZone] SlidingZone_Right = [new] [SlidingZone]();]                                                |
|                                                                                                                                                                                                                    |
| [      SlidingZone_Right.ID = [\"RightSlidingZone\"];]                                                                                                  |
|                                                                                                                                                                                                                    |
| [      SlidingZone_Right.SlideDirection= [SplitterSlideDirection].Left;]                                                                                  |
|                                                                                                                                                                                                                    |
| [      SplitPane_Right.Controls.Add( SlidingZone_Right );]                                                                                                                     |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                    |
| [      [for]( [int] i = 1; i \<= 3; i++ )]                                                                                           |
|                                                                                                                                                                                                                    |
| [      {]                                                                                                                                                                      |
|                                                                                                                                                                                                                    |
| [            [SlidingPane] slidingpane = [new] [SlidingPane]();]                                                |
|                                                                                                                                                                                                                    |
| [            slidingpane.ID = [\"RightPane\"] + i;               ]                                                                                      |
|                                                                                                                                                                                                                    |
| [            slidingpane.Title = [\"RightPane\"] + i;]                                                                                                  |
|                                                                                                                                                                                                                    |
| [            slidingpane.Width = [Unit].Pixel( 120 );]                                                                                                    |
|                                                                                                                                                                                                                    |
| [            SlidingZone_Right.Items.Add( slidingpane );]                                                                                                                      |
|                                                                                                                                                                                                                    |
| [      }           ]                                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The result will look like this.

[] 

{border="0"}

Figure 394: Splitting control with Sliding zones added through code

 

[]{#related-topics}

