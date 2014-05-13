from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.template import Context
import program
import requests

def stats(request):
    html = requests.get('http://in.pycon.org/funnel/2014/')
    page = html.content
    total = program.total(page)
    proposallist = program.proposallist(page)
    section = program.section(page)
    beginnerlist = program.beginner(page)
    intermediatelist = program.intermediate(page)
    advancedlist = program.advanced(page)
    bcore = program.b_core(page)
    bembedded = program.b_embedded(page)
    binfra = program.b_infrastructure(page)
    bscientific = program.b_scientific(page)
    bsoftware = program.b_software(page)
    bweb = program.b_web(page)
    bwork = program.b_workshops(page)
    icore = program.i_core(page)
    iembedded = program.i_embedded(page)
    iinfra = program.i_infrastructure(page)
    iscientific = program.i_scientific(page)
    isoftware = program.i_software(page)
    iweb = program.i_web(page)
    iwork = program.i_workshops(page)
    acore = program.a_core(page)
    aembedded = program.a_embedded(page)
    ainfra = program.a_infrastructure(page)
    ascientific = program.a_scientific(page)
    asoftware = program.a_software(page)
    aweb = program.a_web(page)
    awork = program.a_workshops(page)
    beginner_graph = program.beginner_graph(page)
    intermediate_graph = program.intermediate_graph(page)
    advanced_graph = program.advanced_graph(page)
    context = Context({'total':total, 'begineer':proposallist[0],
            'intermediate': proposallist[1],'advanced':proposallist[2], 
            'beginnerchart': section[0], 'intermediatechart': section[1], 
            'advancedchart': section[2], 'corebeginners' : beginnerlist[0],
            'embeddedbeginners' : beginnerlist[1], 'infrabeginners' : beginnerlist[2],
            'scibeginners' : beginnerlist[3], 'softbeginners' : beginnerlist[4],
            'webbeginners' : beginnerlist[5], 'workbeginners' : beginnerlist[6],
            'coreintermediates' : intermediatelist[0], 'embeddedintermediates' : intermediatelist[1],
            'infraintermediates' : intermediatelist[2], 'sciintermediates' : intermediatelist[3],
            'softintermediates' : intermediatelist[4], 'webintermediates' : intermediatelist[5],
            'workintermediates' : intermediatelist[6], 'coreadvances' : advancedlist[0],
            'embeddedadvances' : advancedlist[1], 'infraadvances' : advancedlist[2],
            'sciadvances' : advancedlist[3], 'softadvances' : advancedlist[4],
            'webadvances' : advancedlist[5], 'workadvaces' : advancedlist[6],
            'bcore' : bcore, 'bembedded' : bembedded, 'binfra' : binfra,
            'bscientific' : bscientific, 'bsoftware' : bsoftware, 'bweb' : bweb,
            'bwork' : bwork, 'icore' : icore, 'iembedded' : iembedded,
            'iinfra' : iinfra, 'iscientific' : iscientific, 'isoftware' : isoftware,
            'iweb' : iweb, 'iwork' : iwork, 'acore' : acore, 'aembedded' : aembedded,
            'ainfra' : ainfra, 'ascientific' : ascientific, 'asoftware' : asoftware,
            'aweb' : aweb, 'awork' : awork, 'beg_graph' : beginner_graph,
            'int_graph' : intermediate_graph, 'adv_graph' : advanced_graph})
    return render_to_response("home.html", context)

