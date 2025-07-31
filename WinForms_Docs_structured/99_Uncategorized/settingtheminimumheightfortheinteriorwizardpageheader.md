---
title: settingtheminimumheightfortheinteriorwizardpageheader.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingtheminimumheightfortheinteriorwizardpageheader.md
created_at: 2025-07-03
---






#### Setting the Minimum Height for the Interior Wizard Page Header {#setting-the-minimum-height-for-the-interior-wizard-page-header style="tab-stops: 0pt"}

[] 

You can set the minimum height for the header of the Interior wizard page by using the **InteriorPageHeaderMinHeight** property.

 

Use the following code snippet for setting the minimum height for the page header.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][syncfusion][:][WizardControl][ Name][=\"wizardControl\"][ InteriorPageHeaderMinHeight][=\"150\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    ][\<][syncfusion][:][WizardPage][ Name][=\"wizardPage\" /\>]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][syncfusion][:][WizardControl][\>]                                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                                 |
| []                                                            |
|                                                                                                                                 |
| [WizardControl wizardControl = [new] WizardControl();] |
|                                                                                                                                 |
| [grid.Children.Add(wizardControl);]                                         |
|                                                                                                                                 |
| [WizardPage wizardPage = [new] WizardPage();]          |
|                                                                                                                                 |
| [wizardControl.Items.Add(wizardPage);]                                      |
|                                                                                                                                 |
| [wizardControl.InteriorPageHeaderMinHeight = 150; ]                         |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

*[]* 

Figure 1200: InteriorPageHeaderMinHeight = \"150\"

[] 

See Also

[] 

[]{#p646}[]

[]{#related-topics}

