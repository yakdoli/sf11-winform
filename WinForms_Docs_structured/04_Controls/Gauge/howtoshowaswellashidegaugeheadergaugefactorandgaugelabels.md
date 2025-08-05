---
title: howtoshowaswellashidegaugeheadergaugefactorandgaugelabels.md
original_path: WinForms_Docs/04_Controls/Gauge/howtoshowaswellashidegaugeheadergaugefactorandgaugelabels.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### How to show as well as hide gauge header, gauge factor and gauge labels? {#how-to-show-as-well-as-hide-gauge-header-gauge-factor-and-gauge-labels style="tab-stops: 0pt"}

The *OLAP Gauge* control provides support to customize the header, which displays the measure and KPI name. The *ShowGaugeHeader* property allows you to show or hide the gauge header. If the property is set to true it displays the gauge header.If it is false, then it hides the gauge header. Similarly *ShowGaugeFactors* and *ShowGaugeLabels* properties are used for showing and hiding the gauge factors and labels. The following is the code snippet.

 

+-----------------------------------------------------------------------+
| **\[C#\]**                                                            |
|                                                                       |
|                                                                       |
|                                                                       |
| [this].olapGauge1.ShowGaugeHeaders = true;       |
|                                                                       |
| [this].olapGauge1.ShowGaugeFactors = true;       |
|                                                                       |
| [this].olapGauge1.ShowGaugeLabels = true;        |
+-----------------------------------------------------------------------+

 

+-----------------------------------------------------------------------+
| **\[VB\]**                                                            |
|                                                                       |
|                                                                       |
|                                                                       |
| [Me].olapGauge1.ShowGaugeHeaders = True          |
|                                                                       |
| [Me].olapGauge1.ShowGaugeFactors = True          |
|                                                                       |
| [Me].olapGauge1.ShowGaugeLabels = True           |
+-----------------------------------------------------------------------+

 

The following screen shot shows the output:

[] 

{border="0"}

 

Figure 13:  Showing gauge header, factors and labels

 

+-----------------------------------------------------------------------+
| **\[C#\]**                                                            |
|                                                                       |
|                                                                       |
|                                                                       |
| [this].olapGauge1.ShowGaugeHeaders = false;      |
|                                                                       |
| [this].olapGauge1.ShowGaugeFactors = false;      |
|                                                                       |
| [this].olapGauge1.ShowGaugeLabels = false;       |
+-----------------------------------------------------------------------+

 

+-----------------------------------------------------------------------+
| **\[VB\]**                                                            |
|                                                                       |
|                                                                       |
|                                                                       |
| [Me].olapGauge1.ShowGaugeHeaders = False         |
|                                                                       |
| [Me].olapGauge1.ShowGaugeFactors = False         |
|                                                                       |
| [Me].olapGauge1.ShowGaugeLabels = False          |
+-----------------------------------------------------------------------+

 

The following screen shot shows the output:

 

                       

{border="0"}

 

Figure 14: Hiding gauge header, factors and labels

***[]***  

Sample Location

**[]**  

A sample demo is available at the following location:

**..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\WPF\\OLAPGauge.WPF\\Samples\\Product ShowCase\\Product Showcase Demo\\**

 

[]{#related-topics}

