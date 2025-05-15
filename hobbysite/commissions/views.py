"""This file sets up the views for the commissions app."""
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.base import TemplateView

from .models import Commission, Job, JobApplication
from user_management.models import Profile
from .forms import CommissionForm, JobForm, JobApplicationForm


class CommissionListView(ListView):
    """Creates List View for the Commission model."""

    model = Commission
    template_name = 'commission_list.html'

    def get_queryset(self, *args, **kwargs): 
        qs = super(CommissionListView, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("status") 
        return qs


class CommissionDetailView(DetailView):
    """Creates Detail View for the Commission model."""

    model = Commission
    template_name = 'commission_detail.html'


    # def get_context_data(self, **kwargs):
    #     ctx = super().get_context_data(**kwargs)
    #     ctx['sum_manpower'] = sum_of_manpower_required
    #     return ctx

    def post(self, request, *args, **kwargs):
            jobpk = request.POST.get('jobpk')

            job = Job.objects.get(pk=jobpk)


            accepted_application = 0
            for application in (JobApplication.objects.filter(job=job)):
                if application.status == 'B':
                    accepted_application += 1
                

            if (accepted_application == job.manpower_required):
                job.status = "B"
                job.save()


            if(job.status == 'A'):
                ja = JobApplication()
                ja.job = job
                ja.applicant = request.user.profile

                ja.save()

            return self.get(request, *args, **kwargs)


class CommissionCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'commission_create.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['commission_form'] = CommissionForm()
        ctx['job_form'] = JobForm()
        return ctx
    
    def post(self, request, *args, **kwargs):
        commission_form = CommissionForm(request.POST)
        job_form = JobForm(request.POST)

        if (commission_form.is_valid()):
            c = Commission()
            c.title = request.POST.get('title')
            c.author = request.user.profile
            c.description = request.POST.get('description')
            c.status = request.POST.get('status')

            c.save()

            pk = c.pk

            if(job_form.is_valid()):
                j = Job()
                j.commission = c
                j.role = request.POST.get('role')
                j.manpower_required = request.POST.get('manpower_required')
                j.status = request.POST.get('status')

                j.save()

            return redirect(reverse('commissions:commissions-detail', args=[pk]))
        
        else:
            print(commission_form.is_valid())
            context = self.get_context_data(**kwargs)
            context['commission_form'] = CommissionForm()
            context['job_form'] = JobForm()
            return self.render_to_response(context)


class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commission_update.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        ctx['form'] = CommissionForm(instance=self.get_object())
        ctx['job_form'] = JobForm()
        ctx['jobapplication_form'] = JobApplicationForm()
        return ctx
    
    def post(self, request, *args, **kwargs):
        form = CommissionForm(request.POST)
        job_form = JobForm(request.POST)
        jobapplication_form = JobApplicationForm(request.POST)

        pk = self.kwargs['pk']

        if (form.is_valid()):
            c = Commission.objects.get(pk=pk)
            c.title = request.POST.get('title')
            c.author = request.user.profile
            c.description = request.POST.get('description')
            c.status = request.POST.get('status')

            c.save()

            pk = c.pk

            if(job_form.is_valid()):
                j = Job()
                j.commission = c
                j.role = request.POST.get('role')
                j.manpower_required = request.POST.get('manpower_required')
                j.status = request.POST.get('status')

                j.save()

            japk = request.POST.get('japk')

            if(jobapplication_form.is_valid()):
                ja = JobApplication.objects.get(pk=japk)

                ja.status - request.POST.get('status')


            return redirect(reverse('commissions:commissions-detail', args=[pk]))
        
        else:
            self.object_list = self.get_queryset()
            context = self.get_context_data(**kwargs)
            context['form'] = CommissionForm(instance=self.get_object())
            context['job_form'] = JobForm()
            context['jobapplication_form'] = JobApplicationForm()
            return self.render_to_response(context)