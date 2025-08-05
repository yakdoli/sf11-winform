---
title: throughcode9.md
original_path: WinForms_Docs/99_Uncategorized/throughcode9.md
created_at: 2025-08-05
---






##### [Through Code]{.Heading3Char} {#through-code style="tab-stops: 0pt"}

The button control can be created programmatically too.

To create a button in ASP.NET Code:

1.  Create a new ASP.NET Web application.

2.   In the .cs file include the following directories

 


+------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                             |
|                                                                                                                                          |
| [using  ][Syncfusion.Web.UI.WebControls.Shared;] |
|                                                                                                                                          |
| [using  ][Syncfusion.Web.UI;]                    |
+------------------------------------------------------------------------------------------------------------------------------------------+


 


+-------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                              |
|                                                                                                                                           |
| [Imports  ][Syncfusion.Web.UI.WebControls.Shared] |
|                                                                                                                                           |
| [Imports  ][Syncfusion.Web.UI]                    |
+-------------------------------------------------------------------------------------------------------------------------------------------+


 

3.   In code view, the control is instantiated and should be added as follows:


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [\[C#\]     ]                                                                                                                                                                   |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [private][ [void] Page_Init([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| [   BuildButton();]                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [private][ [void] BuildButton()]                                                                          |
|                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| [        [ButtonAdv] Button = [new] [ButtonAdv]();]                                                        |
|                                                                                                                                                                                                                     |
| [        Button.ID = [\"Button2\"];]                                                                                                                    |
|                                                                                                                                                                                                                     |
| [        Button.ImageUrl = [\"Img/Save16.png\"];]                                                                                                       |
|                                                                                                                                                                                                                     |
| [        Button.CustomClass = [\"buttonback\"];]                                                                                                        |
|                                                                                                                                                                                                                     |
| [        Button.Text = [\"Save\"];]                                                                                                                     |
|                                                                                                                                                                                                                     |
| [        form1.Controls.Add(Button);]                                                                                                                                           |
|                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [\[VB\]     ]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ ButtonAdvance [As] [New] ButtonAdv]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] Page_Init([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] [MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [        [\'Put user code to initialize the page here]]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [        BuildButton()]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [Public][ [Sub] BuildButton()]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [        ButtonAdvance.ID = [\"Button2\"]]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [        ButtonAdvance.ImageUrl = [\"Img/Save16.png\"]]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [        ButtonAdvance.CustomClass = [\"buttonback\"]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [        ButtonAdvance.Text = [\"Save\"]]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [        [Me].Controls.Add(ButtonAdvance)]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]][]                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

4.   To have a look at how the button will turn out, in terms of look and feel, add the custom .css class to the .aspx page.


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [\[Css Styles\][]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                  |
| [\<][style][ [type] [=\"text/css\"] [\>]] |
|                                                                                                                                                                                                                                                  |
| [       [.buttonback]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| [       {]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| [            [background-image] : [(\"Img/background.png\")];]                                                                                                      |
|                                                                                                                                                                                                                                                  |
| [            [background-color]: [#C1DBFF];]                                                                                                                        |
|                                                                                                                                                                                                                                                  |
| [       }]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| [\</][style][\>]                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

5.   Build and run the application. The result will be displayed as follows:

{border="0"}

Figure 154: Button through Code

 

 

[]{#related-topics}

