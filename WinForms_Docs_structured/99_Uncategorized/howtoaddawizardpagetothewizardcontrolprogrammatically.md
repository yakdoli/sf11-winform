---
title: howtoaddawizardpagetothewizardcontrolprogrammatically.md
original_path: WinForms_Docs/99_Uncategorized/howtoaddawizardpagetothewizardcontrolprogrammatically.md
created_at: 2025-08-05
---






##### How to add a wizard page to the Wizard Control programmatically? {#how-to-add-a-wizard-page-to-the-wizard-control-programmatically style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

You can add a Wizard page to the Wizard Control using **AddPage** Method.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                     |
| [private][ Syncfusion.Windows.Forms.Tools.[WizardControlPage] NewPage;]                                                                   |
|                                                                                                                                                                                                                                                     |
| [this][.NewPage = [new] Syncfusion.Windows.Forms.Tools.[WizardControlPage]([this].components);] |
|                                                                                                                                                                                                                                                     |
| [this][.wizardControl1.AddPage(NewPage);]                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| [NewPage.Title = [\"Finishing Page\"];]                                                                                                                                                  |
|                                                                                                                                                                                                                                                     |
| [NewPage.][Description][ = [\"Give a Finish Text\"];][]                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET\]][]**                                               |
|                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [Private][ NewPage [As] Syncfusion.Windows.Forms.Tools.WizardControlPage]                                      |
|                                                                                                                                                                                                                          |
| [Me][.NewPage = [New] Syncfusion.Windows.Forms.Tools.WizardControlPage([Me].components) ] |
|                                                                                                                                                                                                                          |
| [Me][.wizardControl1.AddPage(NewPage) ]                                                                                             |
|                                                                                                                                                                                                                          |
| [NewPage.Title = [\"Finishing Page\"] ]                                                                                                                       |
|                                                                                                                                                                                                                          |
| [NewPage.Description = [\"Give a Finish Text\"] ]                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1239: New page Added using AddPage Method

 

[]{#related-topics}

