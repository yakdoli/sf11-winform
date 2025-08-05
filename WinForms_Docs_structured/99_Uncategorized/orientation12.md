---
title: orientation12.md
original_path: WinForms_Docs/99_Uncategorized/orientation12.md
created_at: 2025-08-05
---






#### Orientation {#orientation style="LINE-HEIGHT: 12pt; TEXT-INDENT: -43.2pt; MARGIN: 10pt 0pt 0pt 43.2pt; tab-stops: 43.2pt"}

The Splitter control supports both horizontal and vertical orientations.

 

**Properties**

+-------------+--------------------------------------------------------------------+------------------+-----------------------------+-------------+
| Name        | Description                                                        | Type of Property | Value it Accepts            | Dependency  |
+-------------+--------------------------------------------------------------------+------------------+-----------------------------+-------------+
| Orientation | Specifies the orientation of the splitter: vertical or horizontal. | Enum             | Horizontal                  | NA          |
|             |                                                                    |                  |                             |             |
|             | Orientation.Horizontal                                             |                  | Vertical                    |             |
|             |                                                                    |                  |                             |             |
|             | Orientation.Vertical                                               |                  | Default value is Horizontal |             |
+-------------+--------------------------------------------------------------------+------------------+-----------------------------+-------------+

 

You can orient the Splitter control in two different ways:

**[Using Builder]**

The following steps guide you in configuring the orientation through Builder.

1.   In the **view**, invoke the **Splitter** helper with the splitter ID as the first argument, and enable the **Orientation** method with the desired option as its argument.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [\<%][=][Html.Syncfusion().Splitter([\"splitter\"])][.SplitterPanes(panes1=\>{ ] |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [panes1.Add().PaneSize([Unit].Percentage(50)).ContentTemplate(()=\>{[%\>]]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [             [\<][p][\>]inner first pane[\</][p][\>]]                                                              |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [\<%][}).SplitterBar(b=\>b.AllowSplitterBar([true])); ]                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [panes1.Add().PaneSize([Unit].Percentage(30)).ContentTemplate(()=\>{[%\>]]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [             [\<][p][\>]inner second pane[\</][p][\>]]                                                             |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [   [\<%]});]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [})]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                        |
| [.**Orientation([SplitterOrientation].Horizontal)** [%\>]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                        |
| [   ]                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**[]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\@{][Html.Syncfusion().Splitter([\"splitter\"])][.SplitterPanes(panes1=\>{ ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [panes1.Add().PaneSize([Unit].Percentage(50)).ContentTemplate(]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [@][\<][p][\>][inner first pane[\</][p][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [).SplitterBar(b=\>b.AllowSplitterBar([true])); ]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [panes1.Add().PaneSize([Unit].Percentage(30)).ContentTemplate(]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [         [@][\<][p][\>]inner second pane[\</][p][\>]]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [  );]                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [})]                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [.**Orientation([SplitterOrientation].Horizontal)**.Render() [}]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [   ]                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Run the application.

 

The following figures show the output.

**[]** 

{border="0"}[]

Figure 257: Horizontal Splitter Control

 

{border="0"}

Figure 258: Vertical Splitter Control

 

[]{#related-topics}

