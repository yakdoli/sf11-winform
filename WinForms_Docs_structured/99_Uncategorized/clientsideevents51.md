---
title: clientsideevents51.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents51.md
created_at: 2025-08-05
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

  ------------ --------------------------------------------------------- -------------
  Name         Description                                               Arguments
  OnLoad       Raised when the control is loaded from the client side.   sender
  OnExpand     Raised on expanding panes.                                sender,args
  OnCollapse   Raised on collapsing panes.                               sender,args
  OnResizing   Raised on resizing panes.                                 sender,args
  ------------ --------------------------------------------------------- -------------

[] 

You can handle client-side events in the following two ways:

 

**[Using Builder]**

The following steps explain how to handlie client-side events through Builder.

1.   In the **view**, invoke the **Splitter** helper with the splitter contents ID as the first argument, and enable the **OnLoad** and **OnExapnd **with the respective handlers as shown below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                        |
| [\<%][=][Html.Syncfusion().Splitter([\"splitter\"])][.SplitterPanes(panes1=\>{ ] |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [panes1.Add().PaneSize([Unit].Percentage(50)).ContentTemplate(()=\>{[%\>]]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [             [\<][p][\>]inner first pane[\</][p][\>]]                                                              |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [\<%][}).SplitterBar(b=\>b.AllowSplitterBar([true])); ]                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [panes1.Add().PaneSize([Unit].Percentage(30)).ContentTemplate(()=\>{[%\>]]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [             [\<][p][\>]inner second pane[\</][p][\>]]                                                             |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                        |
| [   [\<%]});]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| [})]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                        |
| **[.OnLoad([\"OnLoaded\"]).OnExpand([\"OnExpand\"]).OnCollapse([\"OnCollapse\"])]**[]                                                                  |
|                                                                                                                                                                                                                                                                                                        |
| **[.OnResizing([\"OnResizing\"]) ]**[%\>][ ]                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Define the callback methods in the script to handle the specified events.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**[]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                 |
| [        [function] OnLoaded() {[]]                                                                                                              |
|                                                                                                                                                                                                                                 |
| [                    }]                                                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| [        [function] OnExpand(inst, args) {]                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of splitter object]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.Id -- splitter control id]]                                                                                                            |
|                                                                                                                                                                                                                                 |
| [            [//          args.currentSplitterBar     - splitterbar element.]]                                                                                        |
|                                                                                                                                                                                                                                 |
| [              ]                                                                                                                                                              |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnCollapse(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of splitter object]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.Id -- splitter control id]]                                                                                                            |
|                                                                                                                                                                                                                                 |
| [            [//          args.currentSplitterBar     - splitterbar element.]]                                                                                        |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        [function] OnResizing(inst, args) {]                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [            [//inst - instance of splitter object]]                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [            [//args :    args.Id -- splitter control id]]                                                                                                            |
|                                                                                                                                                                                                                                 |
| [            [//          args.currentSplitterBar     - splitterbar element.]]                                                                                        |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Run the application.

 

{border="0"}

Figure 261: Splitter Control[]

[] 

[]{#related-topics}

