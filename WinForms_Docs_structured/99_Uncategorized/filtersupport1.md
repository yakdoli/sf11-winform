---
title: filtersupport1.md
original_path: WinForms_Docs/99_Uncategorized/filtersupport1.md
created_at: 2025-08-05
---






#### Filter Support {#filter-support style="tab-stops: 0pt"}

Filter support is used to filter the matched list of items from the data source. It depends on the text entered in the AutoComplete textbox. AutoComplete allows you to filter the items using *IsFilter* property.

 

Adding Filter Support to an Application

If *IsFilter* property is set to True, once you enter the text in AutoComplete textbox the matched list of items will be displayed in the drop-down list. If this property is set to False, the matched list of items will not be displayed in the drop-down list; instead all the items will be displayed.

The following code illustrates the usage of *IsFilter* property:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][AutoComplete][ x][:][Name][=\"AutoComplete1\"][ IsFilter][=\"true\"/\>][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [AutoComplete][ autoComplete1 = [new] [AutoComplete]();]                                            |
|                                                                                                                                                                                                                                    |
| [this][.][autoComplete1][.IsFilter = [true];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Tables for property, and Event

 

Properties

           Table 9: Properties Table for Filter

  ---------- --------------------------------------------------------- -------------------- ------------ -----------------
  Property   Description                                               Type                 Data Type    Reference links
  IsFilter   Gets or sets the value of IsFilter in the AutoComplete.   DependencyProperty   bool(true)   NA
  ---------- --------------------------------------------------------- -------------------- ------------ -----------------

 

 

**Events**

Table 10: Events Table for Filter

+-----------------+---------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| Event           | Description                                                         | Arguments                          | Type                              | Reference links |
+-----------------+---------------------------------------------------------------------+------------------------------------+-----------------------------------+-----------------+
| IsFilterChanged | When the value of IsFilter is changed this event will be triggered. | DependencyObject,                  | DependencyPropertyChangedCallBack | NA              |
|                 |                                                                     |                                    |                                   |                 |
|                 | It cannot be cancelled.                                             | DependencyPropertyChangedEventArgs |                                   |                 |
+=================+=====================================================================+====================================+===================================+=================+

 

Sample Link

 

To access a Basic Core Features demo:

1.  Open the Syncfusion Dashboard.

2.  Click the **Windows Phones** drop-down list and select **Explore Samples**.

3.  Navigate to **WindowsPhoneSampleBrowser-\> Tools -\> AutoComplete Demo**

 

[]{#related-topics}

