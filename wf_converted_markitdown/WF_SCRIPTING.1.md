Content from the zip file `wf\WF_SCRIPTING.1.mshc`:

## File: StopWordList.txt

a
about
above
across
after
afterwards
again
against
all
almost
alone
along
already
also
although
always
am
among
amongst
amount
an
and
another
any
anyone
anything
anyway
anywhere
are
around
as
at
back
be
became
because
become
becomes
becoming
been
before
beforehand
behind
being
below
beside
besides
between
beyond
both
bottom
but
by
can
cannot
come
con
could
dec
did
do
does
doing
done
down
due
during
each
early
either
else
elsewhere
enough
etc
etcetera
even
ever
every
everyone
everything
everywhere
except
far
few
fill
find
fire
for
former
formerly
found
from
front
full
further
get
give
had
has
have
he
hence
her
here
hereafter
hereby
herein
hereupon
hers
herself
him
himself
his
how
however
i
if
in
inc
indeed
interest
into
is
it
its
itself
keep
last
late
later
latter
latterly
least
less
made
many
may
me
meanwhile
med
might
mine
more
moreover
most
mostly
move
much
must
myself
name
namely
near
neither
never
nevertheless
next
no
nobody
non
none
noone
nor
not
note
nothing
now
nowhere
of
off
often
on
once
only
onto
or
other
others
otherwise
our
ours
ourselves
out
over
own
per
perhaps
please
pre
pro
put
raise
rather
run
same
saw
see
seem
seemed
seeming
seems
seen
several
she
should
show
side
since
sincere
so
some
somehow
someone
something
sometime
sometimes
somewhere
still
such
take
tha
than
that
the
their
them
themselves
then
thence
there
thereafter
thereby
therefore
therein
thereupon
these
they
thick
thin
this
tho
those
though
through
throughout
thru
thus
thy
tip
to
together
too
toward
towards
under
until
up
upon
us
use
very
via
was
we
well
were
what
whatever
when
whence
whenever
where
whereafter
whereas
whereby
wherein
whereupon
wherever
whether
which
while
whither
who
whoever
whole
whom
whose
why
will
with
within
without
would
yet
you
your
yours
yourself
yourselves

