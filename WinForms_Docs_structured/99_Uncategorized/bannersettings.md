---
title: bannersettings.md
original_path: WinForms_Docs/99_Uncategorized/bannersettings.md
created_at: 2025-08-05
---






##### Banner Settings {#banner-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The controls inside the Banner Control include Banner Panel, Title, description and a picture box. The section will walk you through the properties which customizes these controls.

 

**Banner Panel**

 

A Banner Panel is a simple gradient panel which holds a Title label, a Description label and a Picture box controls.

[] 


  ------------- -----------------------------------------------------------------------
  Property      Description
  Banner        Gets or sets the picture box for the wizard using the Image property.
  Description   Sets the label that can describe the current page.
  Title         Sets the title of the current page.
  ------------- -----------------------------------------------------------------------


[] 


{border="0"} Note: The Title and Description settings can be set for individual Wizard Pages using WizardPage.Title and WizardPage.Description properties respectively. See [[Wizard Page Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Wizard_Page_Settings).


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.wizardControl1.Banner = [this].pictureBox2;]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.pictureBox2.Image = ((System.Drawing.[Image])(resources.GetObject([\"pictureBox2.Image\"])));]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.label1.Text = [\"Page Title\"];]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.label2.Text = [\"This is]][ the ][description of the Wizard Page\"][;][] |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.gradientPanel1.Controls.Add([this].label1);]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.gradientPanel1.Controls.Add([this].label2);]                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Me][.wizardControl1.Banner = [Me].pictureBox2 ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Me][.pictureBox2.Image = [DirectCast]((resources.GetObject([\"pictureBox2.Image\"])), System.Drawing.Image) ]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Me][.label1.Text = [\"Page Title\"] ]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Me][.label2.Text = [\"This is]][ the ][description of the Wizard Page\"][ ][] |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Me][.gradientPanel1.Controls.Add([Me].label1) ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Me][.gradientPanel1.Controls.Add([Me].label2)][]                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1212: Page Title, Page Description and Picture Box Image set for the Banner Panel

[] 


[] 

{border="0"} Note: The appearance of a Banner panel can be customized using the properties of the gradient panel. See [[[Border styles]]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Border_Styles) for border settings of a Banner Panel.


[]{#p1046} 

Layout of the Banner Controls

 

The below properties controls the layout of the respective banner controls.

[] 


  ----------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Property                Description
  AutoLayoutBanner        When set to true, the picture box will be automatically laid out at a specific position, in the banner control. Setting false will not layout the picture box automatically.
  AutoLayoutDescription   When set to true, the description text will be automatically laid out at a specific position, in the Description control. Setting false will not layout the text automatically.
  AutoLayoutTitle         When set to true, the title will be automatically laid out at a specific position, in the banner control. Setting false will not layout the title automatically.
  ----------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                   |
| [this][.wizardControl1.AutoLayoutBanner = [true];]                                      |
|                                                                                                                                                                                                   |
| [this][.wizardControl1.AutoLayoutDescription = [true];]                                 |
|                                                                                                                                                                                                   |
| [this][.wizardControl1.AutoLayoutTitle = [true];][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                          |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                             |
| [Me][.wizardControl1.AutoLayoutBanner = [True]]                                                   |
|                                                                                                                                                                                                             |
| [Me][.wizardControl1.AutoLayoutDescription = [True]]                                              |
|                                                                                                                                                                                                             |
| [Me][.wizardControl1.AutoLayoutTitle = [True]][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[[Border styles]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Border_Styles)[ for Banner Panel, ][[Title and Description Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Title_and_Description)[, BannerPanel Background settings in ][[Background Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Background_Settings_1)[]{.UGHyperlink}

 

 

 

 

###### []{#_Title_and_Description}3.13.1.4.1.1    Title and Description Settings {#title-and-description-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

**Title Text**

 

The font style and the fore color for the Title text can be edited through **Label.Font** and **Label.Font** property.

[] 


  ----------- ---------------------------------------------------------------
  Property    Description
  Font        Sets the font style for the Page Title in the Wizard Control.
  ForeColor   Sets the forecolor for the Page Title in the Wizard Control.
  ----------- ---------------------------------------------------------------


[] 

{border="0"}

[] 

Figure 1213: Accessing Font and ForeColor Properties for Page Title Through Designer[]{#p1047}

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [//Setting Font Style for the Label]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [this][.label1.Font = [new] System.Drawing.[Font]([\"Verdana\"], 9F, System.Drawing.[FontStyle].Bold);] |
|                                                                                                                                                                                                                                                                                    |
| [this][.label1.ForeColor = System.Drawing.[Color].DarkBlue;][]                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1048}[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [\'Setting Font Style for the Label]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [Me][.label1.Font = [New] System.Drawing.[Font]([\"Verdana\"], 9F, System.Drawing.[FontStyle].Bold)] |
|                                                                                                                                                                                                                                                                                 |
| [this][.label1.ForeColor = System.Drawing.[Color].DarkBlue;][]                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1214: PageTitle Text with FontStyle = \"Verdana, 9, Bold\"; ForeColor = \"DarkBlue\"

**[]** 

Description Text

 

The appearance of the description text for a wizard control can be edited using the description label properties.

[] 


  ----------- ---------------------------------------------------------------------
  Property    Description
  Font        Sets the font style for the Page description in the Wizard Control.
  ForeColor   Sets the forecolor for the Page description in the Wizard Control.
  ----------- ---------------------------------------------------------------------


[] 

{border="0"}

[] 

Figure 1215: Accessing Font and ForeColor Properties for Page Description Through Designer

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [//Setting Font Style for the Label]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.label1.Font = ][new][ ][System.Drawing.[Font]([\"Verdana\"], 8F);][] |
|                                                                                                                                                                                                                                                                                                                                                                            |
| [this][.label1.ForeColor = System.Drawing.[Color].DarkBlue;][]                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                                                |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [\'Setting Font Style for the Label]                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [Me][.label1.Font = [New] System.Drawing.[Font]([\"Verdana\"], 8F)] |
|                                                                                                                                                                                                                           |
| [this][.label1.ForeColor = System.Drawing.[Color].DarkBlue]                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1216: Page Description Text with FontStyle = \"Verdana, 8\"; ForeColor = \"DarkBlue\"

**[]** 


{border="0"} Note: A WizardControl can have only one page title label and one page description label. We can change only the text of these two labels for individual pages using WizardPage.Title and WizardPage.Description properties and not their appearance. Hence Font and ForeColor settings will be similar in all the page.


 

 

[]{#related-topics}

