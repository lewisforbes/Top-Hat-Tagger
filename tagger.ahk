; this script has been tested in Chrome
; it relies on your pc being fast - close all apps/tabs apart from tophat

; to use, run the script then (within 3 seconds) click on the first question in the folder.
Sleep, 3000
Loop, 10
{
	Prefix = F2S3
	Qindex := A_index+3
	Suffix = Q%Qindex%
	Send, {Tab}{Tab}{Tab}{Tab}{Tab}{Tab}
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
	Sleep, 1000
	Send, {Tab}{Tab}{Tab}{Tab}
	Send, {Down}{Enter}
	Sleep, 1000
}
Send, {Down}
Sleep, 200
Send, {Enter}
Sleep, 1000
Loop, 8
{
	Prefix = F2S4
	Qindex := A_index+3
	Suffix = Q%Qindex%
	Send, {Tab}{Tab}{Tab}{Tab}{Tab}{Tab}
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
	Sleep, 1000
	Send, {Tab}{Tab}{Tab}{Tab}
	Send, {Down}{Enter}
	Sleep, 1000
}
Send, {Down}
Sleep, 200
Send, {Enter}
Sleep, 1000
Loop, 2
{
	Prefix = F2S5
	Qindex := A_index+3
	Suffix = Q%Qindex%
	Send, {Tab}{Tab}{Tab}{Tab}{Tab}{Tab}
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
	Sleep, 1000
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