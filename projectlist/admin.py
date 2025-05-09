from django.contrib import admin
from .models import Project, Rating
from django.db.models import Avg
# admin.site.register(Project)
# admin.site.register(Rating)
# admin.site.register



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_rank', 'average_rating_display', 'created_at')

    def average_rating_display(self, obj):
        avg = obj.average_rating()
        return f"{avg:.2f}" if avg else "N/A"
    average_rating_display.short_description = '평균 별점'

    def get_rank(self, obj):
        # 전체 프로젝트 평균 점수 기준으로 랭킹 계산
        all_projects = Project.objects.annotate(avg=Avg('ratings__score'))
        sorted_projects = sorted(all_projects, key=lambda p: p.avg or 0, reverse=True)

        for idx, project in enumerate(sorted_projects, start=1):
            if project.id == obj.id:
                return idx
        return "-"
    get_rank.short_description = '등위'