from django.contrib.auth import login, authenticate, forms, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from apps.accounts.models import User
from apps.pokes.models import Who, Poke
from django.db.models import Count, Min, Sum, Avg


class Dashboard(View):
    def get(self, request):   
        
        # Other users
        try:
            #other_users = User.objects.exclude(id=request.user.id)
            other_users = User.objects.all()
            pokehist = Poke.objects.all().annotate(tot_pokes=Sum('num_poke'))
            pokehst = User.objects.annotate(tot_pokes=Sum('poke__num_poke'))
        except User.DoesNotExist:
            other_users = { }
        
        # Pokers
        pokers = Who.objects.filter(pokes__whom_id=request.user)
        print pokers.count()

        dictionary = {
            "count" : pokers.count(),
        	"others1": other_users,
            "others2": pokers,
            "pokehist": pokehist,
            "pokehst" : pokehst,
    	}
        return render(request, "pokes/dashboard.html", dictionary)

def poke(request, id):
        print "who am i"
        print request.user.name
        wm_id = User.objects.get(id=id)
        print "poked"
        print wm_id.name
        try:
            who_id = Who.objects.get(usr_id=request.user)
            try:
                findwhom = who_id.pokes.get(whom_id=wm_id)
                findwhom.num_poke += 1
                findwhom.save()
                print findwhom.num_poke
            except Poke.DoesNotExist:
                p = Poke.objects.create(whom_id=wm_id)
                p.num_poke = 1
                p.save()
                who_id.pokes.add(p)
        except Who.DoesNotExist:
            print "Creating everything"
            who_id = Who.objects.create(usr_id=request.user)
            print who_id
            p = Poke.objects.create(whom_id=wm_id)
            p.num_poke = 1
            who_id.pokes.add(p)
            who_id.save()

        # Other users
        try:
            other_users = User.objects.exclude(id=request.user.id)
        except User.DoesNotExist:
            other_users = { }
        
        # Pokers
        pokers = Who.objects.filter(pokes=Poke.objects.filter(whom_id=request.user))

        dictionary = {
            "others1": other_users,
            "others2": pokers,
        }
        return render(request, "pokes/dashboard.html", dictionary)

