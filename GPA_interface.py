from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk
import PIL
from pyautogui import alert
import pymsgbox
import tabula
from regular_SGPA import *
from Revaluation import *
from CGPA import *
from Statistics import *
from User_guide import *
from branch_wise_analysis import *
import os
import sys
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

master=Tk()
master.geometry("1250x900+300+0")
master.configure(bg="#1E90FF")
master.title("CGPA/SGPA Calculator")
img=PhotoImage(file=resource_path("Background.png"))
logo=PIL.Image.open(resource_path("JNTUK logo.png"))
new_logo=logo.resize((100,100))
new_logo=ImageTk.PhotoImage(new_logo)
my_canvas=Canvas(master,width=1000,height=1000)
my_canvas.pack(fill='both',expand=True)
my_canvas.create_image(0,0,image=img,anchor="nw")
my_canvas.create_image(20,20,image=new_logo,anchor="nw")
my_canvas.create_text(110,20,text="University College of Engineering Narasaraopet",anchor="nw",font=('Algerian',25),fill="Black")
my_canvas.create_text(150,60,text="Jawaharlal Nehru Technological University Kakinada",anchor="nw",font=('Algerian',20),fill="Black")
my_canvas.create_text(1100,850,text="K. Devika Yasaswi",font=("Vladimir Script",18))
root=Frame(my_canvas,padx=20,pady=20,bg="#FFE9E3")
root.pack(pady=110)
input_file=''
GPA_file=''
input_file_excel=''
Label_font=('Times new Roman',18)   #Font style for labels
Entry_font=('Times new Roman',15)   #Font style for entry boxes
pdf_type = [("pdf Files",'.*pdf')]
excel_type=[("xlsx Files",".*xlsx")]
s_temp=0
status1=0
#Sem selection variables
sem1=IntVar()
sem2=IntVar()
sem3=IntVar()
sem4=IntVar()
sem5=IntVar()
sem6=IntVar()
sem7=IntVar()
sem8=IntVar()

#File Paths
sem1_file=""
sem2_file=""
sem3_file=""
sem4_file=""
sem5_file=""
sem6_file=""
sem7_file=""
sem8_file=""

#File reading function for SGPA-Regular
def input_marks_file():
    global input_file
    input_file=askopenfilename(filetypes=pdf_type)

#File reading function for SGPA-supple/Revaluation
def GPA_file_func():
    global GPA_file
    GPA_file=askopenfilename(filetypes=excel_type)

#File reading function for SGPA-Regular
def input_marks_excel():
    global input_file_excel
    input_file_excel=askopenfilename(filetypes=excel_type)

def variable_sem_files():
    global sem_label_list,sem_button_list
    sem_selection=[sem1.get(),sem2.get(),sem3.get(),sem4.get(),sem5.get(),sem6.get(),sem7.get(),sem8.get()]
    if 1 in sem_selection:        
        try:
            for i in range(len(sem_selection)):
                if sem_selection[i]==0:                    
                    sem_label_list[i].grid_forget()
                    sem_button_list[i].grid_forget()
        except:
            pass
        upload_sem_files()

#Semester selection check boxes   
sem_select_label=Label(root,text="Choose Semesters for CGPA",font=Label_font,bg="#FFE9E3")
sem1_cbutton=Checkbutton(root,text="Sem 1",font=Entry_font,variable=sem1,bg="#FFE9E3",command=variable_sem_files)
sem2_cbutton=Checkbutton(root,text="Sem 2",font=Entry_font,variable=sem2,bg="#FFE9E3",command=variable_sem_files)
sem3_cbutton=Checkbutton(root,text="Sem 3",font=Entry_font,variable=sem3,bg="#FFE9E3",command=variable_sem_files)
sem4_cbutton=Checkbutton(root,text="Sem 4",font=Entry_font,variable=sem4,bg="#FFE9E3",command=variable_sem_files)
sem5_cbutton=Checkbutton(root,text="Sem 5",font=Entry_font,variable=sem5,bg="#FFE9E3",command=variable_sem_files)
sem6_cbutton=Checkbutton(root,text="Sem 6",font=Entry_font,variable=sem6,bg="#FFE9E3",command=variable_sem_files)
sem7_cbutton=Checkbutton(root,text="Sem 7",font=Entry_font,variable=sem7,bg="#FFE9E3",command=variable_sem_files)
sem8_cbutton=Checkbutton(root,text="Sem 8",font=Entry_font,variable=sem8,bg="#FFE9E3",command=variable_sem_files)

