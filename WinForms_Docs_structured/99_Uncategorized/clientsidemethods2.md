---
title: clientsidemethods2.md
original_path: WinForms_Docs/99_Uncategorized/clientsidemethods2.md
created_at: 2025-08-05
---






#### Client-Side Methods {#client-side-methods style="tab-stops: 0pt"}

The Button control supports a set of Client-Side methods to control its behavior.

[] 

Use Case Scenarios

The Button control allows for easy customization of the behavior of the button.

**[]** 

Adding Client-Side Methods to an Application

The following steps guides you in using the Client-Side Methods.

[] 

1.   In View, invoke the normal Button helper with the button id as the first argument followed by the **Skin** methods.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                  |
|                                                                                                                                                                         |
| [        [\<%][=]Html.Syncfusion().Button([\"myButton\"])] |
|                                                                                                                                                                         |
| [        .Text([\"Save\"])]                                                                                 |
|                                                                                                                                                                         |
| [        .Skin([Skins].Almond)]                                                                             |
|                                                                                                                                                                         |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                            |
|                                                                                                                                                                         |
| [        .ContentType([ContentTypes].TextAndImage)]                                                         |
|                                                                                                                                                                         |
| [        [%\>]]                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                |
|                                                                                                                                                                         |
| [        [\@{][ ]Html.Syncfusion().Button([\"myButton\"])] |
|                                                                                                                                                                         |
| [        .Text([\"Save\"])]                                                                                 |
|                                                                                                                                                                         |
| [        .Skin([Skins].Almond)]                                                                             |
|                                                                                                                                                                         |
| [        .ImageUrl([\"Content/icon_save.png\"])]                                                            |
|                                                                                                                                                                         |
| [        .ContentType([ContentTypes].TextAndImage)]                                                         |
|                                                                                                                                                                         |
| [        .Render();]                                                                                                                |
|                                                                                                                                                                         |
| [        [}]]                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   In Javascript, use the methods to enable and disable an item as follows.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [\<][script][ [type][=\"text/javascript\"\>]]                               |
|                                                                                                                                                                                                                                                               |
| [        [function] DisableButton() {]                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [            [// Code to disable the Button.]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [            \$find([\"]][myButton][\"][).Disable();] |
|                                                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [        [function] EnableButton() {]                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [            [// Code to enable the Button.]]                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [            \$find([\"]][myButton][\"][).Enable();]  |
|                                                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [ [\</][script][\>]]                                                                                                                                    |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Run the application.

 

The output is shown in the following screenshot.

 

 

{border="0"}

Figure 90: Button in the disabled state

 

 

{border="0"}

Figure 91: Button in an enabled state

 

[] 

[] 

**Methods**

The following table illustrates the client-side methods of button.

 


  Method    Description                    Parameters   Type     Return Type   Reference links
  --------- ------------------------------ ------------ -------- ------------- -----------------
  Disable   Disables the button.           \-           Client   \-            \-
  Enable    Enables the disabled button.   \-           Client   \-            \-


[] 

Sample Link

To view the samples, follow the steps below:

1.   Open the Tools Sample Browser from the dashboard. (Refer to the Samples and Location chapter)

2.   Navigate to **Tools.Mvc -\> Button -\> Client-Side API.**

 

[]{#related-topics}

