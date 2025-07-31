---
title: actions.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\actions.md
created_at: 2025-07-03
---






#### Actions {#actions style="tab-stops: 0pt"}

 

Essential PDF supports different actions triggered by different events and user interaction. There are a lot of possible actions such as playing a particular sound or movie, launching an application or URI, and so on.

 

Essential PDF supports the following types of actions.

 

[·      ]**PdfSoundAction,** which plays the specified music file

[·      ]**PdfUriAction** that launches the specified URI

[·      ]**PdfGoToAction** that goes to the specified page of the document

[·      ]**PdfJavaScriptAction**, which executes specified PDF javascript code

[·      ]**PdfLaunchAction** that launches the application or opens the document

[·      ]**PdfNamedAction**, which goes to the named destination: next, previous, first or last page

[·      ]**PdfSubmitAction**, which submits the data that is entered into the PDF form

[·      ]**PdfResetAction** that resets the fields of the PDF form

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [PdfUriAction][ uriAction = [new] [PdfUriAction]([\"http://www.google.com\"]);]                    |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [PdfDestination][ dest = [new] [PdfDestination](page, [new] [Point](0, 100));]  |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [PdfGoToAction][ goToAction = [new] [PdfGoToAction](page);]                                                               |
|                                                                                                                                                                                                                                                          |
| [goToAction.Destination = dest;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [uriAction.Next = goToAction;]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [PdfJavaScriptAction][ javaAction = [new] [PdfJavaScriptAction]([\"app.alert(\\\"Hello \\\")\"]);] |
|                                                                                                                                                                                                                                                          |
| [goToAction.Next = javaAction;]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [document.Actions.AfterOpen = soundAction;]                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                      |
| [Dim][ uriAction [As] Syncfusion.Pdf.Interactive.PdfUriAction = [New] Syncfusion.Pdf.Interactive.PdfUriAction([\"http://www.google.com\"])]                    |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [Dim][ dest [As] Syncfusion.Pdf.Interactive.PdfDestination = [New] Syncfusion.Pdf.Interactive.PdfDestination(page, [New] Point(0, 100))]                         |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [Dim][ goToAction [As] Syncfusion.Pdf.Interactive.PdfGoToAction = [New] Syncfusion.Pdf.Interactive.PdfGoToAction(page)]                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [goToAction.Destination = dest]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                      |
| [uriAction.Next = goToAction]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [Dim][ javaAction [As] Syncfusion.Pdf.Interactive.PdfJavaScriptAction = [New] Syncfusion.Pdf.Interactive.PdfJavaScriptAction([\"app.alert(\"\"Hello \"\")\"])] |
|                                                                                                                                                                                                                                                                                                                      |
| [goToAction.Next = javaAction]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                      |
| [document.Actions.AfterOpen = soundAction]                                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Next property of an action is used to specify the queue of actions as illustrated in the preceding example.


[] 

1.   Following are the actions for Document Object:

**[]** 

[·      ]**AfterOpen** action to be performed after the document is opened

[·      ]**AfterPrint** action to be performed after the document is printed

[·      ]**AfterSave** action to be performed after the document is saved

[·      ]**BeforeClose** action to be performed before the document is closed

[·      ]**BeforePrint** action to be performed before the document is printed

[·      ]**BeforeSave** action to be performed before the document is saved

[] 

2.   Following are the actions for Annotation Object:

[] 

[·      ]**GotFocus** action to be performed when the annotation gets focus

[·      ]**LostFocus** action to be performed when the annotation loses focus

[·      ]**MouseEnter** action to be performed when the cursor enters the active area of the annotation

[·      ]**MouseLeave** action to be performed when the cursor leaves the active area of the annotation

[·      ]**MouseDown** action to be performed when the mouse button is pressed inside the active area of the annotation

[·      ]**MouseUp** action to be performed when the mouse button is released inside the active area of the annotation

**[]** 

3.   Following are the actions for Form Field Object:

[] 

[·      ]**Calculate** javascript action to be performed to recalculate the value of the field

[·      ]**Format** javascript action to be performed before the field is formatted to display the value

[·      ]**Validate** javascript action to be performed when the value of the field is changed

[·      ]**KeyPressed** javascript action to be performed when the user types, key-stroke into a text field or combo box, or modifies the selection in a scrollable list box

 

Additionally, the fields support all the actions that are supported by annotations.

 

[]{#related-topics}

