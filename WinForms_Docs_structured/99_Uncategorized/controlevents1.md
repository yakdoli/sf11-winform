---
title: controlevents1.md
original_path: WinForms_Docs/99_Uncategorized/controlevents1.md
created_at: 2025-08-05
---








  









## Control Events {#control-events style="tab-stops: 0pt"}

 

HTMLUI control comes with a rich set of events to help the application developer in keeping track of the execution. These events are programmed based on the Event arguments containing data related to the event.

 

The events executed by the HTMLUI control are as follows:

[] 

[**[• ]**]{.UGHyperlink}[LinkClicked Event]{.UGHyperlink}[]{.UGHyperlink}

[**[• ]**]{.UGHyperlink}[LoadStarted Event]{.UGHyperlink}[]{.UGHyperlink}

[**[• ]**]{.UGHyperlink}[LoadFinished Event]{.UGHyperlink}[]{.UGHyperlink}

[**[• ]**]{.UGHyperlink}[LoadError Event]{.UGHyperlink}[]{.UGHyperlink}

[**[• ]**]{.UGHyperlink}[PreRenderDocument Event]{.UGHyperlink}[]{.UGHyperlink}

[**[• ]**]{.UGHyperlink}[ShowTitleChanged Event]{.UGHyperlink}[]{.UGHyperlink}

[**[• ]**]{.UGHyperlink}[TitleChanged Event]{.UGHyperlink}[]{.UGHyperlink}

[] 

