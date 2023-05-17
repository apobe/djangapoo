from django.contrib import admin
from .models import makale,commentt

# Register your models here.
#admin.site.register(makale) böyle yazmak yerine
admin.site.register(commentt)
@admin.register(makale)
class makaleadmin(admin.ModelAdmin):
    list_display=["title","author","datetime"]#extra tabloya bilgi eklemek için
    list_display_links=["title","datetime"]
    search_fields=["title"]#arama çubuğu ekler
    list_filter=["datetime"]#veri süzgecine benzer sağda bir şey olusturur
    class Meta:#bu yapı özel metadan başka bir şey yazamazsın
        model=makale
