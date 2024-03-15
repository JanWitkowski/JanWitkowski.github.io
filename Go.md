# History of Go
Go was designed atGooglein 2007 to improveprogramming productivityin an era ofmulticore,networkedmachinesand largecodebases.[22]The designers wanted to address criticisms of other languages in use at Google, but keep their useful characteristics:[23]
Its designers were primarily motivated by their shareddislike of C++.[25][26][27]
Go was publicly announced in November 2009,[28]and version 1.0 was released in March 2012.[29][30]Go is widely used in production at Google[31]and in many other organizations and open-source projects.
## Branding and styling[edit]
TheGophermascotwas introduced in 2009 for theopen sourcelaunch of the language.  The design, byRenée French, borrowed from a c. 2000WFMUpromotion.[32]
In November 2016, the Go and Go Mono fonts were released by type designersCharles BigelowandKris Holmesspecifically for use by the Go project. Go is ahumanist sans-serifresemblingLucida Grande, and Go Mono ismonospaced. Both fonts adhere to theWGL4character set and were designed to be legible with a largex-heightand distinctletterforms. Both Go and Go Mono adhere to theDIN1450 standard by having a slashed zero, lowercaselwith a tail, and an uppercaseIwith serifs.[33][34]
In April 2018, the original logo was redesigned by brand designerAdam Smith. The new logo is a modern, stylized GO slanting right with trailing streamlines. (The Gopher mascot remained the same.[35])
## Generics[edit]
The lack of support forgeneric programmingin initial versions of Go drew considerable criticism.[36]The designers expressed an openness to generic programming and noted that built-in functionswerein fact type-generic, but are treated as special cases; Pike called this a weakness that might be changed at some point.[37]The Google team built at least one compiler for an experimental Go dialect with generics, but did not release it.[38]
In August 2018, the Go principal contributors published draft designs for generic programming anderror handlingand asked users to submit feedback.[39][40]However, the error handling proposal was eventually abandoned.[41]
In June 2020, a new draft design document[42]was published that would add the necessary syntax to Go for declaring generic functions and types. A code translation tool,go2go, was provided to allow users to try the new syntax, along with a generics-enabled version of the online Go Playground.[43]
Generics were finally added to Go in version 1.18.[44]
## Versioning[edit]
Go 1 guarantees compatibility[45]for the language specification and major parts of the standard library. All versions up to the current Go 1.21 release[46]have maintained this promise.
Each major Go release is supported until there are two newer major releases.[47]