## File: html/00a7843d-61be-6183-a06c-0fb9a1444924.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TreeNodeType Enumeration |
| [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Indicated a node type which must be created.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public enum TreeNodeType ``` |

| Visual Basic |
| --- |
| ``` Public Enumeration TreeNodeType ``` |

| Visual C++ |
| --- |
| ``` public enum class TreeNodeType ``` |

| JScript |
| --- |
| ``` public enum TreeNodeType ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.TreeNodeType = function(); Syncfusion.Scripting.Design.TreeNodeType.createEnum('Syncfusion.Scripting.Design.TreeNodeType', false); ``` |

# ![](icons/collapse_all.gif)Members

|  | Member name | Value | Description |
|  | Object | 0 | For creating "object" type of tree node. |
|  | Property | 1 | For creating "property" type of tree node. |
|  | Item | 2 | For creating "item" type of tree node. |
|  | Event | 3 | For creating "event" type of tree node. |
|  | EventHandler | 4 | Already created event handler. |

# ![](icons/collapse_all.gif)See Also

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/0297717a-1770-f743-b425-93dad595a5ed.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptUITypeEditor..::..PaintValue Method |
| ScriptUITypeEditor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Handles painting the value for the editor.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public override void PaintValue( 	PaintValueEventArgs e ) ``` |

| Visual Basic |
| --- |
| ``` Public Overrides Sub PaintValue ( _ 	e As PaintValueEventArgs _ ) ``` |

| Visual C++ |
| --- |
| ``` public: virtual void PaintValue( 	PaintValueEventArgs^ e ) override ``` |

| JScript |
| --- |
| ``` public override function PaintValue( 	e : PaintValueEventArgs ) ``` |

| JavaScript |
| --- |
| ``` function PaintValue(e); ``` |

#### Parameters

e
:   Type: [System.Drawing.Design..::..PaintValueEventArgs](http://msdn2.microsoft.com/en-us/library/ty527cas)

# ![](icons/collapse_all.gif)Remarks

Does nothing except call the base class PaintValue method.

# ![](icons/collapse_all.gif)See Also

ScriptUITypeEditor Class

ScriptUITypeEditor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/03b282cf-7e88-bfe9-d1c1-1f8bd8a52e98.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..AddAssemblyReference Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Adds the assembly to the list of referenced assemblies.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void AddAssemblyReference( 	string assembly ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub AddAssemblyReference ( _ 	assembly As String _ ) ``` |

| Visual C++ |
| --- |
| ``` public: void AddAssemblyReference( 	String^ assembly ) ``` |

| JScript |
| --- |
| ``` public function AddAssemblyReference( 	assembly : String ) ``` |

| JavaScript |
| --- |
| ``` function AddAssemblyReference(assembly); ``` |

#### Parameters

assembly
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)
    New assembly to reference.

# ![](icons/collapse_all.gif)Exceptions

| Exception | Condition |
| --- | --- |
| [System..::..ArgumentException](http://msdn2.microsoft.com/en-us/library/3w1b3114) | When assembly is null. |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/0765cc30-74c3-9a8e-5c7e-3c7a6279d543.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TagContainer Constructor (Object, String, TreeNodeType) |
| TagContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public TagContainer( 	Object prop, 	string name, 	TreeNodeType nodeType ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	prop As Object, _ 	name As String, _ 	nodeType As TreeNodeType _ ) ``` |

| Visual C++ |
| --- |
| ``` public: TagContainer( 	Object^ prop,  	String^ name,  	TreeNodeType nodeType ) ``` |

| JScript |
| --- |
| ``` public function TagContainer( 	prop : Object,  	name : String,  	nodeType : TreeNodeType ) ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.TagContainer = function(prop, name, nodeType); ``` |

#### Parameters

prop
:   Type: [System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)

name
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

nodeType
:   Type: Syncfusion.Scripting.Design..::..TreeNodeType

# ![](icons/collapse_all.gif)See Also

TagContainer Class

TagContainer Members

TagContainer Overload

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/096ac728-4da7-4162-641e-912849158886.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..EnableExternalRun Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public bool EnableExternalRun { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property EnableExternalRun As Boolean 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property bool EnableExternalRun { 	bool get (); 	void set (bool value); } ``` |

| JScript |
| --- |
| ``` function get EnableExternalRun () : boolean function set EnableExternalRun (value : boolean) ``` |

| JavaScript |
| --- |
| ``` function get_EnableExternalRun(); function set_EnableExternalRun(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/0f8ae5be-f319-5d24-c405-c07bcde2f470.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..RootMoniker Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public string RootMoniker { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property RootMoniker As String 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property String^ RootMoniker { 	String^ get (); 	void set (String^ value); } ``` |

| JScript |
| --- |
| ``` function get RootMoniker () : String function set RootMoniker (value : String) ``` |

| JavaScript |
| --- |
| ``` function get_RootMoniker(); function set_RootMoniker(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/0fa1fb2a-61ea-9971-c58f-c21a94b0ef46.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper..::..GetEventUnsubscriberScript Method |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public static string GetEventUnsubscriberScript( 	ScriptLanguages language, 	string nmespace, 	string scriptclass, 	string classname, 	EventInfo evinfo ) ``` |

| Visual Basic |
| --- |
| ``` Public Shared Function GetEventUnsubscriberScript ( _ 	language As ScriptLanguages, _ 	nmespace As String, _ 	scriptclass As String, _ 	classname As String, _ 	evinfo As EventInfo _ ) As String ``` |

| Visual C++ |
| --- |
| ``` public: static String^ GetEventUnsubscriberScript( 	ScriptLanguages language,  	String^ nmespace,  	String^ scriptclass,  	String^ classname,  	EventInfo^ evinfo ) ``` |

| JScript |
| --- |
| ``` public static function GetEventUnsubscriberScript( 	language : ScriptLanguages,  	nmespace : String,  	scriptclass : String,  	classname : String,  	evinfo : EventInfo ) : String ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper.GetEventUnsubscriberScript = function(language, nmespace, scriptclass, classname, evinfo); ``` |

#### Parameters

language
:   Type: ScriptLanguages

nmespace
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

scriptclass
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

classname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

evinfo
:   Type: [System.Reflection..::..EventInfo](http://msdn2.microsoft.com/en-us/library/wzdwwzya)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptWrapper.GetEventUnsubscriberScript(Syncfusion.Scripting.ScriptLanguages,System.String,System.String,System.String,System.Reflection.EventInfo)"]

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/10b704eb-06d6-e037-1176-92fcc7de4b30.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptUITypeEditor..::..GetPaintValueSupported Method |
| ScriptUITypeEditor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Determines if the editor manually draws the value in the property grid.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public override bool GetPaintValueSupported( 	ITypeDescriptorContext context ) ``` |

| Visual Basic |
| --- |
| ``` Public Overrides Function GetPaintValueSupported ( _ 	context As ITypeDescriptorContext _ ) As Boolean ``` |

| Visual C++ |
| --- |
| ``` public: virtual bool GetPaintValueSupported( 	ITypeDescriptorContext^ context ) override ``` |

| JScript |
| --- |
| ``` public override function GetPaintValueSupported( 	context : ITypeDescriptorContext ) : boolean ``` |

| JavaScript |
| --- |
| ``` function GetPaintValueSupported(context); ``` |

#### Parameters

context
:   Type: [System.ComponentModel..::..ITypeDescriptorContext](http://msdn2.microsoft.com/en-us/library/8d4c9xy5)

#### Return Value

Always returns false

# ![](icons/collapse_all.gif)See Also

ScriptUITypeEditor Class

ScriptUITypeEditor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/13d5fbe5-89b3-2561-cb40-a6aff15192f2.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..SaveToFile Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void SaveToFile() ``` |

| Visual Basic |
| --- |
| ``` Public Sub SaveToFile ``` |

| Visual C++ |
| --- |
| ``` public: void SaveToFile() ``` |

| JScript |
| --- |
| ``` public function SaveToFile() ``` |

| JavaScript |
| --- |
| ``` function SaveToFile(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/16bc1847-4d28-0f7f-83bf-95e8cf3fa678.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| NodeDoubleClickEventArgs Class |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public class NodeDoubleClickEventArgs : EventArgs ``` |

| Visual Basic |
| --- |
| ``` Public Class NodeDoubleClickEventArgs _ 	Inherits EventArgs ``` |

| Visual C++ |
| --- |
| ``` public ref class NodeDoubleClickEventArgs : public EventArgs ``` |

| JScript |
| --- |
| ``` public class NodeDoubleClickEventArgs extends EventArgs ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.NodeDoubleClickEventArgs = function();  Type.createClass( 	'Syncfusion.Scripting.Design.NodeDoubleClickEventArgs', 	EventArgs); ``` |

# ![](icons/collapse_all.gif)Inheritance Hierarchy

[System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)
  [System..::..EventArgs](http://msdn2.microsoft.com/en-us/library/118wxtk3)
    Syncfusion.Scripting.Design..::..NodeDoubleClickEventArgs

# ![](icons/collapse_all.gif)See Also

NodeDoubleClickEventArgs Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/171960ff-fcee-a854-30b6-d61038da8828.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| IScriptEditor..::..UpdateScript Method |
| IScriptEditor Interface [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Updates the script object with the current values in the editor.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` void UpdateScript( 	Script script ) ``` |

| Visual Basic |
| --- |
| ``` Sub UpdateScript ( _ 	script As Script _ ) ``` |

| Visual C++ |
| --- |
| ``` void UpdateScript( 	Script^ script ) ``` |

| JScript |
| --- |
| ``` function UpdateScript( 	script : Script ) ``` |

| JavaScript |
| --- |
| ``` function UpdateScript(script); ``` |

#### Parameters

script
:   Type: Script
    Script to update

# ![](icons/collapse_all.gif)See Also

IScriptEditor Interface

IScriptEditor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/17513dc8-4824-6e4b-e29e-bb64f56ab87d.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl Class |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Script Engine control. Support writing multi-language script.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public class ScriptEditControl : UserControl ``` |

| Visual Basic |
| --- |
| ``` Public Class ScriptEditControl _ 	Inherits UserControl ``` |

| Visual C++ |
| --- |
| ``` public ref class ScriptEditControl : public UserControl ``` |

| JScript |
| --- |
| ``` public class ScriptEditControl extends UserControl ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptEditControl = function();  Type.createClass( 	'Syncfusion.Scripting.Design.ScriptEditControl', 	UserControl); ``` |

# ![](icons/collapse_all.gif)Inheritance Hierarchy

[System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)
  [System..::..MarshalByRefObject](http://msdn2.microsoft.com/en-us/library/w4302s1f)
    [System.ComponentModel..::..Component](http://msdn2.microsoft.com/en-us/library/9wbadbce)
      [System.Windows.Forms..::..Control](http://msdn2.microsoft.com/en-us/library/36cd312w)
        [System.Windows.Forms..::..ScrollableControl](http://msdn2.microsoft.com/en-us/library/7xhk8yhk)
          [System.Windows.Forms..::..ContainerControl](http://msdn2.microsoft.com/en-us/library/e7d2a552)
            [System.Windows.Forms..::..UserControl](http://msdn2.microsoft.com/en-us/library/97855yck)
              Syncfusion.Scripting.Design..::..ScriptEditControl

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/1a9b3149-6a85-2ab1-d3f8-ac35cf0d386d.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..SelectedObject Property |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Object used for browse in TreeView.
Get or set.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptObject SelectedObject { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property SelectedObject As ScriptObject 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property ScriptObject^ SelectedObject { 	ScriptObject^ get (); 	void set (ScriptObject^ value); } ``` |

| JScript |
| --- |
| ``` function get SelectedObject () : ScriptObject function set SelectedObject (value : ScriptObject) ``` |

| JavaScript |
| --- |
| ``` function get_SelectedObject(); function set_SelectedObject(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/2561d862-0efd-8d60-fc00-c89d1ed62f8c.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..ScriptChanged Event |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Send when script is changed.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public event EventHandler ScriptChanged ``` |

| Visual Basic |
| --- |
| ``` Public Event ScriptChanged As EventHandler ``` |

| Visual C++ |
| --- |
| ``` public:  event EventHandler^ ScriptChanged { 	void add (EventHandler^ value); 	void remove (EventHandler^ value); } ``` |

| JScript |
| --- |
| ``` JScript does not support events. ``` |

| JavaScript |
| --- |
| ``` function add_ScriptChanged(value); function remove_ScriptChanged(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/29738453-4b82-4a7c-b2b3-58f12f60003d.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..Script Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public Script Script { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property Script As Script 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property Script^ Script { 	Script^ get (); 	void set (Script^ value); } ``` |

| JScript |
| --- |
| ``` function get Script () : Script function set Script (value : Script) ``` |

| JavaScript |
| --- |
| ``` function get_Script(); function set_Script(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/2b89f719-83d6-d972-e79a-aa654009f054.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..bExternalCompile Field |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected bool bExternalCompile ``` |

| Visual Basic |
| --- |
| ``` Protected bExternalCompile As Boolean ``` |

| Visual C++ |
| --- |
| ``` protected: bool bExternalCompile ``` |

| JScript |
| --- |
| ``` protected var bExternalCompile : boolean ``` |

| JavaScript |
| --- |
| ``` var bExternalCompile ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/310ce54e-1dda-4a0a-8a1a-de2dadc199f0.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptEditControl Methods |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptEditControl type exposes the following members.

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | AddAssemblyReference | Adds the assembly to the list of referenced assemblies. |
| ![Public method](icons/pubmethod.gif "Public method") | AddScriptableObject |  |
| ![Public method](icons/pubmethod.gif "Public method") | ClearAssemblyReferences |  |
| ![Public method](icons/pubmethod.gif "Public method") | CompileScript |  |
| ![Protected method](icons/protmethod.gif "Protected method") | Dispose | Clean up any resources being used. (Overrides [ContainerControl..::..Dispose(Boolean)](http://msdn2.microsoft.com/en-us/library/1ekay3aw).) |
| ![Protected method](icons/protmethod.gif "Protected method") | GetFileDialogFilter |  |
| ![Public method](icons/pubmethod.gif "Public method") | InitializeScriptEditor(Script) | Loads the data from the script into the editor. |
| ![Public method](icons/pubmethod.gif "Public method") | InitializeScriptEditor(ScriptingManager) |  |
| ![Public method](icons/pubmethod.gif "Public method") | New |  |
| ![Public method](icons/pubmethod.gif "Public method") | ObjectBrowser\_NodeDoubleClick |  |
| ![Protected method](icons/protmethod.gif "Protected method") | OnLanguageChange |  |
| ![Protected method](icons/protmethod.gif "Protected method") | OnScriptChange |  |
| ![Public method](icons/pubmethod.gif "Public method") | OpenFile |  |
| ![Public method](icons/pubmethod.gif "Public method") | RemoveScriptableObject |  |
| ![Public method](icons/pubmethod.gif "Public method") | RunScript |  |
| ![Public method](icons/pubmethod.gif "Public method") | SaveToFile |  |
| ![Protected method](icons/protmethod.gif "Protected method") | scriptingManager\_CompileError |  |
| ![Protected method](icons/protmethod.gif "Protected method") | SetCompileButtonsState |  |
| ![Public method](icons/pubmethod.gif "Public method") | StopScript |  |
| ![Public method](icons/pubmethod.gif "Public method") | UpdateScript | Updates the script object with the current values in the editor. |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/31740a0c-3e20-d191-cce0-f195391f5d34.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper Class |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Summary description for ScriptWrapper.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public class ScriptWrapper ``` |

| Visual Basic |
| --- |
| ``` Public Class ScriptWrapper ``` |

| Visual C++ |
| --- |
| ``` public ref class ScriptWrapper ``` |

| JScript |
| --- |
| ``` public class ScriptWrapper ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper = function();  Type.createClass( 	'Syncfusion.Scripting.Design.ScriptWrapper'); ``` |

# ![](icons/collapse_all.gif)Inheritance Hierarchy

[System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)
  Syncfusion.Scripting.Design..::..ScriptWrapper

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/31a549d7-f6d8-9623-8468-2021915ee413.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..ScriptLanguage Property |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Sets or gets script

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptLanguages ScriptLanguage { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property ScriptLanguage As ScriptLanguages 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property ScriptLanguages ScriptLanguage { 	ScriptLanguages get (); 	void set (ScriptLanguages value); } ``` |

| JScript |
| --- |
| ``` function get ScriptLanguage () : ScriptLanguages function set ScriptLanguage (value : ScriptLanguages) ``` |

| JavaScript |
| --- |
| ``` function get_ScriptLanguage(); function set_ScriptLanguage(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/3635480a-8289-8b7a-a6b4-e1eb5665f66b.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..CompileScript Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public bool CompileScript() ``` |

| Visual Basic |
| --- |
| ``` Public Function CompileScript As Boolean ``` |

| Visual C++ |
| --- |
| ``` public: bool CompileScript() ``` |

| JScript |
| --- |
| ``` public function CompileScript() : boolean ``` |

| JavaScript |
| --- |
| ``` function CompileScript(); ``` |

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptEditControl.CompileScript"]

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/3749a60c-3668-4133-9e4f-978d94b0ca59.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptUITypeEditor..::..GetEditStyle Method |
| ScriptUITypeEditor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Returns the editor style.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public override UITypeEditorEditStyle GetEditStyle( 	ITypeDescriptorContext context ) ``` |

| Visual Basic |
| --- |
| ``` Public Overrides Function GetEditStyle ( _ 	context As ITypeDescriptorContext _ ) As UITypeEditorEditStyle ``` |

| Visual C++ |
| --- |
| ``` public: virtual UITypeEditorEditStyle GetEditStyle( 	ITypeDescriptorContext^ context ) override ``` |

| JScript |
| --- |
| ``` public override function GetEditStyle( 	context : ITypeDescriptorContext ) : UITypeEditorEditStyle ``` |

| JavaScript |
| --- |
| ``` function GetEditStyle(context); ``` |

#### Parameters

context
:   Type: [System.ComponentModel..::..ITypeDescriptorContext](http://msdn2.microsoft.com/en-us/library/8d4c9xy5)
    Designer host context

#### Return Value

Always returns UITypeEditorEditStyle.Modal as the editor style

# ![](icons/collapse_all.gif)See Also

ScriptUITypeEditor Class

ScriptUITypeEditor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/37b3b39b-7853-325c-f587-3642626fa241.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ErrorDescriptor Members |
| ErrorDescriptor Class [Constructors](#constructorTableToggle) [Methods](#methodTableToggle) [Properties](#propertyTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ErrorDescriptor type exposes the following members.

# ![](icons/collapse_all.gif)Constructors

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | ErrorDescriptor | Initialized class properties. |

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | ToString | (Overrides [Object..::..ToString()()()()](http://msdn2.microsoft.com/en-us/library/7bxwbwt2).) |

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | Column | Error colum number |
| ![Public property](icons/pubproperty.gif "Public property") | Line | Error line |
| ![Public property](icons/pubproperty.gif "Public property") | Message | Error Message |

# ![](icons/collapse_all.gif)See Also

ErrorDescriptor Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/3847b6b7-d43c-f998-f152-e07873121479.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..InitializeScriptEditor Method (Script) |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Loads the data from the script into the editor.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public virtual void InitializeScriptEditor( 	Script script ) ``` |

| Visual Basic |
| --- |
| ``` Public Overridable Sub InitializeScriptEditor ( _ 	script As Script _ ) ``` |

| Visual C++ |
| --- |
| ``` public: virtual void InitializeScriptEditor( 	Script^ script ) ``` |

| JScript |
| --- |
| ``` public function InitializeScriptEditor( 	script : Script ) ``` |

| JavaScript |
| --- |
| ``` function InitializeScriptEditor(script); ``` |

#### Parameters

script
:   Type: Script
    Script to load into the editor

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

InitializeScriptEditor Overload

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/3ce2056d-8757-bc0b-dc81-68f0a24fde74.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser Methods |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptObjectBrowser type exposes the following members.

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Protected method](icons/protmethod.gif "Protected method") | BuildEventsList |  |
| ![Protected method](icons/protmethod.gif "Protected method") | BuildItemsCollection |  |
| ![Protected method](icons/protmethod.gif "Protected method") | BuildPropertiesList |  |
| ![Protected method](icons/protmethod.gif "Protected method") | BuildTreeNodeItem |  |
| ![Protected method](icons/protmethod.gif "Protected method") | Dispose | Clean up any resources being used. (Overrides [Control..::..Dispose(Boolean)](http://msdn2.microsoft.com/en-us/library/a4zkb31d).) |
| ![Protected method](icons/protmethod.gif "Protected method") | IsBrowsableCollection |  |
| ![Protected method](icons/protmethod.gif "Protected method") | IsScriptBrowsable(MemberInfo) |  |
| ![Protected method](icons/protmethod.gif "Protected method") | IsScriptBrowsable(MemberInfo, array<ScriptBrowsableAttribute>[]()[][]%) |  |
| ![Protected method](icons/protmethod.gif "Protected method") | OnNodeDoubleClick |  |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/3e183b41-47e5-01c0-79d4-9ea0f9a917f5.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper..::..GetWrappedScript Method |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public static string GetWrappedScript( 	ScriptLanguages language, 	string script, 	string namespacedirective, 	string directives, 	string globalcode, 	string classname, 	string baseclassname ) ``` |

| Visual Basic |
| --- |
| ``` Public Shared Function GetWrappedScript ( _ 	language As ScriptLanguages, _ 	script As String, _ 	namespacedirective As String, _ 	directives As String, _ 	globalcode As String, _ 	classname As String, _ 	baseclassname As String _ ) As String ``` |

| Visual C++ |
| --- |
| ``` public: static String^ GetWrappedScript( 	ScriptLanguages language,  	String^ script,  	String^ namespacedirective,  	String^ directives,  	String^ globalcode,  	String^ classname,  	String^ baseclassname ) ``` |

| JScript |
| --- |
| ``` public static function GetWrappedScript( 	language : ScriptLanguages,  	script : String,  	namespacedirective : String,  	directives : String,  	globalcode : String,  	classname : String,  	baseclassname : String ) : String ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper.GetWrappedScript = function(language, script, namespacedirective, directives, globalcode, classname, baseclassname); ``` |

#### Parameters

language
:   Type: ScriptLanguages

script
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

namespacedirective
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

directives
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

globalcode
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

classname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

baseclassname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptWrapper.GetWrappedScript(Syncfusion.Scripting.ScriptLanguages,System.String,System.String,System.String,System.String,System.String,System.String)"]

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/3e223ae8-eb1c-18a3-5352-726a0d1ce4a5.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| TagContainer Constructor |
| TagContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

# ![](icons/collapse_all.gif)Overload List

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | TagContainer(Object, String, TreeNodeType) |  |
| ![Public method](icons/pubmethod.gif "Public method") | TagContainer(EventInfo, String, TreeNodeType) |  |

# ![](icons/collapse_all.gif)See Also

TagContainer Class

TagContainer Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/40d092e2-0843-9dc0-97b7-722802ae7d76.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| NodeDoubleClickEventArgs..::..TagContainer Property |
| NodeDoubleClickEventArgs Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Gets node tag container.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public TagContainer TagContainer { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property TagContainer As TagContainer 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property TagContainer^ TagContainer { 	TagContainer^ get (); } ``` |

| JScript |
| --- |
| ``` function get TagContainer () : TagContainer  ``` |

| JavaScript |
| --- |
| ``` function get_TagContainer();  ``` |

# ![](icons/collapse_all.gif)See Also

NodeDoubleClickEventArgs Class

NodeDoubleClickEventArgs Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/4329d644-df03-0919-239d-5c04a615d489.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| AssemblyTypeMap Constructor |
| AssemblyTypeMap Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public AssemblyTypeMap() ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

| Visual C++ |
| --- |
| ``` public: AssemblyTypeMap() ``` |

| JScript |
| --- |
| ``` public function AssemblyTypeMap() ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.AssemblyTypeMap = function(); ``` |

# ![](icons/collapse_all.gif)See Also

AssemblyTypeMap Class

AssemblyTypeMap Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/441034b7-2273-c777-7f6b-a9fc27bce6da.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptWrapper Methods |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptWrapper type exposes the following members.

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | AddEventSubscriptionToScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetEventHandlerScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetEventHandlerScriptByType |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetEventSubscriberScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetEventUnsubscriberScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetLanguageKeywords |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetNewMethodScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetUnwrappedScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetWrappedScript |  |

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/4511e833-4029-7b46-a6d5-076d2c10a513.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..EnableExternalCompile Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Indicates if the ScriptingManager is being used for external compilation of the script.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public bool EnableExternalCompile { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property EnableExternalCompile As Boolean 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property bool EnableExternalCompile { 	bool get (); 	void set (bool value); } ``` |

| JScript |
| --- |
| ``` function get EnableExternalCompile () : boolean function set EnableExternalCompile (value : boolean) ``` |

| JavaScript |
| --- |
| ``` function get_EnableExternalCompile(); function set_EnableExternalCompile(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/49430b31-e8b6-c93e-6bd7-1b9456bfd0d5.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..bPendingSave Field |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected bool bPendingSave ``` |

| Visual Basic |
| --- |
| ``` Protected bPendingSave As Boolean ``` |

| Visual C++ |
| --- |
| ``` protected: bool bPendingSave ``` |

| JScript |
| --- |
| ``` protected var bPendingSave : boolean ``` |

| JavaScript |
| --- |
| ``` var bPendingSave ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/496a33d6-e246-8b1c-1128-310758fd9921.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TagContainer Class |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public class TagContainer ``` |

| Visual Basic |
| --- |
| ``` Public Class TagContainer ``` |

| Visual C++ |
| --- |
| ``` public ref class TagContainer ``` |

| JScript |
| --- |
| ``` public class TagContainer ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.TagContainer = function();  Type.createClass( 	'Syncfusion.Scripting.Design.TagContainer'); ``` |

# ![](icons/collapse_all.gif)Inheritance Hierarchy

[System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)
  Syncfusion.Scripting.Design..::..TagContainer
    Syncfusion.Scripting.Design..::..TagEventContainer

# ![](icons/collapse_all.gif)See Also

TagContainer Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/49773ada-0347-791f-eb9f-77e46858c03d.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..SetCompileButtonsState Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected void SetCompileButtonsState() ``` |

| Visual Basic |
| --- |
| ``` Protected Sub SetCompileButtonsState ``` |

| Visual C++ |
| --- |
| ``` protected: void SetCompileButtonsState() ``` |

| JScript |
| --- |
| ``` protected function SetCompileButtonsState() ``` |

| JavaScript |
| --- |
| ``` function SetCompileButtonsState(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/4cb1e482-9cd9-0028-1e3f-6de7fdf0533f.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser Properties |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptObjectBrowser type exposes the following members.

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | BrowserTreeView |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptLanguage | Sets or gets script |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptSite |  |
| ![Public property](icons/pubproperty.gif "Public property") | SelectedObject | Object used for browse in TreeView. Get or set. |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/4e1f1724-c30d-bef7-e1f3-d217ebd9d5ff.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..bExternalRun Field |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected bool bExternalRun ``` |

| Visual Basic |
| --- |
| ``` Protected bExternalRun As Boolean ``` |

| Visual C++ |
| --- |
| ``` protected: bool bExternalRun ``` |

| JScript |
| --- |
| ``` protected var bExternalRun : boolean ``` |

| JavaScript |
| --- |
| ``` var bExternalRun ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/4e7425a1-b8fc-3078-e753-2661292f958e.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..AddScriptableObject Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void AddScriptableObject( 	ScriptObject scriptableitem ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub AddScriptableObject ( _ 	scriptableitem As ScriptObject _ ) ``` |

| Visual C++ |
| --- |
| ``` public: void AddScriptableObject( 	ScriptObject^ scriptableitem ) ``` |

| JScript |
| --- |
| ``` public function AddScriptableObject( 	scriptableitem : ScriptObject ) ``` |

| JavaScript |
| --- |
| ``` function AddScriptableObject(scriptableitem); ``` |

#### Parameters

scriptableitem
:   Type: ScriptObject

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/501f3167-78c0-4138-dd2f-37e47ea5be82.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..ScriptingManager Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptingManager ScriptingManager { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property ScriptingManager As ScriptingManager 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property ScriptingManager^ ScriptingManager { 	ScriptingManager^ get (); 	void set (ScriptingManager^ value); } ``` |

| JScript |
| --- |
| ``` function get ScriptingManager () : ScriptingManager function set ScriptingManager (value : ScriptingManager) ``` |

| JavaScript |
| --- |
| ``` function get_ScriptingManager(); function set_ScriptingManager(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/536f9b95-02a0-4460-b85a-8243b076fbc6.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptUITypeEditor Methods |
| ScriptUITypeEditor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptUITypeEditor type exposes the following members.

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | EditValue | Called by the designer to edit a script. (Overrides [UITypeEditor..::..EditValue(ITypeDescriptorContext, IServiceProvider, Object)](http://msdn2.microsoft.com/en-us/library/yezs56kx).) |
| ![Public method](icons/pubmethod.gif "Public method") | GetEditStyle | Returns the editor style. (Overrides [UITypeEditor..::..GetEditStyle(ITypeDescriptorContext)](http://msdn2.microsoft.com/en-us/library/xtsths3h).) |
| ![Public method](icons/pubmethod.gif "Public method") | GetPaintValueSupported | Determines if the editor manually draws the value in the property grid. (Overrides [UITypeEditor..::..GetPaintValueSupported(ITypeDescriptorContext)](http://msdn2.microsoft.com/en-us/library/3h427xby).) |
| ![Public method](icons/pubmethod.gif "Public method") | PaintValue | Handles painting the value for the editor. (Overrides [UITypeEditor..::..PaintValue(PaintValueEventArgs)](http://msdn2.microsoft.com/en-us/library/aahy196s).) |

# ![](icons/collapse_all.gif)See Also

ScriptUITypeEditor Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/5394ee54-cb7d-4c08-b4e0-3d1997b37bf9.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..InitializeScriptEditor Method (ScriptingManager) |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void InitializeScriptEditor( 	ScriptingManager scriptmanager ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub InitializeScriptEditor ( _ 	scriptmanager As ScriptingManager _ ) ``` |

| Visual C++ |
| --- |
| ``` public: void InitializeScriptEditor( 	ScriptingManager^ scriptmanager ) ``` |

| JScript |
| --- |
| ``` public function InitializeScriptEditor( 	scriptmanager : ScriptingManager ) ``` |

| JavaScript |
| --- |
| ``` function InitializeScriptEditor(scriptmanager); ``` |

#### Parameters

scriptmanager
:   Type: ScriptingManager

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

InitializeScriptEditor Overload

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/55334ad4-84fb-ba10-4274-df8e35a05310.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..UpdateScript Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Updates the script object with the current values in the editor.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void UpdateScript( 	Script script ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub UpdateScript ( _ 	script As Script _ ) ``` |

| Visual C++ |
| --- |
| ``` public: void UpdateScript( 	Script^ script ) ``` |

| JScript |
| --- |
| ``` public function UpdateScript( 	script : Script ) ``` |

| JavaScript |
| --- |
| ``` function UpdateScript(script); ``` |

#### Parameters

script
:   Type: Script
    Script to update

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/5770b950-f070-4db8-505e-bebbc51c23bc.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..IsScriptBrowsable Method (MemberInfo) |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected bool IsScriptBrowsable( 	MemberInfo type ) ``` |

| Visual Basic |
| --- |
| ``` Protected Function IsScriptBrowsable ( _ 	type As MemberInfo _ ) As Boolean ``` |

| Visual C++ |
| --- |
| ``` protected: bool IsScriptBrowsable( 	MemberInfo^ type ) ``` |

| JScript |
| --- |
| ``` protected function IsScriptBrowsable( 	type : MemberInfo ) : boolean ``` |

| JavaScript |
| --- |
| ``` function IsScriptBrowsable(type); ``` |

#### Parameters

type
:   Type: [System.Reflection..::..MemberInfo](http://msdn2.microsoft.com/en-us/library/8fek28hz)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptObjectBrowser.IsScriptBrowsable(System.Reflection.MemberInfo)"]

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

IsScriptBrowsable Overload

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/58b77276-156a-cf91-bc13-c1e1dc75e7a8.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..RunScript Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void RunScript() ``` |

| Visual Basic |
| --- |
| ``` Public Sub RunScript ``` |

| Visual C++ |
| --- |
| ``` public: void RunScript() ``` |

| JScript |
| --- |
| ``` public function RunScript() ``` |

| JavaScript |
| --- |
| ``` function RunScript(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/590ec367-9303-3748-ff05-82d7787429cb.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TagEventContainer Constructor |
| TagEventContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public TagEventContainer( 	EventInfo evInfo, 	string name, 	TreeNodeType nodeType ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	evInfo As EventInfo, _ 	name As String, _ 	nodeType As TreeNodeType _ ) ``` |

| Visual C++ |
| --- |
| ``` public: TagEventContainer( 	EventInfo^ evInfo,  	String^ name,  	TreeNodeType nodeType ) ``` |

| JScript |
| --- |
| ``` public function TagEventContainer( 	evInfo : EventInfo,  	name : String,  	nodeType : TreeNodeType ) ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.TagEventContainer = function(evInfo, name, nodeType); ``` |

#### Parameters

evInfo
:   Type: [System.Reflection..::..EventInfo](http://msdn2.microsoft.com/en-us/library/wzdwwzya)

name
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

nodeType
:   Type: Syncfusion.Scripting.Design..::..TreeNodeType

# ![](icons/collapse_all.gif)See Also

TagEventContainer Class

TagEventContainer Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/5abaa03d-0f30-8834-6ca8-c5c8fea568a4.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ErrorDescriptor Constructor |
| ErrorDescriptor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Initialized class properties.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ErrorDescriptor( 	string errMessage, 	int line, 	int col ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	errMessage As String, _ 	line As Integer, _ 	col As Integer _ ) ``` |

| Visual C++ |
| --- |
| ``` public: ErrorDescriptor( 	String^ errMessage,  	int line,  	int col ) ``` |

| JScript |
| --- |
| ``` public function ErrorDescriptor( 	errMessage : String,  	line : int,  	col : int ) ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ErrorDescriptor = function(errMessage, line, col); ``` |

#### Parameters

errMessage
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

line
:   Type: [System..::..Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

col
:   Type: [System..::..Int32](http://msdn2.microsoft.com/en-us/library/td2s409d)

# ![](icons/collapse_all.gif)See Also

ErrorDescriptor Class

ErrorDescriptor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/5bc7cb8d-a110-c258-30ef-230c03eca5a8.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptEditForm Properties |
| ScriptEditForm Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptEditForm type exposes the following members.

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | Form |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptEditControl |  |

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/5d402ece-bd6c-a21d-85e3-2fa286630284.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper..::..GetNewMethodScript Method |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public static string GetNewMethodScript( 	ScriptLanguages language, 	string methodname ) ``` |

| Visual Basic |
| --- |
| ``` Public Shared Function GetNewMethodScript ( _ 	language As ScriptLanguages, _ 	methodname As String _ ) As String ``` |

| Visual C++ |
| --- |
| ``` public: static String^ GetNewMethodScript( 	ScriptLanguages language,  	String^ methodname ) ``` |

| JScript |
| --- |
| ``` public static function GetNewMethodScript( 	language : ScriptLanguages,  	methodname : String ) : String ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper.GetNewMethodScript = function(language, methodname); ``` |

#### Parameters

language
:   Type: ScriptLanguages

methodname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptWrapper.GetNewMethodScript(Syncfusion.Scripting.ScriptLanguages,System.String)"]

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/5da0d8d3-bab8-7bb9-e305-dd4e7fec3fa3.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditForm..::..ScriptEditControl Property |
| ScriptEditForm Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptEditControl ScriptEditControl { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property ScriptEditControl As ScriptEditControl 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property ScriptEditControl^ ScriptEditControl { 	ScriptEditControl^ get (); } ``` |

| JScript |
| --- |
| ``` function get ScriptEditControl () : ScriptEditControl  ``` |

| JavaScript |
| --- |
| ``` function get_ScriptEditControl();  ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Class

ScriptEditForm Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/5f5bd106-dada-40d1-879a-e672d76022aa.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| NodeDoubleClickEventArgs Properties |
| NodeDoubleClickEventArgs Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The NodeDoubleClickEventArgs type exposes the following members.

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | NodeName | Gets node name. |
| ![Public property](icons/pubproperty.gif "Public property") | TagContainer | Gets node tag container. |

# ![](icons/collapse_all.gif)See Also

NodeDoubleClickEventArgs Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/5f849dd3-d55d-72e9-f8dc-b1d56ae35f4d.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptWrapper Members |
| ScriptWrapper Class [Constructors](#constructorTableToggle) [Methods](#methodTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptWrapper type exposes the following members.

# ![](icons/collapse_all.gif)Constructors

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | ScriptWrapper |  |

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | AddEventSubscriptionToScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetEventHandlerScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetEventHandlerScriptByType |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetEventSubscriberScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetEventUnsubscriberScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetLanguageKeywords |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetNewMethodScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetUnwrappedScript |  |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetWrappedScript |  |

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/5f928903-e459-6185-5135-f00e1ad909df.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper..::..GetUnwrappedScript Method |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public static string GetUnwrappedScript( 	ScriptLanguages language, 	string script, 	ref string namespacedirective, 	ref string directives, 	ref string globalcode, 	string classname, 	string baseclassname ) ``` |

| Visual Basic |
| --- |
| ``` Public Shared Function GetUnwrappedScript ( _ 	language As ScriptLanguages, _ 	script As String, _ 	ByRef namespacedirective As String, _ 	ByRef directives As String, _ 	ByRef globalcode As String, _ 	classname As String, _ 	baseclassname As String _ ) As String ``` |

| Visual C++ |
| --- |
| ``` public: static String^ GetUnwrappedScript( 	ScriptLanguages language,  	String^ script,  	String^% namespacedirective,  	String^% directives,  	String^% globalcode,  	String^ classname,  	String^ baseclassname ) ``` |

| JScript |
| --- |
| ``` public static function GetUnwrappedScript( 	language : ScriptLanguages,  	script : String,  	namespacedirective : String,  	directives : String,  	globalcode : String,  	classname : String,  	baseclassname : String ) : String ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper.GetUnwrappedScript = function(language, script, namespacedirective, directives, globalcode, classname, baseclassname); ``` |

#### Parameters

language
:   Type: ScriptLanguages

script
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

namespacedirective
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)%

directives
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)%

globalcode
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)%

classname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

baseclassname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptWrapper.GetUnwrappedScript(Syncfusion.Scripting.ScriptLanguages,System.String,System.String@,System.String@,System.String@,System.String,System.String)"]

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/6247d55b-db80-1c75-2a4b-c4a47bfcf816.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| TagEventContainer Members |
| TagEventContainer Class [Constructors](#constructorTableToggle) [Properties](#propertyTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The TagEventContainer type exposes the following members.

# ![](icons/collapse_all.gif)Constructors

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | TagEventContainer |  |

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | ClassName |  |

# ![](icons/collapse_all.gif)See Also

TagEventContainer Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/63194c5c-7d65-1766-aeba-2f0f93b653a1.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser Constructor |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptObjectBrowser() ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

| Visual C++ |
| --- |
| ``` public: ScriptObjectBrowser() ``` |

| JScript |
| --- |
| ``` public function ScriptObjectBrowser() ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptObjectBrowser = function(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/678cbb79-320a-1fe8-be50-68dd03c777c2.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| IScriptEditor Methods |
| IScriptEditor Interface [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The IScriptEditor type exposes the following members.

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | UpdateEditor | Loads the data from the script into the editor. |
| ![Public method](icons/pubmethod.gif "Public method") | UpdateScript | Updates the script object with the current values in the editor. |

# ![](icons/collapse_all.gif)See Also

IScriptEditor Interface

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/67eb6565-e318-7958-7b35-94ecd79836ef.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptUITypeEditor Members |
| ScriptUITypeEditor Class [Constructors](#constructorTableToggle) [Methods](#methodTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptUITypeEditor type exposes the following members.

# ![](icons/collapse_all.gif)Constructors

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | ScriptUITypeEditor | Default constructor. |

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | EditValue | Called by the designer to edit a script. (Overrides [UITypeEditor..::..EditValue(ITypeDescriptorContext, IServiceProvider, Object)](http://msdn2.microsoft.com/en-us/library/yezs56kx).) |
| ![Public method](icons/pubmethod.gif "Public method") | GetEditStyle | Returns the editor style. (Overrides [UITypeEditor..::..GetEditStyle(ITypeDescriptorContext)](http://msdn2.microsoft.com/en-us/library/xtsths3h).) |
| ![Public method](icons/pubmethod.gif "Public method") | GetPaintValueSupported | Determines if the editor manually draws the value in the property grid. (Overrides [UITypeEditor..::..GetPaintValueSupported(ITypeDescriptorContext)](http://msdn2.microsoft.com/en-us/library/3h427xby).) |
| ![Public method](icons/pubmethod.gif "Public method") | PaintValue | Handles painting the value for the editor. (Overrides [UITypeEditor..::..PaintValue(PaintValueEventArgs)](http://msdn2.microsoft.com/en-us/library/aahy196s).) |

# ![](icons/collapse_all.gif)See Also

ScriptUITypeEditor Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/6941a880-5fb8-ab0f-65dc-e5dca0992276.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptUITypeEditor Constructor |
| ScriptUITypeEditor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Default constructor.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptUITypeEditor() ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

| Visual C++ |
| --- |
| ``` public: ScriptUITypeEditor() ``` |

| JScript |
| --- |
| ``` public function ScriptUITypeEditor() ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptUITypeEditor = function(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptUITypeEditor Class

ScriptUITypeEditor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/6a78b959-625d-aca6-aa95-31a04e0c9cdc.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| IScriptEditor Properties |
| IScriptEditor Interface [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The IScriptEditor type exposes the following members.

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | Form | The Form object that implements the user interface. |

# ![](icons/collapse_all.gif)See Also

IScriptEditor Interface

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/71eede80-6885-dac3-0111-15696111470f.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..scriptingManager\_CompileError Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected void scriptingManager_CompileError( 	Object sender, 	VsaErrorEventArgs eventargs ) ``` |

| Visual Basic |
| --- |
| ``` Protected Sub scriptingManager_CompileError ( _ 	sender As Object, _ 	eventargs As VsaErrorEventArgs _ ) ``` |

| Visual C++ |
| --- |
| ``` protected: void scriptingManager_CompileError( 	Object^ sender,  	VsaErrorEventArgs^ eventargs ) ``` |

| JScript |
| --- |
| ``` protected function scriptingManager_CompileError( 	sender : Object,  	eventargs : VsaErrorEventArgs ) ``` |

| JavaScript |
| --- |
| ``` function scriptingManager_CompileError(sender, eventargs); ``` |

#### Parameters

sender
:   Type: [System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)

eventargs
:   Type: VsaErrorEventArgs

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/7357cbff-c5dc-7f5e-f5e3-0f8125a3a5ce.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ErrorDescriptor..::..ToString Method |
| ErrorDescriptor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public override string ToString() ``` |

| Visual Basic |
| --- |
| ``` Public Overrides Function ToString As String ``` |

| Visual C++ |
| --- |
| ``` public: virtual String^ ToString() override ``` |

| JScript |
| --- |
| ``` public override function ToString() : String ``` |

| JavaScript |
| --- |
| ``` function ToString(); ``` |

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ErrorDescriptor.ToString"]

# ![](icons/collapse_all.gif)See Also

ErrorDescriptor Class

ErrorDescriptor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/74d30286-6768-da16-f67c-952d208a702e.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditForm..::..SetManager Method |
| ScriptEditForm Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected void SetManager( 	ScriptingManager manager ) ``` |

| Visual Basic |
| --- |
| ``` Protected Sub SetManager ( _ 	manager As ScriptingManager _ ) ``` |

| Visual C++ |
| --- |
| ``` protected: void SetManager( 	ScriptingManager^ manager ) ``` |

| JScript |
| --- |
| ``` protected function SetManager( 	manager : ScriptingManager ) ``` |

| JavaScript |
| --- |
| ``` function SetManager(manager); ``` |

#### Parameters

manager
:   Type: ScriptingManager

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Class

ScriptEditForm Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/750673bb-6896-647f-b463-29539ef4d480.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..Dispose Method |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Clean up any resources being used.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected override void Dispose( 	bool disposing ) ``` |

| Visual Basic |
| --- |
| ``` Protected Overrides Sub Dispose ( _ 	disposing As Boolean _ ) ``` |

| Visual C++ |
| --- |
| ``` protected: virtual void Dispose( 	bool disposing ) override ``` |

| JScript |
| --- |
| ``` protected override function Dispose( 	disposing : boolean ) ``` |

| JavaScript |
| --- |
| ``` function Dispose(disposing); ``` |

#### Parameters

disposing
:   Type: [System..::..Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/7754a3ce-7292-4bdb-386d-aa1f0edf8e40.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..ScriptLanguage Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptLanguages ScriptLanguage { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property ScriptLanguage As ScriptLanguages 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property ScriptLanguages ScriptLanguage { 	ScriptLanguages get (); 	void set (ScriptLanguages value); } ``` |

| JScript |
| --- |
| ``` function get ScriptLanguage () : ScriptLanguages function set ScriptLanguage (value : ScriptLanguages) ``` |

| JavaScript |
| --- |
| ``` function get_ScriptLanguage(); function set_ScriptLanguage(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/7baecd8e-04bd-351e-6b05-840c07a39472.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ErrorDescriptor..::..Message Property |
| ErrorDescriptor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Error Message

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public string Message { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Message As String 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property String^ Message { 	String^ get (); } ``` |

| JScript |
| --- |
| ``` function get Message () : String  ``` |

| JavaScript |
| --- |
| ``` function get_Message();  ``` |

# ![](icons/collapse_all.gif)See Also

ErrorDescriptor Class

ErrorDescriptor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/7cbbec28-d0e0-d38e-b152-33333daf9962.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..New Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void New() ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

| Visual C++ |
| --- |
| ``` public: void New() ``` |

| JScript |
| --- |
| ``` public function New() ``` |

| JavaScript |
| --- |
| ``` function New(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/7e7aa46a-7b8b-22a4-3634-74efabf24c7b.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..BuildEventsList Method |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected void BuildEventsList( 	TreeNode node, 	EventInfo[] events ) ``` |

| Visual Basic |
| --- |
| ``` Protected Sub BuildEventsList ( _ 	node As TreeNode, _ 	events As EventInfo() _ ) ``` |

| Visual C++ |
| --- |
| ``` protected: void BuildEventsList( 	TreeNode^ node,  	array<EventInfo^>^ events ) ``` |

| JScript |
| --- |
| ``` protected function BuildEventsList( 	node : TreeNode,  	events : EventInfo[] ) ``` |

| JavaScript |
| --- |
| ``` function BuildEventsList(node, events); ``` |

#### Parameters

node
:   Type: [System.Windows.Forms..::..TreeNode](http://msdn2.microsoft.com/en-us/library/bctbxtcb)

events
:   Type: array<[System.Reflection..::..EventInfo](http://msdn2.microsoft.com/en-us/library/wzdwwzya)>[]()[][]

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/7f3190c1-2d1f-cde4-137d-16af4077975f.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ErrorDescriptor..::..Column Property |
| ErrorDescriptor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Error colum number

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public int Column { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Column As Integer 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property int Column { 	int get (); } ``` |

| JScript |
| --- |
| ``` function get Column () : int  ``` |

| JavaScript |
| --- |
| ``` function get_Column();  ``` |

# ![](icons/collapse_all.gif)See Also

ErrorDescriptor Class

ErrorDescriptor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/7fc7805e-2b6a-669c-a30e-c47556f42e86.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..AssemblyReferences Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public string[] AssemblyReferences { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property AssemblyReferences As String() 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property array<String^>^ AssemblyReferences { 	array<String^>^ get (); } ``` |

| JScript |
| --- |
| ``` function get AssemblyReferences () : String[]  ``` |

| JavaScript |
| --- |
| ``` function get_AssemblyReferences();  ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/82315633-52c0-5984-2854-97c55969a0fb.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..ClearAssemblyReferences Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void ClearAssemblyReferences() ``` |

| Visual Basic |
| --- |
| ``` Public Sub ClearAssemblyReferences ``` |

| Visual C++ |
| --- |
| ``` public: void ClearAssemblyReferences() ``` |

| JScript |
| --- |
| ``` public function ClearAssemblyReferences() ``` |

| JavaScript |
| --- |
| ``` function ClearAssemblyReferences(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/830cd4cf-db3c-c342-4c40-3a3197a4a13e.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| AssemblyTypeMap Members |
| AssemblyTypeMap Class [Constructors](#constructorTableToggle) [Methods](#methodTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The AssemblyTypeMap type exposes the following members.

# ![](icons/collapse_all.gif)Constructors

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | AssemblyTypeMap |  |

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetType |  |

# ![](icons/collapse_all.gif)See Also

AssemblyTypeMap Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/83c4aabd-4827-4198-765b-4f8d642f1001.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| IScriptEditor..::..Form Property |
| IScriptEditor Interface [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The Form object that implements the user interface.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` Form Form { get; } ``` |

| Visual Basic |
| --- |
| ``` ReadOnly Property Form As Form 	Get ``` |

| Visual C++ |
| --- |
| ``` property Form^ Form { 	Form^ get (); } ``` |

| JScript |
| --- |
| ``` function get Form () : Form  ``` |

| JavaScript |
| --- |
| ``` function get_Form();  ``` |

# ![](icons/collapse_all.gif)See Also

IScriptEditor Interface

IScriptEditor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/83eb264d-a5c5-a78b-05d7-21969c6a898e.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper..::..GetEventHandlerScriptByType Method |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public static string GetEventHandlerScriptByType( 	ScriptLanguages language, 	string classname, 	EventInfo evInfo ) ``` |

| Visual Basic |
| --- |
| ``` Public Shared Function GetEventHandlerScriptByType ( _ 	language As ScriptLanguages, _ 	classname As String, _ 	evInfo As EventInfo _ ) As String ``` |

| Visual C++ |
| --- |
| ``` public: static String^ GetEventHandlerScriptByType( 	ScriptLanguages language,  	String^ classname,  	EventInfo^ evInfo ) ``` |

| JScript |
| --- |
| ``` public static function GetEventHandlerScriptByType( 	language : ScriptLanguages,  	classname : String,  	evInfo : EventInfo ) : String ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper.GetEventHandlerScriptByType = function(language, classname, evInfo); ``` |

#### Parameters

language
:   Type: ScriptLanguages

classname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

evInfo
:   Type: [System.Reflection..::..EventInfo](http://msdn2.microsoft.com/en-us/library/wzdwwzya)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptWrapper.GetEventHandlerScriptByType(Syncfusion.Scripting.ScriptLanguages,System.String,System.Reflection.EventInfo)"]

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/87911ae5-6ac8-0326-e23e-a54e7aca0f24.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..ObjectBrowser\_NodeDoubleClick Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void ObjectBrowser_NodeDoubleClick( 	Object sender, 	NodeDoubleClickEventArgs e ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub ObjectBrowser_NodeDoubleClick ( _ 	sender As Object, _ 	e As NodeDoubleClickEventArgs _ ) ``` |

| Visual C++ |
| --- |
| ``` public: void ObjectBrowser_NodeDoubleClick( 	Object^ sender,  	NodeDoubleClickEventArgs^ e ) ``` |

| JScript |
| --- |
| ``` public function ObjectBrowser_NodeDoubleClick( 	sender : Object,  	e : NodeDoubleClickEventArgs ) ``` |

| JavaScript |
| --- |
| ``` function ObjectBrowser_NodeDoubleClick(sender, e); ``` |

#### Parameters

sender
:   Type: [System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)

e
:   Type: Syncfusion.Scripting.Design..::..NodeDoubleClickEventArgs

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/89112f62-a9d1-af99-951a-d5e2be8c7a0a.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ErrorDescriptor Methods |
| ErrorDescriptor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ErrorDescriptor type exposes the following members.

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | ToString | (Overrides [Object..::..ToString()()()()](http://msdn2.microsoft.com/en-us/library/7bxwbwt2).) |

# ![](icons/collapse_all.gif)See Also

ErrorDescriptor Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/8bd11de0-0d96-6156-fddc-389a546d7c76.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TagContainer..::..Name Property |
| TagContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public string Name { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Name As String 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property String^ Name { 	String^ get (); } ``` |

| JScript |
| --- |
| ``` function get Name () : String  ``` |

| JavaScript |
| --- |
| ``` function get_Name();  ``` |

# ![](icons/collapse_all.gif)See Also

TagContainer Class

TagContainer Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/8be3bc43-3810-e1e2-805c-fe2f46d28125.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..strScriptStart Field |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected string strScriptStart ``` |

| Visual Basic |
| --- |
| ``` Protected strScriptStart As String ``` |

| Visual C++ |
| --- |
| ``` protected: String^ strScriptStart ``` |

| JScript |
| --- |
| ``` protected var strScriptStart : String ``` |

| JavaScript |
| --- |
| ``` var strScriptStart ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/8c9cfb22-1cb1-26a0-47ea-d40ad56ceaac.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TagEventContainer Class |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public class TagEventContainer : TagContainer ``` |

| Visual Basic |
| --- |
| ``` Public Class TagEventContainer _ 	Inherits TagContainer ``` |

| Visual C++ |
| --- |
| ``` public ref class TagEventContainer : public TagContainer ``` |

| JScript |
| --- |
| ``` public class TagEventContainer extends TagContainer ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.TagEventContainer = function();  Type.createClass( 	'Syncfusion.Scripting.Design.TagEventContainer', 	Syncfusion.Scripting.Design.TagContainer); ``` |

# ![](icons/collapse_all.gif)Inheritance Hierarchy

[System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)
  Syncfusion.Scripting.Design..::..TagContainer
    Syncfusion.Scripting.Design..::..TagEventContainer

# ![](icons/collapse_all.gif)See Also

TagEventContainer Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/8d9c8be4-fa2b-e044-ea7c-c61e8d365f28.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..ScriptText Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Gets or sets script source code.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public string ScriptText { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property ScriptText As String 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property String^ ScriptText { 	String^ get (); 	void set (String^ value); } ``` |

| JScript |
| --- |
| ``` function get ScriptText () : String function set ScriptText (value : String) ``` |

| JavaScript |
| --- |
| ``` function get_ScriptText(); function set_ScriptText(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/8def267c-4676-9c18-0f5b-06ebfc724625.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..Dispose Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Clean up any resources being used.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected override void Dispose( 	bool disposing ) ``` |

| Visual Basic |
| --- |
| ``` Protected Overrides Sub Dispose ( _ 	disposing As Boolean _ ) ``` |

| Visual C++ |
| --- |
| ``` protected: virtual void Dispose( 	bool disposing ) override ``` |

| JScript |
| --- |
| ``` protected override function Dispose( 	disposing : boolean ) ``` |

| JavaScript |
| --- |
| ``` function Dispose(disposing); ``` |

#### Parameters

disposing
:   Type: [System..::..Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/902a7482-9c7f-fd43-af49-a46a8f26105d.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..OnNodeDoubleClick Method |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected virtual void OnNodeDoubleClick() ``` |

| Visual Basic |
| --- |
| ``` Protected Overridable Sub OnNodeDoubleClick ``` |

| Visual C++ |
| --- |
| ``` protected: virtual void OnNodeDoubleClick() ``` |

| JScript |
| --- |
| ``` protected function OnNodeDoubleClick() ``` |

| JavaScript |
| --- |
| ``` function OnNodeDoubleClick(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/99f595f7-2e38-f2d4-0360-b9e054e7eeaa.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TagContainer..::..EventInfo Property |
| TagContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public EventInfo EventInfo { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property EventInfo As EventInfo 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property EventInfo^ EventInfo { 	EventInfo^ get (); } ``` |

| JScript |
| --- |
| ``` function get EventInfo () : EventInfo  ``` |

| JavaScript |
| --- |
| ``` function get_EventInfo();  ``` |

# ![](icons/collapse_all.gif)See Also

TagContainer Class

TagContainer Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/99f88cdc-9405-3abe-ed6b-8cdab2891003.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TagContainer..::..NodeType Property |
| TagContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public TreeNodeType NodeType { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property NodeType As TreeNodeType 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property TreeNodeType NodeType { 	TreeNodeType get (); } ``` |

| JScript |
| --- |
| ``` function get NodeType () : TreeNodeType  ``` |

| JavaScript |
| --- |
| ``` function get_NodeType();  ``` |

# ![](icons/collapse_all.gif)See Also

TagContainer Class

TagContainer Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/9acf6ed1-b0f2-ecaf-9b36-610d6627029a.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TagContainer..::..Property Property |
| TagContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public Object Property { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Property As Object 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property Object^ Property { 	Object^ get (); } ``` |

| JScript |
| --- |
| ``` function get Property () : Object  ``` |

| JavaScript |
| --- |
| ``` function get_Property();  ``` |

# ![](icons/collapse_all.gif)See Also

TagContainer Class

TagContainer Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/9ca02aeb-c9bf-fd47-b3c9-ae9e9f5e7293.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..ScriptName Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public string ScriptName { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property ScriptName As String 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property String^ ScriptName { 	String^ get (); 	void set (String^ value); } ``` |

| JScript |
| --- |
| ``` function get ScriptName () : String function set ScriptName (value : String) ``` |

| JavaScript |
| --- |
| ``` function get_ScriptName(); function set_ScriptName(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/9ec50906-d965-e2b3-6d0a-0c28935d647c.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..EntryPoint Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public string EntryPoint { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property EntryPoint As String 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property String^ EntryPoint { 	String^ get (); 	void set (String^ value); } ``` |

| JScript |
| --- |
| ``` function get EntryPoint () : String function set EntryPoint (value : String) ``` |

| JavaScript |
| --- |
| ``` function get_EntryPoint(); function set_EntryPoint(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/9f89ff5b-c67d-acd1-5fa0-e6af262861ff.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..PendingSave Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public bool PendingSave { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property PendingSave As Boolean 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property bool PendingSave { 	bool get (); } ``` |

| JScript |
| --- |
| ``` function get PendingSave () : boolean  ``` |

| JavaScript |
| --- |
| ``` function get_PendingSave();  ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/a3691e69-8f5e-eb39-c908-1c197b51e776.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditForm Constructor |
| ScriptEditForm Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptEditForm() ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

| Visual C++ |
| --- |
| ``` public: ScriptEditForm() ``` |

| JScript |
| --- |
| ``` public function ScriptEditForm() ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptEditForm = function(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Class

ScriptEditForm Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/a49733ab-1583-1f8b-315f-4c88be677f40.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper..::..GetLanguageKeywords Method |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public static void GetLanguageKeywords( 	ScriptLanguages language, 	out string usingWord, 	out string usingDelimiter, 	out string classHeader, 	out string classFooter, 	out string inheritDelimiter ) ``` |

| Visual Basic |
| --- |
| ``` Public Shared Sub GetLanguageKeywords ( _ 	language As ScriptLanguages, _ 	<OutAttribute> ByRef usingWord As String, _ 	<OutAttribute> ByRef usingDelimiter As String, _ 	<OutAttribute> ByRef classHeader As String, _ 	<OutAttribute> ByRef classFooter As String, _ 	<OutAttribute> ByRef inheritDelimiter As String _ ) ``` |

| Visual C++ |
| --- |
| ``` public: static void GetLanguageKeywords( 	ScriptLanguages language,  	[OutAttribute] String^% usingWord,  	[OutAttribute] String^% usingDelimiter,  	[OutAttribute] String^% classHeader,  	[OutAttribute] String^% classFooter,  	[OutAttribute] String^% inheritDelimiter ) ``` |

| JScript |
| --- |
| ``` public static function GetLanguageKeywords( 	language : ScriptLanguages,  	usingWord : String,  	usingDelimiter : String,  	classHeader : String,  	classFooter : String,  	inheritDelimiter : String ) ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper.GetLanguageKeywords = function(language, usingWord, usingDelimiter, classHeader, classFooter, inheritDelimiter); ``` |

#### Parameters

language
:   Type: ScriptLanguages

usingWord
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)%

usingDelimiter
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)%

classHeader
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)%

classFooter
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)%

inheritDelimiter
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)%

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/a58918a7-8fbe-ee95-d7f7-09c34afd499f.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| AssemblyTypeMap..::..GetType Method |
| AssemblyTypeMap Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public static Type GetType( 	string typename ) ``` |

| Visual Basic |
| --- |
| ``` Public Shared Function GetType ( _ 	typename As String _ ) As Type ``` |

| Visual C++ |
| --- |
| ``` public: static Type^ GetType( 	String^ typename ) ``` |

| JScript |
| --- |
| ``` public static function GetType( 	typename : String ) : Type ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.AssemblyTypeMap.GetType = function(typename); ``` |

#### Parameters

typename
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.AssemblyTypeMap.GetType(System.String)"]

# ![](icons/collapse_all.gif)See Also

AssemblyTypeMap Class

AssemblyTypeMap Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/a7bf4415-c6a0-5afa-e61a-05a07a17fdf9.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| NodeDoubleClickEventHandler Delegate |
| [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public delegate void NodeDoubleClickEventHandler( 	Object sender, 	NodeDoubleClickEventArgs e ) ``` |

| Visual Basic |
| --- |
| ``` Public Delegate Sub NodeDoubleClickEventHandler ( _ 	sender As Object, _ 	e As NodeDoubleClickEventArgs _ ) ``` |

| Visual C++ |
| --- |
| ``` public delegate void NodeDoubleClickEventHandler( 	Object^ sender,  	NodeDoubleClickEventArgs^ e ) ``` |

| JScript |
| --- |
| ``` JScript does not support delegates. ``` |

| JavaScript |
| --- |
| ``` function(sender, e); ``` |

#### Parameters

sender
:   Type: [System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)

e
:   Type: Syncfusion.Scripting.Design..::..NodeDoubleClickEventArgs

# ![](icons/collapse_all.gif)See Also

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/a86c1e07-1a2c-f8ba-7867-3e52aecbe423.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptEditControl Members |
| ScriptEditControl Class [Constructors](#constructorTableToggle) [Methods](#methodTableToggle) [Fields](#fieldTableToggle) [Properties](#propertyTableToggle) [Events](#eventTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptEditControl type exposes the following members.

# ![](icons/collapse_all.gif)Constructors

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | ScriptEditControl | Default constructor |

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | AddAssemblyReference | Adds the assembly to the list of referenced assemblies. |
| ![Public method](icons/pubmethod.gif "Public method") | AddScriptableObject |  |
| ![Public method](icons/pubmethod.gif "Public method") | ClearAssemblyReferences |  |
| ![Public method](icons/pubmethod.gif "Public method") | CompileScript |  |
| ![Protected method](icons/protmethod.gif "Protected method") | Dispose | Clean up any resources being used. (Overrides [ContainerControl..::..Dispose(Boolean)](http://msdn2.microsoft.com/en-us/library/1ekay3aw).) |
| ![Protected method](icons/protmethod.gif "Protected method") | GetFileDialogFilter |  |
| ![Public method](icons/pubmethod.gif "Public method") | InitializeScriptEditor(Script) | Loads the data from the script into the editor. |
| ![Public method](icons/pubmethod.gif "Public method") | InitializeScriptEditor(ScriptingManager) |  |
| ![Public method](icons/pubmethod.gif "Public method") | New |  |
| ![Public method](icons/pubmethod.gif "Public method") | ObjectBrowser\_NodeDoubleClick |  |
| ![Protected method](icons/protmethod.gif "Protected method") | OnLanguageChange |  |
| ![Protected method](icons/protmethod.gif "Protected method") | OnScriptChange |  |
| ![Public method](icons/pubmethod.gif "Public method") | OpenFile |  |
| ![Public method](icons/pubmethod.gif "Public method") | RemoveScriptableObject |  |
| ![Public method](icons/pubmethod.gif "Public method") | RunScript |  |
| ![Public method](icons/pubmethod.gif "Public method") | SaveToFile |  |
| ![Protected method](icons/protmethod.gif "Protected method") | scriptingManager\_CompileError |  |
| ![Protected method](icons/protmethod.gif "Protected method") | SetCompileButtonsState |  |
| ![Public method](icons/pubmethod.gif "Public method") | StopScript |  |
| ![Public method](icons/pubmethod.gif "Public method") | UpdateScript | Updates the script object with the current values in the editor. |

# ![](icons/collapse_all.gif)Fields

|  | Name | Description |
| ![Protected field](icons/protfield.gif "Protected field") | assemblyDirectives |  |
| ![Protected field](icons/protfield.gif "Protected field") | bExternalCompile |  |
| ![Protected field](icons/protfield.gif "Protected field") | bExternalRun |  |
| ![Protected field](icons/protfield.gif "Protected field") | bPendingSave |  |
| ![Protected field](icons/protfield.gif "Protected field") | globalCode |  |
| ![Protected field](icons/protfield.gif "Protected field") | nameSpaceDefine |  |
| ![Protected field](icons/protfield.gif "Protected field") | scriptManager |  |
| ![Protected field](icons/protfield.gif "Protected field") | strScriptStart |  |
| ![Protected field](icons/protfield.gif "Protected field") | strScriptStop |  |

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | AssemblyReferences |  |
| ![Public property](icons/pubproperty.gif "Public property") | BaseClass |  |
| ![Public property](icons/pubproperty.gif "Public property") | EnableExternalCompile | Indicates if the ScriptingManager is being used for external compilation of the script. |
| ![Public property](icons/pubproperty.gif "Public property") | EnableExternalRun |  |
| ![Public property](icons/pubproperty.gif "Public property") | EntryPoint |  |
| ![Public property](icons/pubproperty.gif "Public property") | PendingSave |  |
| ![Public property](icons/pubproperty.gif "Public property") | RootMoniker |  |
| ![Public property](icons/pubproperty.gif "Public property") | RootNamespace |  |
| ![Public property](icons/pubproperty.gif "Public property") | Script |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptingManager |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptLanguage |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptName |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptText | Gets or sets script source code. |
| ![Public property](icons/pubproperty.gif "Public property") | SelectedItem |  |

# ![](icons/collapse_all.gif)Events

|  | Name | Description |
| ![Public event](icons/pubevent.gif "Public event") | ScriptChanged | Send when script is changed. |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/a8bf921f-2f0e-0a5d-1d46-b01fd6e62b47.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..globalCode Field |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected string globalCode ``` |

| Visual Basic |
| --- |
| ``` Protected globalCode As String ``` |

| Visual C++ |
| --- |
| ``` protected: String^ globalCode ``` |

| JScript |
| --- |
| ``` protected var globalCode : String ``` |

| JavaScript |
| --- |
| ``` var globalCode ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/a9ff0a38-7ae8-f4b3-4351-2f86f4e09a1c.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper Constructor |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptWrapper() ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

| Visual C++ |
| --- |
| ``` public: ScriptWrapper() ``` |

| JScript |
| --- |
| ``` public function ScriptWrapper() ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper = function(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/ab7ab602-5bae-0ca0-c88d-d2e40a451957.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| IScriptEditor Members |
| IScriptEditor Interface [Methods](#methodTableToggle) [Properties](#propertyTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The IScriptEditor type exposes the following members.

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | UpdateEditor | Loads the data from the script into the editor. |
| ![Public method](icons/pubmethod.gif "Public method") | UpdateScript | Updates the script object with the current values in the editor. |

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | Form | The Form object that implements the user interface. |

# ![](icons/collapse_all.gif)See Also

IScriptEditor Interface

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/b0f4d845-2a69-7d93-fc03-fe8c95837f52.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..BuildTreeNodeItem Method |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected void BuildTreeNodeItem( 	TreeNode node, 	Object value ) ``` |

| Visual Basic |
| --- |
| ``` Protected Sub BuildTreeNodeItem ( _ 	node As TreeNode, _ 	value As Object _ ) ``` |

| Visual C++ |
| --- |
| ``` protected: void BuildTreeNodeItem( 	TreeNode^ node,  	Object^ value ) ``` |

| JScript |
| --- |
| ``` protected function BuildTreeNodeItem( 	node : TreeNode,  	value : Object ) ``` |

| JavaScript |
| --- |
| ``` function BuildTreeNodeItem(node, value); ``` |

#### Parameters

node
:   Type: [System.Windows.Forms..::..TreeNode](http://msdn2.microsoft.com/en-us/library/bctbxtcb)

value
:   Type: [System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/b0f9e54e-6bfd-31a3-0944-2cc2d71597ca.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif)Â Collapse AllExpand AllÂ Â Â Â Â ![](icons/dropdown.gif)Â Code: AllÂ Code: MultipleÂ Code: C#Â Code: Visual BasicÂ Code: Visual C++Â Code: JScriptÂ Code: JavaScriptÂ Code: XAMLÂ Code: ASP.NETÂ |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| Syncfusion.Scripting.Design Namespace |
| Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Â

# ![](icons/collapse_all.gif)Classes

| Â | Class | Description |
| ![Public class](icons/pubclass.gif "Public class") | AssemblyTypeMap |  |
| ![Public class](icons/pubclass.gif "Public class") | ErrorDescriptor | Represents item for error listBox |
| ![Public class](icons/pubclass.gif "Public class") | NodeDoubleClickEventArgs |  |
| ![Public class](icons/pubclass.gif "Public class") | ScriptEditControl | Script Engine control. Support writing multi-language script. |
| ![Public class](icons/pubclass.gif "Public class") | ScriptEditForm | Summary description for ScriptEditForm. |
| ![Public class](icons/pubclass.gif "Public class") | ScriptObjectBrowser | This control display property tree for browsable object and show properties by selected branch of tree |
| ![Public class](icons/pubclass.gif "Public class") | ScriptUITypeEditor | Implements a UITypeEditor for editing Script objects. |
| ![Public class](icons/pubclass.gif "Public class") | ScriptWrapper | Summary description for ScriptWrapper. |
| ![Public class](icons/pubclass.gif "Public class") | TagContainer |  |
| ![Public class](icons/pubclass.gif "Public class") | TagEventContainer |  |

# ![](icons/collapse_all.gif)Interfaces

| Â | Interface | Description |
| ![Public interface](icons/pubinterface.gif "Public interface") | IScriptEditor | Interface to script editors. |

# ![](icons/collapse_all.gif)Delegates

| Â | Delegate | Description |
| ![Public delegate](icons/pubdelegate.gif "Public delegate") | NodeDoubleClickEventHandler |  |

# ![](icons/collapse_all.gif)Enumerations

| Â | Enumeration | Description |
| ![Public enumeration](icons/pubenumeration.gif "Public enumeration") | TreeNodeType | Indicated a node type which must be created. |

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/b1a3c052-7433-ca29-84cf-fccd107aad63.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| NodeDoubleClickEventArgs Constructor |
| NodeDoubleClickEventArgs Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public NodeDoubleClickEventArgs( 	string name, 	TagContainer tag ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	name As String, _ 	tag As TagContainer _ ) ``` |

| Visual C++ |
| --- |
| ``` public: NodeDoubleClickEventArgs( 	String^ name,  	TagContainer^ tag ) ``` |

| JScript |
| --- |
| ``` public function NodeDoubleClickEventArgs( 	name : String,  	tag : TagContainer ) ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.NodeDoubleClickEventArgs = function(name, tag); ``` |

#### Parameters

name
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

tag
:   Type: Syncfusion.Scripting.Design..::..TagContainer

# ![](icons/collapse_all.gif)See Also

NodeDoubleClickEventArgs Class

NodeDoubleClickEventArgs Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/b238c999-64e8-f3bf-7368-dc1808a17ef4.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..NodeDoubleClick Event |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Send when user is double click by tree node.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public event NodeDoubleClickEventHandler NodeDoubleClick ``` |

| Visual Basic |
| --- |
| ``` Public Event NodeDoubleClick As NodeDoubleClickEventHandler ``` |

| Visual C++ |
| --- |
| ``` public:  event NodeDoubleClickEventHandler^ NodeDoubleClick { 	void add (NodeDoubleClickEventHandler^ value); 	void remove (NodeDoubleClickEventHandler^ value); } ``` |

| JScript |
| --- |
| ``` JScript does not support events. ``` |

| JavaScript |
| --- |
| ``` function add_NodeDoubleClick(value); function remove_NodeDoubleClick(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/b2beb885-7879-b3f7-cc16-a8a3dbb0bc68.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..BuildItemsCollection Method |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected void BuildItemsCollection( 	TreeNode node, 	ICollection collection ) ``` |

| Visual Basic |
| --- |
| ``` Protected Sub BuildItemsCollection ( _ 	node As TreeNode, _ 	collection As ICollection _ ) ``` |

| Visual C++ |
| --- |
| ``` protected: void BuildItemsCollection( 	TreeNode^ node,  	ICollection^ collection ) ``` |

| JScript |
| --- |
| ``` protected function BuildItemsCollection( 	node : TreeNode,  	collection : ICollection ) ``` |

| JavaScript |
| --- |
| ``` function BuildItemsCollection(node, collection); ``` |

#### Parameters

node
:   Type: [System.Windows.Forms..::..TreeNode](http://msdn2.microsoft.com/en-us/library/bctbxtcb)

collection
:   Type: [System.Collections..::..ICollection](http://msdn2.microsoft.com/en-us/library/b1ht6113)

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/b44948a6-c16a-a7cd-6633-7b4669a58117.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditForm Class |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Summary description for ScriptEditForm.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public class ScriptEditForm : Form,  	IScriptEditor ``` |

| Visual Basic |
| --- |
| ``` Public Class ScriptEditForm _ 	Inherits Form _ 	Implements IScriptEditor ``` |

| Visual C++ |
| --- |
| ``` public ref class ScriptEditForm : public Form,  	IScriptEditor ``` |

| JScript |
| --- |
| ``` public class ScriptEditForm extends Form implements IScriptEditor ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptEditForm = function();  Type.createClass( 	'Syncfusion.Scripting.Design.ScriptEditForm', 	Form, 	Syncfusion.Scripting.Design.IScriptEditor); ``` |

# ![](icons/collapse_all.gif)Inheritance Hierarchy

[System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)
  [System..::..MarshalByRefObject](http://msdn2.microsoft.com/en-us/library/w4302s1f)
    [System.ComponentModel..::..Component](http://msdn2.microsoft.com/en-us/library/9wbadbce)
      [System.Windows.Forms..::..Control](http://msdn2.microsoft.com/en-us/library/36cd312w)
        [System.Windows.Forms..::..ScrollableControl](http://msdn2.microsoft.com/en-us/library/7xhk8yhk)
          [System.Windows.Forms..::..ContainerControl](http://msdn2.microsoft.com/en-us/library/e7d2a552)
            [System.Windows.Forms..::..Form](http://msdn2.microsoft.com/en-us/library/w4bcxb43)
              Syncfusion.Scripting.Design..::..ScriptEditForm

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/b502e9b9-47f7-c25e-76ad-c08a4977182d.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..OnScriptChange Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected virtual void OnScriptChange() ``` |

| Visual Basic |
| --- |
| ``` Protected Overridable Sub OnScriptChange ``` |

| Visual C++ |
| --- |
| ``` protected: virtual void OnScriptChange() ``` |

| JScript |
| --- |
| ``` protected function OnScriptChange() ``` |

| JavaScript |
| --- |
| ``` function OnScriptChange(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/b6bc5745-e0eb-0747-fb37-fb626536964e.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| TagContainer Members |
| TagContainer Class [Constructors](#constructorTableToggle) [Properties](#propertyTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The TagContainer type exposes the following members.

# ![](icons/collapse_all.gif)Constructors

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | TagContainer(Object, String, TreeNodeType) |  |
| ![Public method](icons/pubmethod.gif "Public method") | TagContainer(EventInfo, String, TreeNodeType) |  |

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | EventInfo |  |
| ![Public property](icons/pubproperty.gif "Public property") | Name |  |
| ![Public property](icons/pubproperty.gif "Public property") | NodeType |  |
| ![Public property](icons/pubproperty.gif "Public property") | Property |  |

# ![](icons/collapse_all.gif)See Also

TagContainer Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/b8cced88-1436-0ff4-08e6-0f1fafbb5d5b.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptEditControl Properties |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptEditControl type exposes the following members.

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | AssemblyReferences |  |
| ![Public property](icons/pubproperty.gif "Public property") | BaseClass |  |
| ![Public property](icons/pubproperty.gif "Public property") | EnableExternalCompile | Indicates if the ScriptingManager is being used for external compilation of the script. |
| ![Public property](icons/pubproperty.gif "Public property") | EnableExternalRun |  |
| ![Public property](icons/pubproperty.gif "Public property") | EntryPoint |  |
| ![Public property](icons/pubproperty.gif "Public property") | PendingSave |  |
| ![Public property](icons/pubproperty.gif "Public property") | RootMoniker |  |
| ![Public property](icons/pubproperty.gif "Public property") | RootNamespace |  |
| ![Public property](icons/pubproperty.gif "Public property") | Script |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptingManager |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptLanguage |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptName |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptText | Gets or sets script source code. |
| ![Public property](icons/pubproperty.gif "Public property") | SelectedItem |  |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/b8d580aa-f908-2871-28d9-afb09a288035.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ErrorDescriptor Properties |
| ErrorDescriptor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ErrorDescriptor type exposes the following members.

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | Column | Error colum number |
| ![Public property](icons/pubproperty.gif "Public property") | Line | Error line |
| ![Public property](icons/pubproperty.gif "Public property") | Message | Error Message |

# ![](icons/collapse_all.gif)See Also

ErrorDescriptor Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/ba807c8d-e0ba-bcec-a249-983abaaeca56.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..BrowserTreeView Property |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public TreeView BrowserTreeView { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property BrowserTreeView As TreeView 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property TreeView^ BrowserTreeView { 	TreeView^ get (); } ``` |

| JScript |
| --- |
| ``` function get BrowserTreeView () : TreeView  ``` |

| JavaScript |
| --- |
| ``` function get_BrowserTreeView();  ``` |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/bb85f6de-7686-ed13-6213-d64660fdf46d.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..BaseClass Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public Type BaseClass { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property BaseClass As Type 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property Type^ BaseClass { 	Type^ get (); } ``` |

| JScript |
| --- |
| ``` function get BaseClass () : Type  ``` |

| JavaScript |
| --- |
| ``` function get_BaseClass();  ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/bbb24734-827f-ee10-9897-f7a651ffcb10.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..assemblyDirectives Field |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected string assemblyDirectives ``` |

| Visual Basic |
| --- |
| ``` Protected assemblyDirectives As String ``` |

| Visual C++ |
| --- |
| ``` protected: String^ assemblyDirectives ``` |

| JScript |
| --- |
| ``` protected var assemblyDirectives : String ``` |

| JavaScript |
| --- |
| ``` var assemblyDirectives ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/bbc177aa-7d6d-03d2-02ae-20d567ffbda9.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..GetFileDialogFilter Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected virtual string GetFileDialogFilter( 	ScriptLanguages language ) ``` |

| Visual Basic |
| --- |
| ``` Protected Overridable Function GetFileDialogFilter ( _ 	language As ScriptLanguages _ ) As String ``` |

| Visual C++ |
| --- |
| ``` protected: virtual String^ GetFileDialogFilter( 	ScriptLanguages language ) ``` |

| JScript |
| --- |
| ``` protected function GetFileDialogFilter( 	language : ScriptLanguages ) : String ``` |

| JavaScript |
| --- |
| ``` function GetFileDialogFilter(language); ``` |

#### Parameters

language
:   Type: ScriptLanguages

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptEditControl.GetFileDialogFilter(Syncfusion.Scripting.ScriptLanguages)"]

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/bcb869c8-64cb-ecc9-8573-f41225ce0760.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper..::..GetEventHandlerScript Method |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public static string GetEventHandlerScript( 	ScriptLanguages language, 	string classname, 	string eventname, 	string argsType ) ``` |

| Visual Basic |
| --- |
| ``` Public Shared Function GetEventHandlerScript ( _ 	language As ScriptLanguages, _ 	classname As String, _ 	eventname As String, _ 	argsType As String _ ) As String ``` |

| Visual C++ |
| --- |
| ``` public: static String^ GetEventHandlerScript( 	ScriptLanguages language,  	String^ classname,  	String^ eventname,  	String^ argsType ) ``` |

| JScript |
| --- |
| ``` public static function GetEventHandlerScript( 	language : ScriptLanguages,  	classname : String,  	eventname : String,  	argsType : String ) : String ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper.GetEventHandlerScript = function(language, classname, eventname, argsType); ``` |

#### Parameters

language
:   Type: ScriptLanguages

classname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

eventname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

argsType
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptWrapper.GetEventHandlerScript(Syncfusion.Scripting.ScriptLanguages,System.String,System.String,System.String)"]

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/bd5a4efa-57f2-78dd-2514-e5630e3bf6c2.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..scriptManager Field |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected ScriptingManager scriptManager ``` |

| Visual Basic |
| --- |
| ``` Protected scriptManager As ScriptingManager ``` |

| Visual C++ |
| --- |
| ``` protected: ScriptingManager^ scriptManager ``` |

| JScript |
| --- |
| ``` protected var scriptManager : ScriptingManager ``` |

| JavaScript |
| --- |
| ``` var scriptManager ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/be1dbe38-e70b-ae94-b40a-14eaa1208313.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| NodeDoubleClickEventArgs Members |
| NodeDoubleClickEventArgs Class [Constructors](#constructorTableToggle) [Properties](#propertyTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The NodeDoubleClickEventArgs type exposes the following members.

# ![](icons/collapse_all.gif)Constructors

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | NodeDoubleClickEventArgs |  |

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | NodeName | Gets node name. |
| ![Public property](icons/pubproperty.gif "Public property") | TagContainer | Gets node tag container. |

# ![](icons/collapse_all.gif)See Also

NodeDoubleClickEventArgs Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/c0910241-9f0c-068e-3540-b4692498eafb.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser Class |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

This control display property tree for browsable object
and show properties by selected branch of tree

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public class ScriptObjectBrowser : Control ``` |

| Visual Basic |
| --- |
| ``` Public Class ScriptObjectBrowser _ 	Inherits Control ``` |

| Visual C++ |
| --- |
| ``` public ref class ScriptObjectBrowser : public Control ``` |

| JScript |
| --- |
| ``` public class ScriptObjectBrowser extends Control ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptObjectBrowser = function();  Type.createClass( 	'Syncfusion.Scripting.Design.ScriptObjectBrowser', 	Control); ``` |

# ![](icons/collapse_all.gif)Inheritance Hierarchy

[System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)
  [System..::..MarshalByRefObject](http://msdn2.microsoft.com/en-us/library/w4302s1f)
    [System.ComponentModel..::..Component](http://msdn2.microsoft.com/en-us/library/9wbadbce)
      [System.Windows.Forms..::..Control](http://msdn2.microsoft.com/en-us/library/36cd312w)
        Syncfusion.Scripting.Design..::..ScriptObjectBrowser

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/c38425fe-a843-4177-3d6a-2f039102f2c6.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..SelectedItem Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptObject SelectedItem { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property SelectedItem As ScriptObject 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property ScriptObject^ SelectedItem { 	ScriptObject^ get (); 	void set (ScriptObject^ value); } ``` |

| JScript |
| --- |
| ``` function get SelectedItem () : ScriptObject function set SelectedItem (value : ScriptObject) ``` |

| JavaScript |
| --- |
| ``` function get_SelectedItem(); function set_SelectedItem(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/c4350537-ea6e-4946-4d2d-d271ad751501.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| IScriptEditor..::..UpdateEditor Method |
| IScriptEditor Interface [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Loads the data from the script into the editor.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` void UpdateEditor( 	Script script ) ``` |

| Visual Basic |
| --- |
| ``` Sub UpdateEditor ( _ 	script As Script _ ) ``` |

| Visual C++ |
| --- |
| ``` void UpdateEditor( 	Script^ script ) ``` |

| JScript |
| --- |
| ``` function UpdateEditor( 	script : Script ) ``` |

| JavaScript |
| --- |
| ``` function UpdateEditor(script); ``` |

#### Parameters

script
:   Type: Script
    Script to load into the editor

# ![](icons/collapse_all.gif)See Also

IScriptEditor Interface

IScriptEditor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/c4d90d22-2c25-fabd-ebde-3b0943e51942.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..IsScriptBrowsable Method |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

# ![](icons/collapse_all.gif)Overload List

|  | Name | Description |
| ![Protected method](icons/protmethod.gif "Protected method") | IsScriptBrowsable(MemberInfo) |  |
| ![Protected method](icons/protmethod.gif "Protected method") | IsScriptBrowsable(MemberInfo, array<ScriptBrowsableAttribute>[]()[][]%) |  |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/cab120d2-478c-13a4-a5bf-fa8650065e10.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TagContainer Constructor (EventInfo, String, TreeNodeType) |
| TagContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public TagContainer( 	EventInfo evInfo, 	string name, 	TreeNodeType nodeType ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ( _ 	evInfo As EventInfo, _ 	name As String, _ 	nodeType As TreeNodeType _ ) ``` |

| Visual C++ |
| --- |
| ``` public: TagContainer( 	EventInfo^ evInfo,  	String^ name,  	TreeNodeType nodeType ) ``` |

| JScript |
| --- |
| ``` public function TagContainer( 	evInfo : EventInfo,  	name : String,  	nodeType : TreeNodeType ) ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.TagContainer = function(evInfo, name, nodeType); ``` |

#### Parameters

evInfo
:   Type: [System.Reflection..::..EventInfo](http://msdn2.microsoft.com/en-us/library/wzdwwzya)

name
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

nodeType
:   Type: Syncfusion.Scripting.Design..::..TreeNodeType

# ![](icons/collapse_all.gif)See Also

TagContainer Class

TagContainer Members

TagContainer Overload

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/ccc65b2a-9ee1-8459-a75c-b962186497d5.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| NodeDoubleClickEventArgs..::..NodeName Property |
| NodeDoubleClickEventArgs Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Gets node name.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public string NodeName { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property NodeName As String 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property String^ NodeName { 	String^ get (); } ``` |

| JScript |
| --- |
| ``` function get NodeName () : String  ``` |

| JavaScript |
| --- |
| ``` function get_NodeName();  ``` |

# ![](icons/collapse_all.gif)See Also

NodeDoubleClickEventArgs Class

NodeDoubleClickEventArgs Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/cde9b7b5-58a5-de75-706b-7da8c0401b70.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditForm..::..UpdateEditor Method |
| ScriptEditForm Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void UpdateEditor( 	Script script ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub UpdateEditor ( _ 	script As Script _ ) ``` |

| Visual C++ |
| --- |
| ``` public: virtual void UpdateEditor( 	Script^ script ) sealed ``` |

| JScript |
| --- |
| ``` public final function UpdateEditor( 	script : Script ) ``` |

| JavaScript |
| --- |
| ``` function UpdateEditor(script); ``` |

#### Parameters

script
:   Type: Script

#### Implements

IScriptEditor..::..UpdateEditor(Script)

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Class

ScriptEditForm Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/ced73ebf-e912-6d55-63e9-8e12a0a0fda3.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptEditForm Members |
| ScriptEditForm Class [Constructors](#constructorTableToggle) [Methods](#methodTableToggle) [Properties](#propertyTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptEditForm type exposes the following members.

# ![](icons/collapse_all.gif)Constructors

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | ScriptEditForm |  |

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Protected method](icons/protmethod.gif "Protected method") | Dispose | Clean up any resources being used. (Overrides [Form..::..Dispose(Boolean)](http://msdn2.microsoft.com/en-us/library/aw58wzka).) |
| ![Protected method](icons/protmethod.gif "Protected method") | SetManager |  |
| ![Public method](icons/pubmethod.gif "Public method") | UpdateEditor |  |
| ![Public method](icons/pubmethod.gif "Public method") | UpdateScript |  |

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | Form |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptEditControl |  |

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/cf800f3a-20e1-ef22-0663-b84c1a2b4796.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptUITypeEditor..::..EditValue Method |
| ScriptUITypeEditor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Called by the designer to edit a script.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public override Object EditValue( 	ITypeDescriptorContext context, 	IServiceProvider provider, 	Object value ) ``` |

| Visual Basic |
| --- |
| ``` Public Overrides Function EditValue ( _ 	context As ITypeDescriptorContext, _ 	provider As IServiceProvider, _ 	value As Object _ ) As Object ``` |

| Visual C++ |
| --- |
| ``` public: virtual Object^ EditValue( 	ITypeDescriptorContext^ context,  	IServiceProvider^ provider,  	Object^ value ) override ``` |

| JScript |
| --- |
| ``` public override function EditValue( 	context : ITypeDescriptorContext,  	provider : IServiceProvider,  	value : Object ) : Object ``` |

| JavaScript |
| --- |
| ``` function EditValue(context, provider, value); ``` |

#### Parameters

context
:   Type: [System.ComponentModel..::..ITypeDescriptorContext](http://msdn2.microsoft.com/en-us/library/8d4c9xy5)

provider
:   Type: [System..::..IServiceProvider](http://msdn2.microsoft.com/en-us/library/zbywf1tw)

value
:   Type: [System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)

#### Return Value

Returns the updated value of the Script

# ![](icons/collapse_all.gif)See Also

ScriptUITypeEditor Class

ScriptUITypeEditor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/d4ea2a89-f2f7-26f7-36f0-ea369843ffe1.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper..::..GetEventSubscriberScript Method |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public static string GetEventSubscriberScript( 	ScriptLanguages language, 	string nmespace, 	string scriptclass, 	string classname, 	EventInfo evinfo ) ``` |

| Visual Basic |
| --- |
| ``` Public Shared Function GetEventSubscriberScript ( _ 	language As ScriptLanguages, _ 	nmespace As String, _ 	scriptclass As String, _ 	classname As String, _ 	evinfo As EventInfo _ ) As String ``` |

| Visual C++ |
| --- |
| ``` public: static String^ GetEventSubscriberScript( 	ScriptLanguages language,  	String^ nmespace,  	String^ scriptclass,  	String^ classname,  	EventInfo^ evinfo ) ``` |

| JScript |
| --- |
| ``` public static function GetEventSubscriberScript( 	language : ScriptLanguages,  	nmespace : String,  	scriptclass : String,  	classname : String,  	evinfo : EventInfo ) : String ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper.GetEventSubscriberScript = function(language, nmespace, scriptclass, classname, evinfo); ``` |

#### Parameters

language
:   Type: ScriptLanguages

nmespace
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

scriptclass
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

classname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

evinfo
:   Type: [System.Reflection..::..EventInfo](http://msdn2.microsoft.com/en-us/library/wzdwwzya)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptWrapper.GetEventSubscriberScript(Syncfusion.Scripting.ScriptLanguages,System.String,System.String,System.String,System.Reflection.EventInfo)"]

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/d87e8f55-7f0d-1e38-ade0-4b0c7bb60ea3.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ErrorDescriptor Class |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Represents item for error listBox

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public class ErrorDescriptor ``` |

| Visual Basic |
| --- |
| ``` Public Class ErrorDescriptor ``` |

| Visual C++ |
| --- |
| ``` public ref class ErrorDescriptor ``` |

| JScript |
| --- |
| ``` public class ErrorDescriptor ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ErrorDescriptor = function();  Type.createClass( 	'Syncfusion.Scripting.Design.ErrorDescriptor'); ``` |

# ![](icons/collapse_all.gif)Inheritance Hierarchy

[System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)
  Syncfusion.Scripting.Design..::..ErrorDescriptor

# ![](icons/collapse_all.gif)See Also

ErrorDescriptor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/dc46dcfb-4e99-c047-33ce-a50adb9b3e67.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser Members |
| ScriptObjectBrowser Class [Constructors](#constructorTableToggle) [Methods](#methodTableToggle) [Properties](#propertyTableToggle) [Events](#eventTableToggle) [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptObjectBrowser type exposes the following members.

# ![](icons/collapse_all.gif)Constructors

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | ScriptObjectBrowser |  |

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Protected method](icons/protmethod.gif "Protected method") | BuildEventsList |  |
| ![Protected method](icons/protmethod.gif "Protected method") | BuildItemsCollection |  |
| ![Protected method](icons/protmethod.gif "Protected method") | BuildPropertiesList |  |
| ![Protected method](icons/protmethod.gif "Protected method") | BuildTreeNodeItem |  |
| ![Protected method](icons/protmethod.gif "Protected method") | Dispose | Clean up any resources being used. (Overrides [Control..::..Dispose(Boolean)](http://msdn2.microsoft.com/en-us/library/a4zkb31d).) |
| ![Protected method](icons/protmethod.gif "Protected method") | IsBrowsableCollection |  |
| ![Protected method](icons/protmethod.gif "Protected method") | IsScriptBrowsable(MemberInfo) |  |
| ![Protected method](icons/protmethod.gif "Protected method") | IsScriptBrowsable(MemberInfo, array<ScriptBrowsableAttribute>[]()[][]%) |  |
| ![Protected method](icons/protmethod.gif "Protected method") | OnNodeDoubleClick |  |

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | BrowserTreeView |  |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptLanguage | Sets or gets script |
| ![Public property](icons/pubproperty.gif "Public property") | ScriptSite |  |
| ![Public property](icons/pubproperty.gif "Public property") | SelectedObject | Object used for browse in TreeView. Get or set. |

# ![](icons/collapse_all.gif)Events

|  | Name | Description |
| ![Public event](icons/pubevent.gif "Public event") | NodeDoubleClick | Send when user is double click by tree node. |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/dd9f6f74-a509-182c-f430-a45ca0af43ab.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..RemoveScriptableObject Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void RemoveScriptableObject( 	ScriptObject scriptableitem ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub RemoveScriptableObject ( _ 	scriptableitem As ScriptObject _ ) ``` |

| Visual C++ |
| --- |
| ``` public: void RemoveScriptableObject( 	ScriptObject^ scriptableitem ) ``` |

| JScript |
| --- |
| ``` public function RemoveScriptableObject( 	scriptableitem : ScriptObject ) ``` |

| JavaScript |
| --- |
| ``` function RemoveScriptableObject(scriptableitem); ``` |

#### Parameters

scriptableitem
:   Type: ScriptObject

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/e0611dea-d216-4ba8-a491-cdedf718a8f5.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..IsBrowsableCollection Method |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected bool IsBrowsableCollection( 	MemberInfo type ) ``` |

| Visual Basic |
| --- |
| ``` Protected Function IsBrowsableCollection ( _ 	type As MemberInfo _ ) As Boolean ``` |

| Visual C++ |
| --- |
| ``` protected: bool IsBrowsableCollection( 	MemberInfo^ type ) ``` |

| JScript |
| --- |
| ``` protected function IsBrowsableCollection( 	type : MemberInfo ) : boolean ``` |

| JavaScript |
| --- |
| ``` function IsBrowsableCollection(type); ``` |

#### Parameters

type
:   Type: [System.Reflection..::..MemberInfo](http://msdn2.microsoft.com/en-us/library/8fek28hz)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptObjectBrowser.IsBrowsableCollection(System.Reflection.MemberInfo)"]

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/e1e9584c-280e-3f7a-f5c8-c91f8beb05e0.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..strScriptStop Field |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected string strScriptStop ``` |

| Visual Basic |
| --- |
| ``` Protected strScriptStop As String ``` |

| Visual C++ |
| --- |
| ``` protected: String^ strScriptStop ``` |

| JScript |
| --- |
| ``` protected var strScriptStop : String ``` |

| JavaScript |
| --- |
| ``` var strScriptStop ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/e1fcf68f-81da-9728-fe28-5030de20672a.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..StopScript Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void StopScript() ``` |

| Visual Basic |
| --- |
| ``` Public Sub StopScript ``` |

| Visual C++ |
| --- |
| ``` public: void StopScript() ``` |

| JScript |
| --- |
| ``` public function StopScript() ``` |

| JavaScript |
| --- |
| ``` function StopScript(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/e2f25851-6038-8f74-f9ec-5419044f09f2.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..InitializeScriptEditor Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

# ![](icons/collapse_all.gif)Overload List

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method") | InitializeScriptEditor(Script) | Loads the data from the script into the editor. |
| ![Public method](icons/pubmethod.gif "Public method") | InitializeScriptEditor(ScriptingManager) |  |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/e3286e88-7698-b9cb-6602-f2e50aa2440f.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| TagEventContainer Properties |
| TagEventContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The TagEventContainer type exposes the following members.

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | ClassName |  |

# ![](icons/collapse_all.gif)See Also

TagEventContainer Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/e407df53-de71-6570-d3bb-eb517735da61.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| AssemblyTypeMap Methods |
| AssemblyTypeMap Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The AssemblyTypeMap type exposes the following members.

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Public method](icons/pubmethod.gif "Public method")![Static member](icons/static.gif "Static member") | GetType |  |

# ![](icons/collapse_all.gif)See Also

AssemblyTypeMap Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/e479bc7d-fbbb-ed63-d09a-aff7c8aa8cba.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..OpenFile Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void OpenFile() ``` |

| Visual Basic |
| --- |
| ``` Public Sub OpenFile ``` |

| Visual C++ |
| --- |
| ``` public: void OpenFile() ``` |

| JScript |
| --- |
| ``` public function OpenFile() ``` |

| JavaScript |
| --- |
| ``` function OpenFile(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/e6dc6c02-81e5-e790-b985-9a2fb1a05188.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| TagEventContainer..::..ClassName Property |
| TagEventContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public string ClassName { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property ClassName As String 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property String^ ClassName { 	String^ get (); 	void set (String^ value); } ``` |

| JScript |
| --- |
| ``` function get ClassName () : String function set ClassName (value : String) ``` |

| JavaScript |
| --- |
| ``` function get_ClassName(); function set_ClassName(value); ``` |

# ![](icons/collapse_all.gif)See Also

TagEventContainer Class

TagEventContainer Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/e920c35c-1ca8-8501-d8d2-c8a753b30d29.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptEditForm Methods |
| ScriptEditForm Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptEditForm type exposes the following members.

# ![](icons/collapse_all.gif)Methods

|  | Name | Description |
| ![Protected method](icons/protmethod.gif "Protected method") | Dispose | Clean up any resources being used. (Overrides [Form..::..Dispose(Boolean)](http://msdn2.microsoft.com/en-us/library/aw58wzka).) |
| ![Protected method](icons/protmethod.gif "Protected method") | SetManager |  |
| ![Public method](icons/pubmethod.gif "Public method") | UpdateEditor |  |
| ![Public method](icons/pubmethod.gif "Public method") | UpdateScript |  |

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/e944d12b-9523-2381-bf78-61100f0ab0c7.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| AssemblyTypeMap Class |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public class AssemblyTypeMap ``` |

| Visual Basic |
| --- |
| ``` Public Class AssemblyTypeMap ``` |

| Visual C++ |
| --- |
| ``` public ref class AssemblyTypeMap ``` |

| JScript |
| --- |
| ``` public class AssemblyTypeMap ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.AssemblyTypeMap = function();  Type.createClass( 	'Syncfusion.Scripting.Design.AssemblyTypeMap'); ``` |

# ![](icons/collapse_all.gif)Inheritance Hierarchy

[System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)
  Syncfusion.Scripting.Design..::..AssemblyTypeMap

# ![](icons/collapse_all.gif)See Also

AssemblyTypeMap Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/eb82134b-a246-896f-0b3d-3be00600057f.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..ScriptSite Property |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public IVsaSite ScriptSite { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property ScriptSite As IVsaSite 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property IVsaSite^ ScriptSite { 	IVsaSite^ get (); 	void set (IVsaSite^ value); } ``` |

| JScript |
| --- |
| ``` function get ScriptSite () : IVsaSite function set ScriptSite (value : IVsaSite) ``` |

| JavaScript |
| --- |
| ``` function get_ScriptSite(); function set_ScriptSite(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/ed8ae927-524a-79de-0ce3-4c9c531fe94c.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptEditControl Fields |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptEditControl type exposes the following members.

# ![](icons/collapse_all.gif)Fields

|  | Name | Description |
| ![Protected field](icons/protfield.gif "Protected field") | assemblyDirectives |  |
| ![Protected field](icons/protfield.gif "Protected field") | bExternalCompile |  |
| ![Protected field](icons/protfield.gif "Protected field") | bExternalRun |  |
| ![Protected field](icons/protfield.gif "Protected field") | bPendingSave |  |
| ![Protected field](icons/protfield.gif "Protected field") | globalCode |  |
| ![Protected field](icons/protfield.gif "Protected field") | nameSpaceDefine |  |
| ![Protected field](icons/protfield.gif "Protected field") | scriptManager |  |
| ![Protected field](icons/protfield.gif "Protected field") | strScriptStart |  |
| ![Protected field](icons/protfield.gif "Protected field") | strScriptStop |  |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/ef07d0bf-1a9f-0e0f-eb99-99d8566c57bc.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptUITypeEditor Class |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Implements a UITypeEditor for editing Script objects.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public class ScriptUITypeEditor : UITypeEditor ``` |

| Visual Basic |
| --- |
| ``` Public Class ScriptUITypeEditor _ 	Inherits UITypeEditor ``` |

| Visual C++ |
| --- |
| ``` public ref class ScriptUITypeEditor : public UITypeEditor ``` |

| JScript |
| --- |
| ``` public class ScriptUITypeEditor extends UITypeEditor ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptUITypeEditor = function();  Type.createClass( 	'Syncfusion.Scripting.Design.ScriptUITypeEditor', 	UITypeEditor); ``` |

# ![](icons/collapse_all.gif)Remarks

This class is the design-time editor for the Script property of
the [!:Syncfusion.Scripting.Design.ScriptingManager]
class.

# ![](icons/collapse_all.gif)Inheritance Hierarchy

[System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)
  [System.Drawing.Design..::..UITypeEditor](http://msdn2.microsoft.com/en-us/library/92s1974b)
    Syncfusion.Scripting.Design..::..ScriptUITypeEditor

# ![](icons/collapse_all.gif)See Also

ScriptUITypeEditor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/ef57b56e-88ca-1159-7c3d-8ca9ea6871af.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser Events |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptObjectBrowser type exposes the following members.

# ![](icons/collapse_all.gif)Events

|  | Name | Description |
| ![Public event](icons/pubevent.gif "Public event") | NodeDoubleClick | Send when user is double click by tree node. |

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/ef779908-75b6-eaa3-409a-9433dacf9a6a.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| ScriptEditControl Events |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The ScriptEditControl type exposes the following members.

# ![](icons/collapse_all.gif)Events

|  | Name | Description |
| ![Public event](icons/pubevent.gif "Public event") | ScriptChanged | Send when script is changed. |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/f219a311-948b-4bce-5fcc-f83038797176.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..OnLanguageChange Method |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected virtual void OnLanguageChange( 	ScriptLanguages language ) ``` |

| Visual Basic |
| --- |
| ``` Protected Overridable Sub OnLanguageChange ( _ 	language As ScriptLanguages _ ) ``` |

| Visual C++ |
| --- |
| ``` protected: virtual void OnLanguageChange( 	ScriptLanguages language ) ``` |

| JScript |
| --- |
| ``` protected function OnLanguageChange( 	language : ScriptLanguages ) ``` |

| JavaScript |
| --- |
| ``` function OnLanguageChange(language); ``` |

#### Parameters

language
:   Type: ScriptLanguages

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/f3d24252-5deb-f610-9092-002571aab98a.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditForm..::..Dispose Method |
| ScriptEditForm Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Clean up any resources being used.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected override void Dispose( 	bool disposing ) ``` |

| Visual Basic |
| --- |
| ``` Protected Overrides Sub Dispose ( _ 	disposing As Boolean _ ) ``` |

| Visual C++ |
| --- |
| ``` protected: virtual void Dispose( 	bool disposing ) override ``` |

| JScript |
| --- |
| ``` protected override function Dispose( 	disposing : boolean ) ``` |

| JavaScript |
| --- |
| ``` function Dispose(disposing); ``` |

#### Parameters

disposing
:   Type: [System..::..Boolean](http://msdn2.microsoft.com/en-us/library/a28wyd50)

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Class

ScriptEditForm Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/f42dfad4-f2c8-cdd1-091f-0aea1aaf2ea5.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditForm..::..Form Property |
| ScriptEditForm Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public Form Form { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Form As Form 	Get ``` |

| Visual C++ |
| --- |
| ``` public: virtual property Form^ Form { 	Form^ get () sealed; } ``` |

| JScript |
| --- |
| ``` final function get Form () : Form  ``` |

| JavaScript |
| --- |
| ``` function get_Form();  ``` |

#### Implements

IScriptEditor..::..Form

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Class

ScriptEditForm Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/f52d9327-b14b-94ce-1074-b2eed85ddc31.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..BuildPropertiesList Method |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected void BuildPropertiesList( 	TreeNode node, 	PropertyInfo[] properties, 	Object value ) ``` |

| Visual Basic |
| --- |
| ``` Protected Sub BuildPropertiesList ( _ 	node As TreeNode, _ 	properties As PropertyInfo(), _ 	value As Object _ ) ``` |

| Visual C++ |
| --- |
| ``` protected: void BuildPropertiesList( 	TreeNode^ node,  	array<PropertyInfo^>^ properties,  	Object^ value ) ``` |

| JScript |
| --- |
| ``` protected function BuildPropertiesList( 	node : TreeNode,  	properties : PropertyInfo[],  	value : Object ) ``` |

| JavaScript |
| --- |
| ``` function BuildPropertiesList(node, properties, value); ``` |

#### Parameters

node
:   Type: [System.Windows.Forms..::..TreeNode](http://msdn2.microsoft.com/en-us/library/bctbxtcb)

properties
:   Type: array<[System.Reflection..::..PropertyInfo](http://msdn2.microsoft.com/en-us/library/8z852kf5)>[]()[][]

value
:   Type: [System..::..Object](http://msdn2.microsoft.com/en-us/library/e5kfa45b)

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/f5b7db75-cb75-a545-cc3e-51660197883d.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| IScriptEditor Interface |
| Members [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Interface to script editors.

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public interface IScriptEditor ``` |

| Visual Basic |
| --- |
| ``` Public Interface IScriptEditor ``` |

| Visual C++ |
| --- |
| ``` public interface class IScriptEditor ``` |

| JScript |
| --- |
| ``` public interface IScriptEditor ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.IScriptEditor = function(); Syncfusion.Scripting.Design.IScriptEditor.createInterface('Syncfusion.Scripting.Design.IScriptEditor'); ``` |

# ![](icons/collapse_all.gif)Remarks

This interface is implemented by classes that edit script objects.

# ![](icons/collapse_all.gif)See Also

IScriptEditor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/f683cfcc-4a1b-b745-92b3-f13614a74378.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl Constructor |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Default constructor

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public ScriptEditControl() ``` |

| Visual Basic |
| --- |
| ``` Public Sub New ``` |

| Visual C++ |
| --- |
| ``` public: ScriptEditControl() ``` |

| JScript |
| --- |
| ``` public function ScriptEditControl() ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptEditControl = function(); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/f8805c74-e3f7-b6cf-e246-cc2845a04e96.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET     ![](icons/dropdown.gif) Members: Show All Members: Filtered Members: Filtered Members: Filtered |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

Include Protected Members
Include Inherited Members

|  |
| --- |
| Essential Scripting |
| TagContainer Properties |
| TagContainer Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

The TagContainer type exposes the following members.

# ![](icons/collapse_all.gif)Properties

|  | Name | Description |
| ![Public property](icons/pubproperty.gif "Public property") | EventInfo |  |
| ![Public property](icons/pubproperty.gif "Public property") | Name |  |
| ![Public property](icons/pubproperty.gif "Public property") | NodeType |  |
| ![Public property](icons/pubproperty.gif "Public property") | Property |  |

# ![](icons/collapse_all.gif)See Also

TagContainer Class

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/f8cb501b-723a-b934-0ea5-217f832ed43d.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptWrapper..::..AddEventSubscriptionToScript Method |
| ScriptWrapper Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public static string AddEventSubscriptionToScript( 	ScriptLanguages language, 	string scriptcode, 	string methodname, 	string eventscript ) ``` |

| Visual Basic |
| --- |
| ``` Public Shared Function AddEventSubscriptionToScript ( _ 	language As ScriptLanguages, _ 	scriptcode As String, _ 	methodname As String, _ 	eventscript As String _ ) As String ``` |

| Visual C++ |
| --- |
| ``` public: static String^ AddEventSubscriptionToScript( 	ScriptLanguages language,  	String^ scriptcode,  	String^ methodname,  	String^ eventscript ) ``` |

| JScript |
| --- |
| ``` public static function AddEventSubscriptionToScript( 	language : ScriptLanguages,  	scriptcode : String,  	methodname : String,  	eventscript : String ) : String ``` |

| JavaScript |
| --- |
| ``` Syncfusion.Scripting.Design.ScriptWrapper.AddEventSubscriptionToScript = function(language, scriptcode, methodname, eventscript); ``` |

#### Parameters

language
:   Type: ScriptLanguages

scriptcode
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

methodname
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

eventscript
:   Type: [System..::..String](http://msdn2.microsoft.com/en-us/library/s1wwdcbf)

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptWrapper.AddEventSubscriptionToScript(Syncfusion.Scripting.ScriptLanguages,System.String,System.String,System.String)"]

# ![](icons/collapse_all.gif)See Also

ScriptWrapper Class

ScriptWrapper Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/fad6f20b-9569-900d-b4a5-6e8ee8c7aead.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..RootNamespace Property |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public string RootNamespace { get; set; } ``` |

| Visual Basic |
| --- |
| ``` Public Property RootNamespace As String 	Get 	Set ``` |

| Visual C++ |
| --- |
| ``` public: property String^ RootNamespace { 	String^ get (); 	void set (String^ value); } ``` |

| JScript |
| --- |
| ``` function get RootNamespace () : String function set RootNamespace (value : String) ``` |

| JavaScript |
| --- |
| ``` function get_RootNamespace(); function set_RootNamespace(value); ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/fadb7a19-462c-2bbb-3169-42c59db8d714.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditForm..::..UpdateScript Method |
| ScriptEditForm Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public void UpdateScript( 	Script script ) ``` |

| Visual Basic |
| --- |
| ``` Public Sub UpdateScript ( _ 	script As Script _ ) ``` |

| Visual C++ |
| --- |
| ``` public: virtual void UpdateScript( 	Script^ script ) sealed ``` |

| JScript |
| --- |
| ``` public final function UpdateScript( 	script : Script ) ``` |

| JavaScript |
| --- |
| ``` function UpdateScript(script); ``` |

#### Parameters

script
:   Type: Script

#### Implements

IScriptEditor..::..UpdateScript(Script)

# ![](icons/collapse_all.gif)See Also

ScriptEditForm Class

ScriptEditForm Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/fca399d5-a203-0f8b-65d9-c2613398edcf.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptObjectBrowser..::..IsScriptBrowsable Method (MemberInfo, array<ScriptBrowsableAttribute>[]()[][]%) |
| ScriptObjectBrowser Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected bool IsScriptBrowsable( 	MemberInfo type, 	out ScriptBrowsableAttribute[] attr ) ``` |

| Visual Basic |
| --- |
| ``` Protected Function IsScriptBrowsable ( _ 	type As MemberInfo, _ 	<OutAttribute> ByRef attr As ScriptBrowsableAttribute() _ ) As Boolean ``` |

| Visual C++ |
| --- |
| ``` protected: bool IsScriptBrowsable( 	MemberInfo^ type,  	[OutAttribute] array<ScriptBrowsableAttribute^>^% attr ) ``` |

| JScript |
| --- |
| ``` protected function IsScriptBrowsable( 	type : MemberInfo,  	attr : ScriptBrowsableAttribute[] ) : boolean ``` |

| JavaScript |
| --- |
| ``` function IsScriptBrowsable(type, attr); ``` |

#### Parameters

type
:   Type: [System.Reflection..::..MemberInfo](http://msdn2.microsoft.com/en-us/library/8fek28hz)

attr
:   Type: array<ScriptBrowsableAttribute>[]()[][]%

#### Return Value

[Missing <returns> documentation for "M:Syncfusion.Scripting.Design.ScriptObjectBrowser.IsScriptBrowsable(System.Reflection.MemberInfo,Syncfusion.Scripting.ScriptBrowsableAttribute[]@)"]

# ![](icons/collapse_all.gif)See Also

ScriptObjectBrowser Class

ScriptObjectBrowser Members

IsScriptBrowsable Overload

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/fe9f73c4-c14b-9017-0f7b-ea3572e1380e.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ScriptEditControl..::..nameSpaceDefine Field |
| ScriptEditControl Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` protected string nameSpaceDefine ``` |

| Visual Basic |
| --- |
| ``` Protected nameSpaceDefine As String ``` |

| Visual C++ |
| --- |
| ``` protected: String^ nameSpaceDefine ``` |

| JScript |
| --- |
| ``` protected var nameSpaceDefine : String ``` |

| JavaScript |
| --- |
| ``` var nameSpaceDefine ``` |

# ![](icons/collapse_all.gif)See Also

ScriptEditControl Class

ScriptEditControl Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: html/ff6feb5a-8274-f2e8-3b3c-aca6be64c569.htm

![Collapse image](icons/collapse_all.gif "Collapse image")![Expand Image](icons/expand_all.gif "Expand Image")![](icons/collapse_all.gif)![](icons/expand_all.gif)![](icons/dropdown.gif)![](icons/dropdownHover.gif)![Copy image](icons/copycode.gif "Copy image")![CopyHover image](icons/copycodeHighlight.gif "CopyHover image")

|  |
| --- |
| ![](icons/collapse_all.gif) Collapse AllExpand All     ![](icons/dropdown.gif) Code: All Code: Multiple Code: C# Code: Visual Basic Code: Visual C++ Code: JScript Code: JavaScript Code: XAML Code: ASP.NET |

C#
Visual Basic
Visual C++
JScript
JavaScript
XAML
ASP.NET

|  |
| --- |
| Essential Scripting |
| ErrorDescriptor..::..Line Property |
| ErrorDescriptor Class [See Also](#seeAlsoToggle) Send Feedback |

|  |
| --- |
| ![](icons/gradient.gif) |

Error line

**Namespace:** Syncfusion.Scripting.Design
**Assembly:** Syncfusion.Scripting.Windows (in Syncfusion.Scripting.Windows.dll) Version: 11.104.0.21

# ![](icons/collapse_all.gif)Syntax

| C# |
| --- |
| ``` public int Line { get; } ``` |

| Visual Basic |
| --- |
| ``` Public ReadOnly Property Line As Integer 	Get ``` |

| Visual C++ |
| --- |
| ``` public: property int Line { 	int get (); } ``` |

| JScript |
| --- |
| ``` function get Line () : int  ``` |

| JavaScript |
| --- |
| ``` function get_Line();  ``` |

# ![](icons/collapse_all.gif)See Also

ErrorDescriptor Class

ErrorDescriptor Members

Syncfusion.Scripting.Design Namespace

![Footer image](icons/footer.gif "Footer image")

Send comments on this topic to
Email your feedbacks to[Syncfusion Inc 2001 - 2013](http://www.syncfusion.com)

## File: icons/header_prev_next.jpg

## File: icons/header_sql_tutorial_blank.jpg

## File: scripts/CheckboxMenu.js

function CheckboxMenu(id, data, persistkeys, globals)
{
    this.id = id;
    this.menuCheckboxIds = new Array();
    this.data = data;
    this.count = 0;

    var element = document.getElementById(id);
	var checkboxNodes = element.getElementsByTagName("input");

	for(var checkboxCount=0; checkboxCount < checkboxNodes.length; checkboxCount++)
	{
	    var checkboxId = checkboxNodes[checkboxCount].getAttribute('id');
	    var checkboxData = checkboxNodes[checkboxCount].getAttribute('data');
	    var dataSplits = checkboxData.split(',');
	    var defaultValue = checkboxNodes[checkboxCount].getAttribute('value');
	    if (checkboxData != null && checkboxData.indexOf("persist") != -1)
	        persistkeys.push(checkboxId);

	    this.menuCheckboxIds[dataSplits[0]] = checkboxId;

	    // try to get the value for this checkbox id from globals
	    var persistedValue = (globals == null) ? null : globals.VariableExists(checkboxId) ? globals.VariableValue(checkboxId) : null;
	    var currentValue = (persistedValue != null) ? persistedValue : (defaultValue == null) ? "on" : defaultValue;

	    // set the checkbox's check state
	    this.SetCheckState(checkboxId, currentValue);

	    this.count++;
	}
}

CheckboxMenu.prototype.SetCheckState=function(id, value)
{
	var checkbox = document.getElementById(id);
	if(checkbox != null)
	{
	    checkbox.checked = (value == "on") ? true : false;
	}

    // set the value for the checkbox id in the data array
    this.data[id] = value;
}

CheckboxMenu.prototype.GetCheckState=function(id)
{
	var checkbox = document.getElementById(id);
	if(checkbox != null)
	    return checkbox.checked;
	return false;
}

CheckboxMenu.prototype.ToggleCheckState=function(id)
{
    // at least one checkbox must always be checked
    var checkedCount = this.GetCheckedCount();

	if(this.data[id] == "on" && checkedCount > 1)
		this.SetCheckState(id, "off");
	else
		this.SetCheckState(id, "on");
}

// returns the checkbox id associated with a key
CheckboxMenu.prototype.GetCheckboxId=function(key)
{
    return this.menuCheckboxIds[key];
}

// returns the array of checkbox ids
CheckboxMenu.prototype.GetCheckboxIds=function()
{
    return this.menuCheckboxIds;
}

// returns the @data attribute of the checkbox element
CheckboxMenu.prototype.GetCheckboxData=function(checkboxId)
{
    var checkbox = document.getElementById(checkboxId);
    if (checkbox == null) return "";
    return checkbox.getAttribute('data');
}

CheckboxMenu.prototype.GetDropdownLabelId=function()
{
    var checkboxCount = this.count;
    var checkedCount = this.GetCheckedCount();
    var idPrefix = this.id;

    // if all boxes checked, use showall label
    if (checkedCount == checkboxCount)
        return idPrefix.concat("AllLabel");

    // if only one is checked, use label appropriate for that one checkbox
    if (checkedCount == 1)
    {
        for(var key in this.menuCheckboxIds)
        {
            if (this.data[this.menuCheckboxIds[key]] == "on")
            {
                return idPrefix.concat(key,'Label');
            }
        }
    }

    // if multiple or zero checked, use multiple label
    return idPrefix.concat("MultipleLabel");
}

CheckboxMenu.prototype.GetCheckedCount=function()
{
    var count = 0;
    for(var key in this.menuCheckboxIds)
    {
        if (this.data[this.menuCheckboxIds[key]] == "on")
            count++;
    }
    return (count);
}

// returns an array containing the ids of the checkboxes that are checked
CheckboxMenu.prototype.GetCheckedIds=function()
{
    var idArray = new Array();
    for(var key in this.menuCheckboxIds)
    {
        if (this.data[this.menuCheckboxIds[key]] == "on")
            idArray.push(this.menuCheckboxIds[key]);
    }
    return idArray;
}

CheckboxMenu.prototype.GetGroupCheckedCount=function(checkboxGroup)
{
    var count = 0;
    for(var i = 0; i < checkboxGroup.length; i++)
    {
        if (this.data[checkboxGroup[i]] == "on")
            count++;
    }
    return (count);
}

CheckboxMenu.prototype.ToggleGroupCheckState=function(id, checkboxGroup)
{
    // at least one checkbox must always be checked
    var checkedCount = this.GetGroupCheckedCount(checkboxGroup);

    // if the group has multiple checkboxes, one must always be checked; so toggle to "off" only if more than one currently checked
    // if the group has only one checkbox, it's okay to toggle it on/off
	if(this.data[id] == "on" && (checkedCount > 1 || checkboxGroup.length == 1))
		this.SetCheckState(id, "off");
	else
		this.SetCheckState(id, "on");
}

## File: scripts/CommonUtilities.js

//function codeBlockHandler(id, data, value)
function codeBlockHandler()
{
    // handle groups of snippets to make sure at least one from the group is always shown
    HandleSnippetGroups();

    // handle any remaining snippets that aren't in groups
	var spanElements = document.getElementsByTagName("span");
	for(var i = 0; i < spanElements.length; ++i)
	{
	    var devlang = spanElements[i].getAttribute("codeLanguage");
	    if (devlang == null) continue;

	    if (HasSnippetGroupAncestor(spanElements[i])) continue;

        var checkboxId = GetDevlangCheckboxId(devlang);
	    if (checkboxId != null && checkboxId != "")
	    {
            if (docSettings[checkboxId] == "on")
		        spanElements[i].style.display = "";
            else
		        spanElements[i].style.display = "none";
	    }
	}
}

function HasSnippetGroupAncestor(object)
{
    var parent = object.parentElement;
    if (parent == null) return false;

    var className = parent.className;
    if (className != null && className == "snippetgroup")
        return true

    return HasSnippetGroupAncestor(parent);
}

function HandleSnippetGroups()
{
    var divs = document.getElementsByTagName("DIV");
    var divclass;
    for (var i = 0; i < divs.length; i++)
    {
        divclass = divs[i].className;
        if (divclass == null || divclass != "snippetgroup") continue;

        // if all snippets in this group would be hidden by filtering display them all anyhow
        var unfilteredCount = GetUnfilteredSnippetCount(divs[i]);

	    var spanElements = divs[i].getElementsByTagName("span");
	    for(var j = 0; j < spanElements.length; ++j)
	    {
	        var devlang = spanElements[j].getAttribute("codeLanguage");
	        if (devlang == null) continue;

            var checkboxId = GetDevlangCheckboxId(devlang);

	        // for filtered devlangs, determine whether they should be shown/hidden
	        if (checkboxId != null && checkboxId != "")
	        {
	            if (unfilteredCount == 0 || docSettings[checkboxId] == "on")
		            spanElements[j].style.display = "";
                else
		            spanElements[j].style.display = "none";
	        }
	    }
    }
}

function GetUnfilteredSnippetCount(group)
{
    var count = 0;
    var spanElements = group.getElementsByTagName("span");
    for(var i = 0; i < spanElements.length; ++i)
    {
        var devlang = spanElements[i].getAttribute("codeLanguage");
        var checkboxId = GetDevlangCheckboxId(devlang);
        if (checkboxId != null && checkboxId != "")
        {
            if (docSettings[checkboxId] == "on")
	            count++;
        }
    }
    return count;
}

function GetDevlangCheckboxId(devlang)
{
    switch (devlang)
    {
        case "VisualBasic":
        case "VisualBasicDeclaration":
        case "VisualBasicUsage":
            return devlangsMenu.GetCheckboxId("VisualBasic");
        case "CSharp":
            return devlangsMenu.GetCheckboxId("CSharp");
        case "ManagedCPlusPlus":
            return devlangsMenu.GetCheckboxId("ManagedCPlusPlus");
        case "JScript":
            return devlangsMenu.GetCheckboxId("JScript");
        case "JSharp":
            return devlangsMenu.GetCheckboxId("JSharp");
        case "JavaScript":
            return devlangsMenu.GetCheckboxId("JavaScript");
        case "XAML":
            return devlangsMenu.GetCheckboxId("XAML");
        case "FSharp":
            return devlangsMenu.GetCheckboxId("FSharp");
        default:
            return "";
    }
}

// update stylesheet display settings for spans to show according to user's devlang preference
function styleSheetHandler(oneDevlang)
{
    var devlang = (oneDevlang != "") ? oneDevlang : GetDevlangPreference();

    var sd = getStyleDictionary();

    // Ignore if not found (Help Viewer 2)
    if(typeof(sd['span.cs']) == "undefined")
        return;

    if (devlang == 'cs') {
        sd['span.cs'].display = 'inline';
        sd['span.vb'].display = 'none';
        sd['span.cpp'].display = 'none';
        sd['span.nu'].display = 'none';
        sd['span.fs'].display = 'none';
    } else if (devlang == 'vb') {
        sd['span.cs'].display = 'none';
        sd['span.vb'].display = 'inline';
        sd['span.cpp'].display = 'none';
        sd['span.nu'].display = 'none';
        sd['span.fs'].display = 'none';
    } else if (devlang == 'cpp') {
        sd['span.cs'].display = 'none';
        sd['span.vb'].display = 'none';
        sd['span.cpp'].display = 'inline';
        sd['span.nu'].display = 'none';
        sd['span.fs'].display = 'none';
    } else if (devlang == 'nu') {
        sd['span.cs'].display = 'none';
        sd['span.vb'].display = 'none';
        sd['span.cpp'].display = 'none';
        sd['span.nu'].display = 'inline';
        sd['span.fs'].display = 'none';
    } else if (devlang == 'fs') {
        sd['span.cs'].display = 'none';
        sd['span.vb'].display = 'none';
        sd['span.cpp'].display = 'none';
        sd['span.nu'].display = 'none';
        sd['span.fs'].display = 'inline';
    }
}

function getStyleDictionary() {
    var styleDictionary = new Array();

    try
    {
        // iterate through stylesheets
        var sheets = document.styleSheets;

        for(var i=0; i<sheets.length;i++) {
            var sheet = sheets[i];

            // Ignore sheets at ms-help Urls
            if(sheet.href.substr(0,8) == 'ms-help:')
                continue;

            // get sheet rules
            var rules = sheet.cssRules;

            if(rules == null)
                rules = sheet.rules;

            // iterate through rules
            for(j=0; j<rules.length; j++) {
                var rule = rules[j];

                // Ignore ones that aren't defined
                if(rule.selectorText == null)
                    continue;

                // add rule to dictionary
                styleDictionary[rule.selectorText.toLowerCase()] = rule.style;
            }
        }
    }
    catch(e)
    {
        // Ignore errors (Help Viewer 2).  sheet.rules is inaccessible
        // due to security restrictions.
    }

    return(styleDictionary);
}

function GetDevlangPreference()
{
    var devlangCheckboxIds = devlangsMenu.GetCheckboxIds();
    var checkedCount = 0;
    var devlang;
    for (var key in devlangCheckboxIds)
    {
        if (docSettings[devlangCheckboxIds[key]] == "on")
        {
            checkedCount++;
            checkboxData = devlangsMenu.GetCheckboxData(devlangCheckboxIds[key]);
            var dataSplits = checkboxData.split(',');
            if (dataSplits.length > 1)
                devlang = dataSplits[1];
        }
    }
    return (checkedCount == 1 ? devlang : "nu");
}

function memberlistHandler()
{
   // get all the <tr> nodes in the document
	var allRows = document.getElementsByTagName("tr");
	var i;

	for(i = 0; i < allRows.length; ++i)
	{
	    var memberdata = allRows[i].getAttribute("data");
	    if (memberdata != null)
        {
	        if ((ShowBasedOnInheritance(memberdata) == false) ||
	            (ShowBasedOnVisibility(memberdata) == false) ||
	            (ShowBasedOnFramework(memberdata) == false) )
			        allRows[i].style.display = "none";
		    else
			    allRows[i].style.display = "";
        }
	}

	ShowHideFrameworkImages();
	ShowHideFrameworkSpans();
}

function ShowHideFrameworkImages()
{
    // show/hide img nodes for filtered framework icons
    // get all the <img> nodes in the document
	var allImgs = document.getElementsByTagName("img");

	for(var i = 0; i < allImgs.length; i++)
	{
	    var imgdata = allImgs[i].getAttribute("data");
	    if (imgdata != null)
        {
	        var checkboxId = imgdata + "Checkbox";
            if (docSettings[checkboxId] != "on")
	        {
		        allImgs[i].style.display = "none";
	        }
		    else
			    allImgs[i].style.display = "";
        }
	}
}

function ShowHideFrameworkSpans()
{
    // show/hide img nodes for filtered framework icons
    // get all the <img> nodes in the document
	var allImgs = document.getElementsByTagName("span");

	for(var i = 0; i < allImgs.length; i++)
	{
	    var imgdata = allImgs[i].getAttribute("data");
	    if (imgdata != null)
        {
	        var checkboxId = imgdata + "Checkbox";
            if (docSettings[checkboxId] != "on")
	        {
		        allImgs[i].style.display = "none";
	        }
		    else
			    allImgs[i].style.display = "";
        }
	}
}

function ShowBasedOnVisibility(memberdata)
{
    var isPublic = (memberdata.indexOf("public") != -1);
    var isProtected = (memberdata.indexOf("protected") != -1);
    var isPrivate = (memberdata.indexOf("private") != -1);
    var isExplicitII = (memberdata.indexOf("explicit") != -1);

    // if the public checkbox doesn't exist, default to showPublic == true
    var publicCheck = docSettings["PublicCheckbox"];
    var showPublic = (publicCheck == null) ? true : (publicCheck == "on");

    // if the protected checkbox doesn't exist, default to showProtected == true
    var protectedCheck = docSettings["ProtectedCheckbox"];
    var showProtected = (protectedCheck == null) ? true : (protectedCheck == "on");

    if ( (showProtected && isProtected) || (showPublic && isPublic) || isExplicitII || isPrivate)
        return true;

    return false;
}

function ShowBasedOnInheritance(memberdata)
{
    var isInherited = (memberdata.indexOf("inherited") != -1);
    var isDeclared = (memberdata.indexOf("declared") != -1);

    // if the inherited checkbox doesn't exist, default to showInherited == true
    var inheritedCheck = docSettings["InheritedCheckbox"];
    var showInherited = (inheritedCheck == null) ? true : (inheritedCheck == "on");

    // if the declared checkbox doesn't exist, default to showDeclared == true
    var declaredCheck = docSettings["DeclaredCheckbox"];
    var showDeclared = (declaredCheck == null) ? true : (declaredCheck == "on");

    if ( (showInherited && isInherited) || (showDeclared && isDeclared) )
        return true;

    return false;
}

function ShowBasedOnFramework(memberdata) {

    var splitData = memberdata.split(";");
    var foundNotNetfw = false;
    var frameworkFilter = document.getElementById('memberFrameworksMenu') != null;

    for (var i = 0; i < splitData.length; i++) {

        if (splitData[i] == "notNetfw") {
            foundNotNetfw = true;
            continue;
        }
        if (docSettings[splitData[i] + "Checkbox"] == "on")
            return true;
    }
    if (!foundNotNetfw && docSettings["netfwCheckbox"] == "on")
        return true;
    if (foundNotNetfw && docSettings["netfwCheckbox"] == null && !frameworkFilter)
        return true;

    return false;
}

function SetDropdownMenuLabel(menu, dropdown)
{
    var dropdownLabelId = menu.GetDropdownLabelId();
	dropdown.SetActivatorLabel(dropdownLabelId);
	for (var i = 0; i < dropdowns.length; i++)
	{
	    dropdowns[i].reposition();
	}
}

## File: scripts/Dropdown.js

// Dropdown menu control

function Dropdown(activatorId, dropdownId, containerId) {

	// store activator and dropdown elements
	this.activator = document.getElementById(activatorId);
	this.dropdown = document.getElementById(dropdownId);
	this.container = document.getElementById(containerId);
	this.activatorImage = document.getElementById(activatorId + "Image");

	// wire up show/hide events
	registerEventHandler(this.activator,'mouseover', getInstanceDelegate(this, "show"));
	registerEventHandler(this.activator,'mouseout', getInstanceDelegate(this, "requestHide"));
	registerEventHandler(this.dropdown,'mouseover', getInstanceDelegate(this, "show"));
	registerEventHandler(this.dropdown,'mouseout', getInstanceDelegate(this, "requestHide"));

	// fix visibility and position
	this.dropdown.style.visibility = 'hidden';
	this.dropdown.style.position = 'absolute';
	this.reposition(null);

	// wire up repositioning event
	registerEventHandler(window, 'resize', getInstanceDelegate(this, "reposition"));

}

Dropdown.prototype.show = function(e) {
	clearTimeout(this.timer);
	this.dropdown.style.visibility = 'visible';
	if (this.activatorImage != null)
	    this.activatorImage.src = dropDownHoverImage.src;
	if (this.activator != null)
	    this.activator.className = "filterOnHover";
}

Dropdown.prototype.hide = function(e) {
	this.dropdown.style.visibility = 'hidden';
	if (this.activatorImage != null)
	    this.activatorImage.src = dropDownImage.src;
	if (this.activator != null)
	    this.activator.className = "filter";
}

Dropdown.prototype.requestHide = function(e) {
	this.timer = setTimeout( getInstanceDelegate(this, "hide"), 250);
}

Dropdown.prototype.reposition = function(e) {

	// get position of activator
	var offsetLeft = 0;
	var offsetTop = 0;
	var offsetElement = this.activator;

	while (offsetElement && offsetElement != this.container) {
		offsetLeft += offsetElement.offsetLeft;
		offsetTop += offsetElement.offsetTop;
		offsetElement = offsetElement.offsetParent;
	}

	// set position of dropdown relative to it
	this.dropdown.style.left = offsetLeft;
	this.dropdown.style.top = offsetTop + this.activator.offsetHeight;
}

Dropdown.prototype.SetActivatorLabel = function(labelId)
{
    // get the children of the activator node, which includes the label nodes
    var labelNodes = this.activator.childNodes;

    for(var labelCount=0; labelCount < labelNodes.length; labelCount++)
    {
	    if(labelNodes[labelCount].tagName == 'LABEL')
	    {
	        var labelNodeId = labelNodes[labelCount].getAttribute('id');
		    if (labelNodeId == labelId)
		    {
	            labelNodes[labelCount].style.display = "inline";
		    }
		    else
		    {
	            labelNodes[labelCount].style.display = "none";
		    }
	    }
    }
}

## File: scripts/EventUtilities.js

	// attach a handler to a particular event on an element
	// in a browser-independent way
	function registerEventHandler (element, event, handler) {
		if (element.attachEvent) {
			// MS registration model
			element.attachEvent('on' + event, handler);
		} else if (element.addEventListener) {
			// NN (W4C) regisration model
			element.addEventListener(event, handler, false);
		} else {
			// old regisration model as fall-back
			element[event] = handler;
		}
	}

	// get a delegate that refers to an instance method
	function getInstanceDelegate (obj, methodName) {
		return( function(e) {
			e = e || window.event;
			return obj[methodName](e);
		} );
	}

## File: scripts/script_feedBack.js

//Default FeedBack Values
var ratings = 3;
var title = document.title;
var URL = location.href.replace(location.hash,"");
var version = 2007;

/*************************************************************************
 * Methods ********************************************************
 *************************************************************************/

function DeliveryType()
{
 	if (URL.indexOf("ms-help://")!=-1) {return("h");}
	else if (URL.indexOf(".chm::/")!=-1) {return("c");}
	else if (URL.indexOf("http://")!=-1) {return("w");}
	else if (URL.indexOf("file:")!=-1) {return("f");}
	else return("0");
}

function DeliverableValue(deliverable)
{
 	if (URL.indexOf("ms-help://")!=-1)
	{
		delvalue  = location.href.slice(0,location.href.lastIndexOf("/html/"));
		delvalue  = delvalue.slice(delvalue.lastIndexOf("/")+1);
		return delvalue;
	}
	else return(deliverable);
}

function URLValue()
{
	if (URL.indexOf(".chm::")!=-1)
	{
		a = URL;
		while (a.indexOf("\\") < a.indexOf(".chm::") || a.indexOf("//") > a.indexOf(".chm::"))
		{
			if (a.indexOf("\\")==-1)
			{
				break;
			}
			a = a.substring(a.indexOf("\\")+1,a.length);
		}
		return("ms-its:"+a)
	}
	else if (URL.indexOf("file:///")!=-1)
	{
		a = URL;

		b = a.substring(a.lastIndexOf("html")+5,a.length);
		return("file:///"+b);
	}
	else return(URL);
}

function GetLanguage()
{
	var langauge;
  	if(navigator.userAgent.indexOf("Firefox")!=-1)
  	{
  		var index = navigator.userAgent.indexOf('(');
   		var string = navigator.userAgent.substring(navigator.userAgent.indexOf('('), navigator.userAgent.length);
   		var splitString = string.split(';');
	   	language = splitString[3].substring(1, splitString[3].length);
  	}
  	else language = navigator.systemLanguage;
	return(language);
}

//---Gets topic rating.---
function GetRating()
{

	sRating = "0";
	for(var x = 0;x < 5;x++)
  	{
		if(document.formRating) {
		if(document.formRating.fbRating[x].checked) {sRating = x + 1;}}
		else return sRating;
  	}
	return sRating;
}

function SubmitFeedback(alias, product, deliverable, productVersion, documentationVersion, defaultBody, defaultSubject)
{
	var subject = defaultSubject
  		+ " ("
		+ "/1:"
  		+ product
  		+ "/2:"
  		+ productVersion
  		+ "/3:"
  		+ documentationVersion
  		+ "/4:"
  		+ DeliverableValue(deliverable)
  		+ "/5:"
  		+ URLValue()
  		+ "/6:"
  		+ GetRating()
  		+ "/7:"
  		+ DeliveryType()
  		+ "/8:"
  		+ GetLanguage()
		+ "/9:"
  		+ version
		+ ")";

	location.href = "mailto:" + alias + "?subject=" + subject
	+ "&body=" + defaultBody;
}

function AltFeedback(src, title) {
	src.title=title;
	return;
	}

## File: scripts/script_manifold.js

registerEventHandler(window, 'load', getInstanceDelegate(this, "LoadPage"));
registerEventHandler(window, 'unload', getInstanceDelegate(this, "Window_Unload"));
registerEventHandler(window, 'beforeprint', getInstanceDelegate(this, "set_to_print"));
registerEventHandler(window, 'afterprint', getInstanceDelegate(this, "reset_form"));

var scrollPos = 0;

var inheritedMembers;
var protectedMembers;
var netcfMembersOnly;
var netXnaMembersOnly;

// Help 1 and website persistence support
// http://www.helpware.net/FAR/far_faq.htm
// http://msdn.microsoft.com/en-us/library/ms533007.aspx
// http://msdn.microsoft.com/en-us/library/ms644690.aspx
var curLoc = document.location + ".";

if(curLoc.indexOf("mk:@MSITStore") == 0)
{
    curLoc = "ms-its:" + curLoc.substring(14, curLoc.length - 1);
    document.location.replace(curLoc);
}

// Initialize array of section states

var sectionStates = new Array();
var sectionStatesInitialized = false;

//Hide sample source in select element
function HideSelect()
{
	var selectTags = document.getElementsByTagName("SELECT");
	var spanEles = document.getElementsByTagName("span");
	var i = 10;
	var m;

	if (selectTags.length != null || selectTags.length >0)
	{
		for (n=0; n<selectTags.length; n++)
		{
			var lan = selectTags(n).getAttribute("id").substr("10");
			//hide the first select that is on
			switch (lan.toLowerCase())
			{
				case "visualbasic":
					//alert(lan);
					for (m=0; m<spanEles.length; m++)
					{
						if (spanEles[m].getAttribute("codeLanguage") == "VisualBasic" && spanEles[m].style.display != "none" && n <i)
							i = n;
					}
					break;
				case "visualbasicdeclaration":
					for (m=0; m<spanEles.length; m++)
					{
						if (spanEles[m].getAttribute("codeLanguage") == "VisualBasicDeclaration" && spanEles[m].style.display != "none" && n < i)
							i = n;
					}
					break;
				case "visualbasicusage":
					//alert(lan);
					for (m=0; m<spanEles.length; m++)
					{
						if (spanEles[m].getAttribute("codeLanguage") == "VisualBasicUsage" && spanEles[m].style.display != "none" && n <i)
							i = n;
					}
					break;
				case "csharp":
					for (m=0; m<spanEles.length; m++)
					{
						if (spanEles[m].getAttribute("codeLanguage") == "CSharp" && spanEles[m].style.display != "none" && n < i)
							i = n;
					}
					break;
				case "managedcplusplus":
					for (m=0; m<spanEles.length; m++)
					{
						if (spanEles[m].getAttribute("codeLanguage") == "ManagedCPlusPlus" && spanEles[m].style.display != "none" && n < i)
							i = n;
					}
					break;
				case "jsharp":
					for (m=0; m<spanEles.length; m++)
					{
						if (spanEles[m].getAttribute("codeLanguage") == "JSharp" && spanEles[m].style.display != "none" && n < i)
							i = n;
					}
					break;
				case "jscript":
					for (m=0; m<spanEles.length; m++)
					{
						if (spanEles[m].getAttribute("codeLanguage") == "JScript" && spanEles[m].style.display != "none" && n < i)
							i = n;
					}
					break;
				case "xaml":
					//alert(lan);
					for (m=0; m<spanEles.length; m++)
					{
						if (spanEles[m].getAttribute("codeLanguage") == "XAML" && spanEles[m].style.display != "none" && n <i)
							i = n;
					}
					break;
				case "javascript":
					//alert(lan);
					for (m=0; m<spanEles.length; m++)
					{
						if (spanEles[m].getAttribute("codeLanguage") == "JavaScript" && spanEles[m].style.display != "none" && n <i)
							i = n;
					}
					break;
				case "fsharp":
					for (m=0; m<spanEles.length; m++)
					{
						if (spanEles[m].getAttribute("codeLanguage") == "FSharp" && spanEles[m].style.display != "none" && n < i)
							i = n;
					}
					break;
			}
		}
		if (i != 10)
			selectTags(i).style.visibility = "hidden";
	}
	else{ alert("Not found!");}
}

function UnHideSelect()
{
	var selectTags = document.getElementsByTagName("SELECT");
	var n;

	//un-hide all the select sections
	if (selectTags.length != null || selectTags.length >0)
	{
		for (n=0; n<selectTags.length; n++)
			selectTags(n).style.visibility = "visible";
	}
}

function InitSectionStates()
{
    sectionStatesInitialized = true;
    if (globals == null) globals = GetGlobals();
    // SectionStates has the format:
    //
    //     firstSectionId:state;secondSectionId:state;thirdSectionId:state; ... ;lastSectionId:state
    //
    // where state is either "e" (expanded) or "c" (collapsed)

    // get the SectionStates from the previous topics
    var states = Load("SectionStates");

    var start = 0;
    var end;
    var section;
    var state;
    var allCollapsed = false;
    // copy the previous section states to the sectionStates array for the current page
	if (states != null && states != "")
	{
	    allCollapsed = true;
        while (start < states.length)
        {
            end = states.indexOf(":", start);

            section = states.substring(start, end);

            start = end + 1;
            end = states.indexOf(";", start);
            if (end == -1) end = states.length;
            state = states.substring(start, end);
            sectionStates[section] = state;
    	    allCollapsed = allCollapsed && (state == "c");
    	    start = end + 1;
        }
	}

    // now set the state for any section ids in the current document that weren't in previous
	var imgElements = document.getElementsByName("toggleSwitch");
	var i;
	for (i = 0; i < imgElements.length; ++i)
        sectionStates[imgElements[i].id] = GetInitialSectionState(imgElements[i].id, allCollapsed);
}

function GetInitialSectionState(itemId, allCollapsed)
{
    // if the global state is "allCollapsed", set all section states to collapsed
    if (allCollapsed) return "c";

    // generic <section> node ids begin with "sectionToggle", so the same id can refer to different sections in different topics
    // we don't want to persist their state; set it to expanded
    if (itemId.indexOf("sectionToggle", 0) == 0) return "e";

    // the default state for new section ids is expanded
    if (sectionStates[itemId] == null) return "e";

    // otherwise, persist the passed in state
    return sectionStates[itemId];
}

var noReentry = false;

function OnLoadImage(eventObj)
{
    if (noReentry) return;

    if (!sectionStatesInitialized)
	    InitSectionStates();

    var elem;
    if(document.all) elem = eventObj.srcElement;
    else elem = eventObj.target;

    if ((sectionStates[elem.id] == "e"))
		ExpandSection(elem);
	else
		CollapseSection(elem);
}

/*
**********
**********   Begin
**********
*/

var docSettings;
var mainSection;

function LoadPage()
{
	// If not initialized, grab the DTE.Globals object
    if (globals == null)
        globals = GetGlobals();

	// docSettings has settings for the current document,
	//     which include persistent and non-persistent keys for checkbox filters and expand/collapse section states
	// persistKeys is an array of the checkbox ids to persist
	if (docSettings == null)
	{
        docSettings = new Array();
        persistKeys = new Array();
	}

    if (!sectionStatesInitialized)
	    InitSectionStates();

	var imgElements = document.getElementsByName("toggleSwitch");

	for (i = 0; i < imgElements.length; i++)
	{
		if ((sectionStates[imgElements[i].id] == "e"))
			ExpandSection(imgElements[i]);
		else
			CollapseSection(imgElements[i]);
	}

	SetCollapseAll();

	// split screen
	mainSection = document.getElementById("mainSection");
	if (!mainSection)
	    mainSection = document.getElementById("mainSectionMHS");

	var screen = new SplitScreen('header', mainSection.id);

	// init devlang filter checkboxes
	SetupDevlangsFilter();

	// init memberlist filter checkboxes for protected, inherited, etc
	SetupMemberOptionsFilter();

	// init memberlist platforms filter checkboxes, e.g. .Net Framework, CompactFramework, XNA, Silverlight, etc.
	SetupMemberFrameworksFilter();

	// removes blank target from in the self links for Microsoft Help System
	RemoveTargetBlank();

    // set gradient image to the bottom of header for Microsoft Help System
	SetBackground('headerBottom');

	// vs70.js did this to allow up/down arrow scrolling, I think
	try { mainSection.setActive(); } catch(e) { }

	//set the scroll position
	try{mainSection.scrollTop = scrollPos;}
	catch(e){}
}

function Window_Unload()
{
    // for each key in persistArray, write the key/value pair to globals
    for (var i = 0; i < persistKeys.length; i++)
        Save(persistKeys[i],docSettings[persistKeys[i]]);

    // save the expand/collapse section states
    SaveSections();
}

// removes blank target from in the self links for Microsoft Help System
function RemoveTargetBlank() {
    var elems = document.getElementsByTagName("a");
    for (var i = 0; i < elems.length; i++) {
        if (elems[i].getAttribute("target") == "_blank" &&
        elems[i].getAttribute("href", 2).indexOf("#", 0) == 0)
            elems[i].removeAttribute("target");
    }
}

function set_to_print()
{
	//breaks out of divs to print
	var i;

	if (window.text)document.all.text.style.height = "auto";

	for (i=0; i < document.all.length; i++)
	{
		if (document.all[i].tagName == "body")
		{
			document.all[i].scroll = "yes";
		}
		if (document.all[i].id == "header")
		{
			document.all[i].style.margin = "0px 0px 0px 0px";
			document.all[i].style.width = "100%";
		}
		if (document.all[i].id == mainSection.id)
		{
			document.all[i].style.overflow = "visible";
			document.all[i].style.top = "5px";
			document.all[i].style.width = "100%";
			document.all[i].style.padding = "0px 10px 0px 30px";
		}
	}
}

function reset_form()
{
	//returns to the div nonscrolling region after print
	 document.location.reload();
}

/*
**********
**********   End
**********
*/

/*
**********
**********   Begin Language Filtering
**********
*/

var devlangsMenu;
var devlangsDropdown;
var memberOptionsMenu;
var memberOptionsDropdown;
var memberFrameworksMenu;
var memberFrameworksDropdown;
var dropdowns = new Array();

// initialize the devlang filter dropdown menu
function SetupDevlangsFilter()
{
    var divNode = document.getElementById('devlangsMenu');
	if (divNode == null)
	    return;

	var checkboxNodes = divNode.getElementsByTagName("input");

	if (checkboxNodes.length == 1)
	{
	    // only one checkbox, so we don't need a menu
	    // get the devlang and use it to display the correct devlang spans
	    // a one-checkbox setting like this is NOT persisted, nor is it set from the persisted globals
	    var checkboxData = checkboxNodes[0].getAttribute('data');
        var dataSplits = checkboxData.split(',');
        var devlang = "";
        if (dataSplits.length > 1)
            devlang = dataSplits[1];
	    styleSheetHandler(devlang);
	}
	else
	{
	    // setup the dropdown menu
        devlangsMenu = new CheckboxMenu("devlangsMenu", docSettings, persistKeys, globals);
		devlangsDropdown = new Dropdown('devlangsDropdown', 'devlangsMenu', 'header');
		dropdowns.push(devlangsDropdown);

        // update the label of the dropdown menu
        SetDropdownMenuLabel(devlangsMenu, devlangsDropdown);

        // toggle the document's display docSettings
	    codeBlockHandler();
	    styleSheetHandler("");
	}
}

// called onclick in a devlang filter checkbox
// tasks to perform at this event are:
//   toggle the check state of the checkbox that was clicked
//   update the user's devlang preference, based on devlang checkbox states
//   update stylesheet based on user's devlang preference
//   show/hide snippets/syntax based on user's devlang preference
//
function SetLanguage(checkbox)
{
    // toggle the check state of the checkbox that was clicked
    devlangsMenu.ToggleCheckState(checkbox.id);

    // update the label of the dropdown menu
    SetDropdownMenuLabel(devlangsMenu, devlangsDropdown);

    // update the display of the document's items that are dependent on the devlang setting
	codeBlockHandler();
	styleSheetHandler("");

}
/*
**********
**********   End Language Filtering
**********
*/

/*
**********
**********   Begin Members Options Filtering
**********
*/

// initialize the memberlist dropdown menu for protected, inherited, etc
function SetupMemberOptionsFilter()
{
	if (document.getElementById('memberOptionsMenu') != null) {
        memberOptionsMenu = new CheckboxMenu("memberOptionsMenu", docSettings, persistKeys, globals);
		memberOptionsDropdown = new Dropdown('memberOptionsDropdown', 'memberOptionsMenu', 'header');
		dropdowns.push(memberOptionsDropdown);

        // update the label of the dropdown menu
        SetDropdownMenuLabel(memberOptionsMenu, memberOptionsDropdown);

        // show/hide memberlist rows based on the current docSettings
	    memberlistHandler();
	}
}

// sets the background to an element for Microsoft Help 3 system
function SetBackground(id) {
    var elem = document.getElementById(id);
    if (elem) {
        var img = document.getElementById(id + "Image");
        if (img) {
            elem.setAttribute("background", img.getAttribute("src"));
        }
    }
}

function SetupMemberFrameworksFilter()
{
	if (document.getElementById('memberFrameworksMenu') != null)
	{
        memberFrameworksMenu = new CheckboxMenu("memberFrameworksMenu", docSettings, persistKeys, globals);
		memberFrameworksDropdown = new Dropdown('memberFrameworksDropdown', 'memberFrameworksMenu', 'header');
		dropdowns.push(memberFrameworksDropdown);

        // update the label of the dropdown menu
        SetDropdownMenuLabel(memberFrameworksMenu, memberFrameworksDropdown);

        // show/hide memberlist rows based on the current docSettings
	    memberlistHandler();
	}
}

function SetMemberOptions(checkbox, groupName)
{
    var checkboxGroup = new Array();
    if (groupName == "vis")
    {
        if (document.getElementById('PublicCheckbox') != null)
            checkboxGroup.push('PublicCheckbox');
        if (document.getElementById('ProtectedCheckbox') != null)
            checkboxGroup.push('ProtectedCheckbox');
    }
    else if (groupName == "decl")
    {
        if (document.getElementById('DeclaredCheckbox') != null)
            checkboxGroup.push('DeclaredCheckbox');
        if (document.getElementById('InheritedCheckbox') != null)
            checkboxGroup.push('InheritedCheckbox');
    }

    // toggle the check state of the checkbox that was clicked
    memberOptionsMenu.ToggleGroupCheckState(checkbox.id, checkboxGroup);

    // update the label of the dropdown menu
    SetDropdownMenuLabel(memberOptionsMenu, memberOptionsDropdown);

    // update the display of the document's items that are dependent on the member options settings
    memberlistHandler();
}

function SetMemberFrameworks(checkbox)
{
    // toggle the check state of the checkbox that was clicked
    memberFrameworksMenu.ToggleCheckState(checkbox.id);

    // update the label of the dropdown menu
    SetDropdownMenuLabel(memberFrameworksMenu, memberFrameworksDropdown);

    // update the display of the document's items that are dependent on the member platforms settings
    memberlistHandler();
}

function DisplayFilteredMembers()
{
	var iAllMembers = document.getElementsByTagName("tr");
	var i;

	for(i = 0; i < iAllMembers.length; ++i)
	{
		if (((iAllMembers[i].notSupportedOnXna == "true") && (netXnaMembersOnly == "on")) ||
			((iAllMembers[i].getAttribute("name") == "inheritedMember") && (inheritedMembers == "off")) ||
			((iAllMembers[i].getAttribute("notSupportedOn") == "netcf") && (netcfMembersOnly == "on")))
			iAllMembers[i].style.display = "none";
		else
			iAllMembers[i].style.display = "";
	}

	// protected members are in separate collapseable sections in vs2005, so expand or collapse the sections
	ExpandCollapseProtectedMemberSections();
}

function ExpandCollapseProtectedMemberSections()
{
	var imgElements = document.getElementsByName("toggleSwitch");
	var i;
	// Family
	for(i = 0; i < imgElements.length; ++i)
	{
		if(imgElements[i].id.indexOf("protected", 0) == 0)
		{
	        if ((sectionStates[imgElements[i].id] == "e" && protectedMembers == "off") ||
	            (sectionStates[imgElements[i].id] == "c" && protectedMembers == "on"))
			{
				ExpandCollapse(imgElements[i]);
			}
		}
	}
}

/*
**********
**********   End Members Options Filtering
**********
*/

/*
**********
**********   Begin Expand/Collapse
**********
*/

// expand or collapse a section
function ExpandCollapse(imageItem)
{
	if (sectionStates[imageItem.id] == "e")
		CollapseSection(imageItem);
	else
		ExpandSection(imageItem);

	SetCollapseAll();
}

// expand or collapse all sections
function ExpandCollapseAll(imageItem)
{
    var collapseAllImage = document.getElementById("collapseAllImage");
    var expandAllImage = document.getElementById("expandAllImage");
    if (imageItem == null || collapseAllImage == null || expandAllImage == null) return;
    noReentry = true; // Prevent entry to OnLoadImage

	var imgElements = document.getElementsByName("toggleSwitch");
	var i;
	var collapseAll = (imageItem.src == collapseAllImage.src);
	if (collapseAll)
	{
		imageItem.src = expandAllImage.src;
		imageItem.alt = expandAllImage.alt;

		for (i = 0; i < imgElements.length; ++i)
		{
			CollapseSection(imgElements[i]);
		}
	}
	else
	{
		imageItem.src = collapseAllImage.src;
		imageItem.alt = collapseAllImage.alt;

		for (i = 0; i < imgElements.length; ++i)
		{
			ExpandSection(imgElements[i]);
		}
	}
	SetAllSectionStates(collapseAll);
	SetToggleAllLabel(collapseAll);

	noReentry = false;
}

function ExpandCollapse_CheckKey(imageItem, eventObj)
{
	if(eventObj.keyCode == 13)
		ExpandCollapse(imageItem);
}

function ExpandCollapseAll_CheckKey(imageItem, eventObj)
{
	if(eventObj.keyCode == 13)
		ExpandCollapseAll(imageItem);
}

function SetAllSectionStates(collapsed)
{
    for (var sectionId in sectionStates)
        sectionStates[sectionId] = (collapsed) ? "c" : "e";
}

function ExpandSection(imageItem)
{
    noReentry = true; // Prevent re-entry to OnLoadImage
    try
    {
        var collapseImage = document.getElementById("collapseImage");
		imageItem.src = collapseImage.src;
		imageItem.alt = collapseImage.alt;

	    imageItem.parentNode.parentNode.nextSibling.style.display = "";
	    sectionStates[imageItem.id] = "e";
    }
    catch (e)
    {
    }
    noReentry = false;
}

function CollapseSection(imageItem)
{
    noReentry = true; // Prevent re-entry to OnLoadImage
    var expandImage = document.getElementById("expandImage");
	imageItem.src = expandImage.src;
	imageItem.alt = expandImage.alt;
	imageItem.parentNode.parentNode.nextSibling.style.display = "none";
	sectionStates[imageItem.id] = "c";
    noReentry = false;
}

function AllCollapsed()
{
	var imgElements = document.getElementsByName("toggleSwitch");
	var allCollapsed = true;
	var i;

	for (i = 0; i < imgElements.length; i++) allCollapsed = allCollapsed && (sectionStates[imgElements[i].id] == "c");

	return allCollapsed;
}

function SetCollapseAll()
{
	var imageElement = document.getElementById("toggleAllImage");
	if (imageElement == null) return;

	var allCollapsed = AllCollapsed();
	if (allCollapsed)
	{
        var expandAllImage = document.getElementById("expandAllImage");
	    if (expandAllImage == null) return;
		imageElement.src = expandAllImage.src;
		imageElement.alt = expandAllImage.alt;
	}
	else
	{
        var collapseAllImage = document.getElementById("collapseAllImage");
	    if (collapseAllImage == null) return;
		imageElement.src = collapseAllImage.src;
		imageElement.alt = collapseAllImage.alt;
	}

	SetToggleAllLabel(allCollapsed);
}

function SetToggleAllLabel(allCollapsed)
{
	var collapseLabelElement = document.getElementById("collapseAllLabel");
	var expandLabelElement = document.getElementById("expandAllLabel");

	if (collapseLabelElement == null || expandLabelElement == null) return;

	if (allCollapsed)
	{
		collapseLabelElement.style.display = "none";
		expandLabelElement.style.display = "inline";
	}
	else
	{
		collapseLabelElement.style.display = "inline";
		expandLabelElement.style.display = "none";
	}
}

function SaveSections()
{
    try
    {
        var states = "";

        for (var sectionId in sectionStates) states += sectionId + ":" + sectionStates[sectionId] + ";";

        Save("SectionStates", states.substring(0, states.length - 1));
    }
    catch (e)
    {
    }

}

function OpenSection(imageItem)
{
	if (sectionStates[imageItem.id] == "c") ExpandCollapse(imageItem);
}

/*
**********
**********   End Expand/Collapse
**********
*/

/*
**********
**********   Begin Copy Code
**********
*/

function CopyCode(key)
{
	var trElements = document.getElementsByTagName("tr");
	var i;
	for(i = 0; i < trElements.length; ++i)
	{
		if(key.parentNode.parentNode.parentNode == trElements[i].parentNode)
		{
		    if (window.clipboardData)
            {
                // the IE-manner
                window.clipboardData.setData("Text", trElements[i].innerText);
            }
            else if (window.netscape)
            {
                // Gives unrestricted access to browser APIs using XPConnect
		try
		{
			netscape.security.PrivilegeManager.enablePrivilege("UniversalXPConnect");
		}
	        catch(e)
		{
			alert("Universal Connect was refused, cannot copy to " +
				"clipboard.  Go to about:config and set " +
				"signed.applets.codebase_principal_support to true to " +
				"enable clipboard support.");
			return;
		}

                // Creates an instance of nsIClipboard
                var clip = Components.classes['@mozilla.org/widget/clipboard;1'].createInstance(Components.interfaces.nsIClipboard);
                if (!clip) return;

                // Creates an instance of nsITransferable
                var trans = Components.classes['@mozilla.org/widget/transferable;1'].createInstance(Components.interfaces.nsITransferable);
                if (!trans) return;

                // register the data flavor
                trans.addDataFlavor('text/unicode');

                // Create object to hold the data
                var str = new Object();

                // Creates an instance of nsISupportsString
                var str = Components.classes["@mozilla.org/supports-string;1"].createInstance(Components.interfaces.nsISupportsString);

                //Assigns the data to be copied
                var copytext = trElements[i].textContent;
                str.data = copytext;

                // Add data objects to transferable
                trans.setTransferData("text/unicode",str,copytext.length*2);
                var clipid = Components.interfaces.nsIClipboard;
                if (!clip) return false;

                // Transfer the data to clipboard
                clip.setData(trans,null,clipid.kGlobalClipboard);
            }
        }
	}
}

function ChangeCopyCodeIcon(key)
{
	var i;
	var imageElements = document.getElementsByName("ccImage")
	for(i=0; i<imageElements.length; ++i)
	{
		if(imageElements[i].parentNode == key)
		{
			if(imageElements[i].src == copyImage.src)
			{
				imageElements[i].src = copyHoverImage.src;
				imageElements[i].alt = copyHoverImage.alt;
				key.className = 'copyCodeOnHover';
			}
			else
			{
				imageElements[i].src = copyImage.src;
				imageElements[i].alt = copyImage.alt;
				key.className = 'copyCode';
			}
		}
	}
}

function CopyCode_CheckKey(key, eventObj)
{
	if(eventObj.keyCode == 13)
		CopyCode(key);
}

/*
**********
**********   End Copy Code
**********
*/

/*
**********
**********   Begin Maintain Scroll Position
**********
*/

function loadAll(){
	try
	{
		scrollPos = allHistory.getAttribute("Scroll");
	}
	catch(e){}
}

function saveAll(){
	try
	{
		allHistory.setAttribute("Scroll", mainSection.scrollTop);
	}
	catch(e){}
}

/*
**********
**********   End Maintain Scroll Position
**********
*/

/*
**********
**********   Begin Send Mail
**********
*/

function formatMailToLink(anchor)
{
	var release = "Release: " + anchor.doc_Release;
	var topicId = "Topic ID: " + anchor.doc_TopicID;
	var topicTitle = "Topic Title: " + anchor.doc_TopicTitle;
	var url = "URL: " + document.URL;
	var browser = "Browser: " + window.navigator.userAgent;

	var crlf = "%0d%0a";
	var body = release + crlf + topicId + crlf + topicTitle + crlf + url + crlf + browser + crlf + crlf + "Comments:" + crlf + crlf;

	anchor.href = anchor.href + "&body=" + body;
}

/*
**********
**********   End Send Mail
**********
*/

/*
**********
**********   Begin Persistence
**********
*/

var globals;

// get global vars from persistent store
function GetGlobals()
{
	var tmp;

	// Try to get VS implementation
	try
    {
        tmp = window.external.Globals;
    }
	catch(e)
    {
        tmp = null;
    }

	// Try to get DExplore implementation
	try
    {
        if(tmp == null)
            tmp = window.external.GetObject("DTE", "").Globals;
    }
	catch (e)
    {
        tmp = null;
    }

    // Help 1 and website persistence support
	isHelp1OrWebsite = false;

	if(tmp == null)
	{
	    tmp = Help1AndWebsiteGlobals;
	    isHelp1OrWebsite = true;

        // If this fails, we're probably under Help Viewer 2.0 and this won't work at all
        try
        {
            tmp.VariableExists("X");
        }
        catch(e)
        {
            tmp = null;
        }
	}

	return tmp;
}

function Load(key)
{
	try
	{
	    // Help 1 and website persistence support
	    if(isHelp1OrWebsite)
	        return globals.Load(key);

		return globals.VariableExists(key) ? globals.VariableValue(key) : null;
	}
	catch(e)
	{
		return null;
	}
}

function Save(key, value)
{
	try
	{
	    // Help 1 and website persistence support
	    if(isHelp1OrWebsite)
	        globals.Save(key, value);
	    else
	    {
		    globals.VariableValue(key) = value;
		    globals.VariablePersists(key) = true;
	    }
	}
	catch(e)
	{
	}
}

// Help 1 and website persistence support
var isHelp1OrWebsite;

var Help1AndWebsiteGlobals =
{
    UserDataCache: function()
    {
        // The hidden element is defined by Sandcastle in each topic
        // <input type="hidden" id="userDataCache" class="userDataStyle" />
        var userData = document.getElementById("userDataCache");

        return userData;
    },

    // CheckboxMenu requires this
    VariableExists: function(key)
    {
        var userData = this.UserDataCache();
        userData.load("userDataSettings");

        var value = userData.getAttribute(key);

        return (value != null);
    },

    // CheckboxMenu requires this
    VariableValue: function(key)
    {
        var userData = this.UserDataCache();
        userData.load("userDataSettings");
        var value = userData.getAttribute(key);

        return value;
    },

    Load: function(key)
    {
        var userData = this.UserDataCache();
        userData.load("userDataSettings");
        var value = userData.getAttribute(key);

        return value;
    },

    Save: function(key, value)
    {
        var userData = this.UserDataCache();
        userData.setAttribute(key, value);
        userData.save("userDataSettings");
    }
};

/*
**********
**********   End Persistence
**********
*/

/* This is the part for Glossary popups */
// The method is called when the user positions the mouse cursor over a glossary term in a document.
// Current implementation assumes the existence of an associative array (g_glossary).
// The keys of the array correspond to the argument passed to this function.

var bGlossary=true;
var oDialog;
var oTimeout="";
var oTimein="";
var iTimein=.5;
var iTimeout=30;
var oLastNode;
var oNode;
var bInit=false;
var aTerms=new Array();

// Called from mouseover and when the contextmenu behavior fires oncontextopen.
function clearDef(eventObj){
    if(eventObj){
        var elem;
        if(document.all) elem = eventObj.toElement;
        else elem = eventObj.relatedTarget;
	    if(elem!=null || elem!="undefined"){
		    if(typeof(oTimein)=="number"){
			    window.clearTimeout(oTimein);
		    }
		    if(oDialog.dlg_status==true){
			    hideDef();
		    }
		}
	}
}
function hideDef(eventObj){
	window.clearTimeout(oTimeout);
	oTimeout="";
	oDialog.style.display="none";
	oDialog.dlg_status=false;
}
function showDef(oSource){
	if(bInit==false){
		glossaryInit();
		bInit=true;
	}
	if(bGlossary==true){
		if(typeof(arguments[0])=="object"){
			oNode=oSource;
		}
		else{
		    if(document.all) oNode = eventObj.srcElement;
		    else oNode = eventObj.target;
		}
		var bStatus=oDialog.dlg_status; // BUGBUG: oDialog is null.
		if((oLastNode!=oNode)||(bStatus==false)){
			if((typeof(oTimein)=="number")&& eventObj){

			    var elem;
			    if(document.all) elem = eventObj.fromElement;
			    else elem = eventObj.relatedTarget;

			    if( elem != null || elem != "undefined")
				    window.clearTimeout(oTimein);
			}
			oTimein=window.setTimeout("openDialog(oNode)",iTimein*1000);
		}
	}
}

function glossaryInit(){
		oDialog=fnCreateDialog(150,50);
}

function navigateTerm(eventObj){
    var oNode;
    if(document.all) oNode = eventObj.srcElement;
    else oNode = eventObj.target;

	var iTermID=oNode.termID;
	if(oNode!=aTerms[iTermID]){
		var iAbsTop=getAbsoluteTop(aTerms[iTermID]);
		if(iAbsTop<document.body.scrollTop){
			window.scrollTo(document.body.scrollLeft,getAbsoluteTop(aTerms[iTermID]));
		}
		openDialog(aTerms[iTermID]);
	}
}
function disableGlossary(eventObj){
	if(bGlossary==true){
	    if(document.all) eventObj.srcElement.innerText="Enable Automatic Glossary";
		else eventObj.target.innerText="Enable Automatic Glossary";
		bGlossary=false;
		hideDef();
	}
	else{
	    if(document.all) eventObj.srcElement.innerText="Disable Automatic Glossary";
		else eventObj.target.innerText="Disable Automatic Glossary";
		bGlossary=true;
	}
}
function openGlossary(){

}
function fnSetMenus(eventObj){
    var oNode;
    if(document.all) oNode = eventObj.srcElement;
    else oNode = eventObj.target;

	var oMenu=oNode.createMenu("SPAN","G_RID");
	var oSubItem1=oNode.createMenuItem("Glossary",fnStub,oMenu,true);
	document.body.createMenuItem("Open External Glossary",openGlossary,oSubItem1.subMenu);
	document.body.createMenuItem("Disable Automatic Glossary",disableGlossary,oSubItem1.subMenu);
	for(var i=0;i<aTerms.length;i++){
		var oItem=document.body.createMenuItem(aTerms[i].innerText,navigateTerm,oMenu);
		oItem.termID=i;
	}
}
// This is a bogus stub.  It should be sniffed out rather than added in.
function fnStub(){

}
function fnAttachMenus(aTips){
	// This walk is only necessary for the context menu.
	var aTips=document.getElementsByTagName("SPAN");
	for(var i=0;i<aTips.length;i++){
		var oNode=aTips[i];
		if(oNode.getAttribute("G_RID")){
			var sTerm=oNode.getAttribute("G_RID");
			if(typeof(g_glossary[sTerm])=="string"){
				// Removed client-side scripting to add events.  This entire process should be singled out for IE 5 and later .. and, its only for the context menu.
				aTerms[aTerms.length]=oNode;
			}
		}
	}
	if(oBD.majorVer>=5){
		document.body.addBehavior(gsContextMenuPath);
		document.body.onbehaviorready="fnSetMenus()";
		document.body.oncontextopen="clearDef()";
	}

}
// Called by showDef.  The showDef function sniffs for initialization.
function openDialog(oNode,x,y){
 	var bStatus=oDialog.dlg_status; // BUGBUG: This code assumes that oDialog has been initialized
	if(bStatus==false){
		oDialog.dlg_status=true;
		oDialog.style.display="block";
	}
	else{
		if(typeof(oTimeout)=="number"){
			window.clearTimeout(oTimeout);
		}
	}

	var sTerm=oNode.getAttribute("G_RID");
	var oDef=oNode.children(0);
	var sDef=oDef.text;
	sDef=sDef.substr(4,sDef.length-7);	//Strips the html comment markers from the definition.
	oDialog.innerHTML=sDef

	//oDialog.innerHTML=g_glossary[sTerm];

	var iScrollLeft=document.body.scrollLeft;
	var iScrollTop=document.body.scrollTop;
	var iOffsetLeft=getAbsoluteLeft(oNode)// - iScrollLeft;
	var iOffsetWidth=oNode.offsetWidth;
	var oParent=oNode.parentNode;
	var iOffsetParentLeft=getAbsoluteLeft(oParent);
	var iOffsetTop=getAbsoluteTop(oNode); //- iScrollTop;
	var iOffsetDialogWidth=oDialog.offsetWidth;

	if((iOffsetLeft + iOffsetWidth) > (iOffsetParentLeft + oParent.offsetWidth)){
		iOffsetLeft=iOffsetParentLeft;
		if(iOffsetLeft - iOffsetDialogWidth>0){
			iOffsetTop+=oNode.offsetHeight;
		}
	}
	var iLeft=0;
	var iTop=0;
	if((iOffsetLeft + iOffsetWidth - iScrollLeft + iOffsetDialogWidth) < document.body.offsetWidth ){
		iLeft=iOffsetLeft + iOffsetWidth;
	}
	else{
		if(iOffsetLeft - iOffsetDialogWidth>0){
			iLeft=iOffsetLeft - iOffsetDialogWidth;
		}
		else{
			iLeft=iOffsetParentLeft;
		}
	}
	if(iOffsetTop - iScrollTop<oDialog.offsetHeight){
		iTop=iOffsetTop + oNode.offsetHeight;
	}
	else{
		iTop=iOffsetTop - oDialog.offsetHeight;
	}
	oDialog.style.top=iTop;
	oDialog.style.left=iLeft;
	oTimeout=window.setTimeout("hideDef()",iTimeout*1000);
}
function getAbsoluteTop(oNode){
	var oCurrentNode=oNode;
	var iTop=0;
	while(oCurrentNode.tagName!="BODY"){
		iTop+=oCurrentNode.offsetTop;
		oCurrentNode=oCurrentNode.offsetParent;
	}
	return iTop;
}
function getAbsoluteLeft(oNode){
	var oCurrentNode=oNode;
	var iLeft=0;
	while(oCurrentNode.tagName!="BODY"){
		iLeft+=oCurrentNode.offsetLeft;
		oCurrentNode=oCurrentNode.offsetParent;
	}
	return iLeft;
}
function fnCreateDialog(iWidth,iHeight){
	document.body.insertAdjacentHTML("BeforeEnd","<DIV></DIV>");
	oNewDialog=document.body.children(document.body.children.length-1);
	oNewDialog.className="clsTooltip";
	oNewDialog.style.width=iWidth;
	oNewDialog.dlg_status=false;
	return oNewDialog;
}

function sendfeedback(subject, id,alias){
	var rExp = /\"/gi;
	var url = location.href;
	// Need to replace the double quotes with single quotes for the mailto to work.
	var rExpSingleQuotes = /\'\'"/gi;
	var title = document.getElementsByTagName("TITLE")[0].innerText.replace(rExp, "''");
	location.href = "mailto:" + alias + "?subject=" + subject + title + "&body=Topic%20ID:%20" + id + "%0d%0aURL:%20" + url + "%0d%0a%0d%0aComments:%20";
}

## File: scripts/SplitScreen.js

	function SplitScreen (nonScrollingRegionId, scrollingRegionId) {

		// store references to the two regions
		this.nonScrollingRegion = document.getElementById(nonScrollingRegionId);
		this.scrollingRegion = document.getElementById(scrollingRegionId);

		// set the scrolling settings
		this.scrollingRegion.parentElement.style.margin = "0px";
		this.scrollingRegion.parentElement.style.overflow = "hidden";
		this.scrollingRegion.style.overflow = "auto";

		// fix the size of the scrolling region
		this.resize(null);

		// add an event handler to resize the scrolling region when the window is resized
		registerEventHandler(window, 'resize', getInstanceDelegate(this, "resize"));

		// Added by ComponentOne
		this.resize(null);
	}

	SplitScreen.prototype.resize = function(e) {
		var height = document.body.clientHeight - this.nonScrollingRegion.offsetHeight;
		if (height > 0) {
			this.scrollingRegion.style.height = height;
		} else {
			this.scrollingRegion.style.height = 0;
		}
		this.scrollingRegion.style.width = this.scrollingRegion.parentElement.clientWidth;
	}

## File: styles/Presentation.css

﻿/* * * This file was autogenerated by Styler at 02:02 on 02/15/2003 * * */

/***********************************************************
 *             SCRIPT-SUPPORTING STYLES
 ***********************************************************/

/* Defines the userData cache persistence mechanism. */
.userDataStyle
{
	behavior: url(#default#userdata);
}

/* Used to save the scroll bar position when navigating away from a page. */
div.saveHistory
{
	behavior: url(#default#savehistory);
}

/* Formats the expand/collapse images for all collapsible regions. */
img.toggle
{
	border: 0;
	margin-right: 5;
}

/* Formats the Collapse All/Expand All images. */
img#toggleAllImage
{
	margin-left: 0;
	vertical-align: middle;
}

/* Supports XLinks */
MSHelp\:link
{
 	text-decoration: underline;
	color: #0000ff;
	hoverColor: #3366ff;
	filterString: ;
}

/***********************************************************
 *             CONTENT PRESENTATION STYLES
 ***********************************************************/

body
{
	background:	#FFFFFF;
	color: #000000;
	font-family:	Verdana;
	font-size: medium;
	font-style: normal;
	font-weight: normal;
	margin-top:	0;
	margin-bottom:	0;
	margin-left:	0;
	margin-right:	0;
	width:	100%;
}

dl
{
	margin-top:	15;
	margin-bottom:5;
	padding-left:	1;
}

dl.authored dt {
	font-weight: bold;
	margin-top: 5px;
}

dl.authored dd {
	margin-left: 20px;
    margin-bottom: 5px;
}

dd {
	margin-left:	0;
}

ul
{
	margin-top: 1em;
	margin-bottom: 1em;
}

ol {
	margin-top: 1em;
	margin-bottom: 1em;
}

li {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

ul.nobullet
{
    list-style-type: none;
}

p {
	margin-top: 10;
	margin-bottom: 5;
}

a:link {
	color:	#0000FF;
}

a:visited {
	color:	#0000FF;
}

a:hover {
	color: #DD7C3B;
}

div#header a, div#mainSectionMHS a {
    text-decoration: underline;
}

code
{
    font-family: Consolas, "Courier New", Courier, monospace;
	font-size: 105%;
	color:	#000066;
}

span.parameter {
	font-style: italic;
}

span.italic {
	font-style: italic;
}

span.selflink {
	font-weight: bold;
}

span.nolink {
	font-weight: bold;
}

/***********************************************************
 *             STRUCTURE PRESENTATION STYLES
 ***********************************************************/

/* Applies to everything below the non-scrolling header region. */
div#mainSection
{
	font-size: 62.5%;
	width: 100%;
}
div#mainSectionMHS
{
    font-family: Verdana;
	font-size: 81%;
	width: 100%;
}
html>body #mainSection, html>body #mainSectionMHS
{
	font-size:73%;
	width: 100%;
}

/* Applies to everything below the non-scrolling header region, minus the footer. */
div#mainBody
{
	font-size: 100%;
	margin-left: 15;
	margin-top: 10;
	/*padding-bottom: 20;*/
}

html>body #mainBody
{
	font-size: 93%;
	margin-left: 15;
	margin-top: 10;
	padding-bottom: 20;
}

/* Adds right padding for all blocks in mainBody */
div#mainBody p, div#mainBody ol, div#mainBody ul, div#mainBody dl
{
	padding-right: 5;
}

/*------------------------------ Begin Non-scrolling Header Region Styles -------------------------------*/
/* Applies to the entire non-scrolling header region. */
div#header
{
    font-family: Verdana;
	background-color: #FFFFFF;
	padding-top:	0;
	padding-bottom:	0;
	padding-left:	0;
	padding-right:	0;
	width:	100%;
}

/* Applies to both tables in the non-scrolling header region. */
div#header table
{
	width:	100%;
}

/* Applies to cells in both tables in the non-scrolling header region. */
div#header table td
{
	color: #0000FF;
	font-size: 70%;
	margin-top:	0;
	margin-bottom:	0;
	padding-right: 20;
}

/* Applies to first row in the upper table of the non-scrolling header region. */
div#header table#toptable td
{
	padding-left: 15px;
}

/* Applies to second row in the upper table of the non-scrolling header region. */
div#header table tr#headerTableRow2 td
{
	padding-left: 13px;
}

/* Applies to the last row in the upper table of the non-scrolling header region. Text
   in this row includes See Also, Constructors, Methods, and Properties. */
div#header table tr#headerTableRow3 td
{
	padding-top: 2px;
	padding-left: 15;
}

/* Applies to the lower table in the non-scrolling header region. Text in this table
   includes Collapse All/Expand All, Language Filter, and Members Options. */
div#header table#bottomTable
{
	border-top-color: #FFFFFF;
	border-top-style: solid;
	border-top-width: 1;
	text-align: left;
	padding-left: 15;
	padding-top: 5px;
	padding-bottom: 5px;
}

/* Formats the first column--the one that displays icons--in mref list tables (such as Public Constructors,
   Protected Constructors, Public Properties, Protected Properties, and so on). */
div#mainSection table td.imageCell, div#mainSectionMHS table td.imageCell
{
	white-space: nowrap;
}
/*------------------------------ End General Table Styles -------------------------------*/

/*------------------------------ Begin General Table Styles -------------------------------*/

div#mainBody div.alert, div#mainBody div.code, div#mainBody div.tableSection
{
	width:98.9%;
}

div#mainBody div.section div.alert, div#mainBody div.section div.code,
div#mainBody div.section div.tableSection
{
	width:100%;
}

div#mainBody div.section ul div.alert, div#mainBody div.section ul div.code,
div#mainBody div.section ul div.tableSection, div#mainBody div.section ol div.alert,
div#mainBody div.section ol div.code, div#mainBody div.section ol div.tableSection
{
	width:100%;
}

div.alert p, div.code p
{
	margin-top:5;
	margin-bottom:8;
}
dd p
{
	margin-top:2;
	margin-bottom:8;
}
div.tableSection p
{
	margin-top:1;
	margin-bottom:4;
}
li p
{
	margin-top:2px;
	margin-bottom:8px;
}
div.seeAlsoNoToggleSection dl
{
	margin-top:8;
	margin-bottom:1;
	padding-left:1;
}
div.seeAlsoNoToggleSection dd p
{
	margin-top:2;
	margin-bottom:8;
}
div.section dl
{
	margin-top:8;
	margin-bottom:1;
	padding-left:1;
}
div.section dd p
{
	margin-top:2;
	margin-bottom:8;
}
/*------------------------------ End General Table Styles -------------------------------*/

/*------------------------------ Begin Non-scrolling Header Region Styles -------------------------------*/

/* Applies to the running header text in the first row of the upper table in the
   non-scrolling header region. */
span#runningHeaderText
{
	color: #8C8C8C;
	font-size: 90%;
}

/* Applies to the topic title in the second row of the upper table in the
   non-scrolling header region. */
span#nsrTitle
{
	color: #000000;
	font-size: 160%;
	font-weight: 400;
	font-family: arial;
}
/*------------------------------ End Non-scrolling Header Region Styles -------------------------------*/

/* Formats the footer. Currently, the transforms pass in two parameters to the
   footer SSC, but the default footer SSC doesn't use either parameter.
   TODO: Investigate whether the default footer SSC has any impact on doc spec. */
div#footer
{
	font-size: 80%;
	margin-top:	0;
	margin-bottom:	0;
	margin-left:	0;
	margin-right:	0;
	padding-top:	8;
	padding-bottom:	6;
	padding-left:	1;
	padding-right:	1;
	width:	100%;
}

html>body div#footer
{
	font-size: 80%;
	margin-top:	0;
	margin-bottom:	0;
	margin-left:	0;
	margin-right:	0;
	padding-top:	2;
	padding-bottom:	6;
	padding-left:	1;
	padding-right:	1;
	width:	98%;
}

/* Unable to find this style in the transforms. The default footer SSC adds a plain horizontal rule.
   TODO: Determine whether this style is required by the doc spec. */
/*
hr#footerHR
{
	border-bottom-color: #EEEEFF;
	border-bottom-style: solid;
	border-bottom-width: 1;
	border-top-color: C8CDDE;
	border-top-style: solid;
	border-top-width: 1;
	height: 3;
	color: #D4DFFF;
}
*/

/********************************************************************************************************************
	Collapsible Section Structure

	<h1 class="heading">							// Format of the collapsible section text
		<span onclick="ExpandCollapse(xxxToggle)">	// Defines the onclick procedure for the expand/collapse section
			<img id="xxxToggle">					// Expand/collapse image
			</img>
		</span>
	</h1>

	<div id="xxxSection" class="section">			// The body of the collapsible section; hidden by default
	</div>

	The ExpandCollapse() function is responsible for toggling the expand/collapse image, and for
	displaying/hiding the body of the collapsible section.
********************************************************************************************************************/

/* Applies to the body of a collapsible section */
div.seeAlsoNoToggleSection
{
	margin-left:0;
	padding-top:	2;
	padding-bottom:	2;
	padding-left:	0;
	padding-right:	15;
	width:	100%;
}

div.section
{
	margin-left:0;
	padding-top:	0;
	padding-bottom:	0;
	padding-left:	16;
	padding-right:	15;
	width:	100%;
}
html>body div.section
{
	margin-left:0;
	padding-top:	2;
	padding-bottom:	2;
	padding-left:	16;
	padding-right:	15;
	width:	97%;
}
div.seeSection
{
	margin-left:0;
	padding-top:	0;
	padding-bottom:	2;
	padding-left:	16;
	padding-right:	15;
	width:	100%;
}

/*------------------------------ Begin Heading Styles -------------------------------*/
/* As far as I can tell, only <h1> tags use this class.
   TODO: Decide whether to roll these attributes into the h1.heading style */
.heading
{
	font-weight:	bold;
	margin-top:		18;
	margin-bottom:	8;
}

/* All <h1> headings. */
h1.heading
{
    font-family: Verdana;
	color: #000000;
	font-size:	130%;
}

/* Applies to table titles and subsection titles. */
.subHeading
{
	font-weight:	bold;
	margin-bottom:	4;
}
.procedureSubHeading
{
	font-weight: bold;
	margin-bottom: 4;
}

/* Formats the titles of author-generated tables. */
h3.subHeading
{
    font-family: Verdana;
	color:  #000000;
	font-size: 120%;
    font-weight:800;
}

h3.procedureSubHeading
{
    font-family: Verdana;
	color: #000000;
	font-size: 120%;
}

/* Formats the titles of all subsections. */
h4.subHeading
{
    font-family: Verdana;
	color: #000000;
	font-size: 110%;
	font-weight:800;
}
span.labelheading, div.labelheading
{
	font-size:100%;
	color:#003399;
}

/*------------------------------ End Heading Styles -------------------------------*/

/*------------------------------ Begin Image Styles -------------------------------*/
img.copyCodeImage
{
	border: 0;
	margin: 1;
	margin-right: 3;
}

img.downloadCodeImage
{
	border: 0;
	margin-right: 3;
}

img.viewCodeImage
{
	border: 0;
	margin-right: 3;
}

img.note
{
	border: 0;
	margin-right: 3;
}
/*------------------------------ End Image Styles -------------------------------*/

/*------------------------------ Begin General Table Styles -------------------------------*/
div#mainSection table, div#mainSectionMHS table
{
	border: 0;
	font-size: 100%;
	width:	98.9%;
	margin-top: 5px;
	margin-bottom: 5px;
}

div#mainSection table tr, div#mainSectionMHS table tr
{
	vertical-align: top;
}

div#mainSection table th, div#mainSectionMHS table th
{
	background-color: #EFEFF7;
	border-bottom: 1px solid #C8CDDE;
	border-left: 1px none #D5D5D3;
	color: #000066;
	padding-left: 5px;
	padding-right: 5px;
	text-align: left;
}

div#mainSection table td, div#mainSectionMHS table td
{
	background-color: #F7F7FF;
	border-bottom: 1px solid #D5D5D3;
	border-left: 1px none #D5D5D3;
	padding-left: 5px;
	padding-right: 5px;
}

/* Formats the first column--the one that displays icons--in mref list tables (such as Public Constructors,
   Protected Constructors, Public Properties, Protected Properties, and so on). */
div#mainSection table td.imageCell, div#mainSectionMHS table td.imageCell
{
	white-space: nowrap;
}
/*------------------------------ End General Table Styles -------------------------------*/

/*------------------------------ Begin Syntax and Snipper Code Block Styles -------------------------------*/

div.code table
{
	border: 0 none;
	font-size: 95%;
	margin-bottom: 5px;
	width: 100%
}

div.code table th
{
    border: 0 none;
	border-bottom-color: #C8CDDE;
	border-bottom-style: solid;
	border-bottom-width: 1px;
	font-weight: bold;
	padding-left: 5px;
	padding-right: 5px;
	padding-top: 2px;
	padding-bottom: 2px;
	vertical-align: middle;
}

div.code table td
{
	background:	#F7F7FF;
	border-top-color: #FFFFFF;
	border-top-style: solid;
	border-top-width: 1px;
	padding-left: 5px;
	padding-right: 5px;
	padding-top: 5px;
}
/*------------------------------ End Syntax and Snipper Code Block Styles -------------------------------*/

/*------------------------------ Begin Note Styles -------------------------------*/
div.alert table
{
    border: 0px;
    font-size: 100%;
    width: 100%;
    margin-top: 5px;
    margin-bottom: 5px;
}

div.alert table th
{
    text-align: left;
    background: #EFEFF7;
    border-bottom-width: 0px;
    color: #000066;
    padding-left: 5px;
    padding-right: 5px;
}

div.alert table td
{
	background:	#F7F7FF;
	border-top-color: #FFFFFF;
	border-top-style: solid;
	border-top-width: 1px;
	padding-left: 5px;
	padding-right: 5px;
}

/*------------------------------ End Note Styles -------------------------------*/

/* Applies to the copy code text and image. */
span.copyCode
{
	color: #0000ff;
	font-size: 90%;
	font-weight: normal;
	cursor: pointer;
	float: right;
	display: inline;
	text-align: right;
	text-decoration: underline;
}

span.copyCodeOnHover
{
	color: #E85F17;
	font-size:xx-small;
	font-weight: normal;
	cursor: pointer;
	float: right;
	display: inline;
	text-align: right;
	text-decoration: underline;
}

.downloadCode
{
	color: #0000ff;
	font-size: 90%;
	font-weight: normal;
	cursor: pointer;
}

.viewCode
{
	color: #0000ff;
	font-size: 90%;
	font-weight: normal;
	cursor: pointer;
}

/* Formats the code in syntax and usage blocks, and the code in non-snippet code blocks. */
div.code pre
{
    font-family: Consolas, "Courier New", Courier, monospace;
	font-size: 105%;
	color:	#000066;
	background: #F7F7FF;
    margin-bottom: 5px;
}

/* Formats parameter tooltips. */
.tip
{
	color:	#0000FF;
	font-style: italic;
	cursor: pointer;
	text-decoration:underline;
}

/* Applies to text styled as math. This text is passed as a parameter to the italics SSC definition */
.math
{
	font-family: Times New Roman;
	font-size: 125%
}

/* The sourceCodeList class doesn't appear in the transforms.
   TODO: Find out whether this style is needed for the doc spec. */
/*
.sourceCodeList
{
	font-family: Verdana;
	font-size: 90%;
}
*/

/* The viewCode class doesn't appear in the transforms.
   TODO: Find out whether this style is needed for the doc spec. */
/*
pre.viewCode
{
	width: 100%;
	overflow: auto;
}
*/

/* Dropdown areas */

#devlangsMenu {
	position: absolute;
	visibility: hidden;
	border-style: solid;
	border-width: 1px;
	border-color: #f3cbb5;
	background: #FCECE4;
	padding-top: 4px;
	padding-bottom: 4px;
	padding-left: 4px;
	padding-right:8px;
	font-size: 70%;
}

div.OH_outerContent #devlangsMenu {
	font-size: 91%;
}

#memberOptionsMenu {
	position: absolute;
	visibility: hidden;
	border-style: solid;
	border-width: 1px;
	border-color: #f3cbb5;
	background: #FCECE4;
	padding-top: 4px;
	padding-bottom: 4px;
	padding-left: 4px;
	padding-right:8px;
	font-size: 70%;
}

div.OH_outerContent #memberOptionsMenu {
	font-size: 91%;
}

#memberFrameworksMenu {
	position: absolute;
	visibility: hidden;
	border-style: solid;
	border-width: 1px;
	border-color: #f3cbb5;
	background: #FCECE4;
	padding-top: 4px;
	padding-bottom: 4px;
	padding-left: 4px;
	padding-right:8px;
	font-size: 70%;
}

div.OH_outerContent #memberFrameworksMenu {
	font-size: 91%;
}

/* Applies to the checkbox labels in the filter drop-downs for devlang, member options, and member platforms. */
.checkboxLabel
{
	color:	#0000FF;
	cursor: pointer;
	text-decoration:underline;
	padding-bottom:4;
	font-size:90%;
}

img#devlangsDropdownImage
{
	border: 0;
	margin-left: 0;
	vertical-align: middle;
}

/* Formats the Members Options filter drop-down image. */
img#memberOptionsDropdownImage
{
	border: 0;
	margin-left: 0;
	vertical-align: middle;
}

/* Formats the Members Platforms filter drop-down image. */
img#memberFrameworksDropdownImage
{
	border: 0;
	margin-left: 0;
	vertical-align: middle;
}

/* Line seperating footer from main body */

div.footerLine {
	margin: 0;
	width: 100%;
	padding-top:	8;
	padding-bottom:	6;
	/*padding-left:	5;
	padding-right:	2;*/

}

div.hr1 {
	margin: 0;
	width: 100%;
	height: 1px;
	padding: 0;
	background: #C8CDDE;
	font-size: 1px;
}

div.hr2 {
	margin: 0;
	width: 100%;
	height: 1px;
	padding: 0;
	background: #D4DFFF;
	font-size: 1px;
}

div.hr3 {
	margin: 0;
	width: 100%;
	height: 1px;
	padding: 0;
	background: #EEEEFF;
	font-size: 1px;
}

span.cs {
	display: none;
}

span.vb {
	display: none;
}

span.cpp {
	display: none;
}

span.nu {
	display: inline;
}

span.fs
{
	display: none;
}

span.code, span.command {
    font-family: Consolas, "Courier New", Courier, monospace;
	font-size: 105%;
	color:	#000066;
}
span.literalValue
{
	color:#8B0000;
}
span.ui {
	font-weight: bold;
}
span.math {
	font-style: italic;
}
span.input {
	font-weight: bold;
}
span.term {
	font-style: italic;
}
span.label
{
	font-weight: bold;
}
q
{
	font-style: italic;
}
span.foreignPhrase, span.phrase {
	font-style: italic;
}
span.placeholder {
	font-style: italic;
}
span.keyword
{
/*	font-weight: bold;*/
}
span.typeparameter
{
	font-style:italic;
}

span.media {
	margin-left: 5px;
	margin-right: 5px;
    vertical-align: middle;
}

div.mediaNear {
	text-align: left;
	margin-top: 1em;
	margin-bottom: 1em;
}

div.mediaFar {
	text-align: right;
	margin-top: 1em;
	margin-bottom: 1em;
}

div.mediaCenter {
	text-align: center;
	margin-top: 1em;
	margin-bottom: 1em;
}

div.preliminary
{
	margin-top: 1em;
	margin-bottom: 1em;
	font-weight: bold;
	font-size: 110%;
	color: #333333;
}

div.caption
{
	margin-top: 1em;
	margin-bottom: 1em;
	font-size:100%;
	color:#003399;
}

span.captionLead
{
  font-weight: bold;
  margin-right: .5em;
}

/* syntax styles */

div.code span.identifier
{
	/*font-weight: bold;*/
}

div.code span.keyword
{
	/*color: green;*/
	color: #871F78;
}

div.code span.parameter
{
	font-style: italic;
	/*color: purple;*/
}

div.code span.literal
{
	/*color: purple;*/
	color:#8B0000;
}

div.code span.comment
{
	/*color: red;*/
	color: #006400;
}

span.syntaxLabel
{
	color:#0481DA;
	font-weight:bold;
}
span.introStyle
{
	color:DarkGray;
}

div.seeAlsoStyle
{
	padding-top:5px;

}

td.nsrBottom
{
	height: 0.6em;
	width: 100%;
}

/* end of syntax styles */

/* Glossary */
SPAN.clsGlossary {cursor: default; color: #509950; font-weight: bold;}
DIV.clsTooltip {border: 1px solid black; padding: 2px; position: absolute; top: 0; left: 0; display: none; background-color: #FFFFAA; color: black; font-size: 8pt; font-family: Arial;}

/* FB STYLES */
span.feedbackcss
{
    font-size: 110%;
    width:100%;
    margin-left: 15px;
/*
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    border-color:#C8CDDE;
*/
}

div#feedbackarea table
{
    margin-bottom:0px;
    margin-top:0px;
    margin-left: 0;
    width:300;
    border-width: 0px 0px 0px 0px;
}

div#feedbackarea table td
{
    /*background-color: #D4DFFF;*/
    font-family:Verdana;
    font-size:100%;
    text-align:center;
    /*color: #003399;*/
    border-bottom:0px;
}

div#feedbackarea p
{
    font-size:100%;
    /*background-color: #D4DFFF;*/
    width: 100%;
    margin-bottom:  0;
    margin-top:	    0;
    margin-left:    6;
    margin-right:   5;
}
div#feedbackarea H5
{
margin-top:0px;
    margin-bottom:0.7em;
	font-size:10pt;
    margin-left: 6;
}
p.feedbackarea
{
    width:expression(document.body.clientWidth-27);
    font-size:100%;
    background-color: #D4DFFF;
}

input#submitFeedback
{
    font-size:100%;
    text-align:center;
    /*background-color:#D4DFFF; */
}

span#feedbackarea
{
/*
	background-color: #D4DFFF;
	color: #003399;
   	border-color:#C8CDDE;
*/
	width:100%;
}
div#feedbackarea
{
	/*background-color: #D4DFFF;
	color: #003399;*/
	width:100%;
}
span.filterOnHover
{
 	color: #E85F17;
}
span.filter
{
	color: #0000FF;
}

/* Glossary styles */

h1.glossaryTitle
{
  color: #000000;
  font-size: 140%;
  margin-top: 10px;
  margin-bottom: 10px;
}

div.glossaryDiv
{
}

h2.glossaryDivHeading
{
  color: Black;
  font-size: 115%;
  margin-top: 1em;
  margin-bottom: 0px;
}

div.glossaryLetterBar
{
  font-size: 90%;
}

hr.glossaryRule
{
  text-align: left;
  color: Black;
}

h3.glossaryGroupHeading
{
  font-size: 120%;
  color: Gray;
  margin: 5px 0 5px 0;
}

div.glossaryGroup
{
}

dl.glossaryGroupList
{
  margin: 0;
  color: Black;
}

dt.glossaryEntry
{
  font-weight: bold;
  margin-left: 2em;
}

dd.glossaryEntry
{
  margin-left: 2em;
  margin-bottom: 2em;
}

div.relatedEntry
{
  margin-bottom: 4px;
}

/* Bibliography */
div.bibliographStyle
{
  padding-top:5px;
}

span.bibliographyNumber
{
}

span.bibliographyAuthor
{
  font-weight: bold;
}

span.bibliographyTitle
{
  font-style: italic;
}

span.bibliographyPublisher
{
}

sup.citation a:link a:visited a:active
{
  text-decoration: none;
}

/* autoOutline styles */
ul.autoOutline
{
}

li.outlineSectionEntry
{
}

div.outlineSectionEntrySummary
{
}

/* table styles */

table.members th.iconColumn {
	width: 60px;
}

table.members th.nameColumn {
	width: 33%;
}

table.members th.valueColumn {
	width: 10%;
}

table.members th.descriptionColumn {
/*	No fixed width, use whatever is left over */
}

/* These two entries were added by ComponentOne to fix MS Help Viewer 1.0 display issues */
table#bottomTable, table#bottomTable tr, table#bottomTable td,
	table#topTable, table#topTable tr, table#topTable td,
	table#gradientTable, table#gradientTable tr, table#gradientTable td,
	table#logoTable, table#logoTable tr, table#logoTable td
{
	border: 0 none;
}

body
{
	overflow: auto;
}

## File: styles/Whidbey/Presentation.css

/* * * This file was autogenerated by Styler at 02:02 on 02/15/2003 * * */

/***********************************************************
 *             SCRIPT-SUPPORTING STYLES
 ***********************************************************/

/* Defines the userData cache persistence mechanism. */
.userDataStyle
{
	behavior: url(#default#userdata);
}

/* Used to save the scroll bar position when navigating away from a page. */
div.saveHistory
{
	behavior: url(#default#savehistory);
}

/* Formats the expand/collapse images for all collapsible regions. */
img.toggle
{
	border: 0;
	margin-right: 5;
}

/* Formats the Collapse All/Expand All images. */
img#toggleAllImage
{
	margin-left: 0;
	vertical-align: middle;
}

/* Supports XLinks */
MSHelp\:link
{
 	text-decoration: underline;
	color: #0000ff;
	hoverColor: #3366ff;
	filterString: ;
}

/***********************************************************
 *             CONTENT PRESENTATION STYLES
 ***********************************************************/

body
{
	background:	#FFFFFF;
	color: #000000;
	font-family:	Verdana;
	font-size: medium;
	font-style: normal;
	font-weight: normal;
	margin-top:	0;
	margin-bottom:	0;
	margin-left:	0;
	margin-right:	0;
	width:	100%;
}

dl
{
	margin-top:	15;
	margin-bottom:5;
	padding-left:	1;
}

dl.authored dt {
	font-style:	bold;
}

dl.authored dd {
	margin-left: 20px;
    margin-bottom: 5px;
}

dd {
	margin-left:	0;
}

ul
{
	margin-top:0;
	margin-bottom:0;
	margin-left: 17;
	list-style-type: disc;
}

ul ul
{
	margin-bottom: 4;
	margin-left: 17;
	margin-top: 3;
	list-style-type: disc;
}

ol {
	margin-top:0;
	margin-bottom:0;
	margin-left: 28;
	list-style-type: decimal;
}

ol ol {
	margin-bottom: 4;
	margin-left: 28;
	margin-top: 3;
	list-style-type: lower-alpha;
}

li {
	margin-top: 5;
	margin-bottom: 5;
}

ul.nobullet
{
    list-style-type: none;
}

p {
	margin-top: 10;
	margin-bottom: 5;
}

a:link {
	color:	#0000FF;
}

a:visited {
	color:	#0000FF;
}

a:hover {
	color: #DD7C3B;
}

div#header a, div#mainSectionMHS a {
    text-decoration: underline;
}

code
{
	font-family:	Monospace, Courier New, Courier;
	font-size: 105%;
	color:	#000066;
}

span.parameter {
	font-style: italic;
	font-weight:bold;
}

span.italic {
	font-style: italic;
}

span.selflink {
	font-weight: bold;
}

span.nolink {

}

/***********************************************************
 *             STRUCTURE PRESENTATION STYLES
 ***********************************************************/

/* Applies to everything below the non-scrolling header region. */
div#mainSection
{
	font-size: 62.5%;
	width: 100%;
}
div#mainSectionMHS
{
    font-family: Verdana;
	font-size: 81%;
	width: 100%;
}
html>body #mainSection, html>body #mainSectionMHS
{
	font-size: 73%;
	width: 100%;
}

/* Applies to everything below the non-scrolling header region, minus the footer. */
div#mainBody
{
	font-size: 100%;
	margin-left: 15;
	margin-top: 10;
	padding-bottom: 20;
}

html>body #mainBody
{
	font-size: 93%;
	margin-left: 15;
	margin-top: 10;
	padding-bottom: 20;
}

/* Adds right padding for all blocks in mainBody */
div#mainBody p, div#mainBody ol, div#mainBody ul, div#mainBody dl
{
	padding-right: 5;
}

/*------------------------------ Begin Non-scrolling Header Region Styles -------------------------------*/
/* Applies to the entire non-scrolling header region. */
div#header
{
	background-color: #D4DFFF;
	padding-top:	0;
	padding-bottom:	0;
	padding-left:	0;
	padding-right:	0;
	width:	100%;
}

/* Applies to both tables in the non-scrolling header region. */
div#header table
{
	border-bottom-color: #C8CDDE;
	border-bottom-style: solid;
	border-bottom-width: 1;
	width:	100%;
}

/* Applies to cells in both tables in the non-scrolling header region. */
div#header table td
{
	color: #0000FF;
	font-size: 70%;
	margin-top:	0;
	margin-bottom:	0;
	padding-right: 20;
}
/* Applies to second row in the upper table of the non-scrolling header region. */
div#header table tr#headerTableRow2 td
{
	padding-left: 13px;
}

/* Applies to the last row in the upper table of the non-scrolling header region. Text
   in this row includes See Also, Constructors, Methods, and Properties. */
div#header table tr#headerTableRow3 td
{
	padding-bottom: 2;
	padding-top: 5;
	padding-left: 15;
}

/* Applies to the lower table in the non-scrolling header region. Text in this table
   includes Collapse All/Expand All, Language Filter, and Members Options. */
div#header table#bottomTable
{
	border-top-color: #FFFFFF;
	border-top-style: solid;
	border-top-width: 1;
	text-align: left;
	padding-left: 15;
}

/* Formats the first column--the one that displays icons--in mref list tables (such as Public Constructors,
   Protected Constructors, Public Properties, Protected Properties, and so on). */
div#mainSection table td.imageCell, div#mainSectionMHS table td.imageCell
{
	white-space: nowrap;
}
/*------------------------------ End General Table Styles -------------------------------*/

/*------------------------------ Begin General Table Styles -------------------------------*/

div#mainBody div.alert, div#mainBody div.code, div#mainBody div.tableSection
{
	width:98.9%;
}

div#mainBody div.section div.alert, div#mainBody div.section div.code,
div#mainBody div.section div.tableSection
{
	width:100%;
}

div#mainBody div.section ul div.alert, div#mainBody div.section ul div.code,
div#mainBody div.section ul div.tableSection, div#mainBody div.section ol div.alert,
div#mainBody div.section ol div.code, div#mainBody div.section ol div.tableSection
{
	width:100%;
}

div.alert p, div.code p
{
	margin-top:5;
	margin-bottom:8;
}
dd p
{
	margin-top:2;
	margin-bottom:8;
}
div.tableSection p
{
	margin-top:1;
	margin-bottom:4;
}
li p
{
	margin-top:2;
	margin-bottom:2;
}
div.seeAlsoNoToggleSection dl
{
	margin-top:8;
	margin-bottom:1;
	padding-left:1;
}
div.seeAlsoNoToggleSection dd p
{
	margin-top:2;
	margin-bottom:8;
}
div.section dl
{
	margin-top:8;
	margin-bottom:1;
	padding-left:1;
}
div.section dd p
{
	margin-top:2;
	margin-bottom:8;
}
/*------------------------------ End General Table Styles -------------------------------*/

/*------------------------------ Begin Non-scrolling Header Region Styles -------------------------------*/

/* Applies to the running header text in the first row of the upper table in the
   non-scrolling header region. */
span#runningHeaderText
{
	color: #003399;
	font-size: 90%;
	padding-left: 13;
}

/* Applies to the topic title in the second row of the upper table in the
   non-scrolling header region. */
span#nsrTitle
{
	color: #003399;
	font-size: 120%;
	font-weight: 600;
}
/*------------------------------ End Non-scrolling Header Region Styles -------------------------------*/

/* Formats the footer. Currently, the transforms pass in two parameters to the
   footer SSC, but the default footer SSC doesn't use either parameter.
   TODO: Investigate whether the default footer SSC has any impact on doc spec. */
div#footer
{
	font-size: 80%;
	margin-top:	0;
	margin-bottom:	0;
	margin-left:	0;
	margin-right:	0;
	padding-top:	8;
	padding-bottom:	6;
	padding-left:	5;
	padding-right:	2;
	width:	100%;
}

html>body div#footer
{
	font-size: 80%;
	margin-top:	0;
	margin-bottom:	0;
	margin-left:	0;
	margin-right:	0;
	padding-top:	2;
	padding-bottom:	6;
	padding-left:	5;
	padding-right:	2;
	width:	98%;
}

/* Unable to find this style in the transforms. The default footer SSC adds a plain horizontal rule.
   TODO: Determine whether this style is required by the doc spec. */
/*
hr#footerHR
{
	border-bottom-color: #EEEEFF;
	border-bottom-style: solid;
	border-bottom-width: 1;
	border-top-color: C8CDDE;
	border-top-style: solid;
	border-top-width: 1;
	height: 3;
	color: #D4DFFF;
}
*/

/********************************************************************************************************************
	Collapsible Section Structure

	<h1 class="heading">							// Format of the collapsible section text
		<span onclick="ExpandCollapse(xxxToggle)">	// Defines the onclick procedure for the expand/collapse section
			<img id="xxxToggle">					// Expand/collapse image
			</img>
		</span>
	</h1>

	<div id="xxxSection" class="section">			// The body of the collapsible section; hidden by default
	</div>

	The ExpandCollapse() function is responsible for toggling the expand/collapse image, and for
	displaying/hiding the body of the collapsible section.
********************************************************************************************************************/

/* Applies to the body of a collapsible section */
div.seeAlsoNoToggleSection
{
	margin-left:0;
	padding-top:	2;
	padding-bottom:	2;
	padding-left:	0;
	padding-right:	15;
	width:	100%;
}

div.section
{
	margin-left:0;
	padding-top:	0;
	padding-bottom:	0;
	padding-left:	16;
	padding-right:	15;
	width:	100%;
}
html>body div.section
{
	margin-left:0;
	padding-top:	2;
	padding-bottom:	2;
	padding-left:	16;
	padding-right:	15;
	width:	97%;
}
div.seeSection
{
	margin-left:0;
	padding-top:	0;
	padding-bottom:	2;
	padding-left:	16;
	padding-right:	15;
	width:	100%;
}

div.section p
{
	margin-top: 0 px;
	margin-bottom: 0px;
}

/*------------------------------ Begin Heading Styles -------------------------------*/
/* As far as I can tell, only <h1> tags use this class.
   TODO: Decide whether to roll these attributes into the h1.heading style */
.heading
{
	font-weight:	bold;
	margin-top:		18;
	margin-bottom:	8;
}

/* All <h1> headings. */
h1.heading
{
	color: #003399;
	font-size:	130%;
}

/* Applies to table titles and subsection titles. */
.subHeading
{
	font-weight:	bold;
	margin-bottom:	4;
}
.procedureSubHeading
{
	font-weight: bold;
	margin-bottom: 4;
}

/* Formats the titles of author-generated tables. */
h3.subHeading
{
	color:  #000000;
	font-size: 120%;
    font-weight:800;
}

h3.procedureSubHeading
{
	color: #003399;
	font-size: 120%;
}

/* Formats the titles of all subsections. */
h4.subHeading
{
	color: #000000;
	font-size: 110%;
	font-weight:800;
}
span.labelheading, div.labelheading
{
	font-size:100%;
	color:#003399;
}

/*------------------------------ End Heading Styles -------------------------------*/

/*------------------------------ Begin Image Styles -------------------------------*/
img.copyCodeImage
{
	border: 0;
	margin: 1;
	margin-right: 3;
}

img.downloadCodeImage
{
	border: 0;
	margin-right: 3;
}

img.viewCodeImage
{
	border: 0;
	margin-right: 3;
}

img.note
{
	border: 0;
	margin-right: 3;
}
/*------------------------------ End Image Styles -------------------------------*/

/*------------------------------ Begin General Table Styles -------------------------------*/
div#mainSection table, div#mainSectionMHS table
{
	border: 0;
	font-size: 100%;
	width:	98.9%;
	margin-top: 5px;
	margin-bottom: 5px;
}

div#mainSection table tr, div#mainSectionMHS table tr
{
	vertical-align: top;
}

div#mainSection table th, div#mainSectionMHS table th
{
	background-color: #EFEFF7;
	border-bottom: 1px solid #C8CDDE;
	border-left: 1px none #D5D5D3;
	color: #000066;
	padding-left: 5px;
	padding-right: 5px;
	text-align: left;
}

div#mainSection table td, div#mainSectionMHS table td
{
	background-color: #F7F7FF;
	border-bottom: 1px solid #D5D5D3;
	border-left: 1px none #D5D5D3;
	padding-left: 5px;
	padding-right: 5px;
}

/* Formats the first column--the one that displays icons--in mref list tables (such as Public Constructors,
   Protected Constructors, Public Properties, Protected Properties, and so on). */
div#mainSection table td.imageCell, div#mainSectionMHS table td.imageCell
{
	white-space: nowrap;
}
/*------------------------------ End General Table Styles -------------------------------*/

/*------------------------------ Begin Syntax and Snipper Code Block Styles -------------------------------*/

div.code table
{
	border: 0;
	font-size: 95%;
	margin-bottom: 5px;
	width: 100%
}

div.code table th
{
	background:	#EFEFF7;
	border-bottom-color: #C8CDDE;
	border-bottom-style: solid;
	border-bottom-width: 1px;
	color: #000066;
	font-weight: bold;
	padding-left: 5px;
	padding-right: 5px;
	padding-top: 2px;
	padding-bottom: 2px;
	vertical-align: middle;
}

div.code table td
{
	background:	#F7F7FF;
	border-top-color: #FFFFFF;
	border-top-style: solid;
	border-top-width: 1px;
	padding-left: 5px;
	padding-right: 5px;
	padding-top: 5px;
}
/*------------------------------ End Syntax and Snipper Code Block Styles -------------------------------*/

/*------------------------------ Begin Note Styles -------------------------------*/
div.alert table
{
	border: 0;
	font-size: 100%;
	width:	100%;
}

div.alert table th
{
	background:	#EFEFF7;
	border-bottom-width: 0;
	color: #000066;
	padding-left: 5;
	padding-right: 5;
}

div.alert table td
{
	background:	#F7F7FF;
	border-top-color: #FFFFFF;
	border-top-style: solid;
	border-top-width: 1;
	padding-left: 5;
	padding-right: 5;
}

/*------------------------------ End Note Styles -------------------------------*/

/* Applies to the copy code text and image. */
span.copyCode
{
	color: #0000ff;
	font-size: 90%;
	font-weight: normal;
	cursor: pointer;
	float: right;
	display: inline;
	text-align: right;
}

span.copyCodeOnHover
{
	color: #E85F17;
	font-size:xx-small;
	font-weight: normal;
	cursor: pointer;
	float: right;
	display: inline;
	text-align: right;
	text-decoration: underline;
}

.downloadCode
{
	color: #0000ff;
	font-size: 90%;
	font-weight: normal;
	cursor: pointer;
}

.viewCode
{
	color: #0000ff;
	font-size: 90%;
	font-weight: normal;
	cursor: pointer;
}

/* Formats the code in syntax and usage blocks, and the code in non-snippet code blocks. */
div.code pre
{
	font-family:	Monospace, Courier New, Courier;
	font-size: 105%;
	color:	#000066;
	background: #F7F7FF;
}

/* Formats parameter tooltips. */
.tip
{
	color:	#0000FF;
	font-style: italic;
	cursor: pointer;
	text-decoration:underline;
}

/* Applies to text styled as math. This text is passed as a parameter to the italics SSC definition */
.math
{
	font-family: Times New Roman;
	font-size: 125%
}

/* The sourceCodeList class doesn't appear in the transforms.
   TODO: Find out whether this style is needed for the doc spec. */
/*
.sourceCodeList
{
	font-family: Verdana;
	font-size: 90%;
}
*/

/* The viewCode class doesn't appear in the transforms.
   TODO: Find out whether this style is needed for the doc spec. */
/*
pre.viewCode
{
	width: 100%;
	overflow: auto;
}
*/

/* Dropdown areas */

#devlangsMenu {
	position: absolute;
	visibility: hidden;
	border-style: solid;
	border-width: 1px;
	border-color: #C8CDDE;
	background: #d4dfff;
	padding: 4px;
	font-size: 70%;
}

div.OH_outerContent #devlangsMenu {
	font-size: 91%;
}

#memberOptionsMenu {
	position: absolute;
	visibility: hidden;
	border-style: solid;
	border-width: 1px;
	border-color: #C8CDDE;
	background: #d4dfff;
	padding: 4px;
	font-size: 70%;
}

div.OH_outerContent #memberOptionsMenu {
	font-size: 91%;
}

#memberFrameworksMenu {
	position: absolute;
	visibility: hidden;
	border-style: solid;
	border-width: 1px;
	border-color: #C8CDDE;
	background: #d4dfff;
	padding: 4px;
	font-size: 70%;
}

div.OH_outerContent #memberFrameworksMenu {
	font-size: 91%;
}

/* Applies to the checkbox labels in the filter drop-downs for devlang, member options, and member platforms. */
.checkboxLabel
{
	color:	#0000FF;
	cursor: pointer;
	text-decoration:underline;
	padding-bottom:4;
}

img#devlangsDropdownImage
{
	border: 0;
	margin-left: 0;
	vertical-align: middle;
}

/* Formats the Members Options filter drop-down image. */
img#memberOptionsDropdownImage
{
	border: 0;
	margin-left: 0;
	vertical-align: middle;
}

/* Formats the Members Platforms filter drop-down image. */
img#memberFrameworksDropdownImage
{
	border: 0;
	margin-left: 0;
	vertical-align: middle;
}

/* Line seperating footer from main body */

div.footerLine {
	margin: 0;
	width: 100%;
	padding-top:	8;
	padding-bottom:	6;
	padding-left:	5;
	padding-right:	2;

}

div.hr1 {
	margin: 0;
	width: 100%;
	height: 1px;
	padding: 0;
	background: #C8CDDE;
	font-size: 1px;
}

div.hr2 {
	margin: 0;
	width: 100%;
	height: 1px;
	padding: 0;
	background: #D4DFFF;
	font-size: 1px;
}

div.hr3 {
	margin: 0;
	width: 100%;
	height: 1px;
	padding: 0;
	background: #EEEEFF;
	font-size: 1px;
}

span.cs {
	display: none;
}

span.vb {
	display: none;
}

span.cpp {
	display: none;
}

span.nu {
	display: inline;
}

span.fs
{
	display: none;
}

span.code, span.command {
	font-family:	Monospace, Courier New, Courier;
	font-size: 105%;
	color:	#000066;
}
span.literalValue
{
	color:#8B0000;
}
span.ui {
	font-weight: bold;
}
span.math {
	font-style: italic;
}
span.input {
	font-weight: bold;
}
span.term {
	font-style: italic;
}
span.label
{
	font-weight: bold;
}
q
{
	font-style: italic;
}
span.foreignPhrase, span.phrase {
	font-style: italic;
}
span.placeholder {
	font-style: italic;
}
span.keyword
{
	font-weight: bold;
}
span.typeparameter
{
	font-style:italic;
}

span.media {
	margin-left: 5px;
	margin-right: 5px;
    vertical-align: middle;
}

div.mediaNear {
	text-align: left;
	margin-top: 1em;
	margin-bottom: 1em;
}

div.mediaFar {
	text-align: right;
	margin-top: 1em;
	margin-bottom: 1em;
}

div.mediaCenter {
	text-align: center;
	margin-top: 1em;
	margin-bottom: 1em;
}

div.preliminary
{
	margin-top: 1em;
	margin-bottom: 1em;
	font-weight: bold;
	font-size: 110%;
	color: #333333;
}

div.caption
{
	font-weight: bold;
	font-size:100%;
	color:#003399;
}

span.captionLead
{
  font-weight: bold;
  margin-right: .5em;
}

/* syntax styles */

div.code span.identifier
{
	font-weight: bold;
}

div.code span.keyword
{
	color: green;
}

div.code span.parameter
{
	font-style: italic;
	color: purple;
}

div.code span.literal
{
	color: purple;
}

div.code span.comment
{
	color: red;
}

span.syntaxLabel
{
	color:#0481DA;
	font-weight:bold;
}
span.introStyle
{
	color:DarkGray;
}

div.seeAlsoStyle
{
	padding-top:5px;

}

td.nsrBottom
{
	height: 0.6em;
	width: 100%;
}

/* end of syntax styles */

/* Glossary */
SPAN.clsGlossary {cursor: default; color: #509950; font-weight: bold;}
DIV.clsTooltip {border: 1px solid black; padding: 2px; position: absolute; top: 0; left: 0; display: none; background-color: #FFFFAA; color: black; font-size: 8pt; font-family: Arial;}

/* FB STYLES */
span.feedbackcss
{
    width:100%;
    margin-left: 5px;
/*
    border-width: 1px 1px 1px 1px;
    border-style: solid;
    border-color:#C8CDDE;
*/
}

div#feedbackarea table
{
    margin-bottom:0px;
    margin-top:0px;
    margin-left: 0;
    width:300;
    border-width: 0px 0px 0px 0px;
}

div#feedbackarea table td
{
    background-color: #D4DFFF;
    font-family:Verdana;
    font-size:100%;
    text-align:center;
    color: #003399;
    border-bottom:0px;
}

div#feedbackarea p
{
    font-size:100%;
    background-color: #D4DFFF;
    width: 100%;
    margin-bottom:  0;
    margin-top:	    0;
    margin-left:    6;
    margin-right:   5;
}
div#feedbackarea H5
{
    margin-bottom:0.7em;
    margin-left: 6;
}
p.feedbackarea
{
    width:expression(document.body.clientWidth-27);
    font-size:100%;
    background-color: #D4DFFF;
}

input#submitFeedback
{
    font-size:105%;
    text-align:center;
    background-color:#D4DFFF;
}

span#feedbackarea
{
/*
	background-color: #D4DFFF;
	color: #003399;
   	border-color:#C8CDDE;
*/
	width:100%;
}
div#feedbackarea
{
 background-color: #D4DFFF;
 color: #003399;
 width:100%;
}
span.filterOnHover
{
 	color: #E85F17;
}
span.filter
{
	color: #0000FF;
}

/* Glossary styles */

h1.glossaryTitle
{
  color: #000000;
  font-size: 140%;
  margin-top: 10px;
  margin-bottom: 10px;
}

div.glossaryDiv
{
}

h2.glossaryDivHeading
{
  color: Black;
  font-size: 115%;
  margin-top: 1em;
  margin-bottom: 0px;
}

div.glossaryLetterBar
{
  font-size: 90%;
}

hr.glossaryRule
{
  text-align: left;
  color: Black;
}

h3.glossaryGroupHeading
{
  font-size: 120%;
  color: Gray;
  margin: 5px 0 5px 0;
}

div.glossaryGroup
{
}

dl.glossaryGroupList
{
  margin: 0;
  color: Black;
}

dt.glossaryEntry
{
  font-weight: bold;
  margin-left: 2em;
}

dd.glossaryEntry
{
  margin-left: 2em;
  margin-bottom: 2em;
}

div.relatedEntry
{
  margin-bottom: 4px;
}

/* Bibliography */
div.bibliographStyle
{
  padding-top:5px;
}

span.bibliographyNumber
{
}

span.bibliographyAuthor
{
  font-weight: bold;
}

span.bibliographyTitle
{
  font-style: italic;
}

span.bibliographyPublisher
{
}

sup.citation a:link a:visited a:active
{
  text-decoration: none;
}

/* autoOutline styles */
ul.autoOutline
{
}

li.outlineSectionEntry
{
}

div.outlineSectionEntrySummary
{
}

/* table styles */

table.members th.iconColumn {
	width: 60px;
}

table.members th.nameColumn {
	width: 33%;
}

table.members th.valueColumn {
	width: 10%;
}

table.members th.descriptionColumn {
/*	No fixed width, use whatever is left over */
}