def semester_selection():
    global sem_select_label,sem1_cbutton,sem2_cbutton,sem3_cbutton,sem4_cbutton,sem5_cbutton,sem6_cbutton,sem7_cbutton,sem8_cbutton,sem
    sem_select_label.grid(row=4,column=0,sticky='w')
    sem1_cbutton.grid(row=4,column=2,sticky='w')    
    sem2_cbutton.grid(row=4,column=3,sticky='w')    
    sem3_cbutton.grid(row=5,column=2,sticky='w')    
    sem4_cbutton.grid(row=5,column=3,sticky='w')    
    sem5_cbutton.grid(row=6,column=2,sticky='w')    
    sem6_cbutton.grid(row=6,column=3,sticky='w')
    sem7_cbutton.grid(row=7,column=2,sticky='w')
    sem8_cbutton.grid(row=7,column=3,sticky='w')
#Sem SGPA file upload functions for CGPA calculation
def sem1_file_function():
    global sem1_file    
    sem1_file=askopenfilename(filetypes=excel_type)
def sem2_file_function():
    global sem2_file
    sem2_file=askopenfilename(filetypes=excel_type)
def sem3_file_function():
    global sem3_file
    sem3_file=askopenfilename(filetypes=excel_type)
def sem4_file_function():
    global sem4_file
    sem4_file=askopenfilename(filetypes=excel_type)
def sem5_file_function():
    global sem5_file
    sem5_file=askopenfilename(filetypes=excel_type)
def sem6_file_function():
    global sem6_file
    sem6_file=askopenfilename(filetypes=excel_type)
def sem7_file_function():
    global sem7_file
    sem7_file=askopenfilename(filetypes=excel_type)
def sem8_file_function():
    global sem8_file
    sem8_file=askopenfilename(filetypes=excel_type)

sem1_label=Label(root,text="Sem1 SGPA file",font=Entry_font,bg="#FFE9E3")
sem1_button=Button(root,text="Upload file",command=sem1_file_function)
sem2_label=Label(root,text="Sem2 SGPA file",font=Entry_font,bg="#FFE9E3")
sem2_button=Button(root,text="Upload file",command=sem2_file_function)
sem3_label=Label(root,text="Sem3 SGPA file",font=Entry_font,bg="#FFE9E3")
sem3_button=Button(root,text="Upload file",command=sem3_file_function)
sem4_label=Label(root,text="Sem4 SGPA file",font=Entry_font,bg="#FFE9E3")
sem4_button=Button(root,text="Upload file",command=sem4_file_function)
sem5_label=Label(root,text="Sem5 SGPA file",font=Entry_font,bg="#FFE9E3")
sem5_button=Button(root,text="Upload file",command=sem5_file_function)
sem6_label=Label(root,text="Sem6 SGPA file",font=Entry_font,bg="#FFE9E3")
sem6_button=Button(root,text="Upload file",command=sem6_file_function)
sem7_label=Label(root,text="Sem7 SGPA file",font=Entry_font,bg="#FFE9E3")
sem7_button=Button(root,text="Upload file",command=sem7_file_function)
sem8_label=Label(root,text="Sem8 SGPA file",font=Entry_font,bg="#FFE9E3")
sem8_button=Button(root,text="Upload file",command=sem8_file_function)

#Result Analysis
options=["Overall Analysis", "Civil Analysis", "EEE Analysis", "Mechanical Analysis", "ECE Analysis", "CSE Analysis"]
clicked=StringVar()
clicked.set("Select")
analysis=OptionMenu(root,clicked,*options)
analysis_type=Label(root,text="Analysis Type",font=Label_font,bg="#FFE9E3")

