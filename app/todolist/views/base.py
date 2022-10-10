
from todolist.models import Tasks
from django.views.generic import TemplateView
from django.utils.timezone import now, timedelta
from django.db.models import Q



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['todo_tasks'] = Tasks.objects.filter(updated_at__gte=now()-timedelta(days=30), status=3)
        context['todo_tasks'] = Tasks.objects.filter(Q(summary__icontains='bug') | Q(type=3)).exclude(status=3)
        return context











