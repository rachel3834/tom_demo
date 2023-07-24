from django.shortcuts import render
from tom_targets.models import Target

# Create your views here.
from django.views.generic.detail import DetailView

class QueryView(DetailView):
    template_name = 'query.html'
    model = Target

    def get_context_data(self, **kwargs):
        return {'target': self.get_object()}

    # Define get method here to send query to Atlas