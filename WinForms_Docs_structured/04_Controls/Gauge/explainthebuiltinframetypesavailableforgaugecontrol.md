---
title: explainthebuiltinframetypesavailableforgaugecontrol.md
original_path: WinForms_Docs/04_Controls/Gauge/explainthebuiltinframetypesavailableforgaugecontrol.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Explain the built-in frame types available for gauge control. {#explain-the-built-in-frame-types-available-for-gauge-control. style="tab-stops: 0pt"}

*OLAP Gauge* supports built-in frame types to provide effective rim styles. The *FrameType* property is used to set the frame type for the *Gauge* control.

 

The following are the frame types supported by *OLAP Gauge*.

[] 

[·      ]CircularWithInnerLeftGradient (Default)

[·      ]CircularWithDarkOuterFrames

[·      ]CircularCenterGradient

[·      ]CircularWithInnerTopGradient

[·      ]Full Circle

[·      ]HalfCircle

[] 

The following code example illustrates how to set the frame type for the OLAP Gauge control.

 

+----------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                 |
|                                                                                                                            |
|                                                                                                                            |
|                                                                                                                            |
| [this].olapGauge1.FrameType = [GaugeFrameType].CircularWithInnerLeftGradient; |
+----------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                              |
|                                                                                                                         |
|                                                                                                                         |
|                                                                                                                         |
| [Me].olapGauge1.FrameType = [GaugeFrameType].CircularWithInnerLeftGradient |
+-------------------------------------------------------------------------------------------------------------------------+

 

The following screen shots illustrate the various frame types.

 

{border="0"}

 

Figure 16: "CircularWithInnerLeftGradient" Frame Type

 

{border="0"}

 

Figure 17: "CircularWithDarkOuterFrames" Frame Type

***[]***  

***[]***  

 

 

{border="0"}

 

Figure 18: "CircularCenterGradient" Frame Type

 

{border="0"}

 

Figure 19: "CircularWithInnerTopGradient" Frame Type

***[]***  

 

 

{border="0"}

Figure 20: "Full Circle" Frame Type

 

 

{border="0"}

Figure 21: "Half Circle" Frame Type

Sample Location

**[]**  

A sample demo is available at the following location:

**..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\WPF\\OlapGauge.WPF\\Samples\\Gauge Customization\\Customization Demo\\**

[]{#related-topics}

