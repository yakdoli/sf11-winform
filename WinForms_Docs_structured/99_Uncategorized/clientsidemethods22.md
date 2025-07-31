---
title: clientsidemethods22.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsidemethods22.md
created_at: 2025-07-03
---






#### Client-Side Methods  {#client-side-methods style="tab-stops: 0pt"}

The Tab control supports client-side methods handling to modify the control's behavior.

Select

The *select* method is used to select a tab, similar to selecting it by clicking.

+-----------------------------------------------------------------------+
| **\[JavaScript\]**                                                    |
|                                                                       |
|  \$(\"#myTab\").tabs(\'select\',2);                                   |
+-----------------------------------------------------------------------+

 

The second argument is the index (zero-based) of the tab to be selected.

 

Remove

The *remove* method is used to remove the particular tab using its index.

+-----------------------------------------------------------------------+
| **\[JavaScript\]**                                                    |
|                                                                       |
|  \$(\"#myTab\").tabs (remove,2);                                      |
+-----------------------------------------------------------------------+

 

The second argument is the index (zero-based) of the tab to be removed.

 

Enable

 The *enable* method is used to enable the disabled tab using its index.

+-----------------------------------------------------------------------+
| **\[JavaScript\]**                                                    |
|                                                                       |
|  \$(\"#myTab\").tabs(enable,2);                                       |
+-----------------------------------------------------------------------+

 

The second argument is the index (zero-based) of the tab to be removed.

 

Enabling Multiple Tabs

 

To enable more than one tab at the same time reset the disabled property as given in the following code.

+-----------------------------------------------------------------------+
| **\[JavaScript\]**                                                    |
|                                                                       |
|  \$(\'#myTab).tabs(\"option\", \"disabled\",\[\]);.                   |
+-----------------------------------------------------------------------+

 

Disable

 The *disable* method is used to disable the particular tab using its index.

+-----------------------------------------------------------------------+
| **\[JavaScript\]**                                                    |
|                                                                       |
|  \$(\"#myTab\").tabs(disable,2);                                      |
+-----------------------------------------------------------------------+

 

The second argument is the index (zero-based) of the tab to be removed.


Note: The selected tab cannot be disabled.


 

Disabling Multiple Tabs

Using array of indexes we can disable multiple tabs. Refer to the following code to disable more than one tab at the same time.

+-----------------------------------------------------------------------+
| **\[JavaScript\]**                                                    |
|                                                                       |
|  \$(\'#myTab).tabs(\"option\",\"disabled\", \[1, 2, 3\]);             |
+-----------------------------------------------------------------------+

 


Note: Similarly, you can use all the client-side methods of Jquery tabs in Essential Tools for MVC Tab control. For more details, refer to the following link.


***[]*** 

[[http://docs.jquery.com/UI/Tabs#methods]{.UGHyperlink}](http://docs.jquery.com/UI/Tabs#methods)[]{.UGHyperlink}

 

 

[]{#related-topics}

