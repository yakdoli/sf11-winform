---
title: clientsidemethods12.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsidemethods12.md
created_at: 2025-07-03
---






#### Client-Side Methods {#client-side-methods style="tab-stops: 0pt"}

The Toggle-Button supports a set of Client-Side methods to control its behavior.

[] 

Use Case Scenarios

It allows for easy customization of the behavior of the Toggle-Button.

[] 

Adding Client-Side Methods to an Application

The following steps guide you in using the Client-Side methods:

[] 

1.   In **View**, invoke the ToggleButton helper with the Button id as the first argument followed by their methods.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                               |
|                                                                                                                                                                                      |
| [        [\<%][=]Html.Syncfusion().ToggleButton([\"myToggleButton \"])] |
|                                                                                                                                                                                      |
| [        .Text([\"Save\"])]                                                                                              |
|                                                                                                                                                                                      |
| [        .Skin([Skins].Almond)]                                                                                          |
|                                                                                                                                                                                      |
| [        .IsChecked = [true],]                                                                                              |
|                                                                                                                                                                                      |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                         |
|                                                                                                                                                                                      |
| [        .ContentType([ContentTypes].TextAndImage)]                                                                      |
|                                                                                                                                                                                      |
| [        [%\>]]                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                             |
|                                                                                                                                                                                      |
| [        [\@{][ ]Html.Syncfusion().ToggleButton([\"myToggleButton \"])] |
|                                                                                                                                                                                      |
| [        .Text([\"Save\"])]                                                                                              |
|                                                                                                                                                                                      |
| [        .Skin([Skins].Almond)]                                                                                          |
|                                                                                                                                                                                      |
| [        .IsChecked = [true],]                                                                                              |
|                                                                                                                                                                                      |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                                         |
|                                                                                                                                                                                      |
| [        .ContentType([ContentTypes].TextAndImage)]                                                                      |
|                                                                                                                                                                                      |
| [        .Render();]                                                                                                                             |
|                                                                                                                                                                                      |
| [        [}]]                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.  In **Javascript**, use the methods to enable and disable an item as follows.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][script][ [type][=\"text/javascript\"\>]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [function] DisableButton() {]                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            [// Code to disable the Toggle-Button.]]                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            \$find([\"]][myToggleButton][\"][).Disable();]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [function] EnableButton() {]                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            [// Code to enable the Toggle-Button.]]                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            \$find([\"]][myToggleButton][\"][).Enable();]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [function] IsChecked(id) {]                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            [// Code to check the status of the Toggle-Button.]]                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            \$find([\"]][myToggleButton][\"][).][IsChecked][("][myToggleButton][");][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [ [\</][script][\>]]                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Run the application.

 

The output is shown in the following screenshot.

 

{border="0"}

Figure 302: Toggle-Button in disabled state

{border="0"}

Figure 303: Toggle-Button in enabled state

Methods

 

The following table illustrates the methods which describes the Client-Side methods of the Toggle-Button.

 

  Method      Description                                     Parameters   Type     Return Type   Reference links
  ----------- ----------------------------------------------- ------------ -------- ------------- -----------------
  Disable     Disables the Toggle-Button.                     \-           Client   \-            \-
  Enable      Enables the disabled Toggled-Button.            \-           Client   \-            \-
  IsChecked   To get the checked state of the Toggle-Button   \-           Client   \-            \-

[] 

Sample Link

To view the samples, follow the steps below.

1.   Open the **Tools** Sample Browser from the dashboard. (Refer to the Samples and Location chapter)

2.   Navigate to **Tools.Mvc -\> Button -\> Client-Side API**.

 

[]{#related-topics}