#sem files uploading labels and buttons
sem_label_list=[sem1_label,sem2_label,sem3_label,sem4_label,sem5_label,sem6_label,sem7_label,sem8_label]
sem_button_list=[sem1_button,sem2_button,sem3_button,sem4_button,sem5_button,sem6_button,sem7_button,sem8_button]
def upload_sem_files():
    global sem,sem_label_list,sem_button_list,sem_selection
    r=8    
    sem_selection=[sem1.get(),sem2.get(),sem3.get(),sem4.get(),sem5.get(),sem6.get(),sem7.get(),sem8.get()]
    for i in range(len(sem_selection)):
        if sem_selection[i]==1:
            sem_label_list[i].grid(row=r,column=0,sticky='w',pady=4)
            sem_button_list[i].grid(row=r,column=2,sticky='w')
            r+=1
C=IntVar()
S=IntVar()
def sem_type():
    global reval,reval_button,upload,upload_button
    if S.get()==2:
        try:
            analysis.grid_forget()
            analysis_type.grid_forget()
        except:
            pass
        reval=Label(root,text="Upload the regular GPA excel",bg="#FFE9E3",font=Entry_font)
        reval.grid(row=6,column=0,sticky='w')
        reval_button=Button(root, text='Upload File', width=20,command = GPA_file_func)
        reval_button.grid(row=6,column=2,sticky='w')
    elif S.get()==1:
        try:
            reval.grid_forget()
            reval_button.grid_forget()
        except:
            pass             
        analysis.grid(row=20,column=2,sticky='w')
        analysis_type.grid(row=20,column=0,sticky='w')
    if S.get()==1 or S.get()==2:
        try:
            upload.grid_forget()
            upload_button.grid_forget()
        except:
            pass
        upload=Label(root,text="Upload the result pdf  ",bg="#FFE9E3",font=Entry_font)
        upload.grid(row=5,column=0,sticky='w',pady=6)
        upload_button=Button(root, text='Upload File', width=20,command = input_marks_file)
        upload_button.grid(row=5,column=2,sticky='w')

#Labels and buttons used in cal_type function
semester_type=Label(root,text="File Type",font=Label_font,bg="#FFE9E3")
regular=Radiobutton(root,text="Regular",value=1,variable=S,font=Entry_font,bg="#FFE9E3",command=sem_type)
revalution=Radiobutton(root,text="Supplementary/Revaluation",value=2,variable=S,font=Entry_font,bg="#FFE9E3",command=sem_type)


def Cal_type():
    global semester_type,revalution,regular,upload,reval,reval_button,upload_button,sem_select_label,sem1_cbutton,sem2_cbutton,sem3_cbutton,sem4_cbutton,sem5_cbutton,sem6_cbutton,sem7_cbutton,sem8_cbutton
    if C.get()==1:     
        try:
            reval.grid_forget()
            reval_button.grid_forget()
        except:
            pass
        try:
            sem_selection=[0,0,0,0,0,0,0,0]
            for i in range(len(sem_selection)):
                sem_label_list[i].grid_forget()
                sem_button_list[i].grid_forget()
        except:
            pass
        try:
            sem_select_label.grid_forget()
            sem1_cbutton.grid_forget()
            sem2_cbutton.grid_forget()
            sem3_cbutton.grid_forget()
            sem4_cbutton.grid_forget()
            sem5_cbutton.grid_forget()
            sem6_cbutton.grid_forget()
            sem7_cbutton.grid_forget()
            sem8_cbutton.grid_forget()
        except:
            pass
        try:
            for i in range(sem.get()):
                sem_label_list[i].grid_forget()
                sem_button_list[i].grid_forget()
        except:
            pass     
        semester_type.grid(row=3,column=0,sticky='w')        
        regular.grid(row=3,column=2,sticky='w')        
        revalution.grid(row=4,column=2,sticky='w')
    elif C.get()==2:
        try:
            semester_selection()
            semester_type.grid_forget()
            regular.grid_forget()
            revalution.grid_forget()
            upload.grid_forget()
            upload_button.grid_forget() 
            reval.grid_forget()
            reval_button.grid_forget()                               
        except:
            pass
        try:
            analysis.grid_forget()
            analysis_type.grid_forget()
        except:
            pass

#Calculation type SGPA=1, CGPA=2
Label(root,text="Calculation Mode",font=Label_font,bg="#FFE9E3").grid(row=0,column=0,sticky='w')
Radiobutton(root,text="SGPA",value=1,variable=C,font=Entry_font,bg="#FFE9E3",command=Cal_type).grid(row=0,column=2,sticky='w')
Radiobutton(root,text="CGPA",value=2,variable=C,font=Entry_font,bg="#FFE9E3",command=Cal_type).grid(row=1,column=2,sticky='w')

