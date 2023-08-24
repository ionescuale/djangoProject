from trainer.models import Trainer


# Context processors este o modalitate de a furniza date sau avriable catre paginile html.
# Contextul este un dictionar pythn care va contine elementele ce vor fi folosite in fisierele .html

# In concluzie , context processors reprezinta o modalitate eficienta de a furniza date globale in pagini html

def get_all_trainers(request):
    get_trainers = Trainer.objects.all()
    return {'trainer': get_trainers}