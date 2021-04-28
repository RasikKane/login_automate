@echo off 

:: unhide and unread-only the login_site.py
attrib -h -r login_site.py				

:: delete previous exe
IF EXIST login_site.exe (
    del login_site.exe
)

:: launch conda python environment
call conda activate webcrawl

:: make executable using login_site.py
call pyinstaller --onefile --windowed login_site.py 	

:: close conda python environment
call conda deactivate

:: move executable created inside .\dist directory in parent folder
move .\dist\*.* .\					

:: remove created system folders
rmdir /S /Q .\build, .\dist, .\__pycache__		

:: remove created spec files	
del /S /Q *.spec					

:: if necessary, hide and read-only the login_site.py
:: attrib +h +r login_site.py				