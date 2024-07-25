from django.shortcuts import render
from django.http import FileResponse, JsonResponse
from utils.SGPA_Calculation import *
from utils.pdfToDataframe import *
from .models import Gradepoints, Branchcodes
from .forms import GradepointForm, BranchcodeForm
from utils.Styling_cells import *
from utils.branch_wise_analysis import *
from utils.revaluation import reval_calculation
from utils.CGPA_calculation import cgpa_calculation,objects_list
from pandas import read_excel

# Create your views here.
def resultAnalysis(request):
    branches=[]
    all_records = Branchcodes.objects.all()
    for i in all_records:
        branches.append(i.Abbrevation)
    return render(request, 'Result Analysis.html',{"branch_abbrevation":branches})
def display_data(request):
    gradepoints = Gradepoints.objects.all().order_by('-Points').values()
    branchcodes = Branchcodes.objects.all().order_by('Code').values()
    gradepoint_form = GradepointForm()
    branchcode_form = BranchcodeForm()
    context = {
        'gradepoints': gradepoints,
        'branchcodes': branchcodes,
        'gradepoint_form': gradepoint_form,
        'branchcode_form': branchcode_form,
    }
    return render(request, 'Display Data.html', context)

def add_gradepoint(request):
    if request.method == 'POST':
        grade = request.POST.get('grade')
        points = request.POST.get('points')
        status = request.POST.get('status')
        presence = request.POST.get('presence')
        
        try:
            # Check for duplicate grade or points
            if Gradepoints.objects.filter(Grade=grade).exists():
                return JsonResponse({'success': False, 'message': 'Grade already exists.'})
            
            # Create and save the new gradepoint
            gradepoint = Gradepoints(Grade=grade, Points=points, Status=status, Presence=presence)
            gradepoint.save()
            return JsonResponse({'success': True})
        except Exception as e:
            # If any error occurs during the addition
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        # If request method is not POST
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def delete_gradepoint(request):
    if request.method == 'POST':
        grade = request.POST.get('grade')
        try:
            # Try to delete the gradepoint with the specified grade
            gradepoint = Gradepoints.objects.get(Grade=grade)
            gradepoint.delete()
            return JsonResponse({'success': True})
        except Gradepoints.DoesNotExist:
            # If gradepoint with the specified grade does not exist
            return JsonResponse({'success': False, 'message': 'Gradepoint not found'})
    else:
        # If request method is not POST
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def add_branchcode(request):
    if request.method == 'POST':
        branch = request.POST.get('branch')
        code = request.POST.get('code')
        abbrevation = request.POST.get('abbrevation')
        
        try:
            # Check for duplicate code
            if Branchcodes.objects.filter(Branch=branch).exists():
                return JsonResponse({'success': False, 'message': 'Branch already exists.'})
            elif Branchcodes.objects.filter(Code=code).exists():
                return JsonResponse({'success': False, 'message': 'Code value already exists for another branch.'})
            
            # Create and save the new branchcode
            branchcode = Branchcodes(Branch=branch, Code=code, Abbrevation=abbrevation)
            branchcode.save()
            return JsonResponse({'success': True})
        except Exception as e:
            # If any error occurs during the addition
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        # If request method is not POST
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def delete_branchcode(request):
    if request.method == 'POST':
        branch_code = request.POST.get('branch')
        try:
            # Try to delete the branchcode with the specified branch
            branchcode = Branchcodes.objects.get(Code=branch_code)
            branchcode.delete()
            return JsonResponse({'success': True})
        except Branchcodes.DoesNotExist:
            # If branchcode with the specified branch does not exist
            return JsonResponse({'success': False, 'message': 'Branchcode not found'})
    else:
        # If request method is not POST
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
def process_regular_sgpa(request):
    grades=[]
    branch_codes=[]
    all_records = Gradepoints.objects.all()
    for i in all_records:
        grades.append([i.Grade,i.Points,i.Status,i.Presence])
    all_records = Branchcodes.objects.all()
    for i in all_records:
        branch_codes.append([i.Branch,i.Code,i.Abbrevation])
    if request.method == 'POST':
        # Get the uploaded file from the request
        regular_class_file = request.FILES.get('regular_class')
        selected_branch=request.POST.get('selected_branch')
        # Get the MIME type of the uploaded file
        file_mime_type = regular_class_file.content_type
        if file_mime_type == 'application/pdf':
            return_data=pdfToDataframe(regular_class_file)
            if isinstance(return_data, pd.DataFrame):
                value=SGPA_calculation(return_data,grades,branch_codes)
                if isinstance(value,str):
                    return JsonResponse({'message': value},safe=False)
                if selected_branch != None:
                    branchwise_analysis('Result.xlsx',selected_branch,grades)
                sgpa_styling("Result.xlsx")
                response = FileResponse(open('Result.xlsx', 'rb'))
                response['Content-Disposition'] = 'attachment; filename="Result.xlsx"'
                return response
            elif isinstance(return_data,str):
                return JsonResponse({'message': return_data},safe=False)
        elif file_mime_type=='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file_mime_type=='application/vnd.ms-excel':
            df=read_excel(regular_class_file)
            value=SGPA_calculation(df,grades,branch_codes)
            if isinstance(value,str):
                return JsonResponse({'message': value},safe=False)
            if selected_branch != None:
                branchwise_analysis('Result.xlsx',selected_branch,grades)
            sgpa_styling("Result.xlsx")
            response = FileResponse(open('Result.xlsx', 'rb'))
            response['Content-Disposition'] = 'attachment; filename="Result.xlsx"'
            return response
        else:
            value='Please upload either excel or pdf only'
            return JsonResponse({'message': value},safe=False)
def process_reval_sgpa(request):
    grades=[]
    branch_codes=[]
    all_records = Gradepoints.objects.all()
    for i in all_records:
        grades.append([i.Grade,i.Points,i.Status,i.Presence])
    all_records = Branchcodes.objects.all()
    for i in all_records:
        branch_codes.append([i.Branch,i.Code,i.Abbrevation])
    if request.method == 'POST':
        supply_result_file = request.FILES.get('supply_class')
        gpa_file=request.FILES.get("supply_gpa_class")
        file_mime_type = supply_result_file.content_type
        if file_mime_type == 'application/pdf':
            return_data=pdfToDataframe(supply_result_file)
            if isinstance(return_data, pd.DataFrame):
                reval_calculation(gpa_file,return_data,grades,branch_codes)
                sgpa_styling("Result.xlsx")
                response = FileResponse(open('Result.xlsx', 'rb'))
                response['Content-Disposition'] = 'attachment; filename="Result.xlsx"'
                return response
            
def cgpa(request):
    branch_codes=[]
    all_records = Branchcodes.objects.all()
    for i in all_records:
        branch_codes.append([i.Branch,i.Code,i.Abbrevation])
    sem_files=[]
    for i in range(8):
        sem_files.append(request.FILES.get('cgpa_class'+str(i+1)))
        if sem_files[i]!=None:
            cgpa_calculation(sem_files[i],i+1)
    for obj in objects_list:
        obj.cgpa_cal()
    with pd.ExcelWriter("Result.xlsx",engine='openpyxl',mode='w') as output:
        for i in range(len(objects_list)):
            for j in range(len(branch_codes)):
                if objects_list[i].branch==branch_codes[j][1]:
                    objects_list[i].cgpa_df.to_excel(output,sheet_name=branch_codes[j][2],index=False)
    cgpa_styling("Result.xlsx")
    response = FileResponse(open('Result.xlsx', 'rb'))
    response['Content-Disposition'] = 'attachment; filename="Result.xlsx"'
    return response
