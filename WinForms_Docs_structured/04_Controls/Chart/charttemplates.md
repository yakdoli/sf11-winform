---
title: charttemplates.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\charttemplates.md
created_at: 2025-07-03
---








  









### Chart Templates {#chart-templates style="tab-stops: 0pt"}

[] 

Working with Chart Template

[] 

Essential Chart is now associated with the creation and loading of chart templates into the ChartControl. It provides easy methods to save and load the templates. This section will walk you through the saving, loading and resetting of the chart templates and the various benefits of using it.

[] 

Benefits

[] 

[·      ]Aesthetic items like appearance, positioning etc., of a chart can be saved in the template.

[·      ]Appearance settings saved in a Chart Template is reusable.

[·      ]Also stores any static data, if available in the chart.

[·      ]The user can save the existing structure of the chart control to an .xml file format.

[·      ]All the charts in your applications can be created with consistent look and feel.

[] 

{border="0"}

[] 

Figure 316: Saving Template through Context Menu

**[]** 

Save Template

[] 

The appearance settings for various components of a Chart like ChartSeries and ChartArea etc., are stored in a template, which can be loaded later into another different ChartControl.

 

A chart template can contain the properties of more than one data series. When such templates are loaded into a destination ChartControl, the appearance settings of the data series will be applied in a sequential order, i.e., the first set of appearance settings of a data series will be applied to the destination Chart\'s first series and the second set of appearance properties of the data series will be applied to the destination Chart\'s second series and so on.

 

If the destination collection\'s length is larger than the source collection, then the settings will repeat itself for these additional entries in the destination collection.

 

These Charts can be saved as templates in the below two ways.

[] 

[·      ]Selecting the **Save Template** option from the context menu as shown above.

[·      ]By clicking the **Save Template** designer verb in the Visual Studio property browser as shown above.

[·      ]ChartTemplate has a static method to save the data programmatically. We need to pass ChartControl instance and a file name(it can accept stream file also.), through this save method.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| **[]**                                                                                                                                                      |
|                                                                                                                                                                                                               |
| [ChartTemplate][.Save([this].ChartWebControl1, [\"TemplateName.xml\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                           |
|                                                                                                                                                                                                          |
| []                                                                                                                                                     |
|                                                                                                                                                                                                          |
| [ChartTemplate][.Save([Me].ChartWebControl1, [\"TemplateName.xml\"])] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Load Template

[] 

Essential Chart provides easy methods to load an already saved Chart template.

[] 

[·      ]At the design time, by selecting the **Load Template** from the context menu.

[·      ]By clicking the **Load Template** designer verb, in the Visual Studio property browser.

[] 

ChartTemplate has static method, to load the template data programmatically. We need to pass the ChartControl that will be applied with the loaded template data.

[] 

Reset Template

**[]** 

The ChartControl, which when loaded with a template will be applied with the appearance and other settings that were stored in the template. These settings can be reset and the Chart can be reverted back to its original appearance by using the below two methods.

[] 

[·      ]At the design time, by selecting the \"Reset Template..\" from the context menu.

[·      ]By clicking the \"Reset Template\" link in the Visual Studio property browser.

[] 

ChartTemplate can be reset using the following simple statements:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| **[]**                                                                                                                             |
|                                                                                                                                                                                      |
| [ChartTemplate][ ct = [new] [ChartTemplate]();] |
|                                                                                                                                                                                      |
| [ct.Reset([this].ChartWebControl1);]                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [ChartTemplate][ ct = [New] [ChartTemplate]()] |
|                                                                                                                                                                                 |
| [ct.Reset([Me].ChartWebControl1)]                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p257} 

[]{#related-topics}

