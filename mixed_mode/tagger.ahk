Sleep, 1000


Loop, 3
{
	Folder = F1
	Qindex := A_index+0
	Question = Q%Qindex%
	Send, {Tab}{Tab}{Tab}{Tab}{Tab}
	Send, {Enter}
	Sleep, 500
	Send, {Home}
    Send, %Folder%%Question%
	SendEvent, {Space}
	Sleep, 1000
	Send, {Shift Down}{Tab}{Tab}{Shift Up}
	Send, {Enter}		
	Sleep, 5000
	Send, {Tab}{Enter}
	Sleep, 3000
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