---
title: howtobrowsethroughthemdichildreninthemdicontainerafterenablingtabbedmdimanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtobrowsethroughthemdichildreninthemdicontainerafterenablingtabbedmdimanager.md
created_at: 2025-07-03
---






#### How to browse through the MDIChildren in the MDIContainer after enabling TabbedMDIManager {#how-to-browse-through-the-mdichildren-in-the-mdicontainer-after-enabling-tabbedmdimanager style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

You should not use the MDIContainer form's MDIChildren property to browse through the MDIChildren. This is because the TabbedMDI framework introduces some additional MDIChildren into your MDIContainer that are not part of your application logic.

 

You should instead use the TabbedMDIManager\'s **MDIChildren** property to get a list of the MDIChildren, as follows:

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [// In your MDIContainer Form.]                                                                                                                                     |
|                                                                                                                                                                                                                       |
| [private][ [void] ParseMDIChildren()]                                                                       |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [string][ children = [String].Empty;]                                                                       |
|                                                                                                                                                                                                                       |
| [foreach][([Form] form [in] [this].tabbedMDIManager.MdiChildren)] |
|                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [children += form.Text + [\"\\r\\n\"];]                                                                                                                    |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                               |
|                                                                                                                                                                                                                       |
| [MessageBox][.Show(children); ]                                                                                                  |
|                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]\                                                                                                                                                                                                 |
| ]**[\                                                                                                                                                                      |
| [\' In your MDIContainer Form.]]                                                                                                                     |
|                                                                                                                                                                                                                |
| [Private][ [Sub] ParseMDIChildren()]                                                                 |
|                                                                                                                                                                                                                |
| [Dim][ children [As] [String] = [String].Empty]            |
|                                                                                                                                                                                                                |
| [Dim][ form [As] Form]                                                                               |
|                                                                                                                                                                                                                |
| [For][ [Each] Form [In] [Me].tabbedMDIManager.MdiChildren] |
|                                                                                                                                                                                                                |
| [children += Form.Text + [\"\\r\\n\"]]                                                                                                              |
|                                                                                                                                                                                                                |
| [Next]                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [MessageBox.Show(children)]                                                                                                                                                |
|                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p934} 

[]{#related-topics}

