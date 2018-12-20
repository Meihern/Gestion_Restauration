from django.contrib import admin
from app.models import *




class ProduitAdmin(admin.ModelAdmin):
    """description of class"""
    fields = ('Designation', 'Prix', 'Categorie')
    list_display = ('Designation', 'Categorie', 'Prix')
    list_filter = ('Categorie',)
    ordering = ('-Prix',)

class CommandeAdmin(admin.ModelAdmin):
    fields = ('Produits', 'Client', 'Montant','Ordre','Valide')
    list_display = ('Client', 'Montant', 'Ordre','Date_Commande')
    filter_horizontal = ('Produits',)
    list_filter = ('Valide',)
    #date_hierarchy = 'Date_Commande'
    ordering = ('-Date_Commande',)

class CategorieAdmin(admin.ModelAdmin):
    fields = ('Libelle',)
    list_display = ('Libelle',)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user','Message','Date_Notif')
    list_filter = ('Vue','user')

class UtilisateurAdmin(admin.ModelAdmin):
    pass

admin.site.register(Produit,ProduitAdmin)
#admin.site.register(Utilisateur,UtilisateurAdmin)
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Commande,CommandeAdmin)
#admin.site.register(Commande_Detail_Qte)
admin.site.register(Notification,NotificationAdmin)
