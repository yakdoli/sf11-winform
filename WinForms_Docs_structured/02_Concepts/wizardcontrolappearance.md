---
title: wizardcontrolappearance.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\wizardcontrolappearance.md
created_at: 2025-07-03
---






##### Wizard Control Appearance {#wizard-control-appearance style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section discusses the various appearance settings of the Wizard controls.

 

 

###### 3.13.1.4.5.1    Foreground Settings {#foreground-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Wizard Control Foreground

[] 

The appearance of the text in the Wizard control can be controlled using the **Font** and **ForeColor** properties.

[] 


  ----------- -----------------------------------------------------------------
  Property    Description
  Font        Sets the font style for the display text in the wizard control.
  ForeColor   Sets the fore color for the display text in the control.
  ----------- -----------------------------------------------------------------


[] 


 

{border="0"} Note: These WizardControl.Font property will be applied only to the Description text and the Button texts of the Wizard Page. WizardControl.ForeColor property will be applied to the Page Title and description text alone. To set Font style for Title and description, see [Title and Description Settings]{.UGHyperlink} topic.


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [//Foreground Settings for the display text ]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.wizardControl1.Font = ][new][ ][System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Regular);][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.wizardControl1.ForeColor = System.Drawing.[Color].DarkBlue;][]                                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1057}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [\'Foreground Settings for the display text ]                                                                                                                                                  |
|                                                                                                                                                                                                                                                  |
| [Me][.wizardControl1.Font = [New] System.Drawing.Font([\"Verdana\"], 8.25F, System.Drawing.FontStyle.Regular) ] |
|                                                                                                                                                                                                                                                  |
| [Me][.wizardControl1.ForeColor = System.Drawing.Color.DarkBlue][]                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1232: Font Style = \"Verdana 8\"; ForeColor = \"DarkBlue\"

[] 


{border="0"} Note: These settings can be overridden by the individual WizardPage.Font and WizardPage.ForeColor settings.


 

The foreground settings for the Button text can be overridden by the **WizardPage.Button.Font** and **WizardPage.Button.ForeColor** settings also. See [Button Appearance]{.UGHyperlink} topic.

[] 

Wizard Page Foreground

 

The font and fore color for the display text in a Wizard page can be controlled through below properties.

[] 


  ----------- --------------------------------------------------------------
  Property    Description
  Font        Sets the font style for the display text in the wizard page.
  ForeColor   Sets the fore color for the display text in the wizard page.
  ----------- --------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [this][.wizardControl1.Font = [new] System.Drawing.[Font]([\"Verdana\"], 8.25F, System.Drawing.[FontStyle].Regular);] |
|                                                                                                                                                                                                                                                                                                  |
| [this][.wizardControl1.ForeColor = System.Drawing.[Color].Black;][]                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1058}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [Me][.wizardControl1.Font = [New] System.Drawing.Font([\"Verdana\"], 8.25F, System.Drawing.FontStyle.Regular) ] |
|                                                                                                                                                                                                                                                  |
| [Me][.wizardControl1.ForeColor = System.Drawing.Color.Black][]                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 1233: Font Style = \"Courier New, 10, Bold\"; ForeColor = \"RoyalBlue\"

 

 

###### 3.13.1.4.5.2    Background Settings {#background-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Wizard Control Background

 

The background of the Wizard control can be customized through the below properties.

[] 


  ----------------------- -----------------------------------------------------------------
  Property                Description
  BackColor               Sets the back color for the Wizard control.
  BackgroundImage         Sets the background image for the Wizard control.
  BackgroundImageLayout   Sets the layout for the background image in the Wizard Control.
  ----------------------- -----------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                     |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                            |
| [this][.wizardControl1.BackColor = System.Drawing.[Color].LightSteelBlue;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1059}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                               |
|                                                                                                                                                                                                  |
| **[]**                                                                                                                                         |
|                                                                                                                                                                                                  |
| [Me][.wizardControl1.BackColor = System.Drawing.Color.LightSteelBlue][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1234: BackColor set for WizardControl**[]**

**[]** 


{border="0"} Note: By default the background settings of the Wizard control will be overridden by the Wizard Container background settings.


[] 

Banner Panel Background

[] 

The below properties lets you customize the[[ ]]{.UGHyperlink}[[[banner panel]]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Banner_Settings) in a Wizard Control.

[] 


  ----------------------- -----------------------------------------------------------------------------------------------------------------------------------
  Property                Description
  BackColor               Sets the back color for the banner panel.
  BackgroundColor         Sets a gradient background for the banner panel in the Wizard control. This overrides the BackColor property of the Banner panel.
  BackgroundImage         Sets the background image for the banner panel.
  BackgroundImageLayout   Sets the layout for the background image in the banner panel.
  ----------------------- -----------------------------------------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [this][.gradientPanel1.BackgroundColor = [new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Vertical, System.Drawing.[Color].AliceBlue, System.Drawing.[Color].LightSteelBlue);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1060}[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                             |
| [Me][.gradientPanel1.BackgroundColor = [New] Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.AliceBlue, System.Drawing.Color.LightSteelBlue) ][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1235: Gradient Background set for Banner Panel

**[]** 

Wizard Page Background

[] 

The below properties lets you customize the [[[Wizard page]]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Wizard_Page_Settings) in a Wizard Control.

[] 


  ----------------------- -----------------------------------------------------------------------------------------------------------------------------------
  Property                Description
  BackColor               Sets the back color for the banner panel.
  BackgroundColor         Sets a gradient background for the banner panel in the Wizard control. This overrides the BackColor property of the Banner panel.
  BackgroundImage         Sets the background image for the banner panel.
  BackgroundImageLayout   Sets the layout for the background image in the banner panel.
  ----------------------- -----------------------------------------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [this][.wizardControlPage2.BackgroundColor = [new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].PathRectangle, System.Drawing.[Color].AliceBlue, System.Drawing.[Color].LightSteelBlue);][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1061}[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.wizardControlPage2.BackgroundColor = [New] Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.PathRectangle, System.Drawing.Color.AliceBlue, System.Drawing.Color.LightSteelBlue) ][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1236: Gradient background set for Wizard Page**[]**

 

###### 3.13.1.4.5.3    Border Styles {#border-styles style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

Wizard Control

 

The various border styles for a Wizard control are as follows.

[] 

[·      ]None

[·      ]FixedSingle and

[·      ]Fixed3D

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                 |
| [this][.wizardControl1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [Me][.wizardControl1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1237: WizardControl.BorderStyle = \"FixedSingle\"

**[]** 

Banner Panel

 

Banner Panel is a simple gradient panel whose 3D border styles are as follows.

*[]* 

[·      ]RaisedOuter

[·      ]SunkenOuter

[·      ]RaisedInner

[·      ]Raised

[·      ]Etched

[·      ]SunkenInner

[·      ]Bump

[·      ]Sunken

[·      ]Adjust

[·      ]Flat

*[]* 


{border="0"} Note: The GradientPanel.BorderStyle property should be set to \"Fixed3D\" to make this setting effective.[]{#p1062}


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| [this][.gradientPanel1.Border3DStyle = System.Windows.Forms.[Border3DStyle].Sunken;]                                    |
|                                                                                                                                                                                                                                   |
| [this][.gradientPanel1.BorderStyle = System.Windows.Forms.[BorderStyle].Fixed3D;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                                                  |
|                                                                                                                                                                                             |
| [Me][.gradientPanel1.Border3DStyle = System.Windows.Forms.[Border3DStyle].Sunken] |
|                                                                                                                                                                                             |
| [Me][.gradientPanel1.BorderStyle = System.Windows.Forms.[BorderStyle].Fixed3D]    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 1238: BannerPanel with Fixed3D BorderStyle = \"Sunken\"

**[]** 

You can use the below properties to set 2D border style for the Banner Control when **GradientPanel.BorderStyle** property is set to \"FixedSingle\".

**[]** 


  ----------------------- ----------------------------------------------------------------------------------------------
  Banner Panel Property   Description
  BorderColor             Sets the border color for the Banner panel.
  BorderSides             Specifies the sides of the control which should have border.
  BorderSingle            Specifies the 2D Border style for the panel when BorderStyle property is set to FixedSingle.
  ----------------------- ----------------------------------------------------------------------------------------------


 

Wizard Page Border

 

The below properties controls the border settings for a Wizard control page.[]{#p1063}

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Wizard Page Property              | Description                                                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| BorderStyle                       | Specifies the border style for Wizard page. The available styles are Fixed3D and FixedSingle.                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Border3DStyle                     | Specifies the 3D border style for Wizard page. The available styles are,                                                     |
|                                   |                                                                                                                              |
|                                   |                                                                                                                              |
|                                   |                                                                                                                              |
|                                   | [·      ]RaisedOuter,                                                                           |
|                                   |                                                                                                                              |
|                                   | [·      ]SunkenOuter,                                                                           |
|                                   |                                                                                                                              |
|                                   | [·      ]RaisedInner,                                                                           |
|                                   |                                                                                                                              |
|                                   | [·      ]Raised,                                                                                |
|                                   |                                                                                                                              |
|                                   | [·      ]Etched,                                                                                |
|                                   |                                                                                                                              |
|                                   | [·      ]SunkenInner,                                                                           |
|                                   |                                                                                                                              |
|                                   | [·      ]Bump,                                                                                  |
|                                   |                                                                                                                              |
|                                   | [·      ]Sunken,                                                                                |
|                                   |                                                                                                                              |
|                                   | [·      ]Adjust and                                                                             |
|                                   |                                                                                                                              |
|                                   | [·      ]Flat.                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| BorderColor                       | Sets the border color for the Wizard page.                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| BorderSides                       | Specifies the sides of the control which should have border.                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| BorderSingle                      | Specifies the 2D Border style for the Wizard page when BorderStyle property is set to FixedSingle. The available styles are, |
|                                   |                                                                                                                              |
|                                   |                                                                                                                              |
|                                   |                                                                                                                              |
|                                   | [·      ]Dotted,                                                                                |
|                                   |                                                                                                                              |
|                                   | [·      ]Dashed,                                                                                |
|                                   |                                                                                                                              |
|                                   | [·      ]Solid,                                                                                 |
|                                   |                                                                                                                              |
|                                   | [·      ]Inset and                                                                              |
|                                   |                                                                                                                              |
|                                   | [·      ]Outset.                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------+


 

[]{#related-topics}

