---
title: autoappendsupport1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\autoappendsupport1.md
created_at: 2025-07-03
---






#### Auto Append Support {#auto-append-support style="tab-stops: 0pt"}

Auto Append is used to guide the complete text by appending the entered text with suitable text from the data source, when a text is entered in the AutoComplete textbox. AutoComplete allows you to enable Auto Append using the *IsAutoAppend* property.

 

 

{border="0"}

Figure 19: Auto Append

 

Adding Auto Append Support to an Application

Set the *IsAutoAppend* property to True. The AutoComplete will guide you to complete the text, by appending the entered text with suitable text from the data source. If this property is set to False, the matched suitable text will not be appended with the entered text.

The following code illustrates how to enable Auto Append support to an Application: 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete1\"][ IsAutoAppend][=\"true\"/\>][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
| [AutoComplete][ autoComplete1 = [new] [AutoComplete]();]                                                |
|                                                                                                                                                                                                                                        |
| [this][.][autoComplete1][.IsAutoAppend = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

Tables for Property, and Event

 

Property

          Table 7: Property Table for Auto Append

  -------------- ------------------------------------------------------------- -------------------- ------------ -----------------
  Property       Description                                                   Type                 Data Type    Reference links
  IsAutoAppend   Gets or sets the value of IsAutoAppend in the AutoComplete.   DependencyProperty   bool(true)   
  -------------- ------------------------------------------------------------- -------------------- ------------ -----------------

 

 

Event

Table 8: Event Table for Auto Append

+---------------------+-------------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| Event               | Description                                                             | Arguments                          | Type                              | Reference links |
+---------------------+-------------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| IsAutoAppendChanged | When the value of IsAutoAppend is changed this event will be triggered. | DependencyObject,                  | DependencyPropertyChangedCallBack |                 |
|                     |                                                                         |                                    |                                   |                 |
|                     | This cannot be cancelled.                                               | DependencyPropertyChangedEventArgs |                                   |                 |
+=====================+=========================================================================+====================================+===================================+=================+

 

Sample Link

To access a Basic Core Features demo:

1.  Open the Syncfusion Dashboard.

2.  Click the **Windows Phones** drop-down list and select **Explore Samples**.

3.  Navigate to **WindowsPhoneSampleBrowser-\> Tools -\> AutoComplete Demo**

[]{#related-topics}

