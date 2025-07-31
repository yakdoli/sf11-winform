---
title: automaticoutlining.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\automaticoutlining.md
created_at: 2025-07-03
---






#### Automatic Outlining {#automatic-outlining style="tab-stops: 0pt"}

 

**Outlining** can be performed by having appropriate \"lexem\", \"split\", and \"extension\" tag entries in the configuration file. Refer to the [Configuration Settings]{.UGHyperlink} topic for more information regarding the configuration file.

 

Essential Edit provides Visual Studio-like support for collapsing and expanding blocks of code through the use of Collapsers (plus-minus buttons). Sections of code which form the outlining blocks can be specified by using the configuration settings. The outlining blocks can be specified for code as well as for plain text.

 

Setting the **ShowOutliningCollapsers** property to **True**, will enable Automatic Outlining. Edit provides the following APIs to support Outlining.

 


  ---------------------- ----------------------------------------------------------------------------------
  Edit Control Method    Description
  Collapse               Collapses all regions in currently selected area or in the current line.
  Expand                 Expands all collapsed regions in currently selected area or in the current line.
  SwitchCollapsingOn     Turns on collapse and collapse all option.
  SwitchCollapsingOff    Turns off collapse option.
  CollapseAll            Collapses all regions.
  ExpandAll              Expands all collapsed regions.
  ToggleLineCollapsing   Toggles collapse option for current line.
  ---------------------- ----------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [// Enabling Automatic Outlining.]                                                                              |
|                                                                                                                                                                   |
| [this][.editControl1.ShowOutliningCollapsers = [true];] |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [// Collapses all regions in currently selected area or in the current line.]                                   |
|                                                                                                                                                                   |
| [this][.editControl1.Collapse();]                                            |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [// Expands all collapsed regions in currently selected area or in the current line.]                           |
|                                                                                                                                                                   |
| [this][.editControl1.Expand();]                                              |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [// Turns on collapse and collapse all option.]                                                                 |
|                                                                                                                                                                   |
| [this][.editControl1.SwitchCollapsingOff();]                                 |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [// Turns off collapse option.]                                                                                 |
|                                                                                                                                                                   |
| [this][.editControl1.SwitchCollapsingOn();]                                  |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [// Collapses all regions.]                                                                                     |
|                                                                                                                                                                   |
| [this][.editControl1.CollapseAll();]                                         |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [// Expands all collapsed regions.]                                                                             |
|                                                                                                                                                                   |
| [this][.editControl1.ExpandAll();]                                           |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [// Toggles collapse option for current line.]                                                                  |
|                                                                                                                                                                   |
| [this][.editControl1.ToggleLineCollapsing();]                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [\' Enabling Automatic Outlining.]                                                                           |
|                                                                                                                                                                |
| [Me][.editControl1.ShowOutliningCollapsers = [True]] |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [\' Collapses all regions in currently selected area or in the current line.]                                |
|                                                                                                                                                                |
| [Me][.editControl1.Collapse()]                                            |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [\' Expands all collapsed regions in currently selected area or in the current line.]                        |
|                                                                                                                                                                |
| [Me][.editControl1.Expand()]                                              |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [\' Turns on collapse and collapse all option.]                                                              |
|                                                                                                                                                                |
| [Me][.editControl1.SwitchCollapsingOff()]                                 |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [\' Turns off collapse option.]                                                                              |
|                                                                                                                                                                |
| [Me][.editControl1.SwitchCollapsingOn()]                                  |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [\' Collapses all regions.]                                                                                  |
|                                                                                                                                                                |
| [Me][.editControl1.CollapseAll()]                                         |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [\' Expands all collapsed regions.]                                                                          |
|                                                                                                                                                                |
| [Me][.editControl1.ExpandAll()]                                           |
|                                                                                                                                                                |
| []                                                                                                                         |
|                                                                                                                                                                |
| [\' Toggles collapse option for current line.]                                                               |
|                                                                                                                                                                |
| [Me][.editControl1.ToggleLineCollapsing()]                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Outlining Operations**

[] 

The Edit Control supports the following events to handle the various Outlining operations.

 


  ------------------------- ------------------------------------------------
  Edit Control Event        Description
  OutliningBeforeCollapse   Occurs before the region is about to collapse.
  OutliningBeforeExpand     Occurs before the region is about to expand.
  OutliningCollapse         Occurs when the region collapses.
  OutliningExpand           Occurs when the region expands.
  CollapsedAll              Occurs when CollapseAll method was called.
  ExpandedAll               Occurs when ExpandedAll method was called.
  CollapsingAll             Occurs when CollapseAll method is called.
  ExpandingAll              Occurs when ExpandAll method is called.
  ------------------------- ------------------------------------------------


 

The above events can be canceled, and can be used to optionally cancel the Outlining Collapse and Expand operations respectively. They are discussed in detail in the Edit Control Events section.

 

The Custom Outlining Demo sample demonstrates how the outlining feature can be used on any custom file or plain text, and not necessarily on programming language code samples. This sample is available in the following location.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Edit.Windows\\Samples\\2.0\\Text Formatting\\CustomOutliningDemo***

 

 

More:





