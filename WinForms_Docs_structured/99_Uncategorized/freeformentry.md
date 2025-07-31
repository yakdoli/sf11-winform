---
title: freeformentry.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\freeformentry.md
created_at: 2025-07-03
---






##### FreeFormEntry {#freeformentry style="tab-stops: 0pt"}

[] 

FreeFormEntry is used to save the entered word, which is not in the AutoComplete drop down list when it is bounded to a data source.

 

The following steps illustrates the working of free form entry of AutoCompleteTextBox control.

[] 

1.   Type a text in **AutoCompleteTextBox**.

2.   If the text is not in the drop-down list of **AutoComplete**, press the **Enter** key.

3.   The server-side event **OnFreeFormEntry** gets triggered and checks for the entered text in the database internally.

4.   If the text is not present in the database, it inserts the text into a database using the event argument **FreeFormText**.

5.   Now the entered text gets automatically listed in the drop-down list of **AutoCompleteTextBox**.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                                                            |
|                                   |                                                                                                                                                            |
| Property                          | Description                                                                                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AllowFreeFormEntry                | Gets / sets whether AutoCompleteTextBox allow free form entry or not. OnFreeFormEntry event gets trigger only when AllowFreeFormEntry property is enabled. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][cc1][:][AutoCompleteTextBox][ [ID][=\"AutoCompleteTextBox1\"] [DataSourceID][=\"SqlDataSource1\"] [DataKeyField][=\"Name\"] [AllowFreeFormEntry][=\"true\"] [OnFreeFormEntry][=\"AutoCompleteTextBox1_FreeFormEntry\"] [/\>]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [protected][ [void] AutoCompleteTextBox1_FreeFormEntry([object] sender, Syncfusion.Web.UI.WebControls.Tools.ACFreeFormEntryEventArgs e)]                             |
|                                                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [    [SqlConnection] con; [string] cmdstr; [SqlCommand] cmd;]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                     |
| [    [string] dbpath = HttpContext.Current.Server.MapPath([@\"App_Data\\Database.mdf\"]);]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [    con = [new] [SqlConnection]([@\"Data Source=.\\SQLEXPRESS;AttachDbFilename=\"] + dbpath + [\";Integrated Security=True;Connect Timeout=30;User Instance=True\"]);] |
|                                                                                                                                                                                                                                                                                                     |
| [    cmdstr = [\"Insert into ACName(Name)Values(\'\"] + e.FreeFormText.ToString() + [\"\')\"];]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                     |
| [    cmd = [new] [SqlCommand](cmdstr, con);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [    con.Open();]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                     |
| [    cmd.ExecuteNonQuery();]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                     |
| [    con.Close();]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Protected][ [Sub] AutoCompleteTextBox1_FreeFormEntry([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Web.UI.WebControls.Tools.ACFreeFormEntryEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    [Dim] con [As] SqlConnection]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    [Dim] cmdstr [As] [String]]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    [Dim] cmd [As] SqlCommand]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    [Dim] dbpath [As] [String] = HttpContext.Current.Server.MapPath([\"App_Data\\Database.mdf\"])]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    con = [New] SqlConnection([\"Data Source=.\\SQLEXPRESS;AttachDbFilename=\"] & dbpath & [\";Integrated Security=True;Connect Timeout=30;User Instance=True\"])]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    cmdstr = [\"Insert into ACName(Name)Values(\'\"] & e.FreeFormText.ToString() & [\"\')\"]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    cmd = [New] SqlCommand(cmdstr, con)]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    con.Open()]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    cmd.ExecuteNonQuery()]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [    con.Close()]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

