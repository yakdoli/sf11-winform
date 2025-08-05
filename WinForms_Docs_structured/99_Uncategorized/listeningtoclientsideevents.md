---
title: listeningtoclientsideevents.md
original_path: WinForms_Docs/99_Uncategorized/listeningtoclientsideevents.md
created_at: 2025-08-05
---








  









## [][]{#p661}Listening to Client Side Events {#listening-to-client-side-events style="tab-stops: 0pt"}

 

[] 

ClientSideXXX properties

**[]** 

Most of the controls in Tools.Web provide properties where you can specify some Java Script code that you want executed for some client event. For example, **Menu.ClientSideOnItemSelect** is a property in our Menu control where you can specify some JS code that you want to be executed when a menu gets selected.

 

The specified value (code) will be evaluated as follows during run time.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [// Java Script:]                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| [\....]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                          |
| [eval( [\"bCont=(\"] + clientCode + [\")\"] ); [// where clientCode is the value of the above ClientSideOnItemSelect property.]] |
|                                                                                                                                                                                                                                          |
| [\....]                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

So, provide Java Script code that are executable without syntax errors, within the above statement.

Some valid values are given below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ClientSideOnItemSelect][=\"someFunction()\"]                                                                                             |
|                                                                                                                                                                                                                                            |
| [ClientSideOnItemSelect][=\"myFunction(this)\" ][// More on the \"this\" pattern below] |
|                                                                                                                                                                                                                                            |
| [ClientSideOnItemSelect][=\"a+b\"]                                                                                                        |
|                                                                                                                                                                                                                                            |
| [ClientSideOnItemSelect][=\"false\"]                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Some invalid values are given below.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [ClientSideOnItemSelect][=\"return false;\" ][\<%\--The \"return\" keyword is invalid in this context. Just specify \"false\".\--%\>]                      |
|                                                                                                                                                                                                                                                                                                               |
| [ClientSideOnItemSelect][=\"a+b;\"][  ][\<%\--Remember not to use \";\" \--%\>]                                                      |
|                                                                                                                                                                                                                                                                                                               |
| [ClientSideOnItemSelect][=\"myFunc(arg1)\" ][\<%\--\"arg1\" will be invalid when evaluated; \"this\" is the only valid argument  that can be passed\--%\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

*[this]* Argument

**[]** 

Note that when your event handler code is executed, it will be executed in the scope of the client side object corresponding to the event you are listening to. In this example, \"this\" would refer to the client side object representing the menu item (not the overall menu) that was selected.

For example, specify the event handler code as follows.

[] 

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Menu][.ClientSideOnItemSelect = [\"MyFunc(this)\"];]
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------

[] 

For the above event handler code, you can define the function as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [function][ MyFunc(oMenuItem)]                                            |
|                                                                                                                                                                |
| [{]                                                                                                                        |
|                                                                                                                                                                |
| [      [var] theEvent = oMenuItem.Event; [// Provides reference to the event.]] |
|                                                                                                                                                                |
| [      [var] text = oMenuItem.Text;    [// Also use the client side API of the menu item.\                                                |
|       \.....]]                                                                                       |
|                                                                                                                                                                |
| [}]                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p662} 

[]{#related-topics}

