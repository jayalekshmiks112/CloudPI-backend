"""
from django.shortcuts import render, redirect,get_object_or_404
from .models import File
from .forms import FileForm

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            return redirect('home')
    else:
        form = FileForm()
    return render(request, 'upload.html', {'form': form})

def delete_file(request, file_id):
    file = get_object_or_404(File, pk=file_id)
    file.delete()
    return redirect('home')
"""
"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import File
from .forms import FileForm
import paramiko
import os

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()

            # upload file to remote server
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect('example.com', username='user', password='password')
            sftp = ssh.open_sftp()
            sftp.put(file.file.path, '/path/to/remote/server/')
            sftp.close()
            ssh.close()
            return redirect('home')
    else:
        form = FileForm()
    return render(request, 'upload.html', {'form': form})

def delete_file(request, file_id):
    file = get_object_or_404(File, pk=file_id) 
    # delete file from remote server
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('example.com', username='user', password='password')
    sftp = ssh.open_sftp()
    sftp.remove('/path/to/remote/server/' + os.path.basename(file.file.path))
    sftp.close()
    ssh.close()

    file.delete()
    return redirect('home')
"""
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import File
from .forms import FileForm
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

def home(request):
    files = File.objects.all()
    return render(request, 'home.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileForm()
    return render(request, 'upload.html', {'form': form})

def delete_file(request, file_id):
    file = File.objects.get(pk=file_id)
    file.delete()
    return redirect('home')

