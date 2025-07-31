---
title: tabalignment1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tabalignment1.md
created_at: 2025-07-03
---






#### Tab Alignment {#tab-alignment style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The tabs in the TabbedMDI layout can be aligned to the Top, Left, Right and Bottom of the form using the **Alignment** property. To access the Alignment property, you should use the **TabControlAdded** event. This event is fired to let the user configure the tab appearance and behavior.

[] 

5.   Call the TabControlAdded event in the form\'s constructor.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [this][.tb.TabControlAdded += [new] TabbedMDITabControlEventHandler(tb_TabControlAdded);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                          |
|                                                                                                                                                                             |
| []                                                                                                                        |
|                                                                                                                                                                             |
| [AddHandler][ tb.TabControlAdded, [AddressOf] tb_TabControlAdded] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Set the Alignment property of Tab Control using the **TabbedMDITabControlEventArgs**.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [private][ [void] tb_TabControlAdded([object] sender, TabbedMDITabControlEventArgs args)] |
|                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [args.TabControl.Alignment=[TabAlignment].Bottom;]                                                                                                             |
|                                                                                                                                                                                                                          |
| [}   ]                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] tb_TabControlAdded([ByVal] sender [As] [Object], [ByVal] args [As] TabbedMDITabControlEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                       |
| [args.TabControl.Alignment = TabAlignment.Bottom]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

[] 

Figure 1090: Tab Aligned To Top, Left, Bottom and Right

**[]** 

See Also

[] 

[[MDI List]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_MDI_List)[]{.UGHyperlink}

 

 

 

[]{#p911} 

[]{#related-topics}

