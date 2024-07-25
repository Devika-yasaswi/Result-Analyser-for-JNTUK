from cx_Freeze import setup, Executable
import sys
sys.setrecursionlimit(5000)
base = None
 
build_exe_options={"include_files":["CGPA.py","Revaluation.py","regular_SGPA.py","Statistics.py","User_guide.py","JNTUK logo.png","Background.png"]}
target = Executable(
    script="GPA_interface.py",
    base="Win32GUI",
    icon="JNTUK logo.ico"
    )
setup(
    name="GPA calculator",
    description="Calculates the SGPA and CGPA of a class",
    author="Devika yasaswi kambala",
    options={"build_exe":build_exe_options},
    executables=[target]
)