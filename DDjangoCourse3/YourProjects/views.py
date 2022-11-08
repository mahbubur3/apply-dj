from django.shortcuts import render


projects_list = [
    {
        'id':'1',
        'title':'Ecommerce Website',
        'description':'Fully functional ecommerse website'
    },
    {
        'id':'2',
        'title':'Portfolio Website',
        'description':'This was a project where I built out my portfolio'
    },
    {
        'id':'3',
        'title':'Social Network',
        'description':'Awesome open source project I am still working'
    },
]

def projects(request):
    page = 'project'

    context = {'page': page, 'projects': projects_list}
    return render(request, 'YourProjects/projects.html', context)


def project(request, pk):
    project_obj = None

    for i in projects_list:
        if i['id'] == pk:
            project_obj = i

    return render(request, 'YourProjects/project.html', {'project': project_obj})