# Labels needed in saving functionality
upload_regular_gpa=Label(root,text='Please upload the regular GPA excel',font=Entry_font,fg='red',bg="#FFE9E3")
upload_result_label=Label(root,text='Please upload the result file',font=Entry_font,fg='red',bg="#FFE9E3")
sem_type_select=Label(root,text='Please select Semester type',font=Entry_font,fg='red',bg="#FFE9E3")
cal_type_select=Label(root,text='Please select Calculation type',font=Entry_font,fg='red',bg="#FFE9E3")
file_error=Label(root,text='The uploaded pdf format is not suitable.',font=Entry_font,fg='red',bg="#FFE9E3")
file_error_continue=Label(root,text='So please try uploading excel.',font=Entry_font,fg='red',bg="#FFE9E3")
new_upload=Label(root,text="Upload the result excel",bg="#FFE9E3",font=Entry_font)
new_upload_button=Button(root, text='Upload File', width=20,command = input_marks_excel)
wrong_upload=Label(root,text='The uploaded excel format is not suitable.',font=Entry_font,fg='red',bg="#FFE9E3")
wrong_file=Label(root,text='The uploaded file is wrong! Try again.',font=Entry_font,fg='red',bg="#FFE9E3")
analysis_selction=Label(root,text="Please select analysis type",font=Entry_font,fg='red',bg="#FFE9E3")
close_file=Label(root,text="Please close the file before modifying it",font=Entry_font,fg='red',bg="#FFE9E3")
#saving functionality
def save():
    global data,status1,civil_credits,mech_credits,eee_credits,ece_credits,cse_credits,input_file,GPA_file,sem1_file,sem2_file,sem3_file,sem4_file,sem5_file,sem6_file,sem7_file,sem8_file   
    try:
        upload_regular_gpa.grid_forget()
    except:
        pass
    try:
        upload_result_label.grid_forget()
    except:
        pass
    try:
        sem_type_select.grid_forget()
    except:
        pass
    try:
        cal_type_select.grid_forget()
    except:
        pass
    try:
        file_error.grid_forget()
        file_error_continue.grid_forget()
    except:
        pass
    try:
        wrong_upload.grid_forget()
    except:
        pass
    try:
        wrong_file.grid_forget()
    except:
        pass
    try:
        analysis_selction.grid_forget()
    except:
        pass
    try:
        close_file.grid_forget()
    except:
        pass
    #checks calculation type selection
    if C.get()==1 or C.get()==2:
        #checks semester type selection
        if C.get()==1:
            if S.get()==1 or S.get()==2:              
                #checks input GPA file
                if input_file=='' and status1==0: 
                    upload_result_label.grid(row=21,column=0,sticky='w') 
                else: 
                    if S.get()==1:
                        if clicked.get()=="Select":
                            analysis_selction.grid(row=21,column=0,sticky='w')
                            return
                    def calculation(data):
                        if S.get()==2 and GPA_file=='':
                            upload_regular_gpa.grid(row=21,column=0,sticky='w')
                        else:
                            if S.get()==1:                                
                                    rno_list=[]
                                    for i in range(len(data)):
                                        x=int(data['Htno'][i][7:10])
                                        rno_list.append(data['Htno'][i][0:6])
                                    new_rno_list=list(set(rno_list))
                                    new=[]
                                    for i in new_rno_list:
                                        new.append(rno_list.count(i))
                                    series=new_rno_list[new.index(max(new))]
                                    new_df=pd.DataFrame(columns=data.columns)
                                    series1=str(int(series[0:2])+1)+"035A"
                                    for i in range(len(data)):
                                        if data.iloc[i,0][0:6]== series or data.iloc[i,0][0:6]==series1:
                                            new_df.loc[len(new_df.index)]=list(data.iloc[i,:])
                                    try:
                                        file_name=Sgpa(new_df,input_file) 
                                        if clicked.get()=="Civil Analysis":
                                            delete_branch(file_name,"Civil")
                                            branchwise_analysis(file_name,"Civil")
                                        elif clicked.get()=="EEE Analysis":
                                            delete_branch(file_name,"EEE")
                                            branchwise_analysis(file_name,"EEE")
                                        elif clicked.get()=="Mechanical Analysis":
                                            delete_branch(file_name,"Mechanical")
                                            branchwise_analysis(file_name,"Mechanical")
                                        elif clicked.get()=="ECE Analysis":
                                            delete_branch(file_name,"ECE")
                                            branchwise_analysis(file_name,"ECE")
                                        elif clicked.get()=="CSE Analysis":
                                            delete_branch(file_name,"CSE")
                                            branchwise_analysis(file_name,"CSE")
                                    except PermissionError:
                                        close_file.grid(row=6,column=0,sticky='w',pady=6)
                                        return
                                    except ZeroDivisionError:
                                        wrong_file.grid(row=6,column=0,sticky='w',pady=6)
                                        return                             
                            else:
                                if S.get()==2:
                                    reval_func(GPA_file,data,input_file)
                            pymsgbox.rootWindowPosition="+700+350"
                            result=alert(text="Result file generation is completed",title="Status",button="Ok")
                            try:                            
                                if result=="Ok":
                                    master.destroy()  
                            except:
                                pass
                    if status1==0:               
                        df=tabula.read_pdf(input_file,pages="all")
                        data=pd.DataFrame()
                        for i in range(len(df)):
                            data=pd.concat([data,df[i]],ignore_index=True)
                        try:
                            if data[list(data.columns)[-1]].isnull().values.any():
                                status1=1                                      
                                file_error.grid(row=21,column=0,sticky='w')    
                                file_error_continue.grid(row=21,column=2,sticky='w') 
                                upload.grid_forget()
                                upload_button.grid_forget()
                                new_upload.grid(row=5,column=0,sticky='w',pady=6)
                                new_upload_button.grid(row=5,column=2,sticky='w')                           
                        except: 
                            status1=1
                            file_error.grid(row=21,column=0,sticky='w')    
                            file_error_continue.grid(row=21,column=2,sticky='w') 
                            upload.grid_forget()
                            upload_button.grid_forget()
                            new_upload.grid(row=5,column=0,sticky='w',pady=6)
                            new_upload_button.grid(row=5,column=2,sticky='w')   
                                                        
                        if status1==0 and data.empty==False:
                            calculation(data)
                    if status1==1:
                        if input_file_excel =="":
                            upload_regular_gpa.grid(row=21,column=0,sticky='w')
                        else:
                            data=read_excel(input_file_excel,engine="openpyxl")
                            if "Htno" not in data.columns:
                                wrong_upload.grid(row=21,column=0,sticky='w')
                            else:
                                calculation(data)
                                    
            else:
                sem_type_select.grid(row=21,column=0,sticky='w')
        elif C.get()==2:
            sem_selection=[sem1.get(),sem2.get(),sem3.get(),sem4.get(),sem5.get(),sem6.get(),sem7.get(),sem8.get()]
            sem_file_list=[sem1_file,sem2_file,sem3_file,sem4_file,sem5_file,sem6_file,sem7_file,sem8_file]
            x=0
            for i in range(len(sem_selection)):
                if sem_selection[i]==1:
                    if sem_file_list[i]=="":
                        Label(root,text='Please Upload Sem'+str(i+1)+" file          ",font=Entry_font,fg='red',bg="#FFE9E3").grid(row=21,column=0,sticky='w')
                        x=1
                        break
            if x==0:
                status2=CGPA_cal(sem_selection,sem_file_list)
                if status2==0:                  
                    pymsgbox.rootWindowPosition="+700+350"
                    result=alert(text="Result file generation is completed",title="Status",button="Ok")                            
                    if result=="Ok":
                        master.destroy()
                else:
                    Label(root,text='Sem'+str(status2)+" file is in incorrect format",font=Entry_font,fg='red',bg="#FFE9E3").grid(row=21,column=0,sticky='w')
    else:
        cal_type_select.grid(row=21,column=0,sticky='w')
    
#Reset functionality
def userGuide():
    user_guide()
#Get result button
Button(root,text="Get Result",command=save,font=('Times new Roman',16)).grid(row=22,column=2)
#Reset button
Button(root,text="User Guide",command=userGuide,font=('Times new Roman',16)).grid(row=22,column=0)
master.mainloop()