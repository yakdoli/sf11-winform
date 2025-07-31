---
title: howtosetspacingbetweenthebrowsingbuttons.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetspacingbetweenthebrowsingbuttons.md
created_at: 2025-07-03
---






##### How to set spacing between the browsing buttons? {#how-to-set-spacing-between-the-browsing-buttons style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The WizardControl internally uses the GridBagLayout to arrange the navigation buttons.

 

You could insert spaces around the buttons using the **Insets** property. The GridBagLayout.GetConstraintsRef returns the object containing the constraints for that particular control. Specifying an Insets value as shown below to this, would create padding around this control.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][C#\]][]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                        |
| [this][.wizardControl1.GridBagLayout.GetConstraintsRef(this.wizardControl1.NextButton).Insets = ][new][ Insets(5, 5, 5, 5);]     |
|                                                                                                                                                                                                                                                                                                                                        |
| [this][.wizardControl1.GridBagLayout.GetConstraintsRef(this.wizardControl1.BackButton).Insets = ][new][ Insets(5, 5, 0, 5);]     |
|                                                                                                                                                                                                                                                                                                                                        |
| [this][.wizardControl1.GridBagLayout.GetConstraintsRef(this.wizardControl1.CancelButton).Insets = ][new][ Insets(0, 5, 5, 5);  ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1069}[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                |
| [Me][.wizardControl1.GridBagLayout.GetConstraintsRef([Me].wizardControl1.NextButton).Insets= [New] Insets(5, 5, 5, 5)]                                          |
|                                                                                                                                                                                                                                                                                                |
| [Me][.wizardControl1.GridBagLayout.GetConstraintsRef([Me].wizardControl1.BackButton).Insets= [New] Insets(5, 5, 0, 5)]                                          |
|                                                                                                                                                                                                                                                                                                |
| [Me][.wizardControl1.GridBagLayout.GetConstraintsRef([Me].wizardControl1.CancelButton).Insets = [New] Insets(0, 5, 5, 5)][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

