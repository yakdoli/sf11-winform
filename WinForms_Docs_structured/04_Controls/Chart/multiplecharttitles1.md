---
title: multiplecharttitles1.md
original_path: WinForms_Docs/04_Controls/Chart/multiplecharttitles1.md
created_at: 2025-08-05
---








  









### Multiple Chart Titles {#multiple-chart-titles style="tab-stops: 0pt"}

 

Default Title

 

Essential Chart\'s **Title** property lets you edit the default title for a chart as follows. We can set font style for the title using **Title.Font** property. The default value is Verdana, 14, Regular.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                 |
| [//Default title]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                 |
| [chartControl1.Title.Text = \"Essential Chart\";]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                 |
| [this][.chartControl1.Title.Font = [new] System.Drawing.[Font]([\"Candara\"], 9F, System.Drawing.[FontStyle].Bold);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [\'Default title]                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [chartControl1.Title.Text = \"Essential Chart\"]                                                                                                                                       |
|                                                                                                                                                                                                                                          |
| [chartControl1.Title.Font = [New] System.Drawing.[Font]([\"Candara\"], 9F, System.Drawing.[FontStyle.]Bold)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 321: Chart Title Set

 

The above default chart title is simply the first in the list of titles that can be specified for the Chart.

 

Multiple Titles

 

[·      ]Multiple custom Chart Titles can be added to **Chart.Titles** Collection.

[·      ]Supports numerous docking styles (Floating, Left, Right, Bottom or Top) for each title.

[·      ]Each of the custom Titles can be aligned to any position as required.

 

Titles Positioning

 

Below listed properties will help you to modify the positioning of the Chart Title.

 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **ChartTitle Property**           | **Description**                                                                                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Position                          | Specifies the position relative to the chart at which to render the chart title panel.                                                                |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**Top** - above the chart(**Default setting**)                                                                  |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**Left** - left of the chart                                                                                    |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**Right** - right of the chart                                                                                  |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**Bottom** - below the chart                                                                                    |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**Floating** - will not be docked to any specific location. Can be docked manually by dragging the title panel. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | When docked to a side, this property specifies how the title panel should be aligned with respect to the chart boundaries.                            |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**Center** - will be aligned to center. **Default** **setting**.                                                |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**Far -** will be aligned Far.                                                                                  |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**Near** - will be aligned Near.                                                                                |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Behavior                          | Specifies the docking behavior of the title.                                                                                                          |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**Docking** - It is dockable on all four sides.                                                                 |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**Movable** - It is movable.                                                                                    |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**All** - It is movable and dockable.                                                                           |
|                                   |                                                                                                                                                       |
|                                   | [·      ]**None** - It is neither movable nor dockable.                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+


 

Title Look and Feel

 

There are several appearance options that can be applied on the ChartTitle instance as illustrated in this **ChartTitle Collection Editor**.

 

{border="0"}

 

Figure 322: ChartTitle Collection Editor

 

In code, you can add more titles to this list as follows.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [//Default title (the first entry in the Titles list)]                                                                                                   |
|                                                                                                                                                                                                            |
| [chartControl1.Title.Text = \"Essential Chart\";]                                                                                                        |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [// Add the title to the Chart control\'s Titles collection.                ]                                                                            |
|                                                                                                                                                                                                            |
| [ChartTitle][ title = [new] Syncfusion.Windows.Forms.Chart.[ChartTitle]();] |
|                                                                                                                                                                                                            |
| [title.Text = \"Custom Chart Title\";]                                                                                                                                 |
|                                                                                                                                                                                                            |
| [this][.chartControl1.Titles.Add(title);]                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| [\'Default title (the first entry in the Titles list)]                                                                                          |
|                                                                                                                                                                                                   |
| [chartControl1.Title.Text = \"Essential Chart\"]                                                                                                |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| **[\' ]**[Add the title to the Chart control\'s Titles collection.                ]           |
|                                                                                                                                                                                                   |
| [Dim][ title [As] [New] Syncfusion.Windows.Forms.Chart.ChartTitle] |
|                                                                                                                                                                                                   |
| [title.Text = \"Custom Chart Title\"]                                                                                                                         |
|                                                                                                                                                                                                   |
| [Me][.ChartControl1.Titles.Add(title)]                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 323: Chart with Multiple Chart Titles

 

Multiline Chart Title

 

You can now wrap the Chart titles and display them as multiline text. Set multiline title text in **ChartTitle.Text** property through designer as follows. Press ENTER key to begin a new line. Press CTRL+ENTER to set the text entered.

 

{border="0"}

 

Figure 324: Multiline Title for Essential Chart

 

[]{#related-topics}

