from django.shortcuts import render_to_response
from django.http.response import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from administracion.models import Proyecto, Fase
from desarrollo.models import Item
from desarrollo.forms import CrearItemForm, ModificarItemForm
from inicio.decorators import permiso_requerido, miembro_proyecto, fase_miembro_proyecto

@login_required(login_url='/login/')
def desarrollo_view(request):
    
    calcular_costo = False
    gestionar_fases = False
    roles = request.user.roles.all()
    for r in roles:
        for p in r.permisos.all():
            if p.nombre == 'Calcular costo de proyecto':
                calcular_costo = True
            elif p.nombre == 'Gestionar fases de proyecto':
                gestionar_fases = True
                
            if calcular_costo and gestionar_fases:
                break
        if calcular_costo and gestionar_fases:
                break
            
    proyectos = Proyecto.objects.filter(estado=1)
    ctx = {'proyectos': proyectos, 'calcular_costo':calcular_costo, 'gestionar_fases':gestionar_fases}
    return render_to_response('desarrollo.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permiso_requerido(permiso="Calcular costo de proyecto")
@miembro_proyecto()
def calcular_costo_view(request, id_proyecto):
    
    proyecto = Proyecto.objects.get(id=id_proyecto)
    fases = proyecto.fases.all()
    fases_valido = False
    items_valido = False
    costo_total = 0
    if fases:
        fases_valido = True
        for f in fases:
            items = f.items.all()
            if items:
                items_valido = True
                for i in items:
                    costo_total = costo_total + i.costo
    ctx = {'proyecto':proyecto, 'fases_valido':fases_valido, 'items_valido':items_valido, 'costo_total':costo_total}
    return render_to_response('costo_total.html', ctx, context_instance=RequestContext(request))
            
@login_required(login_url='/login/')
@permiso_requerido(permiso="Gestionar fases de proyecto")
@miembro_proyecto()
def fases_proyecto_view(request, id_proyecto):
    
    iniciar_fase = False
    finalizar_fase = False
    gestionar_items = False
    roles = request.user.roles.all()
    for r in roles:
        for p in r.permisos.all():
            if p.nombre == 'Iniciar fase':
                iniciar_fase = True
            elif p.nombre == 'Finalizar fase':
                finalizar_fase = True
            elif p.nombre == 'Gestionar items de fase':
                gestionar_items = True
                
            if iniciar_fase and finalizar_fase and gestionar_items:
                break
        if iniciar_fase and finalizar_fase and gestionar_items:
                break
    
    proyecto = Proyecto.objects.get(id=id_proyecto)
    fases = proyecto.fases.all()
    ctx = {'proyecto':proyecto, 'fases':fases, 'iniciar_fase':iniciar_fase, 'finalizar_fase':finalizar_fase, 'gestionar_items':gestionar_items}
    return render_to_response('fases_proyecto.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permiso_requerido(permiso="Iniciar fase")
@fase_miembro_proyecto()
def iniciar_fase_view(request, id_fase, id_proyecto):
    
    fase = Fase.objects.get(id=id_fase)
    proyecto = Proyecto.objects.get(id=id_proyecto)
    inicio_valido = True
    estado_valido = True
    items_valido = True
    roles_valido = True
    
    if fase.estado != 0:
        estado_valido = False
        inicio_valido = False
    if fase.items.count() == 0:
        items_valido = False
        inicio_valido = False
    if fase.roles.count() == 0:
        roles_valido = False
        inicio_valido = False
    
    if inicio_valido:
        fase.estado = 1
        fase.save()
        ctx = {'fase':fase, 'inicio_valido':inicio_valido, 'estado_valido':estado_valido, 'items_valido':items_valido, 'roles_valido':roles_valido, 'proyecto':proyecto}
        return render_to_response('iniciar_fase.html', ctx, context_instance=RequestContext(request))
    else:
        ctx = {'fase':fase, 'inicio_valido':inicio_valido, 'estado_valido':estado_valido, 'items_valido':items_valido, 'roles_valido':roles_valido, 'proyecto':proyecto}
        return render_to_response('iniciar_fase.html', ctx, context_instance=RequestContext(request))
    
@login_required(login_url='/login/')
@permiso_requerido(permiso="Finalizar fase")
@fase_miembro_proyecto()
def finalizar_fase_view(request, id_fase, id_proyecto):
    
    fase = Fase.objects.get(id=id_fase)
    proyecto = Proyecto.objects.get(id=id_proyecto)
    finalizado_valido = True
    estado_valido = True
    
    if fase.estado != 1:
        estado_valido = False
        finalizado_valido = False
    
    if estado_valido:
        finalizado_valido = True
        items = fase.items.all()
        for i in items:
            if i.estado != 2:
                finalizado_valido = False
                break
            
        if finalizado_valido:
            fase.estado = 2
            fase.save()
            ctx = {'fase':fase, 'finalizado_valido':finalizado_valido, 'estado_valido':estado_valido, 'proyecto':proyecto}
            return render_to_response('finalizar_fase.html', ctx, context_instance=RequestContext(request))
        else:
            ctx = {'fase':fase, 'finalizado_valido':finalizado_valido, 'estado_valido':estado_valido, 'proyecto':proyecto}
            return render_to_response('finalizar_fase.html', ctx, context_instance=RequestContext(request))
    else:
        ctx = {'fase':fase, 'finalizado_valido':finalizado_valido, 'estado_valido':estado_valido, 'proyecto':proyecto}
        return render_to_response('finalizar_fase.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permiso_requerido(permiso="Gestionar items de fase")
@fase_miembro_proyecto()
def items_fase_view(request, id_fase, id_proyecto):
    
    crear_item = False
    modificar_item = False
    eliminar_item = False
    visualizar_item = False
    roles = request.user.roles.all()
    for r in roles:
        for p in r.permisos.all():
            if p.nombre == 'Crear item':
                crear_item = True
            elif p.nombre == 'Modificar item':
                modificar_item = True
            elif p.nombre == 'Eliminar item':
                eliminar_item = True
            elif p.nombre == 'Visualizar item':
                visualizar_item = True
                
            if crear_item and modificar_item and eliminar_item and visualizar_item:
                break
        if crear_item and modificar_item and eliminar_item and visualizar_item:
            break
    
    proyecto = Proyecto.objects.get(id=id_proyecto)
    fase = Fase.objects.get(id=id_fase)
    items = fase.items.all()
    ctx = {'proyecto':proyecto, 'fase':fase, 'items':items, 'crear_item':crear_item, 'modificar_item':modificar_item, 'eliminar_item':eliminar_item, 'visualizar_item':visualizar_item}
    return render_to_response('items_fase.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permiso_requerido(permiso="Crear item")
def crear_item_view(request, id_fase, id_proyecto):
    
    fase = Fase.objects.get(id=id_fase[0])
    proyecto = Proyecto.objects.get(id=id_proyecto[0])
    form = CrearItemForm()
    if request.method == "POST":
        form = CrearItemForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            complejidad = form.cleaned_data['complejidad']
            costo = form.cleaned_data['costo']
            
            item = Item.objects.create(nombre=nombre, descripcion=descripcion, complejidad=complejidad, costo=costo)
            item.save()
            fase.items.add(item)
            fase.save()
            return HttpResponseRedirect('/desarrollo/items/fase/%s/proyecto/%s/'%(fase.id, proyecto.id))
            
        else:
            ctx = {'form':form, 'fase':fase, 'proyecto':proyecto}
            return render_to_response('crear_item.html', ctx, context_instance=RequestContext(request))
    ctx = {'form':form, 'fase':fase, 'proyecto':proyecto}
    return render_to_response('crear_item.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permiso_requerido(permiso="Modificar item")
def modificar_item_view(request, id_item, id_fase, id_proyecto):
    
    item = Item.objects.get(id=id_item[0])
    fase = Fase.objects.get(id=id_fase[0])
    proyecto = Proyecto.objects.get(id=id_proyecto[0])
    form = ModificarItemForm()
    if request.method == "POST":
        form = ModificarItemForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            descripcion = form.cleaned_data['descripcion']
            complejidad = form.cleaned_data['complejidad']
            costo = form.cleaned_data['costo']
            
            item.nombre = nombre
            item.descripcion = descripcion
            item.complejidad = complejidad
            item.costo = costo
            item.save()
            return HttpResponseRedirect('/desarrollo/items/item/%s/fase/%s/proyecto/%s/'%(item.id, fase.id, proyecto.id))
    
    if request.method == "GET":
        form = ModificarItemForm(initial={
            'nombre': item.nombre,
            'descripcion': item.descripcion,
            'costo': item.costo,
            'complejidad': item.complejidad,
            })
    ctx = {'form':form, 'item':item, 'fase':fase, 'proyecto':proyecto}
    return render_to_response('modificar_item.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permiso_requerido(permiso="Eliminar item")
def eliminar_item_view(request, id_item, id_fase, id_proyecto):

    item = Item.objects.get(id=id_item)
    fase = Fase.objects.get(id=id_fase[0])
    proyecto = Proyecto.objects.get(id=id_proyecto[0])
    valido = True
    if item.estado == 1 or item.estado == 2 or item.estado == 4:
        valido = False
    if request.method == "POST":
        if valido == True:
            item.delete()
            return HttpResponseRedirect('/desarrollo/items/fase/%s/proyecto/%s/'%(fase.id, proyecto.id))
        else:
            ctx = {'item':item, 'fase':fase, 'proyecto':proyecto, 'valido':valido}
            return render_to_response('eliminar_item.html', ctx, context_instance=RequestContext(request))
    if request.method == "GET":
        ctx = {'item':item, 'fase':fase, 'proyecto':proyecto, 'valido':valido}
        return render_to_response('eliminar_item.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@permiso_requerido(permiso="Visualizar item")
def visualizar_item_view(request, id_item, id_fase, id_proyecto):

    item = Item.objects.get(id=id_item)
    fase = Fase.objects.get(id=id_fase[0])
    proyecto = Proyecto.objects.get(id=id_proyecto[0])
    ctx = {'item':item, 'fase': fase, 'proyecto':proyecto}
    return render_to_response('visualizar_item.html', ctx, context_instance=RequestContext(request))