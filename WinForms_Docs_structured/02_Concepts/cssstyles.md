---
title: cssstyles.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\cssstyles.md
created_at: 2025-07-03
---






##### CSS Styles {#css-styles style="tab-stops: 0pt"}

[] 

The look and feel of the control can be customized using the css properties which has been discussed below.

[] 

Customizing the Button

[  ]

The button image on the right of the control can be customized, and styles can be set using the **ButtonCssClass** and **ButtonHoverCssClass** properties.

[] 


  --------------------- -----------------------------------------------------------------------
  Property              Description
  ButtonCssClass        Specifies the css definitions to apply to the button\'s html element.
  ButtonHoverCssClass   Specifies the css definitions to apply for the button on mouse hover.
  --------------------- -----------------------------------------------------------------------


[] 

{border="0"}

[] 

Figure 133: Styles applied to the Button

[] 

{border="0"}

[] 

**[]** 

Figure 134: Styles applied for Button Hover

[           ]

The below given css definitions must be set to the above discussed properties to apply the styles to the button.

[] 

+-----------------------------------------------------------------------------------+
| [.BtnCSS]                     |
|                                                                                   |
| [{]                           |
|                                                                                   |
| [  border:1px solid #A0DEFF;] |
|                                                                                   |
| [  width:25px;]               |
|                                                                                   |
| [  cursor:pointer;]           |
|                                                                                   |
| [  background-Color:#A0DEFF;] |
|                                                                                   |
| [}]                           |
|                                                                                   |
| []                            |
|                                                                                   |
| [.BtnHoverCSS]                |
|                                                                                   |
| [{]                           |
|                                                                                   |
| [  border:1px solid #FFB26A;] |
|                                                                                   |
| [  width:25px;]               |
|                                                                                   |
| [  cursor:pointer;]           |
|                                                                                   |
| [  background-Color:#FFB26A;] |
|                                                                                   |
| [}]                           |
+-----------------------------------------------------------------------------------+

[] 

Customizing the TextBox

[] 

The TextBox can be customized by using the style properties such as **TextBoxCssClass** and **TextBoxHoverCssClass** which help to set different styles for the text and textbox.

[] 


  ---------------------- -----------------------------------------------------------------------------
  Property               Description
  TextBoxCssClass        Specifies the css definitions to apply to the text container.
  TextBoxHoverCssClass   Specifies the css definitions to apply to the text container on mouse over.
  ---------------------- -----------------------------------------------------------------------------


[] 

{border="0"}

[] 

Figure 135: Styles applied to the TextBox

[] 

{border="0"}

Figure 136

[] 

The below given css definitions must be set to the above discussed properties to apply the styles to both the text and textbox.

[] 

+-------------------------------------------------------------------------------------+
| [.TextBoxCSS]                   |
|                                                                                     |
| [{]                             |
|                                                                                     |
| [  color:#333365;]              |
|                                                                                     |
| [  font-name:tahoma;]           |
|                                                                                     |
| [  font-size:12px;]             |
|                                                                                     |
| [  font-weight:bold;]           |
|                                                                                     |
| [  background-Color:#d0f0ff;]   |
|                                                                                     |
| [  border:1px solid #d0f0ff;  ] |
|                                                                                     |
| [}]                             |
|                                                                                     |
| [.TextBoxHoverCSS]              |
|                                                                                     |
| [{]                             |
|                                                                                     |
| [  color:#ee7a03;]              |
|                                                                                     |
| [  font-name:tahoma;]           |
|                                                                                     |
| [  font-size:12px;]             |
|                                                                                     |
| [  font-weight:bold;]           |
|                                                                                     |
| [  background-Color:#ffe1c4;]   |
|                                                                                     |
| [  border:1px solid #ffe1c4;  ] |
|                                                                                     |
| [}]                             |
+-------------------------------------------------------------------------------------+

[] 

Customizing the TextBox Elements

[] 

Styles can be applied to the outer html elements of the textbox using the properties **ControlRootCssClass**, **ContainerHoverCSSClass** and **ContainerTableCssClass**. These properties can be used to apply styles to the various structured layers of the textbox.

[] 


  ------------------------ -------------------------------------------------------------------------------
  Property                 Description
  ContainerHoverCSSClass   Specifies the css definitions to apply to the container table on mouse hover.
  ContainerTableCssClass   Specifies the css definitions to apply to the container table.
  ControlRootCSSClass      Specifies the css definitions to use for the root elements of the control.
  ------------------------ -------------------------------------------------------------------------------


[] 

Customizing the Popup Container

[] 

The **PopupCSSClass** can be used to apply different styles to the container that pops-up on button click.

[] 


  ----------------------- ----------------------------------------------------------------------------------
  Property                Description
  PopupCssClass           Specifies the css definitions to apply to the control container\'s html element.
  ----------------------- ----------------------------------------------------------------------------------


[] 

{border="0"}

[] 

Figure 137: Styles applied to the Popup Container

 

[]{#related-topics}

