---
title: addingasimplegaugetoanapplication.md
original_path: WinForms_Docs/04_Controls/Gauge/addingasimplegaugetoanapplication.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Adding a Simple Gauge to an application {#adding-a-simple-gauge-to-an-application style="tab-stops: 0pt"}

[] 

To create a simple Gauge control and populate it with simple data, follow the steps that are given below.

[] 

1.   Open **Microsoft Visual Studio**. Go to **File** menu and click **New Website**. In the New Website dialog box, select **ASP.NET Web Application** template, name the website and click **OK**.

[] 

{border="0"}

***[]***  

Figure 35: ASP.NET Web Application template selected in the New Project Dialog Box

[] 

A Web application is created:

[] 

2.   Open the main form of the application in the designer.

3.   Drag the **Gauge Web** control from the toolbox onto the web form.

[] 

{border="0"}

**[]**  

Figure 36: Gauge Web control in Toolbox

[ ] 

4.   Drag the Script Manager from the toolbox into the web form.

 


{border="0"}Note: It is mandatory to add Script Manager to the application. Without this you willnot be able to run the application.


 

**[]**  

5.   The data for the **Gauge** can be added through code. Switch to code view in VS.NET and add the method shown below.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                           |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [protected] [ [void] Page_Load([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [   BuildCircularGauge();]                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [private] [ [void] BuildCircularGauge()]                                                                     |
|                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [        CircularGauge] [ gauge1 = [new][CircularGauge]();]                       |
|                                                                                                                                                                                                                        |
| [        gauge1.ID = [\"CircularGauge1\"];]                                                                                                                |
|                                                                                                                                                                                                                        |
| [        gauge1.Radius = 160;]                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| [        gauge1.Height = [Unit].Pixel(200);]                                                                                                               |
|                                                                                                                                                                                                                        |
| [        gauge1.Width = [Unit].Pixel(400);]                                                                                                                |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [CircularScale] scale1 = [new][CircularScale]();]                                                    |
|                                                                                                                                                                                                                        |
| [        scale1.Minimum = 0;]                                                                                                                                                      |
|                                                                                                                                                                                                                        |
| [        scale1.Maximum = 100;]                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [        scale1.MinorIntervalValue = 2;]                                                                                                                                           |
|                                                                                                                                                                                                                        |
| [        scale1.MajorIntervalValue = 5;]                                                                                                                                           |
|                                                                                                                                                                                                                        |
| [        scale1.Location = [new][Point](50, 50);]                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [CircularGaugeTick] tick1 = [new][CircularGaugeTick]();]                                             |
|                                                                                                                                                                                                                        |
| [        tick1.TickStyle = [TickStyle].MajorInterval;]                                                                                                     |
|                                                                                                                                                                                                                        |
| [        scale1.Ticks.Add(tick1);]                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [CircularGaugeTick] tick2 = [new][CircularGaugeTick]();]                                             |
|                                                                                                                                                                                                                        |
| [        tick2.TickStyle = [TickStyle].MinorInterval;]                                                                                                     |
|                                                                                                                                                                                                                        |
| [        scale1.Ticks.Add(tick2);]                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [CircularGaugeLabel] label1 = [new][CircularGaugeLabel]();]                                          |
|                                                                                                                                                                                                                        |
| [        label1.LabelStyle = [TickStyle].MajorInterval;]                                                                                                   |
|                                                                                                                                                                                                                        |
| [        scale1.Labels.Add(label1);]                                                                                                                                               |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [CircularPointer] pointer1 = [new][CircularPointer]();]                                              |
|                                                                                                                                                                                                                        |
| [        pointer1.NeedleStyle = [NeedleStyle].Arrow;]                                                                                                      |
|                                                                                                                                                                                                                        |
| [        pointer1.PointerLength = 95;]                                                                                                                                             |
|                                                                                                                                                                                                                        |
| [        pointer1.PointerWidth = 10;]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [        scale1.Pointers.Add(pointer1);  ]                                                                                                                                         |
|                                                                                                                                                                                                                        |
| [        ]                                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| [        gauge1.Scales.Add(scale1);]                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [   ]                                                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [        [this].Form.Controls.Add(gauge1);]                                                                                                                   |
|                                                                                                                                                                                                                        |
| [}[]]                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Private] [ [Sub] Page_Load([ByVal] sender [As][Object], [ByVal] e [As] System.EventArgs) [Handles][MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        BuildCircularGauge()]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [End] [ [Sub] ]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [Public] [ [Sub] BuildCircularGauge ()]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        Dim] [ gauge1 [As][New][CircularGauge]()]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        gauge1.ID = [\"CircularGauge1\"]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        gauge1.Radius = 160]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        gauge1.Height = [Unit].Pixel(200)]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        gauge1.Width = [Unit].Pixel(400)]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        [Dim] scale1 [As][New][CircularScale]()]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.Minimum = 0]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.Maximum = 100]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.MinorIntervalValue = 2]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.MajorIntervalValue = 5]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.Location = [New] Point(50, 50)]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        [Dim] tick1 [As][New][CircularGaugeTick]()]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        tick1.TickStyle = [TickStyle].MajorInterval]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.Ticks.Add(tick1)]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        [Dim] tick2 [As][New][CircularGaugeTick]()]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        tick2.TickStyle = [TickStyle].MinorInterval]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.Ticks.Add(tick2)]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        [Dim] label1 [As][New][CircularGaugeLabel]()]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        label1.LabelStyle = [TickStyle].MajorInterval]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.Labels.Add(label1)]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        [Dim] pointer1 [As][New][CircularPointer]()]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        pointer1.NeedleStyle = [NeedleStyle].Arrow]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        pointer1.PointerLength = 95]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        pointer1.PointerWidth = 10]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        scale1.Pointers.Add(pointer1)]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        gauge1.Scales.Add(scale1)]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        [Me].Form.Controls.Add(gauge1)]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [End] [ [Sub] [] ]                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

6.   Now try running the project by selecting the **Debug** **→ Start Debugging**. The gauge will appear as shown below:

[] 

{border="0"}

**[]**  

Figure 37: Gauge Control

**[]** []{.UGHyperlink} 

[]{#p13} 

[] 

 

 

[] 


 


[]{.UGHyperlink} 

[]{#p14} 

[]{#related-topics}

