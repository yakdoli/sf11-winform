---
title: localization19.md
original_path: WinForms_Docs/99_Uncategorized/localization19.md
created_at: 2025-08-05
---








  









## Localization {#localization style="tab-stops: 0pt"}

Localization allows a chart to display data according to the language and culture specific to a particular country or region.

 

Essential Chart now supports localization; built-in resource files for specific languages can be easily added.  Context menu items, exception messages, and some of the toolbar items can be localized.

 

**Use Case Scenario**

This enables you to localize any part of the chart that has static strings in it.

 

Properties

 


  ------------------------------------- ---------------------------------------------- ------------- -------------------------------------------------------------------------------------------------------- ----------------- --------------
  Property                              Description                                    Type          Data Type                                                                                                Reference links   Dependencies
  Localize[ ]   Get or set the localization culture of Grid.   Server side   A string containing the name of the target System.Globalization.CultureInfo[ ]   NA                NA
  ------------------------------------- ---------------------------------------------- ------------- -------------------------------------------------------------------------------------------------------- ----------------- --------------


 

Adding Localization to an application

 

1.   Create your localization resource file (.resx) in the  **bin \> Debug** folder with the following naming convention:

 

[·      ]**ChartControl.\<your culture info name\>.resx**

***[]*** 


Note: It is mandatory to follow this naming convention.


 

 

{border="0"}

Figure 366: Resource File

 

2.   Enter the UI name in the Name column and the equivalent term you want in the Value column of the resource file.

 

[{border="0"}]

Figure 367: Default English resource file

 


Note: It is mantatory to specify equivalent terms for all static element to localize the chart.


 

3.   Specify the culture using the *Localize* property as given in the following code:

 

+-------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                        |
|                                                                                                                               |
| [this][.chartControl1.Localize="de-DE";] |
+-------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------+
| \[VB\]                                                                                                                     |
|                                                                                                                            |
| [Me][.chartControl1.Localize="de-DE"] |
+----------------------------------------------------------------------------------------------------------------------------+

 

 {border="0"}

Figure 368: Localized Chart

 

Sample Link

To view a sample

1.   Open the Syncfusion Dashboard.

2.   Select User Interface \> Windows Forms.

3.   Click Run Samples.

4.   Navigate to **Culture Localization \> Localization sample**.

 

You can find the resource file for the localization in English at the following location:

 

[[ChartControl_Resource]{.UGHyperlink}](http://www.syncfusion.com/uploads/redirect.aspx?&team=support&file=ChartControl_Resource-1347262360.zip)[]{.UGHyperlink}

 

[]{#related-topics}

