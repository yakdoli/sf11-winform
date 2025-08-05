---
title: statemaintenanceandclientobjectid.md
original_path: WinForms_Docs/99_Uncategorized/statemaintenanceandclientobjectid.md
created_at: 2025-08-05
---






##### State Maintenance and ClientObjectID {#state-maintenance-and-clientobjectid style="tab-stops: 0pt"}

[] 

State maintenance

[] 

The state of the client side actions can be maintained by enabling the **ClientSideCookieEnabled** during postback using cookies by creating it on the client and using the cookie information transmitted during client requests.

[] 


  ------------------------- -------------------------------------------------------------------------------------------------
  Property                  Description
  ClientSideCookieEnabled   Specifies whether to create a client side cookie to maintain the state. Default value is false.
  ClientSideCookieName      Specifies the name of the client cookie.
  ------------------------- -------------------------------------------------------------------------------------------------


[] 

For example: When the state of snap elements are changed and a postback is performed only for those element whose ClientSideCookieEnabled is set to True, their new state will be maintained after postback. When it is disabled, the view state will not be maintained and will be changed to the default page load state.

 

**ClientSideCookieName** allows to set the name for the cookie used for state maintenance. If no name is specified for the cookie, then by default it will be set with the \'application path+snap controlname\'.

[] 

+-----------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                          |
|                                                                                                           |
| []                                                       |
|                                                                                                           |
| [Snap1.ClientSideCookieEnabled = [true];]        |
|                                                                                                           |
| [Snap1.ClientSideCookieName = [\"SnapData\"];] |
+-----------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                    |
|                                                                                                                                                                     |
| []                                                                                                                 |
|                                                                                                                                                                     |
| [Private][ Snap1.ClientSideCookieEnabled = [True]]        |
|                                                                                                                                                                     |
| [Private][ Snap1.ClientSideCookieName = [\"SnapData\"]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ClientObjectID

[] 

The client object id can be used to access the control\'s object model on the client side.

 

**ClientObjectId** can be effectively used to refer the control\'s objects when used with MasterPages and UserControls. By default, a client object id is computed by concatenating \'\_sf\' and the control\'s **ID** property. However in the case of hosting the control in a MasterPage or UserControl, the computed client object id is very unintuitive. To make things simpler you can specify a custom value on this property and access the client side object model using that value.

[] 


  ---------------- ------------------------------------------------------------------------
  Property         Description
  ClientObjectID   Specifies the user defined id for accessing the object on client side.
  ---------------- ------------------------------------------------------------------------


[] 

Programmatically the ClientObjectID can be set as follows.

[  ]

+------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                      |
| []                                                  |
|                                                                                                      |
| [Snap1.ClientObjectID = [\"Custom ID\"];] |
+------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                               |
|                                                                                                                                                                |
| []                                                                                                            |
|                                                                                                                                                                |
| [Private][ Snap1.ClientObjectID = [\"Custom ID\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