[LinkClicked Event]{#LinkClickedEvent}

[] 

This event is raised after the hyperlink is clicked and before the hyperlink tries to load a new resource. The event properties associated with the Link Forward Event Arguments are as follows.

[] 

[·      ]**Cancel**: A boolean value which indicates whether the default processing of resource loading should be canceled or not

[·      ]**Path**: Specifies the location of the resource

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                   |
| [// Event that is to be raised after the hyperlink was clicked and before the hyperlink tries to load ]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                   |
| [// a new resource.]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| [this][.htmluiControl1.LinkClicked += [new] Syncfusion.Windows.Forms.HTMLUI.[LinkForwardEventHandler]([this].htmluiControl1_LinkClicked);] |
|                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                   |
| [private][ [void] htmluiControl1_LinkClicked([object] sender, Syncfusion.Windows.Forms.HTMLUI.[LinkForwardEventArgs] e)]                   |
|                                                                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                   |
| [     e.Cancel = [true];]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                   |
| [     Form2 form2 = [new] Form2(GetFilesLocation() + e.Path);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                   |
| [     form2.Show();]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                   |
| [}  ]                                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Event that is to be raised after the hyperlink was clicked and before the hyperlink tries to load ]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' a new resource. ]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Me][.HtmluiControl1.LinkClicked += [New] Syncfusion.Windows.Forms.HTMLUI.LinkForwardEventHandler([Me].htmluiControl1_LinkClicked)]                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] htmluiControl1_LinkClicked([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.HTMLUI.LinkForwardEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [e.Cancel = [True]]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [Dim][ form2 [As] Form2 = [New] Form2(GetFilesLocation() + e.Path)]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [form2.Show()]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

[LoadStarted Event]{#LoadStartedEvent}

[] 

This event is raised when a new HTML document has started loading into the HTMLUI control from the specified resource.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                |
| [// Event that is to be raised when the HTMLUI control starts loading a new html document.]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| [this][.htmluiControl1.LoadStarted += [new]  System.[EventHandler]([this].htmluiControl1_LoadStarted);] |
|                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                |
| [private][ [void] htmluiControl1_LoadStarted([object] sender, System.[EventArgs] e)]                    |
|                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                |
| [      [Console].WriteLine([\"Started Loading\...\"]);                        ]                                                                                                            |
|                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                |
| [\'  Event that is to be raised when the HTMLUI control starts loading a new html document.]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                |
| [Me][.HtmluiControl1.LoadStarted += [New] System.EventHandler([Me].htmluiControl1_LoadStarted)]                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] htmluiControl1_LoadStarted([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\"Started Loading\...\"])]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

[LoadFinished Event]{#LoadFinishedEvent}

[] 

This event is raised after the loading of HTML document inside the HTMLUI control is completed.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                 |
| [// Event that is to raised after the HTML document have been rendered in the control.]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                 |
| [this][.htmluiControl1.LoadFinished += [new] System.[EventHandler]([this].htmluiControl1_LoadFinished);] |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                 |
| [private][ [void] htmluiControl1_LoadFinished([object] sender, System.[EventArgs] e)]                    |
|                                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                 |
| [       [Console].WriteLine([\"Load successfully completed\"]);]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                 |
| [}   ]                                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [\'  Event that is to raised after the HTML document have been rendered in the control.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.HtmluiControl1.LoadFinished += [New] System.EventHandler([Me].htmluiControl1_LoadFinished)]                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] htmluiControl1_LoadFinished([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [Console.WriteLine([\"Load successfully completed\"])]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[LoadError Event]{#LoadErrorEvent}

[] 

This event is raised when an error occurs during loading or rendering an HTML document from the specified resource. The LoadErrorEventArgs contains the following property that defines the data related to the action of this event.

[] 

[·      ]**Document**: Specifies the document whose rendering triggers the execution of the LoadError event

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                             |
| [// Event that is to be raised when an error occurs during HTML document is being rendered in the HTMLUI control.]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [this][.htmluiControl1.LoadError += [new] Syncfusion.Windows.Forms.HTMLUI.[LoadErrorEventHandler]([this].htmluiControl1_LoadError);] |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                             |
| [private][ [void] htmluiControl1_LoadError([object] sender, Syncfusion.Windows.Forms.HTMLUI.[LoadErrorEventArgs] e)]                 |
|                                                                                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                             |
| [      [Console].WriteLine([\"Error loading due to\"]+ e.ToString());]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                             |
| [}  ]                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [\'  Event that is to be raised when an error occurs during HTML document is being rendered in the HTMLUI control.]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Me][.HtmluiControl1.LoadError += [New] Syncfusion.Windows.Forms.HTMLUI.LoadErrorEventHandler([Me].htmluiControl1_LoadError)]                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] htmluiControl1_LoadError([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.HTMLUI.LoadErrorEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\"Error loading due to\"] + e.ToString())]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

[PreRenderDocument Event]{#PreRenderDocumentEvent}

[] 

This event is raised when the elements in the HTML document are created in the HTMLUI control, but their size and location are not calculated yet.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                        |
| [// Event that is to be raised when a tree of element has been created and their size and location have not been calculated yet.]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.htmluiControl1.PreRenderDocument += [new] Syncfusion.Windows.Forms.HTMLUI.[PreRenderDocumentEventHandler]]                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [([this].htmluiControl1_PreRenderDocument);]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| [private][ [void] htmluiControl1_PreRenderDocument([object] sender, Syncfusion.Windows.Forms.HTMLUI.[PreRenderDocumentArgs] e)] |
|                                                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                        |
| [      [Console].WriteLine([\"This is the Prerender document event\"]);]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                        |
| [} ]                                                                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\'  Event that is to be raised when a tree of element has been created and their size and location have not been calculated yet.]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Me][.HtmluiControl1.PreRenderDocument += [New] Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentEventHandler]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [([Me].htmluiControl1_PreRenderDocument)]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] htmluiControl1_PreRenderDocument([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine([\"This is the Prerender document event\"])]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

[ShowTitleChanged Event]{#ShowTitleChangedEvent}

[] 

This event is raised after the **ShowTitle** property of the HTMLUI control is changed. The event handler receives its data from the ValueChangedEventArguments. The following properties are associated with the ShowTitleChanged event handling.

[] 

[·      ]**Empty-**Gets the instance of the class that is found to be empty or having null value

[·      ]**newValue-**Indicates the current value of the ShowTitle property

[·      ]**oldValue-**Indicates the old value of the ShowTitle property

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                              |
| [// Event that is raised after the ShowTitle property of the HTMLUI control is changed.]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                              |
| [this][.htmluiControl1.ShowTitleChanged += [new] Syncfusion.Windows.Forms.HTMLUI.[ValueChangedEventHandler]([this].htmluiControl1_ShowTitleChanged);] |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                              |
| [private][ [void] htmluiControl1_ShowTitleChanged([object] sender, ValueChangedEventArgs e)]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [   [MessageBox].Show([\"ShowTitle Changed\"]);]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                              |
| [}   ]                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [\' Event that is raised after the ShowTitle property of the HTMLUI control is changed.]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Me][.HtmluiControl1.ShowTitleChanged += [New] Syncfusion.Windows.Forms.HTMLUI.ValueChangedEventHandler([Me].htmluiControl1_ShowTitleChanged)]                                                            |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Private][ [Sub] htmluiControl1_ShowTitleChanged([ByVal] sender [As] [Object], [ByVal] e [As] ValueChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [MessageBox.Show([\"ShowTitle Changed\"])]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[TitleChanged Event]{#TitleChangedEvent}

[] 

The TitleChanged event is raised after the **Title** property of the HTMLUI control is changed. The Title value can be set explicitly by the user or it can be extracted from the title tag of the HTML document that is to be loaded into the HTMLUI control[.]

 

The event handler receives its data from the ValueChangedEventArguments. The following properties are associated with the TitleChanged event handling.

[] 

[·      ]**newValue**: Gets the new value for the Title

[·      ]**oldValue**: Gets the old value that has been changed

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                       |
| [// Event is raised after the Title property of the HTMLUI control is changed.]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                       |
| [this][.htmluiControl1.TitleChanged += [new] Syncfusion.Windows.Forms.HTMLUI.[ValueChangedEventHandler] ([this].htmluiControl1_TitleChanged);] |
|                                                                                                                                                                                                                                                                                                                                       |
| [private][ [void] htmluiControl1_TitleChanged([object] sender, ValueChangedEventArgs e)]                                                                               |
|                                                                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                       |
| [MessageBox][.Show([\"Title Changed\"]);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                       |
| [}  ]                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [\'Event is raised after the Title property of the HTMLUI control is changed.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.HtmluiControl1.TitleChanged += [New] Syncfusion.Windows.Forms.HTMLUI.ValueChangedEventHandler([Me].htmluiControl1_TitleChanged)]                                                                |
|                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] htmluiControl1_TitleChanged([ByVal] sender [As] [Object], [ByVal] e [As] ValueChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [MessageBox.Show([\"Title Changed\"])]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p31} 

More:





