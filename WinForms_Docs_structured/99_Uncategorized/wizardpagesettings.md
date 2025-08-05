---
title: wizardpagesettings.md
original_path: WinForms_Docs/99_Uncategorized/wizardpagesettings.md
created_at: 2025-08-05
---






##### Wizard Page Settings {#wizard-page-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

A Wizard Page can include a collection of controls implementing an interactive Wizard interface. The Wizard pages are added to the Wizard Container. You can drag and drop any control into a wizard page. Wizard Control lets you to customize the individual Wizard pages to give a unique functionality for each page.

 

[[Creating a Basic Wizard]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Creating_a_Basic)[ ]topic discussed how to add Wizard Pages. Let us see how to customize the Wizard pages.

 

**Setting Title and Description**

 

You can specify the title and description in the Banner Panel, for a particular Wizard Page using the **WizardPage.Title** and **WizardPage.Description** properties. The appearance of the title and description can be controlled through Label properties. See[ ][Title and Description Settings ]{.UGHyperlink}for details.

[] 


  ------------- -----------------------------------------
  Property      Description
  Title         Specifies the title of the page.
  Description   Specifies the description for the page.
  ------------- -----------------------------------------


[]{#p1049}**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [this][.wizardControlPage1.Title = [\"Registration Details\"];]                                                   |
|                                                                                                                                                                                                                               |
| [this][.wizardControlPage1.Description = [\"Please enter your Details:\"];][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [Me][.wizardControlPage1.Title [= \"Registration Details\"]]                                                                 |
|                                                                                                                                                                                                                                         |
| [Me][.wizardControlPage1.Description [= \"Please enter your Details:\"]][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 1217: Wizard Page with Title and Description Set

**[]** 

Accessing Wizard Pages

 

We can also access the properties of a Wizard Page using SelectedWizardPage property of the WizardControl in the Designer. See [[Page Navigation at Design time]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Page_Selection_at) for details.

[] 


  ----------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Property                Description
  SelectedWizardPage      Specifies the selected wizard page.
  WizardPage.LayoutName   The individual Wizard page is identified using its LayoutName in the SelectedWizardPage property. By default the LayoutName is set as Card1 for the first page added, Card2 for the next page and so on.
  ----------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

{border="0"}

 

Figure 1218: Accessing Properties of a Wizard Page Through SelectedWizardPage Property of Wizard Control

[] 

The header section (GradientPanel and its child controls) can be hidden by setting FullPage property to true. This makes the page occupy the entire space without the header.[]{#p1050}

[] 


  ---------- --------------------------------------------------------------------------------------------------------------
  Property   Description
  FullPage   Gets/sets the boolean value whether the Banner Panel should  be shown for that page. Default value is false.
  ---------- --------------------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                           |
|                                                                                                                                                          |
| []                                                                                                                               |
|                                                                                                                                                          |
| [this][.wizardControlPage1.FullPage = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                    |
|                                                                                                                                                       |
| []                                                                                                                            |
|                                                                                                                                                       |
| [Me][.wizardControlPage1.FullPage = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 1219: Wizard Page without Banner panel by setting FullPage = \"True\"

[] 

A sample which demonstrates a Wizard Control with interactive Wizard pages is available in the below location.

 

***..\\My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Tools.Windows\\Samples\\2.0\\Wizard Package\\WizardControlDemo***

 

**See also**

 

[[Foreground Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Foreground_Settings_1), [[Background Settings]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Background_Settings_1), [[ValidatePage Event]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ValidatePage_Event), [[How to Programmatically control the Page Sequence?]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_Programmatically)[]{.UGHyperlink}

 

 

 

###### []{#_Reordering_Wizard_Pages}3.13.1.4.2.1    Reordering Wizard Pages {#reordering-wizard-pages style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

[]{#p1051}By default, the WizardControl will use the order in which the pages are added to determine the next/previous pages. To reorder the pages, use any one of the following methods.

[] 

[·      ]Select the WizardControl and choose **WizardPages** property in the Property Editor. This will bring out the collection editor, where you can reorder the pages using Up and Down arrow keys.

[] 

{border="0"}

[] 

Figure 1220: Reordering Wizard Pages

[] 

[·      ]In the designer, right click on a page and choose \'Bring To Front\' or \'Send To Back\' options which will move the page to the beginning or to the end of the collection, respectively.

[] 

{border="0"}

 

Figure 1221: Accessing reordering Options(Bring To Front, Send To Back) in Designer

[] 

[·      ]The WizardControlPage has the NextPage and PreviousPage properties with which you can specify the order of page selection. Users may set these properties in the designer for all the pages. If set, the WizardControl will use that as a cue to determine the new page to be selected at run time.

[] 


  ---------------------------- ------------------------------------------
  WizardControlPage Property   Description
  NextPage                     It sets the next page of the wizard.
  PreviousPage                 It sets the previous page of the wizard.
  ---------------------------- ------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                                                      |
|                                                                                                                                                                                 |
| [this][.wizardControlPage2.NextPage = [this].wizardControlPage3;]     |
|                                                                                                                                                                                 |
| [this][.wizardControlPage2.PreviousPage = [this].wizardControlPage1;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                               |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                  |
| [Me][.wizardControlPage2.NextPage = [Me].wizardControlPage3]                                           |
|                                                                                                                                                                                                                  |
| [Me][.wizardControlPage2.PreviousPage = [Me].wizardControlPage1][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[[Page Selection at Design time]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Page_Selection_at)[, ][[ValidatePage Event]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_ValidatePage_Event)[,][ ]{.UGHyperlink}[[How to Programmatically control the Page Sequence?]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_Programmatically)[]

 

 

[]{#related-topics}

