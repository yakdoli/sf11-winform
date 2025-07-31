---
title: clientsideobjectmodel1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideobjectmodel1.md
created_at: 2025-07-03
---






##### [Client-Side Object Model] {#client-side-object-model style="tab-stops: 0pt"}

[] 


  --------- ----------- ------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Method    Parameter   Return Type   Description
  GetHTML   \-          string        Returns HTML editor content.
  SetHTML   string      \-            Sets HTML editor content.
  GetText   \-          string        Returns editor content text (formatting removed).
  SetText   string      \-            Sets editor content text. If HTML tags are present content is HTML-encoded. To set HTML use SetHTML() method.
  Refresh   string      \-            **For .NET Framework version 2.0 only**. Sends callback to server without page refreshing and triggers CallbackRefresh server side RTE event. To perform callback the EnableCallbacks property must be set to true.
  --------- ----------- ------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

The following code example demonstrates how to add link to editor html.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][cc1][:][RichTextEditor][ [ID][=\"RTE\"] [runat][=\"server\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][input][ [type][=\"button\"] [value][=\"Add link\"] [onclick][=\"AddLink()\"] [/\>]]                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[javascript\]]**                                                                                                      |
|                                                                                                                                                               |
| **[]**                                                                                                    |
|                                                                                                                                                               |
| [function][  AddLink()]                  |
|                                                                                                                                                               |
| [{]                                                                                                       |
|                                                                                                                                                               |
| [    [var] sHTML = \_sfRTE.GetHTML();]                                               |
|                                                                                                                                                               |
| [    sHTML += [\"\<br/\>\"];]                                                      |
|                                                                                                                                                               |
| [    sHTML += [\"\<A href=\\\"http://www.syncfusion.com\\\"\>Syncfusion\</A\>\"];] |
|                                                                                                                                                               |
| [    \_sfRTE.SetHTML(sHTML);]                                                                             |
|                                                                                                                                                               |
| [}]                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

RTE ClientEventData object

**[]** 

ClientEventData

**[]** 


  ---------- ------------- ---------------------------------------------
  Property   Parameter     Description
  El         HTMLElement   Represents control root HTML element.
  Self       object        Represents RTE client-side object instance.
  Event      object        Represents event.
  HTML       string        Represents editor HTML content.
  ---------- ------------- ---------------------------------------------


 

 

ClientObjectID

[] 

You can access the Client-Side Object Model  by using the ClientObjectID of the RichTextEditor control.

 

The ClientObjectID can be used effectively to refer to the control\'s objects when used with MasterPages and UserControls. By default, a client object ID is computed by concatenating the *\_sf* and the control\'s *ID* property. In case of hosting the control in a MasterPage or UserControl, the computed client object ID cannot be identified spontaneously. To make this  simple, you can specify a custom value in this property and access the client-side object model using that value.

 


  ---------------- ------------------------------------------------------------------------ ------------- ----------- -----------------
  Property         Description                                                              Type          Data Type   Reference Links
  ClientObjectID   Specifies the user defined ID for accessing the object on client side.   Server side   String      NA
  ---------------- ------------------------------------------------------------------------ ------------- ----------- -----------------


 

[Programmatically the ClientObjectID can be set as given in the following codes:]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
| [this][.RichTextEditor1.ClientObjectID = [\"CustomID\"];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                        |
|                                                                                                                                                                         |
|                                                                                                                                                                         |
|                                                                                                                                                                         |
| [Private][ RichTextEditor1.ClientObjectID = [\"CustomID\"]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code examples demonstrate how to add link to editor HTML using custom ClientObjectID.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][cc1][:][RichTextEditor][ [ID][=\"RTE\"] [runat][=\"server\" ][ClientObjectID][=\"RTEditor\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][input][ [type][=\"button\"] [value][=\"Add link\"] [onclick][=\"AddLink()\"] [/\>]]                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[javascript\]]**                                                                                      |
|                                                                                                                                               |
|                                                                                                                                               |
|                                                                                                                                               |
| [function][  AddLink()]                                  |
|                                                                                                                                               |
| [{]                                                                                                       |
|                                                                                                                                               |
| [    [var] sHTML = RTEditor.GetHTML();]                                              |
|                                                                                                                                               |
| [    sHTML += [\"\<br/\>\"];]                                                      |
|                                                                                                                                               |
| [    sHTML += [\"\<A href=\\\"http://www.syncfusion.com\\\"\>Syncfusion\</A\>\"];] |
|                                                                                                                                               |
| [    RTEditor.SetHTML(sHTML);]                                                                            |
|                                                                                                                                               |
| [}]                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

