---
title: callbackfeature.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\callbackfeature.md
created_at: 2025-07-03
---








  









## CallBack Feature {#callback-feature style="tab-stops: 0pt"}

[] 

The ChartWebControl has a **RefreshFrequency** property, which can be used to enable AJAX style callbacks at specific intervals. For example, if this property is set to **2000**, then for every 2 seconds it will automatically trigger the **RefreshCallback** event in the server where you can update the chart data.

 

On the client side, we can trigger this event by calling the **ChartClientObjectId.Callback()** method. The parameter passed in this method can be received using *CallbackArgument* parameter of the **RefreshCallback** event.

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX/Java Script\]]**                                        |
|                                                                                                                     |
| []                                                                |
|                                                                                                                     |
| [function][ TriggerCallback()] |
|                                                                                                                     |
| [{]                                                                             |
|                                                                                                                     |
| [  Chart1.callback([\"MyCustomArgs\"]);]                 |
|                                                                                                                     |
| [}]                                                                             |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                       |
| [protected][ [void] ChartWebControl1_RefreshCallback([object] sender, Syncfusion.Web.UI.WebControls.Tools.[CallbackEventArgs] e)] |
|                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                       |
| [   if][(e.CallbackArgument == \"MyCustomArgs\")]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                       |
| [   [// Do something on the chart.]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Protected][ [Sub] ChartWebControl1_RefreshCallback([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Web.UI.WebControls.Tools.CallbackEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [  ][If][ ][e.][CallbackArgument = \"MyCustomArgs\" [Then]]                                                 |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [   \'Do something on the chart.]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Scripts used on Callbacks

**[]** 


  ------------------------------------- ------------------------------------------------------------
  Chart Control                         Description
  BeforeCallBackScript                  Script executed before a callback request gets processed.
  AfterCallbackScript                   Script executed after the callback request gets processed.
  BeforeCallbackResponseProcessScript   Script executed before the callback result gets processed.
  AfterCallbackResponseProcessScript    Script executed after the callback result gets processed.
  ------------------------------------- ------------------------------------------------------------


[]{#p259} 

[]{#related-topics}

