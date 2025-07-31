---
title: multiplecharttitles.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\multiplecharttitles.md
created_at: 2025-07-03
---








  









### Multiple Chart Titles {#multiple-chart-titles style="tab-stops: 0pt"}

**[]** 

Default Title

**[]** 

Essential Chart\'s **Title** property lets you edit the default title for a chart as follows. We can set font style for the title using **Title.Font** property. The default value is Verdana, 14, Regular.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                    |
| [//Default title]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                    |
| [ChartWebControl1.Title.Text = \"Essential Chart\";]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| [this][.ChartWebControl1.Title.Font = [new] System.Drawing.[Font]([\"Candara\"], 9F, System.Drawing.[FontStyle].Bold);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [\'Default title]                                                                                                                                                                         |
|                                                                                                                                                                                                                                             |
| [ChartWebControl1.Title.Text = \"Essential Chart\"]                                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [ChartWebControl1.Title.Font = [New] System.Drawing.[Font]([\"Candara\"], 9F, System.Drawing.[FontStyle.]Bold)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 302: Chart Title Set

[] 

The above default chart title is simply the first in the list of titles that can be specified for the Chart.

[] 

Multiple Titles

**[]** 

[·      ]Multiple custom Chart Titles can be added to **Chart.Titles** Collection.

[·      ]Supports numerous docking styles (Floating, Left, Right, Bottom or Top) for each title.

[·      ]Each of the custom Titles can be aligned to any position as required.

**[]** 

Titles Positioning

[] 

Below listed properties will help you to modify the positioning of the Chart Title.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ChartTitle Properties             | Description                                                                                                                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Position                          | Specifies the position relative to the chart at which to render the chart title panel.                                     |
|                                   |                                                                                                                            |
|                                   | Top - above the chart(**Default setting**)                                                                                 |
|                                   |                                                                                                                            |
|                                   | Left - left of the chart                                                                                                   |
|                                   |                                                                                                                            |
|                                   | Right - right of the chart                                                                                                 |
|                                   |                                                                                                                            |
|                                   | Bottom - below the chart                                                                                                   |
|                                   |                                                                                                                            |
|                                   | Floating - will not be docked to any specific location. Can be docked manually by dragging the title panel.                |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Alignment                         | When docked to a side, this property specifies how the title panel should be aligned with respect to the chart boundaries. |
|                                   |                                                                                                                            |
|                                   | Center - will be aligned to center. **Default** **setting**.                                                               |
|                                   |                                                                                                                            |
|                                   | Far - will be aligned Far.                                                                                                 |
|                                   |                                                                                                                            |
|                                   | Near - will be aligned Near.                                                                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------+


**[]** 

Adding Chart Title

**[]** 

In code, you can add more titles to this list as follows.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                     |
|                                                                                                                                                                                    |
| **[]**                                                                                                                           |
|                                                                                                                                                                                    |
| [ChartTitle][ title1 = [new] [ChartTitle]();] |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [//Set the text for the char title.]                                                                                             |
|                                                                                                                                                                                    |
| [title1.Text = [\"Custom Chart Title\"];]                                                                               |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [//Set the position of the chart title.]                                                                                         |
|                                                                                                                                                                                    |
| [title1.Position = ChartTextPosition.Bottom;]                                                                                                  |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [//Set the font size and name for the chart title.]                                                                              |
|                                                                                                                                                                                    |
| [title1.Font = [new] Font([\"Arial\"], 9);]                                                       |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [//Set the chart title forecolor]                                                                                                |
|                                                                                                                                                                                    |
| [title1.ForeColor = Color.White;]                                                                                                              |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [//Added chart title to the title collection.]                                                                                   |
|                                                                                                                                                                                    |
| [this][.ChartWebControl1.Titles.Add(title1);]                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                    |
|                                                                                                                                                                       |
| **[]**                                                                                                              |
|                                                                                                                                                                       |
| [Dim][ title1 [As] [New] ChartTitle()] |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\'Set the text for the char title.]                                                                                |
|                                                                                                                                                                       |
| [title1.Text = [\"Custom Chart Title\"]]                                                                   |
|                                                                                                                                                                       |
| []                                                                                                                 |
|                                                                                                                                                                       |
| [\'Set the position of the chart title.]                                                                            |
|                                                                                                                                                                       |
| [title1.Position = ChartTextPosition.Bottom]                                                                                      |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\'Set the font size and name for the chart title.]                                                                 |
|                                                                                                                                                                       |
| [title1.Font = [New] Font([\"Arial\"], 9)]                                            |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\'Set the chart title forecolor]                                                                                   |
|                                                                                                                                                                       |
| [title1.ForeColor = Color.White]                                                                                                  |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\'Added chart title to the title collection.]                                                                      |
|                                                                                                                                                                       |
| [Me][.ChartWebControl1.Titles.Add(title1)]                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 303: Chart with Multiple Chart Titles

**[]** 

You can insert a new title into an existing title collection or remove a title from the collection using the following methods.

[] 


  -------------------- -------------------------------------------------------------------------------------------------------
  ChartTitle Methods   Description
  RemoveAt             Removes the title at the specified index, which is passed as parameter.
  Insert               Inserts a new title to the title collection at the specified index and with the title name specified.
  -------------------- -------------------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                           |
|                                                                                                                                          |
| []                                                                                                   |
|                                                                                                                                          |
| [//Removes the title at index 1]                                                       |
|                                                                                                                                          |
| [this][.ChartWebControl1.Titles.RemoveAt(1);]       |
|                                                                                                                                          |
| [//Inserts a new title at index 1]                                                     |
|                                                                                                                                          |
| [this][.ChartWebControl1.Titles.Insert(1, title1);] |
+------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                    |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [\'Removes the title at index 1]                                                    |
|                                                                                                                                       |
| [Me][.ChartWebControl1.Titles.RemoveAt(1)]       |
|                                                                                                                                       |
| [\'Inserts a new title at index 1]                                                  |
|                                                                                                                                       |
| [Me][.ChartWebControl1.Titles.Insert(1, title1)] |
+---------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Multiline Chart Title

[] 

You can now wrap the Chart titles and display them as multiline text. Set multiline title text in **ChartTitle.Text** property through designer as follows. Press ENTER key to begin a new line. Press CTRL+ENTER to set the text entered.

[] 

{border="0"}

[] 

Figure 304: Multiline Title for Essential Chart

**[]** 

A sample which demonstrates the above features is available in the following sample installation path.

\<Install Location\>\\Syncfusion\\EssentialStudio\\\<***Version Number***\>\\Web\\chart.web\\Samples\\3.5\\Chart Title and Legends\\Multiple Chart Titles

[]{#p210} 

[]{#related-topics}

