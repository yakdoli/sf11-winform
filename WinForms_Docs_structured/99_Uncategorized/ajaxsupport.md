---
title: ajaxsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\ajaxsupport.md
created_at: 2025-07-03
---






##### AJAX Support {#ajax-support style="tab-stops: 0pt"}

[] 

AutoCompleteTextBox control has built in AJAX support that allows to refresh the data using Callbacks. The various client events that are invoked during the callback process are as follows.

[] 


+----------------------------------------+-----------------------------------------------------------------------------------------+
|                                        |                                                                                         |
|                                        |                                                                                         |
| Property                               | Description                                                                             |
+----------------------------------------+-----------------------------------------------------------------------------------------+
| AfterCallbackResponseProcessedScript   | Specifies the script that will be executed after callback result gets processed.        |
+----------------------------------------+-----------------------------------------------------------------------------------------+
| AfterCallbackScript                    | Specifies the script that will be executed after callback result is sent to the server. |
+----------------------------------------+-----------------------------------------------------------------------------------------+
| AutoPostBack                           | Specifies whether to postback the page when text is modified. Default value is False.   |
+----------------------------------------+-----------------------------------------------------------------------------------------+
| BeforeCallbackResponseProcessingScript | Specifies the script that will be executed before callback result gets processed.       |
+----------------------------------------+-----------------------------------------------------------------------------------------+
| BeforeCallbackScript                   | Specifies the script that will be executed before a callback result gets processed.     |
+----------------------------------------+-----------------------------------------------------------------------------------------+


[] 

To trigger the ajax client events, follow the below given steps.

[] 

1.   Create an application using data binding. For details, see [Creating AutoCompleteTextBox]{.UGHyperlink}.

2.   Define the script functions that should be executed and performed when the client functions are invoked.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[javascript\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                   |
| [function][ BeforeScript()]                                                                                                  |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [    document.getElementById([\'display\']).value+=[\"BeforeCallbackScript event is fired\"]+[\"\\n\"];] |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [function][ AfterScript()]                                                                                                   |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [    document.getElementById([\'display\']).value+=[\"AfterCallbackScript event is fired\"]+[\"\\n\"];]  |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Set the respective functions to the required client events.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[aspx\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][cc1][:][autocompletetextbox][ [id][=\"AutoCompleteTextBox1\"] [runat][=\"server\"] [datakeyfield][=\"Name\" ][rows][=\"2\"] [textmode][=\"SingleLine\" ][columns][=\"200\"] [datasourceid][=\"AccessDataSource2\" ][aftercallbackscript][=\"AfterScript(this)\"] [beforecallbackscript][=\"BeforeScript(this)\" ][precallbackscript][=\"PreCallbackScript(this)\"] [postcallbackscript][=\"PostCallbackScript(this)\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<%][\--template definitions\--][%\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\</][cc1][:][autocompletetextbox][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][textarea][ [id][=\"display\"] [rows][=\"1\"] [cols][=\"1\"] [style][=\"width: 200px; height: 200px;\"\>\</][textarea][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application. When the text is selected from the dropdown, the client events will be invoked displaying the names of the fired events.

 


  --------------- -----------------------------------------------------------------------------
  Properties      Description
  StatusBarText   Specifies the text to display on the browser\'s status bar during callback.
  --------------- -----------------------------------------------------------------------------


 


  ------------------ ----------------------------------------------------------------------------------
  Properties         Description
  CausesValidation   Specifies whether the control causes validation to fire. Default value is False.
  ValidationGroup    Specifies the group to be validated when the control causes a postback.
  ------------------ ----------------------------------------------------------------------------------


 


  ---------------------------------------- ---------------------------------------------------------------------------------------
  Properties                               Description
  AfterCallbackResponseProcessedScript     Specifies the script that will be executed after callback result gets processed.
  AutoPostBack                             Specifies whether to postback the page when text is modified. Default value is False.
  BeforeCallbackResponseProcessingScript   Specifies the script that will be executed before callback result gets processed.
  PostCallbackScript                       Specifies the script function to be executed after callback.
  PreCallbackScript                        Specifies the script function to be executed before callback.
  ---------------------------------------- ---------------------------------------------------------------------------------------


 


  ----------------- ------------------------------------------------------------------------------------
  Properties        Description
  DataColumnIndex   Specifies the column index for selecting the data in Template scenario.
  DataKeyField      Specifies the field to be displayed in the drop-down.
  DataMember        Specifies the table to bind to.
  DataSourceID      Specifies the id of the datasource to populate the values in AutoComplete control.
  ----------------- ------------------------------------------------------------------------------------


 

How do i specify which column data should be displayed in the textbox when more than 1 column is there? Irrespective of what I give in the DataKeyField property, the first column data is only displayed in the textbox. Is it suppose to work that way?

Is Columns used for only setting the width or any other purpose? If width can be set using this, when I give some value and enter multiple entries in the textbox, I am unable to find any width restriction.

When ReadOnly is set, unable to set focus on the control.

Tags appear initially when TextMode is set to Multiline. (Only once in the application, the ctrl was breaking when MultiLine was set.

Why css styles are not applied, when its set through stylesheet?

[]{#p33} 

[]{#related-topics}

