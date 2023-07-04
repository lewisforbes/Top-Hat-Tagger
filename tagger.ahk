; this script has been tested in Chrome
; it relies on your pc being fast - close all apps/tabs apart from tophat

; to use, run the script then (within 3 seconds) click on the first question in the folder.
Sleep, 3000
Loop, 5
{
	Prefix = F1
	Qindex := A_index+0
	Suffix = Q%Qindex%
	Send, {Tab}{Tab}{Tab}{Tab}{Tab}
	Send, {Enter}
	Sleep, 500
	Send, {Home}
    Send, %Prefix%%Suffix%
	SendEvent, {Space}
	Sleep, 1000
	Send, {Shift Down}{Tab}{Tab}{Shift Up}
	Send, {Enter}		
	Sleep, 6000
	Send, {Tab}{Enter}
	Sleep, 200
	Send, {Tab}{Tab}{Tab}{Tab}
	Send, {Down}{Enter}
	Sleep, 1000
}
Send, {Down}
Sleep, 200
Send, {Enter}
Sleep, 1000
Loop, 10
{
	Prefix = F2
	Qindex := A_index+0
	Suffix = Q%Qindex%
	Send, {Tab}{Tab}{Tab}{Tab}{Tab}
	Send, {Enter}
	Sleep, 500
	Send, {Home}
    Send, %Prefix%%Suffix%
	SendEvent, {Space}
	Sleep, 1000
	Send, {Shift Down}{Tab}{Tab}{Shift Up}
	Send, {Enter}		
	Sleep, 6000
	Send, {Tab}{Enter}
	Sleep, 200
	Send, {Tab}{Tab}{Tab}{Tab}
	Send, {Down}{Enter}
	Sleep, 1000
}
Send, {Down}
Sleep, 200
Send, {Enter}
Sleep, 1000


ExitApp

Esc::ExitApp